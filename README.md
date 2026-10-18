# MCP server with the full epistemic-graph engine contract
uv pip install "ciso-assistant-api[mcp]"

# Everything (development)
uv pip install "ciso-assistant-api[all]"      # or: python -m pip install "ciso-assistant-api[all]"
```

### Container images (`:mcp`)

One multi-stage `docker/Dockerfile` builds the MCP-only image (`--target mcp`):

| Image tag | Build target | Contents | Entrypoint |
|-----------|--------------|----------|------------|
| `${CISO_ASSISTANT_MCP_IMAGE}` | `--target mcp` | `ciso-assistant-api[mcp]` — MCP + `epistemic-graph[full]`, no agent runtime | `ciso-assistant-mcp` |

```bash
docker build --target mcp -t "${CISO_ASSISTANT_MCP_IMAGE}" docker/