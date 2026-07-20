"""MCP server build / tool-count tests."""

import asyncio
import sys

from ciso_assistant_api.api._operation_manifest import DOMAINS


def test_mcp_server_lists_all_tools(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["ciso-assistant-mcp", "--transport", "stdio"])
    from ciso_assistant_api.mcp_server import get_mcp_instance

    mcp, args, middlewares, tags = get_mcp_instance()
    # One consolidated tool per domain + the custom_api escape hatch.
    assert len(tags) == len(DOMAINS) + 1
    tools = asyncio.run(mcp.list_tools())
    # Generated domain tools + custom API + the governed native KG ingest tool.
    assert len(tools) == len(DOMAINS) + 2


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


def test_agent_server_importable():
    from ciso_assistant_api.agent_server import agent_server

    assert callable(agent_server)
