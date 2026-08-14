"""Native epistemic-graph ingestion for CISO Assistant GRC records (typed graph nodes).

CONCEPT:AU-KG.ingest.enterprise-source-extractor. This is the record-source twin of
media-downloader's blob ingestion: the package natively pushes its governance-risk-
compliance data into the ONE epistemic-graph knowledge graph as **typed OWL nodes**
(``:RiskAssessment``, ``:RiskScenario``, ``:Control``, ``:Audit``, ``:Incident``,
``:Asset``, ``:Vulnerability`` …) + links, matching the classes federated by
``ciso_assistant_api.ontology`` (``ciso.ttl``).

The write path rides the shared, required primitive
``agent_utilities.knowledge_graph.memory.native_ingest`` — the one connector write
path; there is no self-contained fallback transaction here. The MCP tool surface
(``ciso_assistant_api.mcp.mcp_kg_ingest``) exposes these as best-effort tools that
must never raise on an unreachable/misconfigured KG stack, so ``ingest_entities`` /
``ingest_documents`` stay **best-effort**: they return ``None`` (never raise) for
empty input or when the shared primitive reports :class:`NativeIngestError` (no
reachable engine, or a malformed record). Node ids follow
``ciso:<class>:<externalId>``.
"""

from __future__ import annotations

import logging
from typing import Any

from agent_utilities.knowledge_graph.memory.native_ingest import (
    NativeIngestError,
    ingest_documents as _native_ingest_documents,
    ingest_entities as _native_ingest_entities,
    media_store as _native_media_store,
)
from agent_utilities.security.persistence_privacy import sanitize_for_persistence

logger = logging.getLogger("ciso_assistant_api.kg")

_SOURCE = "ciso-assistant-api"
_DOMAIN = "ciso"


def _privacy_safe(value: Any) -> Any:
    """Sanitize one value before it crosses the durable graph boundary."""
    clean, report = sanitize_for_persistence(value)
    if isinstance(clean, dict) and report.changed:
        clean["privacy_redactions"] = report.redactions
    return clean


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
    """Write typed OWL nodes (+ edges) into epistemic-graph. Best-effort, never raises.

    ``entities``: ``[{"id":..., "node_type":<owl:Class>, ...props}]``.
    ``relationships``: ``[{"source":id, "target":id, "relationship":<link>}]``.
    Returns ``{"nodes":n, "edges":m}`` or ``None`` (empty input / no reachable engine /
    malformed record; never raises). ``client``/``graph`` may be injected (tests);
    otherwise the process-owned governed authority is resolved on demand.
    """
    entities = [
        safe
        for entity in entities or []
        if entity.get("id")
        for safe in [_privacy_safe(entity)]
        if isinstance(safe, dict) and safe.get("id")
    ]
    relationships = [
        safe
        for relationship in relationships or []
        for safe in [_privacy_safe(relationship)]
        if isinstance(safe, dict)
    ]
    if not entities:
        return None
    try:
        return _native_ingest_entities(
            entities,
            relationships,
            source=source,
            domain=domain,
            client=client,
            graph=graph,
        )
    except NativeIngestError as exc:
        logger.debug("KG ingest unavailable/failed: %s", exc)
        return None


def ingest_documents(
    documents: list[dict[str, Any]],
    *,
    source: str = _SOURCE,
    domain: str = _DOMAIN,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Write text records as ``:Document`` nodes (semantic-search fodder). Best-effort.

    Each doc: ``{"id":..., "text":..., "title"?:..., "source_uri"?:..., ...props}``.
    Returns ``{"nodes":n, "edges":0}`` or ``None`` (never raises).
    """
    documents = [
        safe
        for document in documents or []
        for safe in [_privacy_safe(document)]
        if isinstance(safe, dict)
    ]
    if not documents:
        return None
    try:
        return _native_ingest_documents(
            documents, source=source, domain=domain, client=client, graph=graph
        )
    except NativeIngestError as exc:
        logger.debug("KG ingest unavailable/failed: %s", exc)
        return None


def media_store() -> Any | None:
    """Return a ``MediaStore`` over a live engine (raw-blob ingestion), or ``None``."""
    try:
        return _native_media_store()
    except NativeIngestError as exc:
        logger.debug("KG media store unavailable: %s", exc)
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
                "node_type": "RiskAssessment",
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
                    "relationship": "includesScenario",
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
                "node_type": "RiskScenario",
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
                    "relationship": "hasThreat",
                }
            )
        for cid in _rel_ids(rec, "applied_controls"):
            relationships.append(
                {
                    "source": node_id,
                    "target": f"ciso:control:{cid}",
                    "relationship": "mitigatedBy",
                }
            )
        for aid in _rel_ids(rec, "assets"):
            relationships.append(
                {
                    "source": node_id,
                    "target": f"ciso:asset:{aid}",
                    "relationship": "affectsAsset",
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
                "node_type": "Control",
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
                    "relationship": "affectsAsset",
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
                "node_type": "Audit",
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
                    "relationship": "assessesFramework",
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
                "node_type": "Incident",
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
                    "relationship": "affectsAsset",
                }
            )
        for cid in _rel_ids(rec, "applied_controls"):
            relationships.append(
                {
                    "source": node_id,
                    "target": f"ciso:control:{cid}",
                    "relationship": "mitigatedBy",
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
                "node_type": "Asset",
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
                "node_type": "Vulnerability",
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
                    "relationship": "mitigatedBy",
                }
            )
        for aid in _rel_ids(rec, "assets"):
            relationships.append(
                {
                    "source": node_id,
                    "target": f"ciso:asset:{aid}",
                    "relationship": "affectsAsset",
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
