# CONN-CISO-ASSISTANT-API-CONNECTOR-CONTENT — Design and implementation plan

Governing spec: [spec.md](spec.md).

## Architecture

`pyproject.toml` declares `ciso-assistant-mcp` as the connector identity. `create_mcp_server` resolves the packaged content of `ciso_assistant_api` from it.
