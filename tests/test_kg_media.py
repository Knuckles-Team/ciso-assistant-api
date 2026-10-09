"""Epistemic-graph blob ingestion for evidence attachments — Wire-First coverage.

Exercises ``ingest_evidence_attachment`` against a fake ``agent_connector_sdk.ingest``
transport (no engine required), asserting the stored media asset's bytes, mime type,
evidence provenance, and that missing bytes / absent policy approval / no reachable
engine all no-op cleanly. CONCEPT:AU-KG.ingest.list-durable-media.
"""

from __future__ import annotations

from types import SimpleNamespace
from typing import Any

import pytest
from agent_connector_sdk.ingest import KnowledgeIngest

from ciso_assistant_api.kg_media import ingest_evidence_attachment


class _FakeTransport:
    def __init__(self) -> None:
        self.stored_blobs: list[bytes] = []
        self.requests: list[Any] = []

    async def source_status(self, _connector: str, _stream: str) -> Any:
        return SimpleNamespace(accepted_checkpoint=None)

    async def store_blob(self, data: bytes) -> str:
        self.stored_blobs.append(data)
        return "deadbeef"

    async def submit(self, request: Any) -> Any:
        self.requests.append(request)
        media_records = [r for r in request.records if r.record_id == "blob:deadbeef"]
        return SimpleNamespace(
            affected_count=len(request.records),
            relationship_count=len(request.relationships),
            raw_admissions=[
                SimpleNamespace(
                    record_id=record.record_id, raw_digest="deadbeef", deduplicated=False
                )
                for record in media_records
            ],
        )


class _UnavailableTransport:
    async def source_status(self, _connector: str, _stream: str) -> Any:
        raise RuntimeError("epistemic-graph is unreachable")

    async def submit(self, _request: Any) -> Any:
        raise RuntimeError("epistemic-graph is unreachable")

    async def store_blob(self, _data: bytes) -> str:
        raise RuntimeError("epistemic-graph is unreachable")


@pytest.fixture
def ingest() -> tuple[KnowledgeIngest, _FakeTransport]:
    transport = _FakeTransport()
    return KnowledgeIngest(transport, loop=None), transport


@pytest.mark.asyncio
async def test_ingest_evidence_attachment_stores_blob(ingest):
    service, transport = ingest
    res = await ingest_evidence_attachment(
        b"%PDF-1.7 report bytes",
        evidence_id="e-1",
        name="pentest.pdf",
        mime_type="application/pdf",
        ref_id="EV.1",
        link="https://service.example.invalid/e/1",
        ingest=service,
        content_policy_approved=True,
    )
    assert res == {"asset_id": "blob:deadbeef", "digest": "deadbeef", "size_bytes": 21}
    assert transport.stored_blobs == [b"%PDF-1.7 report bytes"]
    request = transport.requests[0]
    media_record = next(r for r in request.records if r.record_id == "blob:deadbeef")
    assert media_record.payload["media_type"] == "document"
    assert media_record.payload["name"] == "pentest.pdf"
    assert media_record.payload["evidence_id"] == "e-1"
    assert media_record.payload["ref_id"] == "EV.1"
    assert "link" not in media_record.payload


@pytest.mark.asyncio
async def test_image_mime_maps_to_image(ingest):
    service, transport = ingest
    await ingest_evidence_attachment(
        b"\x89PNG data",
        evidence_id="e-2",
        mime_type="image/png",
        ingest=service,
        content_policy_approved=True,
    )
    media_record = transport.requests[0].records[0]
    assert media_record.payload["media_type"] == "image"
    assert media_record.payload["name"] == "evidence-e-2"


@pytest.mark.asyncio
async def test_no_bytes_is_noop(ingest):
    service, transport = ingest
    assert (
        await ingest_evidence_attachment(
            b"", evidence_id="e-3", ingest=service, content_policy_approved=True
        )
        is None
    )
    assert transport.stored_blobs == []


@pytest.mark.asyncio
async def test_no_engine_is_noop():
    # No reachable engine -> clean no-op.
    service = KnowledgeIngest(_UnavailableTransport(), loop=None)
    assert (
        await ingest_evidence_attachment(
            b"data", evidence_id="e-4", ingest=service, content_policy_approved=True
        )
        is None
    )


@pytest.mark.asyncio
async def test_content_policy_defaults_to_deny(ingest):
    service, transport = ingest
    assert (
        await ingest_evidence_attachment(b"data", evidence_id="e-5", ingest=service)
        is None
    )
    assert transport.stored_blobs == []
