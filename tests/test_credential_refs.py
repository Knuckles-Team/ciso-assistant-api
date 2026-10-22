"""Credential reference resolution with the fleet-wide OPENBAO_ADDR (no network)."""

import re
from pathlib import Path

import pytest

from ciso_assistant_api.api_client import Api


@pytest.mark.spec("CONN-CISO-ASSISTANT-API-R001")
def test_sdk_floor_is_declared():
    text = (Path(__file__).parent.parent / "pyproject.toml").read_text()
    floors = re.findall(
        r"agent-connector-sdk(?:\[[^\]]*\])?>=(\d+)\.(\d+)\.(\d+)", text
    )
    assert floors
    for floor in floors:
        assert tuple(map(int, floor)) >= (0, 3, 10)


@pytest.mark.spec("CONN-CISO-ASSISTANT-API-R002")
def test_env_refs_resolve_with_openbao_addr_and_no_token_ref(monkeypatch):
    monkeypatch.setenv("OPENBAO_ADDR", "http://openbao.invalid:8200")
    monkeypatch.delenv("OPENBAO_TOKEN_REF", raising=False)
    monkeypatch.delenv("CISO_ASSISTANT_TOKEN_REF", raising=False)
    monkeypatch.setenv("CISO_ASSISTANT_URL", "https://service.example.invalid")
    monkeypatch.setenv("CISO_ASSISTANT_USERNAME_REF", "env://TEST_CISO_USERNAME")
    monkeypatch.setenv("CISO_ASSISTANT_PASSWORD_REF", "env://TEST_CISO_PASSWORD")
    monkeypatch.setenv("TEST_CISO_USERNAME", "operator")
    monkeypatch.setenv("TEST_CISO_PASSWORD", "pw")
    from ciso_assistant_api.auth import get_client

    assert isinstance(get_client(), Api)
