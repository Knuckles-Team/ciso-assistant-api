import dataclasses
from unittest.mock import patch

import httpx
import pytest

reason = "Unit tests using mocks"


@pytest.fixture(autouse=True)
def mock_env(monkeypatch):
    monkeypatch.setenv("CISO_ASSISTANT_URL", "https://test.my.ciso_assistant.com")
    monkeypatch.setenv("CISO_ASSISTANT_TOKEN_REF", "env://TEST_CISO_TOKEN")
    monkeypatch.setenv("TEST_CISO_TOKEN", "mock_token")
    monkeypatch.delenv("ENABLE_DELEGATION", raising=False)


def _make_payload(payload=None):
    return payload if payload is not None else {"id": 1, "name": "test", "content": []}


@pytest.fixture(autouse=True)
def mock_session():
    """Route the governed client through an in-process transport (no network)."""
    from agent_connector_sdk.http.client import create_http_client

    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return httpx.Response(
            200,
            json=_make_payload(),
            headers={"X-Total-Pages": "1"},
        )

    def build(options, transport=None):
        # No DNS pinning for the in-process transport: hosts are fictional.
        plain = dataclasses.replace(
            options, pin_egress=False, allowed_private_hosts=(), allow_loopback=False
        )
        return create_http_client(plain, transport=httpx.MockTransport(handler))

    with patch("ciso_assistant_api.api.api_client_base.create_http_client", build):
        yield calls
