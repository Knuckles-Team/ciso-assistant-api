"""Wire-First native KG ingestion tool for CISO Assistant (CONCEPT:AU-KG.ingest.enterprise-source-extractor).

Exposes ``ciso_ingest`` — one MCP tool that lists a GRC record kind via the real
``Api`` client and pushes it into the epistemic-graph knowledge graph as typed OWL nodes
(and, for evidence, ``:Document`` nodes plus ``:Blob`` / ``:MediaAsset`` attachment
blobs). It is registered by ``mcp_server`` alongside the generated domain-tool surface.
Best-effort: with no reachable engine the ingest is a clean no-op (``"ingested": null``).
"""

from __future__ import annotations

import json
import logging
from typing import Any

from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from ciso_assistant_api.auth import get_client

logger = logging.getLogger("ciso_assistant_api.kg_ingest_tool")

# kind -> (client list-method name, kg_ingest mapper name)
_KIND_MAP: dict[str, tuple[str, str]] = {
    "risk_assessments": ("api_risk_assessments_list", "ingest_risk_assessments"),
    "risk_scenarios": ("api_risk_scenarios_list", "ingest_risk_scenarios"),
    "applied_controls": ("api_applied_controls_list", "ingest_applied_controls"),
    "compliance_assessments": (
        "api_compliance_assessments_list",
        "ingest_compliance_assessments",
    ),
    "incidents": ("api_incidents_list", "ingest_incidents"),
    "assets": ("api_assets_list", "ingest_assets"),
    "vulnerabilities": ("api_vulnerabilities_list", "ingest_vulnerabilities"),
    "evidences": ("api_evidences_list", "ingest_evidences"),
}


def _records(resp: Any) -> list[dict[str, Any]]:
    """Normalize an ``Api`` list Response into a list of plain dict records."""
    data = getattr(resp, "data", resp)
    if data is None:
        return []
    items = data if isinstance(data, list) else [data]
    out: list[dict[str, Any]] = []
    for r in items:
        if r is None:
            continue
        out.append(r.model_dump() if hasattr(r, "model_dump") else r)
    return out


def register_kg_ingest_tools(mcp: FastMCP):
    @mcp.tool(tags={"kg-ingest"})
    async def ciso_ingest(
        kind: str = Field(
            description=(
                "GRC record kind to list and ingest into the knowledge graph. One of: "
                "'risk_assessments', 'risk_scenarios', 'applied_controls', "
                "'compliance_assessments', 'incidents', 'assets', 'vulnerabilities', "
                "'evidences'."
            )
        ),
        params_json: str = Field(
            default="{}",
            description="JSON string of list filters (e.g. folder, limit) for the client.",
        ),
        ingest_attachments: bool = Field(
            default=True,
            description="For kind='evidences', also store attachment file bytes as :Blob/:MediaAsset.",
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """List a CISO Assistant GRC record kind and natively ingest it into epistemic-graph.

        Maps records to typed OWL nodes (``:RiskScenario`` / ``:Control`` / ``:Audit`` /
        ``:Incident`` / ``:Asset`` / ``:Vulnerability``) or, for evidences, ``:Document``
        nodes plus attachment blobs. Best-effort — returns ``{"ingested": null}`` when no
        engine is reachable. CONCEPT:AU-KG.ingest.enterprise-source-extractor.
        """
        if kind not in _KIND_MAP:
            return {"error": f"Unknown kind '{kind}'. Valid: {sorted(_KIND_MAP)}"}
        if ctx:
            await ctx.info(f"ciso_ingest listing {kind}")
        try:
            kwargs = json.loads(params_json) if params_json else {}
        except Exception as e:  # noqa: BLE001
            return {"error": f"Invalid params_json: {e}"}
        if not isinstance(kwargs, dict):
            return {"error": "params_json must decode to a JSON object"}
        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        from ciso_assistant_api import kg_ingest

        list_method, mapper_name = _KIND_MAP[kind]
        resp = getattr(client, list_method)(**kwargs)
        records = _records(resp)
        result = getattr(kg_ingest, mapper_name)(records)

        out: dict[str, Any] = {"kind": kind, "listed": len(records), "ingested": result}

        if kind == "evidences" and ingest_attachments:
            out["attachments"] = _ingest_evidence_blobs(client, records)
        return out

    return None


def _ingest_evidence_blobs(
    client: Any, records: list[dict[str, Any]]
) -> dict[str, int]:
    """Fetch each evidence's attachment bytes and store them as KG blobs."""
    from ciso_assistant_api.kg_media import ingest_evidence_attachment

    stored = 0
    for rec in records:
        rid = rec.get("id")
        if rid is None or not rec.get("attachment"):
            continue
        try:
            resp = client.api_evidences_attachment_retrieve(id=rid)
        except Exception as e:  # noqa: BLE001 — one bad attachment shouldn't abort
            logger.debug("attachment fetch failed for evidence %s: %s", rid, e)
            continue
        raw = getattr(resp, "response", None)
        data = getattr(raw, "content", None) if raw is not None else None
        mime = "application/octet-stream"
        if raw is not None:
            mime = (raw.headers or {}).get("Content-Type", mime).split(";")[0]
        result = ingest_evidence_attachment(
            data,
            evidence_id=rid,
            name=rec.get("attachment") or rec.get("name"),
            mime_type=mime,
            ref_id=rec.get("ref_id"),
            link=rec.get("link"),
        )
        if result is not None:
            stored += 1
    return {"stored": stored}
