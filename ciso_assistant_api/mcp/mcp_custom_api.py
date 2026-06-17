"""MCP tool for arbitrary CISO Assistant REST requests (escape hatch)."""

from typing import Any

from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from ciso_assistant_api.auth import get_client


def register_custom_api_tools(mcp: FastMCP):
    @mcp.tool(tags={"custom-api"})
    async def ciso_assistant_api_request(
        method: str = Field(
            description="HTTP method to use (GET, POST, PUT, DELETE, PATCH)"
        ),
        endpoint: str = Field(
            description="API path appended to the backend host (e.g. /api/assets/)"
        ),
        params_json: str = Field(
            default="{}",
            description="JSON object with optional 'params' (query) and 'json' (body) keys.",
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Execute an arbitrary CISO Assistant REST API request directly."""
        if ctx:
            await ctx.info(f"Executing custom CISO Assistant {method} {endpoint}")
        import json

        try:
            payload = json.loads(params_json) if params_json else {}
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}
        if not isinstance(payload, dict):
            return {"error": "params_json must decode to a JSON object"}
        return client.api_request(
            method=method,
            endpoint=endpoint,
            params=payload.get("params"),
            json=payload.get("json"),
            data=payload.get("data"),
        )
