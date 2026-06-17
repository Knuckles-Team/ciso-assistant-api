"""Authentication factory tests."""

import pytest
from agent_utilities.core.exceptions import MissingParameterError

from ciso_assistant_api.api_client import Api


def test_get_client_token_path(monkeypatch):
    monkeypatch.setenv("CISO_ASSISTANT_URL", "https://ciso.arpa")
    monkeypatch.setenv("CISO_ASSISTANT_TOKEN", "tok")
    from ciso_assistant_api.auth import get_client

    client = get_client()
    assert isinstance(client, Api)


def test_get_client_username_password(monkeypatch):
    monkeypatch.delenv("CISO_ASSISTANT_TOKEN", raising=False)
    monkeypatch.setenv("CISO_ASSISTANT_URL", "https://ciso.arpa")
    monkeypatch.setenv("CISO_ASSISTANT_USERNAME", "admin@ciso.arpa")
    monkeypatch.setenv("CISO_ASSISTANT_PASSWORD", "secret")
    from ciso_assistant_api.auth import get_client

    client = get_client()
    assert isinstance(client, Api)


def test_url_normalized():
    api = Api(url="ciso.arpa", token="x")
    assert api.url == "https://ciso.arpa"
    assert api.hostname == "ciso.arpa"


def test_explicit_scheme_preserved():
    api = Api(url="http://localhost:8000", token="x")
    assert api.url == "http://localhost:8000"


def test_missing_credentials_raises():
    with pytest.raises(MissingParameterError):
        Api(url="https://ciso.arpa")
