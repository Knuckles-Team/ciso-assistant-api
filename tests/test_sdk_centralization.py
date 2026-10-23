"""CONN-CISO-ASSISTANT-API-R005 and R006: the SDK governed client carries all HTTP."""

import dataclasses
import pathlib
import tomllib
from unittest.mock import patch

import httpx
import pytest
from agent_connector_sdk.exceptions import AuthError, UnauthorizedError
from agent_connector_sdk.http.client import create_http_client

from ciso_assistant_api.api_client import Api

ROOT = pathlib.Path(__file__).resolve().parents[1]
URL = "https://service.example.invalid"


def _api(handler, **kwargs) -> Api:
    def build(options, transport=None):
        plain = dataclasses.replace(
            options, pin_egress=False, allowed_private_hosts=(), allow_loopback=False
        )
        return create_http_client(plain, transport=httpx.MockTransport(handler))

    with patch("ciso_assistant_api.api.api_client_base.create_http_client", build):
        return Api(url=URL, **kwargs)


@pytest.mark.spec("CONN-CISO-ASSISTANT-API-R005")
def test_transient_status_is_retried_by_the_sdk_policy():
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        if len(calls) == 1:
            return httpx.Response(503, headers={"Retry-After": "0"})
        return httpx.Response(200, json={"results": []})

    api = _api(handler, token="t", max_retries=2)
    assert api.api_request("GET", "/api/assets/").status_code == 200
    assert len(calls) == 2
    assert calls[0].headers["Authorization"] == "Token t"


@pytest.mark.spec("CONN-CISO-ASSISTANT-API-R005")
def test_exhausted_retries_return_the_last_response():
    api = _api(lambda r: httpx.Response(503), token="t", max_retries=0)
    assert api.api_request("GET", "/api/assets/").status_code == 503


@pytest.mark.spec("CONN-CISO-ASSISTANT-API-R005")
def test_no_direct_requests_dependency_or_import():
    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    assert not [
        dep for dep in project["project"]["dependencies"] if dep.startswith("requests")
    ]
    for path in (ROOT / "ciso_assistant_api").rglob("*.py"):
        text = path.read_text(encoding="utf-8")
        assert "import requests" not in text, path


@pytest.mark.spec("CONN-CISO-ASSISTANT-API-R006")
def test_transport_failure_keeps_the_runtime_error_contract():
    def boom(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("down", request=request)

    api = _api(boom, token="t", max_retries=0)
    with pytest.raises(RuntimeError, match="CISO Assistant request failed"):
        api.api_request("GET", "/api/assets/")


@pytest.mark.spec("CONN-CISO-ASSISTANT-API-R006")
def test_rejected_credentials_map_to_typed_errors():
    assert pytest.raises(
        AuthError,
        _api(lambda r: httpx.Response(401), token="t").api_request,
        "GET",
        "/x",
    )
    assert pytest.raises(
        UnauthorizedError,
        _api(lambda r: httpx.Response(403), token="t").api_request,
        "GET",
        "/x",
    )
