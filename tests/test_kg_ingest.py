"""Native epistemic-graph typed-node ingestion — Wire-First coverage.

Exercises the real ``ingest_entities`` / ``ingest_documents`` seam and the CISO
Assistant record → typed-node mappers with a fake engine client (no engine required),
asserting the txn add_node/commit + edge calls and the class/id mapping.
CONCEPT:AU-KG.ingest.enterprise-source-extractor.
"""

from __future__ import annotations

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


class _FakeTxn:
    def __init__(self):
        self.nodes = {}
        self.committed = False

    def begin(self, graph=None):
        self.graph = graph
        return "txn-1"

    def add_node(self, txn, node_id, props):
        self.nodes[node_id] = props

    def commit(self, txn):
        self.committed = True
        return True


class _FakeEdges:
    def __init__(self):
        self.edges = []

    def add(self, src, dst, props):
        self.edges.append((src, dst, props))


class _FakeClient:
    def __init__(self):
        self.txn = _FakeTxn()
        self.edges = _FakeEdges()


def test_ingest_entities_writes_nodes_and_edges():
    c = _FakeClient()
    res = ingest_entities(
        [
            {"id": "a", "type": "RiskScenario", "name": "s"},
            {"id": "b", "type": "Control"},
        ],
        [{"source": "a", "target": "b", "type": "mitigatedBy"}],
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 2, "edges": 1}
    assert c.txn.committed is True
    assert set(c.txn.nodes) == {"a", "b"}
    assert c.txn.nodes["a"]["source"] == "ciso-assistant-api"
    assert c.txn.nodes["a"]["domain"] == "ciso"
    assert c.edges.edges == [("a", "b", {"type": "mitigatedBy"})]


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
        graph="__commons__",
    )
    assert res == {"nodes": 1, "edges": 3}
    node = c.txn.nodes["ciso:riskscenario:rs-1"]
    assert node["type"] == "RiskScenario"
    assert node["refId"] == "R.1"
    assert node["riskTreatment"] == "mitigate"
    assert node["externalToolId"] == "rs-1"
    assert (
        "ciso:riskscenario:rs-1",
        "ciso:threat:t-1",
        {"type": "hasThreat"},
    ) in c.edges.edges
    assert (
        "ciso:riskscenario:rs-1",
        "ciso:control:c-1",
        {"type": "mitigatedBy"},
    ) in c.edges.edges
    assert (
        "ciso:riskscenario:rs-1",
        "ciso:asset:as-1",
        {"type": "affectsAsset"},
    ) in c.edges.edges


def test_ingest_applied_controls_maps_control():
    c = _FakeClient()
    res = ingest_applied_controls(
        [{"id": "c-9", "name": "MFA", "status": "active", "priority": "P1"}],
        client=c,
    )
    assert res == {"nodes": 1, "edges": 0}
    node = c.txn.nodes["ciso:control:c-9"]
    assert node["type"] == "Control"
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
    node = c.txn.nodes["ciso:audit:a-1"]
    assert node["type"] == "Audit"
    assert node["complianceProgress"] == 42
    assert (
        "ciso:audit:a-1",
        "ciso:framework:fw-1",
        {"type": "assessesFramework"},
    ) in c.edges.edges


def test_ingest_incidents_and_assets_and_vulns():
    c = _FakeClient()
    assert ingest_incidents(
        [{"id": "i-1", "name": "Breach", "severity": "1", "assets": ["as-2"]}],
        client=c,
    ) == {"nodes": 1, "edges": 1}
    assert c.txn.nodes["ciso:incident:i-1"]["type"] == "Incident"

    c2 = _FakeClient()
    assert ingest_assets(
        [{"id": "as-3", "name": "DB", "type": "primary"}], client=c2
    ) == {"nodes": 1, "edges": 0}
    assert c2.txn.nodes["ciso:asset:as-3"]["asset_type"] == "primary"

    c3 = _FakeClient()
    assert ingest_vulnerabilities(
        [{"id": "v-1", "name": "CVE", "severity": "high", "applied_controls": ["c-1"]}],
        client=c3,
    ) == {"nodes": 1, "edges": 1}
    assert c3.txn.nodes["ciso:vulnerability:v-1"]["type"] == "Vulnerability"


def test_ingest_risk_assessments_links_scenarios():
    c = _FakeClient()
    res = ingest_risk_assessments(
        [{"id": "ra-1", "name": "Q3", "risk_scenarios": ["rs-1", "rs-2"]}],
        client=c,
    )
    assert res == {"nodes": 1, "edges": 2}
    assert c.txn.nodes["ciso:riskassessment:ra-1"]["type"] == "RiskAssessment"


def test_ingest_evidences_as_documents():
    c = _FakeClient()
    res = ingest_evidences(
        [{"id": "e-1", "name": "Pentest report", "description": "2024 scope"}],
        client=c,
    )
    assert res == {"nodes": 1, "edges": 0}
    node = c.txn.nodes["ciso:evidence:e-1"]
    assert node["type"] == "Document"
    assert "Pentest report" in node["text"]


def test_ingest_documents_requires_text():
    c = _FakeClient()
    assert ingest_documents([{"id": "d-1"}], client=c) is None


def test_ingest_noops_without_engine():
    assert ingest_entities([{"id": "a", "type": "Control"}]) is None


def test_ingest_empty_is_noop():
    assert ingest_entities([], client=_FakeClient()) is None
    assert ingest_risk_scenarios([], client=_FakeClient()) is None
    assert ingest_assets([], client=_FakeClient()) is None
