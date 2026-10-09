"""Epistemic-graph typed-node ingestion — Wire-First coverage.

Exercises the real ``ingest_entities`` / ``ingest_documents`` seam and the CISO
Assistant record → typed-node mappers against a fake ``agent_connector_sdk.ingest``
transport (no engine required), asserting the committed records/relationships and
the class/id mapping. CONCEPT:AU-KG.ingest.enterprise-source-extractor.

Unlike most fleet connectors, ``ciso_assistant_api.kg_ingest`` is a **best-effort**
surface (its MCP tools must never raise when the KG stack is down), so it converts
``IngestError`` into ``None`` rather than propagating it -- those semantics are
exercised explicitly below.
"""

from __future__ import annotations

from types import SimpleNamespace
from typing import Any

import pytest
from agent_connector_sdk.ingest import KnowledgeIngest
from epistemic_graph.generated.source_ingestion import SourceIngestionRequest

from ciso_assistant_api.kg_ingest import (
    ingest_applied_controls,
    ingest_assets,
    ingest_compliance_assessments,
    ingest_documents,
    ingest_entities,
    ingest_evidences,
    ingest_incidents,
    ingest_risk_assessments,
    ingest_risk_scenarios,
    ingest_vulnerabilities,
)


class _FakeTransport:
    """Records every submitted request; no epistemic-graph engine required."""

    def __init__(self) -> None:
        self.requests: list[SourceIngestionRequest] = []

    async def source_status(self, _connector: str, _stream: str) -> Any:
        return SimpleNamespace(accepted_checkpoint=None)

    async def submit(self, request: SourceIngestionRequest) -> Any:
        self.requests.append(request)
        return SimpleNamespace(
            affected_count=len(request.records),
            relationship_count=len(request.relationships),
        )

    async def store_blob(self, _data: bytes) -> str:
        raise AssertionError("this test exercises node/document ingestion only")


class _UnavailableTransport:
    """Simulates no reachable engine for the best-effort no-op assertions."""

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


@pytest.fixture
def unavailable_ingest() -> KnowledgeIngest:
    return KnowledgeIngest(_UnavailableTransport(), loop=None)


@pytest.mark.asyncio
async def test_ingest_entities_writes_nodes_and_edges(ingest):
    service, transport = ingest
    res = await ingest_entities(
        [
            {"id": "a", "node_type": "RiskScenario", "name": "s"},
            {"id": "b", "node_type": "Control"},
        ],
        [{"source": "a", "target": "b", "relationship": "mitigatedBy"}],
        ingest=service,
    )
    assert res == {"nodes": 2, "edges": 1}
    request = transport.requests[0]
    record_ids = {record.record_id for record in request.records}
    assert record_ids == {"a", "b"}
    assert request.relationships[0].relation_reference.endswith(
        "resources/RiskScenario/relations/mitigatedBy"
    )


@pytest.mark.asyncio
async def test_ingest_risk_scenarios_maps_class_and_links(ingest):
    service, transport = ingest
    res = await ingest_risk_scenarios(
        [
            {
                "id": "rs-1",
                "name": "Ransomware",
                "ref_id": "R.1",
                "treatment": "mitigate",
                "residual_level": "low",
                "threats": [{"id": "t-1"}],
                "applied_controls": ["c-1"],
                "assets": [{"id": "as-1"}],
            }
        ],
        ingest=service,
    )
    assert res == {"nodes": 1, "edges": 3}
    request = transport.requests[0]
    node = next(r for r in request.records if r.record_id == "ciso:riskscenario:rs-1")
    assert node.payload["refId"] == "R.1"
    assert node.payload["riskTreatment"] == "mitigate"
    assert node.payload["externalToolId"] == "rs-1"
    relation_refs = {r.relation_reference for r in request.relationships}
    assert any(ref.endswith("relations/hasThreat") for ref in relation_refs)
    assert any(ref.endswith("relations/mitigatedBy") for ref in relation_refs)
    assert any(ref.endswith("relations/affectsAsset") for ref in relation_refs)


@pytest.mark.asyncio
async def test_ingest_applied_controls_maps_control(ingest):
    service, transport = ingest
    res = await ingest_applied_controls(
        [{"id": "c-9", "name": "MFA", "status": "active", "priority": "P1"}],
        ingest=service,
    )
    assert res == {"nodes": 1, "edges": 0}
    node = transport.requests[0].records[0]
    assert node.record_id == "ciso:control:c-9"
    assert node.payload["controlStatus"] == "active"
    assert node.payload["controlPriority"] == "P1"


@pytest.mark.asyncio
async def test_ingest_compliance_assessments_links_framework(ingest):
    service, transport = ingest
    res = await ingest_compliance_assessments(
        [
            {
                "id": "a-1",
                "name": "ISO 27001 audit",
                "status": "in_progress",
                "progress": 42,
                "framework": {"id": "fw-1"},
            }
        ],
        ingest=service,
    )
    assert res == {"nodes": 1, "edges": 1}
    node = transport.requests[0].records[0]
    assert node.record_id == "ciso:audit:a-1"
    assert node.payload["complianceProgress"] == 42
    assert transport.requests[0].relationships[0].relation_reference.endswith(
        "resources/Audit/relations/assessesFramework"
    )


@pytest.mark.asyncio
async def test_ingest_incidents_and_assets_and_vulns(ingest):
    service, transport = ingest
    assert await ingest_incidents(
        [{"id": "i-1", "name": "Breach", "severity": "1", "assets": ["as-2"]}],
        ingest=service,
    ) == {"nodes": 1, "edges": 1}
    assert transport.requests[0].records[0].record_id == "ciso:incident:i-1"

    service2 = KnowledgeIngest(_FakeTransport(), loop=None)
    assert await ingest_assets(
        [{"id": "as-3", "name": "DB", "type": "primary"}], ingest=service2
    ) == {"nodes": 1, "edges": 0}

    service3 = KnowledgeIngest(_FakeTransport(), loop=None)
    assert await ingest_vulnerabilities(
        [{"id": "v-1", "name": "CVE", "severity": "high", "applied_controls": ["c-1"]}],
        ingest=service3,
    ) == {"nodes": 1, "edges": 1}


@pytest.mark.asyncio
async def test_ingest_risk_assessments_links_scenarios(ingest):
    service, transport = ingest
    res = await ingest_risk_assessments(
        [{"id": "ra-1", "name": "Q3", "risk_scenarios": ["rs-1", "rs-2"]}],
        ingest=service,
    )
    assert res == {"nodes": 1, "edges": 2}
    assert transport.requests[0].records[0].record_id == "ciso:riskassessment:ra-1"


@pytest.mark.asyncio
async def test_ingest_evidences_as_documents(ingest):
    service, transport = ingest
    res = await ingest_evidences(
        [{"id": "e-1", "name": "Pentest report", "description": "2024 scope"}],
        ingest=service,
    )
    assert res == {"nodes": 1, "edges": 0}
    node = transport.requests[0].records[0]
    assert node.record_id == "ciso:evidence:e-1"
    assert "Pentest report" in node.payload["text"]


@pytest.mark.asyncio
async def test_ingest_documents_requires_text(ingest):
    service, transport = ingest
    assert await ingest_documents([{"id": "d-1"}], ingest=service) is None
    assert transport.requests == []


@pytest.mark.asyncio
async def test_ingest_redacts_personal_data_and_locations(ingest):
    service, transport = ingest
    result = await ingest_documents(
        [
            {
                "id": "d-2",
                "text": "Contact person@example.invalid for details",
                "source_uri": "https://private.example.invalid/record/2",
            }
        ],
        ingest=service,
    )
    assert result == {"nodes": 1, "edges": 0}
    node = transport.requests[0].records[0]
    assert "[REDACTED_EMAIL]" in node.payload["text"]
    assert node.payload["source_uri"] == "[REDACTED_LOCATION]"
    assert node.payload["privacy_redactions"] == 2


@pytest.mark.asyncio
async def test_ingest_noops_without_engine(unavailable_ingest):
    # No reachable engine -> clean no-op (best-effort surface).
    assert (
        await ingest_entities(
            [{"id": "a", "node_type": "Control"}], ingest=unavailable_ingest
        )
        is None
    )


@pytest.mark.asyncio
async def test_ingest_rejects_retired_structural_alias_as_noop(ingest):
    # ciso_assistant_api's tool surface is best-effort (never raises): a malformed
    # record (the retired ``type`` alias instead of canonical ``node_type``) is
    # reported back as a clean no-op rather than propagating IngestError.
    service, transport = ingest
    assert await ingest_entities([{"id": "a", "type": "Control"}], ingest=service) is None
    assert transport.requests == []


@pytest.mark.asyncio
async def test_ingest_empty_is_noop(ingest):
    service, _ = ingest
    assert await ingest_entities([], ingest=service) is None
    assert await ingest_risk_scenarios([], ingest=service) is None
    assert await ingest_assets([], ingest=service) is None
