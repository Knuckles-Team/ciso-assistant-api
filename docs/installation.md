# Installation

```bash
pip install ciso-assistant-api[all]      # client + MCP + agent
# or scoped:
pip install ciso-assistant-api[mcp]      # client + MCP + epistemic-graph[full]
pip install ciso-assistant-api[agent]    # client + A2A agent
pip install ciso-assistant-api           # client only
```

## Credentials

CISO Assistant uses Django-REST-Knox **token** auth. Use **one** of:

1. **Pre-minted Knox token** — set `CISO_ASSISTANT_TOKEN_REF` to a runtime
   secret reference.
2. **Username / password** — set `CISO_ASSISTANT_USERNAME_REF` and
   `CISO_ASSISTANT_PASSWORD_REF`; the client resolves them in memory and
   exchanges them for a token at `POST /api/iam/login/`.

## Host configuration

Set `CISO_ASSISTANT_URL` to the backend host. Remote hosts must use HTTPS;
loopback HTTP is accepted for development. Configure private trust, mTLS, and
proxy policy through `CISO_ASSISTANT_TLS_PROFILE` or
`CISO_ASSISTANT_TLS_PROFILE_REF`. Certificate and hostname verification cannot
be disabled.

See [Configuration](configuration.md) and `.env.example` for the full contract.
