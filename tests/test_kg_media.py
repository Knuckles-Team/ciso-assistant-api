"""Native epistemic-graph blob ingestion for evidence attachments — Wire-First coverage.

Exercises ``ingest_evidence_attachment`` with a fake MediaStore (no engine required),
asserting the store_media call carries the evidence provenance and that missing bytes /
no engine no-op cleanly. CONCEPT:AU-KG.ingest.list-durable-media.
"""

from __future__ import annotations

from ciso_assistant_api.kg_media import ingest_evidence_attachment


class _FakeStore:
    def __init__(self):
        self.calls = []

    def store_media(self, data, *, media_type, mime_type, source, name, extra):
        self.calls.append(
            {
                "data": data,
                "media_type": media_type,
                "mime_type": mime_type,
                "source": source,
                "name": name,
                "extra": extra,
            }
        )
        return {"asset_id": "asset-1", "digest": "deadbeef", "size_bytes": len(data)}


def test_ingest_evidence_attachment_stores_blob():
    store = _FakeStore()
    res = ingest_evidence_attachment(
        b"%PDF-1.7 report bytes",
        evidence_id="e-1",
        name="pentest.pdf",
        mime_type="application/pdf",
        ref_id="EV.1",
        link="https://service.example.invalid/e/1",
        media_store=store,
        content_policy_approved=True,
    )
    assert res == {"asset_id": "asset-1", "digest": "deadbeef", "size_bytes": 21}
    call = store.calls[0]
    assert call["media_type"] == "document"
    assert call["source"] == "ciso-assistant-api"
    assert call["name"] == "pentest.pdf"
    assert call["extra"]["evidence_id"] == "e-1"
    assert call["extra"]["ref_id"] == "EV.1"
    assert "source_url" not in call["extra"]


def test_image_mime_maps_to_image():
    store = _FakeStore()
    ingest_evidence_attachment(
        b"\x89PNG data",
        evidence_id="e-2",
        mime_type="image/png",
        media_store=store,
        content_policy_approved=True,
    )
    assert store.calls[0]["media_type"] == "image"
    assert store.calls[0]["name"] == "evidence-e-2"


def test_no_bytes_is_noop():
    store = _FakeStore()
    assert ingest_evidence_attachment(b"", evidence_id="e-3", media_store=store) is None
    assert store.calls == []


def test_no_store_is_noop():
    # No injected store + no reachable engine -> clean no-op.
    assert ingest_evidence_attachment(b"data", evidence_id="e-4") is None


def test_content_policy_defaults_to_deny():
    store = _FakeStore()
    assert (
        ingest_evidence_attachment(b"data", evidence_id="e-5", media_store=store)
        is None
    )
    assert store.calls == []
