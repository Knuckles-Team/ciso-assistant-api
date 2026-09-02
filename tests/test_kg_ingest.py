"""Native epistemic-graph typed-node ingestion — Wire-First coverage.

Exercises the real ``ingest_entities`` / ``ingest_documents`` seam and the CISO
Assistant record → typed-node mappers with a fake ChangeEnvelope-capable engine
client (no engine required), asserting the committed nodes/edges and the
class/id mapping. CONCEPT:AU-KG.ingest.enterprise-source-extractor.

The fake client mirrors agent-utilities' own sanctioned test double
(``agent-utilities/tests/knowledge_graph/test_native_ingest.py``) — the ``txn``-only
fake is retired; ``native_ingest`` now hard-requires an injected client exposing
``.changes``/``.nodes``/``.rdf``/``.supports()``. Unlike most fleet connectors,
``ciso_assistant_api.kg_ingest`` is a **best-effort** surface (its MCP tools must
never raise when the KG stack is down), so it converts ``NativeIngestError`` into
``None`` rather than propagating it — those semantics are exercised explicitly
below.
"""

from __future__ import annotations

from typing import Any

import msgpack
import pytest
from agent_utilities.knowledge_graph.core.session import GraphSession, use_session
from agent_utilities.security.actor_identity import ActorType
from agent_utilities.security.brain_context import ActorContext, use_actor

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


@pytest.fixture(autouse=True)
def _governed_session():
    actor = ActorContext(
        actor_id="subject:opaque:synthetic",
        actor_type=ActorType.AUTOMATED_SERVICE,
        roles=(),
        tenant_id="tenant:opaque:synthetic",
        authenticated=True,
    )
    session = GraphSession(
        actor=actor,
        tenant=actor.tenant_id,
        scopes=frozenset({"kg:write"}),
        graph="graph:opaque:synthetic",
        policy_version="policy:opaque:synthetic",
        audience="epistemic-graph",
    )
    with use_actor(actor), use_session(session):
        yield


class _FakeNodes:
    def __init__(self) -> None:
        self.values: dict[str, dict[str, Any]] = {}

    def properties(self, node_id: str) -> dict[str, Any] | None:
        return self.values.get(node_id)

    def list(self) -> list[tuple[str, dict[str, Any]]]:
        return list(self.values.items())


class _FakeChanges:
    def __init__(self, nodes: _FakeNodes) -> None:
        self.nodes = nodes
        self.edges: list[tuple[str, str, dict[str, Any]]] = []
        self.applied: list[dict[str, Any]] = []
        self.records: dict[str, dict[str, Any]] = {}
        self.versions: dict[str, dict[str, Any]] = {}

    def get(self, envelope_id: str) -> dict[str, Any] | None:
        return self.records.get(envelope_id)

    def content_version(self, object_id: str) -> dict[str, Any] | None:
        return self.versions.get(object_id)

    def cursor(self, _source: str, _partition: str = "") -> None:
        return None

    def apply(self, envelope: dict[str, Any]) -> dict[str, Any]:
        self.applied.append(envelope)
        mutation = envelope["mutation"]
        for operation in mutation["operations"]:
            method = operation["method"]
            params = method["params"]
            properties = msgpack.unpackb(params["properties_msgpack"], raw=False)
            if method["method"] == "AddNode":
                self.nodes.values[params["node_id"]] = properties
            elif method["method"] == "AddEdge":
                self.edges.append(
                    (params["source_id"], params["target_id"], properties)
                )
        version = envelope["content_version"]
        self.versions[version["object_id"]] = version
        self.records[envelope["envelope_id"]] = envelope
        return {
            "batch_id": mutation["batch_id"],
            "replayed": False,
            "projection_pending": False,
        }


class _FakeRdf:
    def validate_shacl(self, _shapes: str, _data_graph: str) -> dict[str, Any]:
        return {"conforms": True, "results": []}


class _FakeClient:
    def __init__(self) -> None:
        self.nodes = _FakeNodes()
        self.changes = _FakeChanges(self.nodes)
        self.rdf = _FakeRdf()

    @staticmethod
    def supports(operation: str) -> bool:
        return operation == "ApplyChangeEnvelope"


def test_ingest_entities_writes_nodes_and_edges():
    c = _FakeClient()
    res = ingest_entities(
        [
            {"id": "a", "node_type": "RiskScenario", "name": "s"},
            {"id": "b", "node_type": "Control"},
        ],
        [{"source": "a", "target": "b", "relationship": "mitigatedBy"}],
        client=c,
    )
    assert res == {"nodes": 2, "edges": 1}
    assert set(c.nodes.values) == {"a", "b"}
    assert c.nodes.values["a"]["source"] == "ciso-assistant-api"
    assert c.nodes.values["a"]["domain"] == "ciso"
    assert c.changes.edges == [("a", "b", {"relationship": "mitigatedBy"})]


def test_ingest_risk_scenarios_maps_class_and_links():
    c = _FakeClient()
    res = ingest_risk_scenarios(
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
        client=c,
    )
    assert res == {"nodes": 1, "edges": 3}
    node = c.nodes.values["ciso:riskscenario:rs-1"]
    assert node["node_type"] == "RiskScenario"
    assert node["refId"] == "R.1"
    assert node["riskTreatment"] == "mitigate"
    assert node["externalToolId"] == "rs-1"
    assert (
        "ciso:riskscenario:rs-1",
        "ciso:threat:t-1",
        {"relationship": "hasThreat"},
    ) in c.changes.edges
    assert (
        "ciso:riskscenario:rs-1",
        "ciso:control:c-1",
        {"relationship": "mitigatedBy"},
    ) in c.changes.edges
    assert (
        "ciso:riskscenario:rs-1",
        "ciso:asset:as-1",
        {"relationship": "affectsAsset"},
    ) in c.changes.edges


def test_ingest_applied_controls_maps_control():
    c = _FakeClient()
    res = ingest_applied_controls(
        [{"id": "c-9", "name": "MFA", "status": "active", "priority": "P1"}],
        client=c,
    )
    assert res == {"nodes": 1, "edges": 0}
    node = c.nodes.values["ciso:control:c-9"]
    assert node["node_type"] == "Control"
    assert node["controlStatus"] == "active"
    assert node["controlPriority"] == "P1"


def test_ingest_compliance_assessments_links_framework():
    c = _FakeClient()
    res = ingest_compliance_assessments(
        [
            {
                "id": "a-1",
                "name": "ISO 27001 audit",
                "status": "in_progress",
                "progress": 42,
                "framework": {"id": "fw-1"},
            }
        ],
        client=c,
    )
    assert res == {"nodes": 1, "edges": 1}
    node = c.nodes.values["ciso:audit:a-1"]
    assert node["node_type"] == "Audit"
    assert node["complianceProgress"] == 42
    assert (
        "ciso:audit:a-1",
        "ciso:framework:fw-1",
        {"relationship": "assessesFramework"},
    ) in c.changes.edges


def test_ingest_incidents_and_assets_and_vulns():
    c = _FakeClient()
    assert ingest_incidents(
        [{"id": "i-1", "name": "Breach", "severity": "1", "assets": ["as-2"]}],
        client=c,
    ) == {"nodes": 1, "edges": 1}
    assert c.nodes.values["ciso:incident:i-1"]["node_type"] == "Incident"

    c2 = _FakeClient()
    assert ingest_assets(
        [{"id": "as-3", "name": "DB", "type": "primary"}], client=c2
    ) == {"nodes": 1, "edges": 0}
    assert c2.nodes.values["ciso:asset:as-3"]["asset_type"] == "primary"

    c3 = _FakeClient()
    assert ingest_vulnerabilities(
        [{"id": "v-1", "name": "CVE", "severity": "high", "applied_controls": ["c-1"]}],
        client=c3,
    ) == {"nodes": 1, "edges": 1}
    assert c3.nodes.values["ciso:vulnerability:v-1"]["node_type"] == "Vulnerability"


def test_ingest_risk_assessments_links_scenarios():
    c = _FakeClient()
    res = ingest_risk_assessments(
        [{"id": "ra-1", "name": "Q3", "risk_scenarios": ["rs-1", "rs-2"]}],
        client=c,
    )
    assert res == {"nodes": 1, "edges": 2}
    assert c.nodes.values["ciso:riskassessment:ra-1"]["node_type"] == "RiskAssessment"


def test_ingest_evidences_as_documents():
    c = _FakeClient()
    res = ingest_evidences(
        [{"id": "e-1", "name": "Pentest report", "description": "2024 scope"}],
        client=c,
    )
    assert res == {"nodes": 1, "edges": 0}
    node = c.nodes.values["ciso:evidence:e-1"]
    assert node["node_type"] == "Document"
    assert "Pentest report" in node["text"]


def test_ingest_documents_requires_text():
    c = _FakeClient()
    assert ingest_documents([{"id": "d-1"}], client=c) is None
    assert c.changes.applied == []


def test_ingest_redacts_personal_data_and_locations():
    c = _FakeClient()
    result = ingest_documents(
        [
            {
                "id": "d-2",
                "text": "Contact person@example.invalid for details",
                "source_uri": "https://private.example.invalid/record/2",
            }
        ],
        client=c,
    )
    assert result == {"nodes": 1, "edges": 0}
    node = c.nodes.values["d-2"]
    assert "[REDACTED_EMAIL]" in node["text"]
    assert node["source_uri"] == "[REDACTED_LOCATION]"
    assert node["privacy_redactions"] == 2


def test_ingest_noops_without_engine():
    # No injected client + no reachable engine -> clean no-op (best-effort surface).
    assert ingest_entities([{"id": "a", "node_type": "Control"}]) is None


def test_ingest_rejects_retired_structural_alias_as_noop():
    # ciso_assistant_api's tool surface is best-effort (never raises): a malformed
    # record (the retired ``type`` alias instead of canonical ``node_type``) is
    # reported back as a clean no-op rather than propagating NativeIngestError.
    c = _FakeClient()
    assert ingest_entities([{"id": "a", "type": "Control"}], client=c) is None
    assert c.changes.applied == []


def test_ingest_empty_is_noop():
    assert ingest_entities([], client=_FakeClient()) is None
    assert ingest_risk_scenarios([], client=_FakeClient()) is None
    assert ingest_assets([], client=_FakeClient()) is None
