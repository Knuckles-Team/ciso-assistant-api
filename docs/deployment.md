# Deployment

## Docker

```bash
docker build -t ciso-assistant-api .
```

```bash
docker run -d --name ciso-assistant-api -p 127.0.0.1:8000:8000 \
  -e TRANSPORT=streamable-http \
  -e CISO_ASSISTANT_URL="https://service.example.invalid" \
  -e CISO_ASSISTANT_TOKEN_REF="secret://connectors/ciso-assistant/token" \
  "${CISO_ASSISTANT_AGENT_IMAGE:?set CISO_ASSISTANT_AGENT_IMAGE}"
```

## Docker Compose

```yaml
services:
  ciso-assistant-api:
    image: ${CISO_ASSISTANT_AGENT_IMAGE:?set CISO_ASSISTANT_AGENT_IMAGE}
    environment:
      - HOST=0.0.0.0
      - PORT=8000
      - TRANSPORT=streamable-http
      - CISO_ASSISTANT_URL=https://service.example.invalid
      - CISO_ASSISTANT_TOKEN_REF=secret://connectors/ciso-assistant/token
    ports:
      - 127.0.0.1:8000:8000
```

## Scoping the tool surface

Disable domains you do not need with `{TAG}TOOL=False` (for example,
`CHATTOOL=False` or `INTEGRATIONSTOOL=False`). All domains default to `True`.

See [Configuration](configuration.md) for AgentConfig, secret, TLS, privacy, and
readiness requirements. Replace all example values through the deployment
environment; do not commit instance-specific endpoints or secret material.
