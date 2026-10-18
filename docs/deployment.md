# Deployment

## Docker

```bash
docker build -t ciso-assistant-api .
```

## Docker Compose

## Scoping the tool surface

Disable domains the operator do not need with `{TAG}TOOL=False` (for example,
`CHATTOOL=False` or `INTEGRATIONSTOOL=False`). All domains default to `True`.

See [Configuration](configuration.md) for AgentConfig, secret, TLS, privacy, and
readiness requirements. Replace all example values through the deployment
environment; do not commit instance-specific endpoints or secret material.
