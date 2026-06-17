# Deployment

## Docker

```bash
docker build -t ciso-assistant-api .
```

```bash
docker run -d --name ciso-assistant-api -p 8000:8000 \
  -e TRANSPORT=streamable-http \
  -e CISO_ASSISTANT_URL="https://ciso.arpa" \
  -e CISO_ASSISTANT_TOKEN="your_token" \
  knucklessg1/ciso-assistant-api:latest
```

## Docker Compose

```yaml
services:
  ciso-assistant-api:
    image: knucklessg1/ciso-assistant-api:latest
    environment:
      - HOST=0.0.0.0
      - PORT=8000
      - TRANSPORT=streamable-http
      - CISO_ASSISTANT_URL=https://ciso.arpa
      - CISO_ASSISTANT_TOKEN=your_token
    ports:
      - 8000:8000
```

## Scoping the tool surface

Disable domains you don't need with `{TAG}TOOL=False` (e.g. `ESGTOOL=False`,
`TRAININGTOOL=False`). All domains default to `True`.
