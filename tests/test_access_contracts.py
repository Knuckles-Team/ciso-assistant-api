"""Access contracts bind fields the served read tools return."""

import asyncio
import json
import sys
from pathlib import Path

import pytest
from fastmcp import Client
from scion_sdk.access_contract import parse_access_contracts

from tests.conftest import _make_response

ROOT = Path(__file__).resolve().parents[1]
ONTOLOGY = ROOT / "ciso_assistant_api/ontology"


def _contracts():
    text = (ONTOLOGY / "access_contracts.ttl").read_text()
    return {c.entity: c for c in parse_access_contracts(text)}


def _serve(monkeypatch, mock_session, contract, recording):
    mock_session.request.return_value = _make_response(recording)
    monkeypatch.setattr(sys, "argv", ["ciso-assistant-mcp", "--transport", "stdio"])
    from ciso_assistant_api.mcp_server import get_mcp_instance

    mcp, _args, _mw, _tags = get_mcp_instance()

    async def call():
        async with Client(mcp) as client:
            return await client.call_tool(contract.operation, {})

    result = asyncio.run(call())
    return result.data if result.data is not None else result.structured_content


@pytest.mark.spec("CONN-CISO-ASSISTANT-API-CONNECTOR-CONTENT-R002")
@pytest.mark.parametrize(
    ("entity", "fields"),
    [
        ("applied_control", {"status", "risk_scenarios"}),
        ("risk_scenario", {"assets", "name"}),
    ],
)
def test_competency_contracts_certified(monkeypatch, mock_session, entity, fields):
    contract = _contracts()[entity]
    recording = json.loads((ROOT / f"tests/recordings/{entity}.json").read_text())
    ontology = (ONTOLOGY / "ciso.ttl").read_text()
    assert contract.access_kind == "mcp_tool"
    assert contract.key_field == "id"
    assert {field for _, field in contract.predicates} == fields
    for prop, _ in contract.predicates:
        local = prop.rsplit("#", 1)[-1]
        assert local == "name" or f":{local} a owl:DatatypeProperty" in ontology
    payload = _serve(monkeypatch, mock_session, contract, recording)
    records = payload
    for part in (contract.records_path or "").split("."):
        if part:
            records = records[part]
    assert records
    for record in records:
        assert contract.key_field in record
        assert all(field in record for field in fields)
