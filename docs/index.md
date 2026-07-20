# ciso-assistant-api

Python **CISO Assistant** API client + **MCP** server + **A2A** agent, with **100%
coverage** of the CISO Assistant public API.

Every one of the ~1,565 operations in the drf-spectacular schema is exposed as
both a typed client method and an action-routed MCP tool — all generated from the
vendored spec and verified by a coverage test.

- **[Overview](overview.md)** — what the package covers and how it is built.
- **[Installation](installation.md)** — install and configure credentials.
- **[Configuration](configuration.md)** — AgentConfig, secret references, TLS,
  privacy, and readiness gates.
- **[Usage](usage.md)** — Python client, MCP server, and A2A agent.
- **[Deployment](deployment.md)** — Docker and container deployment.

```bash
pip install "ciso-assistant-api[all]"
```
