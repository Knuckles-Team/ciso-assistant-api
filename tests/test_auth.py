"""Authentication factory tests."""

import pytest
from agent_utilities.core.exceptions import MissingParameterError, ParameterError

from ciso_assistant_api.api_client import Api


def test_get_client_token_path(monkeypatch):
    monkeypatch.setenv("CISO_ASSISTANT_URL", "https://service.example.invalid")
    monkeypatch.setenv("CISO_ASSISTANT_TOKEN_REF", "env://TEST_CISO_TOKEN")
    monkeypatch.setenv("TEST_CISO_TOKEN", "tok")
    from ciso_assistant_api.auth import get_client

    client = get_client()
    assert isinstance(client, Api)


def test_get_client_username_password(monkeypatch):
    monkeypatch.delenv("CISO_ASSISTANT_TOKEN_REF", raising=False)
    monkeypatch.setenv("CISO_ASSISTANT_URL", "https://service.example.invalid")
    monkeypatch.setenv("CISO_ASSISTANT_USERNAME_REF", "env://TEST_CISO_USERNAME")
    monkeypatch.setenv("CISO_ASSISTANT_PASSWORD_REF", "env://TEST_CISO_PASSWORD")
    monkeypatch.setenv("TEST_CISO_USERNAME", "operator")
    monkeypatch.setenv("TEST_CISO_PASSWORD", "secret")
    from ciso_assistant_api.auth import get_client

    client = get_client()
    assert isinstance(client, Api)


def test_url_normalized():
    api = Api(url="service.example.invalid", token="x")
    assert api.url == "https://service.example.invalid"
    assert api.hostname == "service.example.invalid"


def test_explicit_scheme_preserved():
    api = Api(url="http://localhost:8000", token="x")
    assert api.url == "http://localhost:8000"


def test_missing_credentials_raises():
    with pytest.raises(MissingParameterError):
        Api(url="https://service.example.invalid")


def test_remote_http_is_rejected():
    with pytest.raises(ParameterError, match="must use HTTPS"):
        Api(url="http://service.example.invalid", token="x")


def test_cross_origin_pagination_is_rejected():
    api = Api(url="https://service.example.invalid", token="x")
    with pytest.raises(ParameterError, match="configured origin"):
        api._resolve_url("https://other.example.invalid/api/items", {})
