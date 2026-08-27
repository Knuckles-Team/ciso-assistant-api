"""Characterization tests: CXA-FL-CISOASSISTANTAPI-01 exact action -> client-method routing.

test_every_mcp_action_routes (tests/test_ciso_assistant_brute_force_coverage.py)
already proves every action for every domain is reachable without raising,
driving the generated dispatch code to ~100% line coverage. It does NOT prove
WHICH client method a given action invokes: its mock client is
`MagicMock(spec=Api)`, which permits a call to any valid Api attribute, so an
action silently wired to the wrong (but still valid) client method would not
fail that test. This file closes that one gap for the functions CXA-FL-CISOASSISTANTAPI-01 is
decomposing (CX Phase A, worst-first CCN reduction) -- it is the
characterization baseline commit 1 pins, and commit 2's refactor must leave it
passing, byte-identical.

Not authored from scratch: CXA-FL-CISOASSISTANTAPI-01's functions are auto-generated
`register_*_tools` dispatch chains where (verified by AST walk before any
refactor) every branch is EXACTLY `elif action == "X": return
client.X(**kwargs)` -- no anomalies, no duplicate actions, no dropped kwargs,
no branch-specific error text. The assertions below are the direct, mechanical
characterization of that observed shape.
"""

import asyncio
from unittest.mock import MagicMock

from ciso_assistant_api.api._operation_manifest import ACTIONS_BY_DOMAIN
from ciso_assistant_api.api_client import Api


class _CaptureMCP:
    """Stand-in FastMCP that captures the registered tool callable."""

    def __init__(self):
        self.fns = []

    def tool(self, *args, **kwargs):
        def decorator(fn):
            self.fns.append(fn)
            return fn

        return decorator


from ciso_assistant_api.mcp.mcp_compliance import register_compliance_tools


def test_compliance_actions_route_to_same_named_client_method():
    """Characterizes ciso_assistant_compliance's dispatch: existing test_every_mcp_action_routes
    (test_ciso_assistant_brute_force_coverage.py) already proves every action
    is reachable without raising, but its client is `MagicMock(spec=Api)`, which
    accepts a call to ANY valid Api method name -- so it cannot catch an action
    silently wired to the WRONG (but still valid) client method. This closes
    that gap for ciso_assistant_compliance: for every action in this domain, assert it invokes the
    SAME-NAMED client method, exactly once, with the null-filtered kwargs.
    """
    mock_client = MagicMock(spec=Api)
    cap = _CaptureMCP()
    register_compliance_tools(cap)
    assert len(cap.fns) == 1
    fn = cap.fns[0]
    for action in ACTIONS_BY_DOMAIN["compliance"]:
        mock_client.reset_mock()
        asyncio.run(
            fn(
                action=action,
                params_json='{"probe": "v", "dropped": null}',
                client=mock_client,
                ctx=None,
            )
        )
        target = getattr(mock_client, action)
        target.assert_called_once_with(probe="v")
        # every OTHER method on the mock must be untouched by this action
        other_calls = [
            m for m in mock_client.method_calls if m[0] != action
        ]
        assert other_calls == [], f"{action} also touched {other_calls}"


from ciso_assistant_api.mcp.mcp_resilience import register_resilience_tools


def test_resilience_actions_route_to_same_named_client_method():
    """Characterizes ciso_assistant_resilience's dispatch: existing test_every_mcp_action_routes
    (test_ciso_assistant_brute_force_coverage.py) already proves every action
    is reachable without raising, but its client is `MagicMock(spec=Api)`, which
    accepts a call to ANY valid Api method name -- so it cannot catch an action
    silently wired to the WRONG (but still valid) client method. This closes
    that gap for ciso_assistant_resilience: for every action in this domain, assert it invokes the
    SAME-NAMED client method, exactly once, with the null-filtered kwargs.
    """
    mock_client = MagicMock(spec=Api)
    cap = _CaptureMCP()
    register_resilience_tools(cap)
    assert len(cap.fns) == 1
    fn = cap.fns[0]
    for action in ACTIONS_BY_DOMAIN["resilience"]:
        mock_client.reset_mock()
        asyncio.run(
            fn(
                action=action,
                params_json='{"probe": "v", "dropped": null}',
                client=mock_client,
                ctx=None,
            )
        )
        target = getattr(mock_client, action)
        target.assert_called_once_with(probe="v")
        # every OTHER method on the mock must be untouched by this action
        other_calls = [
            m for m in mock_client.method_calls if m[0] != action
        ]
        assert other_calls == [], f"{action} also touched {other_calls}"


from ciso_assistant_api.mcp.mcp_risk_management import register_risk_management_tools


def test_risk_management_actions_route_to_same_named_client_method():
    """Characterizes ciso_assistant_risk_management's dispatch: existing test_every_mcp_action_routes
    (test_ciso_assistant_brute_force_coverage.py) already proves every action
    is reachable without raising, but its client is `MagicMock(spec=Api)`, which
    accepts a call to ANY valid Api method name -- so it cannot catch an action
    silently wired to the WRONG (but still valid) client method. This closes
    that gap for ciso_assistant_risk_management: for every action in this domain, assert it invokes the
    SAME-NAMED client method, exactly once, with the null-filtered kwargs.
    """
    mock_client = MagicMock(spec=Api)
    cap = _CaptureMCP()
    register_risk_management_tools(cap)
    assert len(cap.fns) == 1
    fn = cap.fns[0]
    for action in ACTIONS_BY_DOMAIN["risk_management"]:
        mock_client.reset_mock()
        asyncio.run(
            fn(
                action=action,
                params_json='{"probe": "v", "dropped": null}',
                client=mock_client,
                ctx=None,
            )
        )
        target = getattr(mock_client, action)
        target.assert_called_once_with(probe="v")
        # every OTHER method on the mock must be untouched by this action
        other_calls = [
            m for m in mock_client.method_calls if m[0] != action
        ]
        assert other_calls == [], f"{action} also touched {other_calls}"


from ciso_assistant_api.mcp.mcp_ebios_rm import register_ebios_rm_tools


def test_ebios_rm_actions_route_to_same_named_client_method():
    """Characterizes ciso_assistant_ebios_rm's dispatch: existing test_every_mcp_action_routes
    (test_ciso_assistant_brute_force_coverage.py) already proves every action
    is reachable without raising, but its client is `MagicMock(spec=Api)`, which
    accepts a call to ANY valid Api method name -- so it cannot catch an action
    silently wired to the WRONG (but still valid) client method. This closes
    that gap for ciso_assistant_ebios_rm: for every action in this domain, assert it invokes the
    SAME-NAMED client method, exactly once, with the null-filtered kwargs.
    """
    mock_client = MagicMock(spec=Api)
    cap = _CaptureMCP()
    register_ebios_rm_tools(cap)
    assert len(cap.fns) == 1
    fn = cap.fns[0]
    for action in ACTIONS_BY_DOMAIN["ebios_rm"]:
        mock_client.reset_mock()
        asyncio.run(
            fn(
                action=action,
                params_json='{"probe": "v", "dropped": null}',
                client=mock_client,
                ctx=None,
            )
        )
        target = getattr(mock_client, action)
        target.assert_called_once_with(probe="v")
        # every OTHER method on the mock must be untouched by this action
        other_calls = [
            m for m in mock_client.method_calls if m[0] != action
        ]
        assert other_calls == [], f"{action} also touched {other_calls}"
