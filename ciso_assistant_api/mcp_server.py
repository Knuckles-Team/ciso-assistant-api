#!/usr/bin/python

import logging
import sys
from typing import Any

from agent_utilities.core.config import load_config, setting
from agent_utilities.mcp.server_factory import create_mcp_server
from agent_utilities.mcp.verbose_tools import register_tool_surface
from fastmcp import FastMCP
from fastmcp.utilities.logging import get_logger

from ciso_assistant_api.api._operation_manifest import OPERATIONS
from ciso_assistant_api.api_client import Api
from ciso_assistant_api.auth import get_client

__version__ = "2.0.0"

# Redirect logging to stderr to prevent MCP stdout corruption
logger = get_logger(name="ciso_assistant_mcp")
logger.setLevel(logging.INFO)


def register_prompts(mcp: FastMCP):
    @mcp.prompt(name="example_prompt", description="Example prompt for CISO Assistant.")
    def example_prompt(query: str) -> str:
        """Example prompt."""
        return f"Please help with '{query}' using CISO Assistant"


def get_mcp_instance() -> tuple[Any, Any, Any, Any]:
    """Initialize and return the CISO Assistant MCP instance, args, and middlewares."""
    load_config()

    args, mcp, middlewares = create_mcp_server(
        name="CISO Assistant MCP",
        version=__version__,
        instructions="CISO Assistant MCP Server",
    )

    # One central call selects the surface per MCP_TOOL_MODE: condensed gates each
    # generated TOOL_REGISTRY domain via setting("<TAG>TOOL", True); verbose adds
    # the fully-typed 1:1 tools sourced from the OpenAPI manifest (OPERATIONS).
    from ciso_assistant_api.mcp import TOOL_REGISTRY

    registered_tags = register_tool_surface(
        mcp,
        client_cls=Api,
        get_client=get_client,
        service="ciso-assistant-api",
        tool_registry=TOOL_REGISTRY,
        manifest=OPERATIONS,
    )

    # Native KG ingestion: privacy-sanitized typed-node persistence. Raw evidence
    # attachments fail closed at the policy-controlled persistence boundary.
    from ciso_assistant_api.mcp.mcp_kg_ingest import register_kg_ingest_tools

    if setting("KG_INGESTTOOL", True):
        register_kg_ingest_tools(mcp)
        toggles = dict(getattr(mcp, "_condensed_tool_toggles", {}) or {})
        toggles["ciso_ingest"] = "KG_INGESTTOOL"
        mcp._condensed_tool_toggles = toggles

    register_prompts(mcp)

    for mw in middlewares:
        mcp.add_middleware(mw)

    return mcp, args, middlewares, registered_tags


def mcp_server():
    mcp, args, middlewares, registered_tags = get_mcp_instance()

    # Clean version announcement (stderr or logger preferred)
    print(f"CISO Assistant MCP v{__version__}", file=sys.stderr)
    print("\nStarting MCP Server", file=sys.stderr)
    print(f"  Transport: {args.transport.upper()}", file=sys.stderr)
    print(f"  Auth: {args.auth_type}", file=sys.stderr)
    print(f"  Dynamic Tags Loaded: {len(registered_tags)}", file=sys.stderr)

    if args.transport == "stdio":
        mcp.run(transport="stdio")
    elif args.transport == "streamable-http":
        mcp.run(transport="streamable-http", host=args.host, port=args.port)
    elif args.transport == "sse":
        mcp.run(transport="sse", host=args.host, port=args.port)
    else:
        logger.error(f"Invalid transport: {args.transport}")
        sys.exit(1)


if __name__ == "__main__":
    mcp_server()
