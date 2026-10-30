"""Authentication factory tests."""

import pytest
from scion_sdk.exceptions import MissingParameterError, ParameterError

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


class _Resp:
    def __init__(self, status=200, body=None):
        self.status_code = status
        self.ok = status < 400
        self._body = body

    def json(self):
        return self._body


def _login_api(monkeypatch, username, resp):
    api = Api(url="https://service.example.invalid", username=username, password="pw")
    calls = []

    def fake_post(**kw):
        calls.append(kw)
        return resp

    monkeypatch.setattr(api._session, "post", fake_post)
    return api, calls


def test_headless_login_returns_access_token(monkeypatch):
    body = {"status": 200, "meta": {"session_token": "s", "access_token": "knox"}}
    api, calls = _login_api(monkeypatch, "op@example.invalid", _Resp(200, body))
    assert api._ensure_token() == "knox"
    assert calls[0]["url"].endswith("/api/_allauth/app/v1/auth/login")
    assert "/api/iam/login" not in calls[0]["url"]
    assert calls[0]["json"] == {"email": "op@example.invalid", "password": "pw"}
    api2, calls2 = _login_api(monkeypatch, "operator", _Resp(200, body))
    api2._ensure_token()
    assert calls2[0]["json"] == {"username": "operator", "password": "pw"}


def test_configured_token_skips_login(monkeypatch):
    api = Api(url="https://service.example.invalid", token="cfg")

    def boom(**kw):
        raise AssertionError("login must not be called")

    monkeypatch.setattr(api._session, "post", boom)
    assert api._ensure_token() == "cfg"
