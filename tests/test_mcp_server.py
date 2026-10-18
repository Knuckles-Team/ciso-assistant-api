"""MCP server build / tool-count tests."""

import asyncio
import sys

from ciso_assistant_api.api._operation_manifest import OPERATIONS


def test_mcp_server_lists_all_tools(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["ciso-assistant-mcp", "--transport", "stdio"])
    from ciso_assistant_api.mcp_server import get_mcp_instance

    mcp, args, middlewares, tags = get_mcp_instance()
    tools = asyncio.run(mcp.list_tools())
    # One typed tool per API operation + the custom API escape hatch + the
    # governed native KG ingest tool.
    assert len(tools) == len(OPERATIONS) + 2
    assert all(
        "action" not in (t.parameters or {}).get("properties", {}) for t in tools
    )


def test_tool_toggles_disable_domains(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["ciso-assistant-mcp", "--transport", "stdio"])
    monkeypatch.setenv("INCIDENTSTOOL", "False")
    from ciso_assistant_api.mcp_server import get_mcp_instance

    _mcp, _args, _mw, tags = get_mcp_instance()
    assert "incidents" not in tags


def test_kg_ingest_toggle_disables_tool(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["ciso-assistant-mcp", "--transport", "stdio"])
    monkeypatch.setenv("KG_INGESTTOOL", "False")
    from ciso_assistant_api.mcp_server import get_mcp_instance

    mcp, _args, _mw, _tags = get_mcp_instance()
    tools = asyncio.run(mcp.list_tools())
    assert "ciso_ingest" not in {tool.name for tool in tools}
