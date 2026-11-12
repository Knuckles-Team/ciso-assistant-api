"""Hand-written MCP registrars.

Every API operation is registered as one typed tool from the operation manifest.
The registrars here add the tools that are not client-method wrappers.
"""

from ciso_assistant_api.mcp.mcp_custom_api import register_custom_api_tools

# (tag, toggle_env_var, register_fn) consumed by mcp_server.register_server_surface().
TOOL_REGISTRY = [
    ("custom-api", "CUSTOM_APITOOL", register_custom_api_tools),
]

__all__ = ["TOOL_REGISTRY", "register_custom_api_tools"]
