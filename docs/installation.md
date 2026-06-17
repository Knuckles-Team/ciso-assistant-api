# Installation

```bash
pip install ciso-assistant-api[all]      # client + MCP + agent
# or scoped:
pip install ciso-assistant-api[mcp]      # client + MCP server
pip install ciso-assistant-api[agent]    # client + A2A agent
pip install ciso-assistant-api           # client only
```

## Credentials

CISO Assistant uses Django-REST-Knox **token** auth. Use **one** of:

1. **Pre-minted Knox token** — set `CISO_ASSISTANT_TOKEN`.
2. **Username / password** — set `CISO_ASSISTANT_USERNAME` and
   `CISO_ASSISTANT_PASSWORD`; the client exchanges them for a token at
   `POST /api/iam/login/`.

## Host configuration

Set `CISO_ASSISTANT_URL` to your backend host (e.g. `https://ciso.arpa` or
`http://localhost:8000`). Set `CISO_ASSISTANT_SSL_VERIFY=False` to skip TLS
verification against a self-signed internal host.

See `.env.example` for the full list.
