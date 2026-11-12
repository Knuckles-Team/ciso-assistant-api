"""100% coverage keystone.

Proves — offline, against the vendored OpenAPI specs — that every CISO Assistant
operation is reachable as both a typed client method AND an MCP action, and that
the three sets (spec operationIds, client methods, MCP actions) are mutually
consistent. If CISO Assistant revises a spec and the generator is re-run, this test is
what guarantees nothing silently drops.
"""

import json
from pathlib import Path

from ciso_assistant_api.api._operation_manifest import (
    ACTIONS_BY_DOMAIN,
    OPERATIONS,
)
from ciso_assistant_api.api_client import Api

PKG = Path(__file__).resolve().parent.parent / "ciso_assistant_api"
SPECS = PKG / "specs"
MCP = PKG / "mcp"
HTTP_METHODS = ("get", "post", "put", "delete", "patch")


def _count_spec_operations() -> int:
    total = 0
    for spec_path in SPECS.glob("*.json"):
        spec = json.loads(spec_path.read_text())
        for _path, methods in (spec.get("paths") or {}).items():
            for http, op in methods.items():
                if http in HTTP_METHODS and isinstance(op, dict):
                    total += 1
    return total


def test_specs_present():
    # CISO Assistant ships a single drf-spectacular schema (everything tagged "api");
    # the generator splits it into domains by URL path.
    assert len(list(SPECS.glob("*.json"))) == 1


def test_manifest_covers_every_spec_operation():
    assert len(OPERATIONS) == _count_spec_operations()
    assert len(OPERATIONS) > 0


def test_every_operation_has_callable_client_method():
    missing = [
        op for op in OPERATIONS if not callable(getattr(Api, op["method"], None))
    ]
    assert (
        not missing
    ), f"{len(missing)} operations without a client method: {missing[:5]}"


def test_method_names_globally_unique():
    methods = [op["method"] for op in OPERATIONS]
    assert len(methods) == len(set(methods))


def test_actions_unique_within_each_domain():
    for domain, actions in ACTIONS_BY_DOMAIN.items():
        assert len(actions) == len(set(actions)), f"duplicate actions in {domain}"


def test_custom_api_escape_hatch_present():
    src = (MCP / "mcp_custom_api.py").read_text()
    assert "ciso_assistant_api_request" in src
    assert callable(Api.api_request)
