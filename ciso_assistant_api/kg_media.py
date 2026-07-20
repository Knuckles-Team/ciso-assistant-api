"""Native epistemic-graph blob ingestion for CISO Assistant evidence attachments.

CONCEPT:AU-KG.ingest.list-durable-media. Evidence in a GRC program is only as good as
its attached artifact (a scan, a signed policy PDF, an exported report). When a live
epistemic-graph engine is reachable, an evidence attachment's raw bytes are stored as a
content-addressed **blob** with a ``:MediaAsset`` graph node (carrying its evidence
metadata) in ONE cross-modal ACID commit, via the agent-utilities ``MediaStore`` reached
through :func:`ciso_assistant_api.kg_ingest.media_store`.

Entirely best-effort and dependency-/engine-guarded: with no KG stack or no reachable
engine every entry point **no-ops** (returns ``None``), so the connector keeps working
with zero KG infrastructure. The stored asset id is ``ciso:evidence:<id>``-derived, so it
can be linked to the matching ``:Evidence`` document via ``:hasAttachment``.
"""

from __future__ import annotations

import logging
from typing import Any

from agent_utilities.security.persistence_privacy import sanitize_for_persistence

from ciso_assistant_api.kg_ingest import media_store as _default_media_store

logger = logging.getLogger("ciso_assistant_api.kg_media")

_SOURCE = "ciso-assistant-api"


def ingest_evidence_attachment(
    data: bytes | None,
    *,
    evidence_id: str | int,
    name: str | None = None,
    mime_type: str = "application/octet-stream",
    ref_id: str | None = None,
    link: str | None = None,
    media_store: Any | None = None,
    content_policy_approved: bool = False,
) -> dict[str, Any] | None:
    """Store an evidence attachment's bytes as a blob + ``:MediaAsset`` in the KG.

    Returns the ``store_media`` result (e.g. ``{asset_id, digest, size_bytes, ...}``) on
    success, or ``None`` when content-policy approval is absent, there is no engine,
    there are no bytes, or the store failed. ``media_store`` may be injected for a
    policy-controlled caller; the public MCP ingestion workflow does not authorize
    this content-bearing persistence path.
    """
    if not data or not content_policy_approved:
        return None
    store = media_store if media_store is not None else _default_media_store()
    if store is None:
        return None

    if mime_type.startswith("image"):
        media_type = "image"
    elif mime_type == "application/pdf":
        media_type = "document"
    else:
        media_type = "file"

    extra = {"evidence_id": str(evidence_id)}
    if ref_id:
        extra["ref_id"] = ref_id
    # ``link`` is accepted as transient source context only.  A deployment URL can
    # reveal environment topology, so it never crosses the durable media boundary.
    safe_extra, _ = sanitize_for_persistence(extra)
    display_name, _ = sanitize_for_persistence(name or f"evidence-{evidence_id}")

    try:
        stored = store.store_media(
            data,
            media_type=media_type,
            mime_type=mime_type,
            source=_SOURCE,
            name=display_name,
            extra=safe_extra,
        )
    except Exception as exc:  # noqa: BLE001 — engine/store failure is non-fatal
        logger.warning("KG media ingest failed (exception_type=%s)", type(exc).__name__)
        return None
    if stored is None:
        return None

    logger.info("KG media ingest stored one policy-approved attachment")
    return stored
