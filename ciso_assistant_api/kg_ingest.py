"""Native epistemic-graph ingestion for CISO Assistant GRC records (typed graph nodes).

CONCEPT:AU-KG.ingest.enterprise-source-extractor. This is the record-source twin of
media-downloader's blob ingestion: the package natively pushes its governance-risk-
compliance data into the ONE epistemic-graph knowledge graph as **typed OWL nodes**
(``:RiskAssessment``, ``:RiskScenario``, ``:Control``, ``:Audit``, ``:Incident``,
``:Asset``, ``:Vulnerability`` …) + links, matching the classes federated by
``ciso_assistant_api.ontology`` (``ciso.ttl``).

The write path rides the shared primitive
``agent_utilities.knowledge_graph.memory.native_ingest`` when present; that import is
GUARDED, and a self-contained txn fallback over the lightweight engine client
(``GraphComputeEngine()._client`` + ``txn``) covers installs where the primitive is not
yet vendored. Everything is dependency-/engine-guarded: with no KG stack or no reachable
engine every entry point **no-ops** (returns ``None``), so the connector runs with zero
KG infrastructure. Node ids follow ``ciso:<class>:<externalId>``.
"""

from __future__ import annotations

import logging
import time
from typing import Any

logger = logging.getLogger("ciso_assistant_api.kg")

_SOURCE = "ciso-assistant-api"
_DOMAIN = "ciso"
_DEFAULT_GRAPH = "__commons__"

# Prefer the shared fleet primitive; fall back to the self-contained txn path below.
try:  # pragma: no cover - exercised only where the primitive is installed
    from agent_utilities.knowledge_graph.memory.native_ingest import (
        ingest_documents as _shared_ingest_documents,
    )
    from agent_utilities.knowledge_graph.memory.native_ingest import (
        ingest_entities as _shared_ingest_entities,
    )
    from agent_utilities.knowledge_graph.memory.native_ingest import (
        media_store as _shared_media_store,
    )

    _HAS_SHARED = True
except Exception:  # noqa: BLE001 - primitive not vendored yet
    _shared_ingest_entities = None
    _shared_ingest_documents = None
    _shared_media_store = None
    _HAS_SHARED = False


# --------------------------------------------------------------- engine client
def _client() -> tuple[Any | None, str]:
    """Return ``(engine_client, graph_name)`` or ``(None, "")`` when unavailable."""
    try:
        from agent_utilities.knowledge_graph.core.graph_compute import (
            GraphComputeEngine,
        )
    except Exception as e:  # noqa: BLE001 — KG stack absent
        logger.debug("KG ingest unavailable (import): %s", e)
        return None, ""
    try:
        engine = GraphComputeEngine()
        client = getattr(engine, "_client", None)
        if client is None:
            return None, ""
        graph = getattr(engine, "graph_name", None) or _DEFAULT_GRAPH
        return client, graph
    except Exception as e:  # noqa: BLE001 — engine unreachable
        logger.debug("KG ingest: engine unreachable: %s", e)
        return None, ""


def _write_nodes(
    client: Any,
    graph: str,
    nodes: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None,
) -> dict[str, int] | None:
    """Self-contained fallback: stamp provenance, MERGE nodes in one txn, add edges."""
    nodes = [n for n in nodes if n.get("id")]
    if not nodes:
        return None
    try:
        txn = client.txn.begin(graph=graph)
        for node in nodes:
            props = {k: v for k, v in node.items() if k != "id" and v is not None}
            props.setdefault("source", _SOURCE)
            props.setdefault("domain", _DOMAIN)
            client.txn.add_node(txn, node["id"], props)
        committed = client.txn.commit(txn)
    except Exception as e:  # noqa: BLE001 — engine/txn failure is non-fatal
        logger.warning("KG ingest: txn failed: %s", e)
        return None
    if not committed:
        logger.warning("KG ingest: txn not committed (conflict)")
        return None

    edges = 0
    for rel in relationships or []:
        try:
            client.edges.add(
                rel["source"], rel["target"], {"type": rel.get("type", "RELATED")}
            )
            edges += 1
        except Exception as e:  # noqa: BLE001 — pure edge link, best-effort
            logger.debug("KG ingest: edge skipped: %s", e)

    logger.info("KG ingest[ciso]: wrote %d nodes, %d edges", len(nodes), edges)
    return {"nodes": len(nodes), "edges": edges}


# ------------------------------------------------------------------ public API
def ingest_entities(
    entities: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None = None,
    *,
    source: str = _SOURCE,
    domain: str = _DOMAIN,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Write typed OWL nodes (+ edges) into epistemic-graph.

    ``entities``: ``[{"id":..., "type":<owl:Class>, ...props}]``.
    ``relationships``: ``[{"source":id, "target":id, "type":<link>}]``.
    Returns ``{"nodes":n, "edges":m}`` or ``None`` (no engine / failure; never raises).
    ``client``/``graph`` may be injected (tests); otherwise resolved on demand.
    """
    entities = [e for e in (entities or []) if e.get("id")]
    if not entities:
        return None
    # Injected client (tests) always uses the self-contained path.
    if client is None and _HAS_SHARED and _shared_ingest_entities is not None:
        return _shared_ingest_entities(
            entities, relationships, source=source, domain=domain
        )
    if client is None:
        client, graph = _client()
    if client is None:
        return None
    return _write_nodes(client, graph or _DEFAULT_GRAPH, entities, relationships)


def ingest_documents(
    documents: list[dict[str, Any]],
    *,
    source: str = _SOURCE,
    domain: str = _DOMAIN,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Write text records as ``:Document`` nodes (semantic-search fodder).

    Each doc: ``{"id":..., "text":..., "title"?:..., "source_uri"?:..., ...props}``.
    Returns ``{"nodes":n, "edges":0}`` or ``None``.
    """
    if client is None and _HAS_SHARED and _shared_ingest_documents is not None:
        return _shared_ingest_documents(documents, source=source, domain=domain)
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    nodes: list[dict[str, Any]] = []
    for doc in documents or []:
        did = doc.get("id")
        text = doc.get("text") or doc.get("content")
        if not did or not text:
            continue
        node = {k: v for k, v in doc.items() if k != "content" and v is not None}
        node["id"] = did
        node["type"] = "Document"
        node["text"] = text
        node.setdefault("created_at", now)
        nodes.append(node)
    if not nodes:
        return None
    if client is None:
        client, graph = _client()
    if client is None:
        return None
    return _write_nodes(client, graph or _DEFAULT_GRAPH, nodes, None)


def media_store() -> Any | None:
    """Return a ``MediaStore`` over a live engine (raw-blob ingestion), or ``None``."""
    if _HAS_SHARED and _shared_media_store is not None:
        store = _shared_media_store()
        if store is not None:
            return store
    client, _ = _client()
    if client is None:
        return None
    try:
        from agent_utilities.knowledge_graph.core.graph_compute import (
            GraphComputeEngine,
        )
        from agent_utilities.knowledge_graph.memory.media_store import MediaStore

        return MediaStore(GraphComputeEngine())
    except Exception as e:  # noqa: BLE001
        logger.debug("KG ingest: media_store unavailable: %s", e)
        return None


# --------------------------------------------------------- record → node maps
def _rel_ids(record: dict[str, Any], field: str) -> list[str]:
    """Pull a list of related object ids from a serializer field (list of id/dict)."""
    out: list[str] = []
    for item in record.get(field) or []:
        if isinstance(item, dict):
            rid = item.get("id") or item.get("str")
        else:
            rid = item
        if rid is not None:
            out.append(str(rid))
    return out


def ingest_risk_assessments(
    assessments: list[dict[str, Any]],
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Map risk-assessment records → ``:RiskAssessment`` nodes (+ scenario links)."""
    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    for rec in assessments or []:
        rid = rec.get("id")
        if rid is None:
            continue
        node_id = f"ciso:riskassessment:{rid}"
        entities.append(
            {
                "id": node_id,
                "type": "RiskAssessment",
                "name": rec.get("name"),
                "refId": rec.get("ref_id"),
                "description": rec.get("description"),
                "complianceStatus": rec.get("status"),
                "version": rec.get("version"),
                "updated_at": rec.get("updated_at"),
                "externalToolId": str(rid),
            }
        )
        for sid in _rel_ids(rec, "risk_scenarios"):
            relationships.append(
                {
                    "source": node_id,
                    "target": f"ciso:riskscenario:{sid}",
                    "type": "includesScenario",
                }
            )
    return ingest_entities(entities, relationships, client=client, graph=graph)


def ingest_risk_scenarios(
    scenarios: list[dict[str, Any]],
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Map risk-scenario records → ``:RiskScenario`` nodes (+ threat/control/asset links)."""
    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    for rec in scenarios or []:
        rid = rec.get("id")
        if rid is None:
            continue
        node_id = f"ciso:riskscenario:{rid}"
        entities.append(
            {
                "id": node_id,
                "type": "RiskScenario",
                "name": rec.get("name"),
                "refId": rec.get("ref_id"),
                "description": rec.get("description"),
                "riskTreatment": rec.get("treatment"),
                "currentLevel": rec.get("current_level"),
                "residualLevel": rec.get("residual_level"),
                "updated_at": rec.get("updated_at"),
                "externalToolId": str(rid),
            }
        )
        for tid in _rel_ids(rec, "threats"):
            relationships.append(
                {
                    "source": node_id,
                    "target": f"ciso:threat:{tid}",
                    "type": "hasThreat",
                }
            )
        for cid in _rel_ids(rec, "applied_controls"):
            relationships.append(
                {
                    "source": node_id,
                    "target": f"ciso:control:{cid}",
                    "type": "mitigatedBy",
                }
            )
        for aid in _rel_ids(rec, "assets"):
            relationships.append(
                {
                    "source": node_id,
                    "target": f"ciso:asset:{aid}",
                    "type": "affectsAsset",
                }
            )
    return ingest_entities(entities, relationships, client=client, graph=graph)


def ingest_applied_controls(
    controls: list[dict[str, Any]],
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Map applied-control records → ``:Control`` nodes (+ asset links)."""
    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    for rec in controls or []:
        rid = rec.get("id")
        if rid is None:
            continue
        node_id = f"ciso:control:{rid}"
        entities.append(
            {
                "id": node_id,
                "type": "Control",
                "name": rec.get("name"),
                "refId": rec.get("ref_id"),
                "description": rec.get("description"),
                "controlStatus": rec.get("status"),
                "controlPriority": rec.get("priority"),
                "category": rec.get("category"),
                "csf_function": rec.get("csf_function"),
                "eta": rec.get("eta"),
                "updated_at": rec.get("updated_at"),
                "externalToolId": str(rid),
            }
        )
        for aid in _rel_ids(rec, "assets"):
            relationships.append(
                {
                    "source": node_id,
                    "target": f"ciso:asset:{aid}",
                    "type": "affectsAsset",
                }
            )
    return ingest_entities(entities, relationships, client=client, graph=graph)


def ingest_compliance_assessments(
    audits: list[dict[str, Any]],
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Map compliance-assessment records → ``:Audit`` nodes (+ framework links)."""
    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    for rec in audits or []:
        rid = rec.get("id")
        if rid is None:
            continue
        node_id = f"ciso:audit:{rid}"
        entities.append(
            {
                "id": node_id,
                "type": "Audit",
                "name": rec.get("name"),
                "refId": rec.get("ref_id"),
                "description": rec.get("description"),
                "complianceStatus": rec.get("status"),
                "complianceProgress": rec.get("progress"),
                "computed_outcome": rec.get("computed_outcome"),
                "updated_at": rec.get("updated_at"),
                "externalToolId": str(rid),
            }
        )
        fw = rec.get("framework")
        fid = fw.get("id") if isinstance(fw, dict) else fw
        if fid is not None:
            relationships.append(
                {
                    "source": node_id,
                    "target": f"ciso:framework:{fid}",
                    "type": "assessesFramework",
                }
            )
    return ingest_entities(entities, relationships, client=client, graph=graph)


def ingest_incidents(
    incidents: list[dict[str, Any]],
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Map incident records → ``:Incident`` nodes (+ asset/control links)."""
    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    for rec in incidents or []:
        rid = rec.get("id")
        if rid is None:
            continue
        node_id = f"ciso:incident:{rid}"
        entities.append(
            {
                "id": node_id,
                "type": "Incident",
                "name": rec.get("name"),
                "refId": rec.get("ref_id"),
                "description": rec.get("description"),
                "severity": rec.get("severity"),
                "complianceStatus": rec.get("status"),
                "reported_at": rec.get("reported_at"),
                "resolved_at": rec.get("resolved_at"),
                "updated_at": rec.get("updated_at"),
                "externalToolId": str(rid),
            }
        )
        for aid in _rel_ids(rec, "assets"):
            relationships.append(
                {
                    "source": node_id,
                    "target": f"ciso:asset:{aid}",
                    "type": "affectsAsset",
                }
            )
        for cid in _rel_ids(rec, "applied_controls"):
            relationships.append(
                {
                    "source": node_id,
                    "target": f"ciso:control:{cid}",
                    "type": "mitigatedBy",
                }
            )
    return ingest_entities(entities, relationships, client=client, graph=graph)


def ingest_assets(
    assets: list[dict[str, Any]],
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Map asset records → ``:Asset`` nodes."""
    entities: list[dict[str, Any]] = []
    for rec in assets or []:
        rid = rec.get("id")
        if rid is None:
            continue
        entities.append(
            {
                "id": f"ciso:asset:{rid}",
                "type": "Asset",
                "name": rec.get("name"),
                "refId": rec.get("ref_id"),
                "description": rec.get("description"),
                "asset_type": rec.get("type"),
                "is_primary": rec.get("is_primary"),
                "updated_at": rec.get("updated_at"),
                "externalToolId": str(rid),
            }
        )
    return ingest_entities(entities, None, client=client, graph=graph)


def ingest_vulnerabilities(
    vulnerabilities: list[dict[str, Any]],
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Map vulnerability records → ``:Vulnerability`` nodes (+ control/asset links)."""
    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    for rec in vulnerabilities or []:
        rid = rec.get("id")
        if rid is None:
            continue
        node_id = f"ciso:vulnerability:{rid}"
        entities.append(
            {
                "id": node_id,
                "type": "Vulnerability",
                "name": rec.get("name"),
                "refId": rec.get("ref_id"),
                "description": rec.get("description"),
                "severity": rec.get("severity"),
                "complianceStatus": rec.get("status"),
                "due_date": rec.get("due_date"),
                "updated_at": rec.get("updated_at"),
                "externalToolId": str(rid),
            }
        )
        for cid in _rel_ids(rec, "applied_controls"):
            relationships.append(
                {
                    "source": node_id,
                    "target": f"ciso:control:{cid}",
                    "type": "mitigatedBy",
                }
            )
        for aid in _rel_ids(rec, "assets"):
            relationships.append(
                {
                    "source": node_id,
                    "target": f"ciso:asset:{aid}",
                    "type": "affectsAsset",
                }
            )
    return ingest_entities(entities, relationships, client=client, graph=graph)


def ingest_evidences(
    evidences: list[dict[str, Any]],
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Map evidence records → ``:Document`` nodes (text = name + description).

    The raw file bytes are ingested separately as ``:Blob`` / ``:MediaAsset`` via
    :mod:`ciso_assistant_api.kg_media`.
    """
    docs: list[dict[str, Any]] = []
    for rec in evidences or []:
        rid = rec.get("id")
        if rid is None:
            continue
        text = " ".join(
            str(v) for v in (rec.get("name"), rec.get("description")) if v
        ).strip()
        if not text:
            continue
        docs.append(
            {
                "id": f"ciso:evidence:{rid}",
                "title": rec.get("name"),
                "text": text,
                "refId": rec.get("ref_id"),
                "evidence_status": rec.get("status"),
                "attachment": rec.get("attachment"),
                "link": rec.get("link"),
                "source_uri": rec.get("link"),
                "updated_at": rec.get("updated_at"),
                "externalToolId": str(rid),
            }
        )
    return ingest_documents(docs, client=client, graph=graph)
