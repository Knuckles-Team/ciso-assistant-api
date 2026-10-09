"""Epistemic-graph blob ingestion for CISO Assistant evidence attachments.

CONCEPT:AU-KG.ingest.list-durable-media. Evidence in a GRC program is only as good as
its attached artifact (a scan, a signed policy PDF, an exported report). When a live
epistemic-graph engine is reachable, an evidence attachment's raw bytes are stored as a
content-addressed **blob** with a ``:MediaAsset`` graph node (carrying its evidence
metadata) in ONE cross-modal ACID commit, via ``agent_connector_sdk.ingest``'s
``ChangeSet(media=(MediaAsset(...),))`` + ``KnowledgeIngest.submit``.

Entirely best-effort and dependency-/engine-guarded: with no KG stack or no reachable
engine every entry point **no-ops** (returns ``None``), so the connector keeps working
with zero KG infrastructure. The stored asset id is ``blob:<digest>``-derived (read back
from the commit receipt's raw admissions), so it can be linked to the matching
``:Evidence`` document via ``:hasAttachment``.
"""

from __future__ import annotations

import logging
from typing import Any

from agent_connector_sdk.ingest import (
    ChangeSet,
    IngestBinding,
    IngestError,
    KnowledgeIngest,
    MediaAsset,
    current_ingest,
)

logger = logging.getLogger("ciso_assistant_api.kg_media")

_BINDING = IngestBinding(connector="ciso-assistant-api", stream="ciso")


async def ingest_evidence_attachment(
    data: bytes | None,
    *,
    evidence_id: str | int,
    name: str | None = None,
    mime_type: str = "application/octet-stream",
    ref_id: str | None = None,
    link: str | None = None,
    ingest: KnowledgeIngest | None = None,
    content_policy_approved: bool = False,
) -> dict[str, Any] | None:
    """Store an evidence attachment's bytes as a blob + ``:MediaAsset`` in the KG.

    Returns ``{asset_id, digest, size_bytes}`` on success, or ``None`` when content-
    policy approval is absent, there is no engine, there are no bytes, or the store
    failed. ``ingest`` may be injected for a policy-controlled caller; the public MCP
    ingestion workflow does not authorize this content-bearing persistence path.
    """
    if not data or not content_policy_approved:
        return None

    if mime_type.startswith("image"):
        media_type = "image"
    elif mime_type == "application/pdf":
        media_type = "document"
    else:
        media_type = "file"

    extra: dict[str, Any] = {"evidence_id": str(evidence_id), "media_type": media_type}
    if ref_id:
        extra["ref_id"] = ref_id
    # ``link`` is accepted as transient source context only. A deployment URL can
    # reveal environment topology, so it never crosses the durable media boundary.
    display_name = name or f"evidence-{evidence_id}"

    asset = MediaAsset(data=data, mime_type=mime_type, name=display_name, properties=extra)
    change_set = ChangeSet(media=(asset,))
    try:
        service = ingest or current_ingest()
        receipt = await service.submit(_BINDING, change_set)
    except IngestError as exc:
        logger.warning("KG media ingest failed (exception_type=%s)", type(exc).__name__)
        return None

    admission = next(
        (a for a in receipt.raw_admissions if a.record_id.startswith("blob:")), None
    )
    if admission is None:
        return None

    logger.info("KG media ingest stored one policy-approved attachment")
    return {
        "asset_id": admission.record_id,
        "digest": admission.raw_digest,
        "size_bytes": len(data),
    }
