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
) -> dict[str, Any] | None:
    """Store an evidence attachment's bytes as a blob + ``:MediaAsset`` in the KG.

    Returns the ``store_media`` result (e.g. ``{asset_id, digest, size_bytes, ...}``) on
    success, or ``None`` when there is no engine, no bytes, or the store failed (never
    raises). ``media_store`` may be injected (tests); otherwise one is built on demand.
    """
    if not data:
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
    if link:
        extra["source_url"] = link
    display_name = name or f"evidence-{evidence_id}"

    try:
        stored = store.store_media(
            data,
            media_type=media_type,
            mime_type=mime_type,
            source=_SOURCE,
            name=display_name,
            extra=extra,
        )
    except Exception as e:  # noqa: BLE001 — engine/store failure is non-fatal
        logger.warning("KG media ingest: store_media failed: %s", e)
        return None
    if stored is None:
        return None

    logger.info(
        "KG media ingest: stored evidence %s attachment %s", evidence_id, display_name
    )
    return stored
