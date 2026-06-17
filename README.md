# CISO Assistant - A2A | AG-UI | MCP

![PyPI - Version](https://img.shields.io/pypi/v/ciso-assistant-api)
![MCP Server](https://badge.mcpx.dev?type=server 'MCP Server')
![PyPI - Downloads](https://img.shields.io/pypi/dd/ciso-assistant-api)
![GitHub Repo stars](https://img.shields.io/github/stars/Knuckles-Team/ciso-assistant-api)
![GitHub forks](https://img.shields.io/github/forks/Knuckles-Team/ciso-assistant-api)
![GitHub contributors](https://img.shields.io/github/contributors/Knuckles-Team/ciso-assistant-api)
![PyPI - License](https://img.shields.io/pypi/l/ciso-assistant-api)
![GitHub](https://img.shields.io/github/license/Knuckles-Team/ciso-assistant-api)

![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/Knuckles-Team/ciso-assistant-api)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Knuckles-Team/ciso-assistant-api)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/Knuckles-Team/ciso-assistant-api)
![GitHub issues](https://img.shields.io/github/issues/Knuckles-Team/ciso-assistant-api)

![GitHub top language](https://img.shields.io/github/languages/top/Knuckles-Team/ciso-assistant-api)
![GitHub language count](https://img.shields.io/github/languages/count/Knuckles-Team/ciso-assistant-api)
![GitHub repo size](https://img.shields.io/github/repo-size/Knuckles-Team/ciso-assistant-api)
![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/Knuckles-Team/ciso-assistant-api)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/ciso-assistant-api)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/ciso-assistant-api)

*Version: 0.1.0*

## Overview

**CISO Assistant** is a production-grade Python API client, Model Context Protocol
(MCP) server, and A2A agent for [CISO Assistant](https://github.com/intuitem/ciso-assistant-community),
intuitem's open-source GRC platform for Risk Management, AppSec, Compliance &
Audit, TPRM, BIA, Privacy, and Reporting.

It provides **100% coverage of the CISO Assistant REST API** — every one of the
**~1,565 operations** in the drf-spectacular schema is exposed as both a typed
client method and an action-routed MCP tool. The client, MCP tools, and a
machine-readable coverage manifest are all **generated from the vendored OpenAPI
spec** (`ciso_assistant_api/specs/ciso_assistant.json`) by
`scripts/generate_from_openapi.py`, and a coverage test asserts the three sets
stay in lock-step.

### Key Features

- **100% Action-Routed MCP Tools** — one consolidated tool per domain (e.g.
  `ciso_assistant_compliance`, `ciso_assistant_risk_management`,
  `ciso_assistant_incidents`) takes an `action` plus a `params_json` payload and
  routes to the underlying API method. 19 domain tools (mirroring the published
  documentation categories) cover every endpoint without flooding the IDE tool list.
- **Full CISO Assistant surface** — Analytics & Metrology, Assets, Authentication
  & Users, Compliance, EBIOS-RM, Evidence & Attachments, Frameworks & Libraries,
  Governance, Incidents, Integrations, Privacy, Quantitative Risk (CRQ),
  Resilience, Risk Management, Security Exceptions & Findings, Settings, Tasks &
  Timeline, and Third-Party Risk Management.
- **Knox token auth** — a pre-minted Knox token *or* a username/password pair
  exchanged for a token at `POST /api/iam/login/`, plus OIDC delegation (RFC 8693)
  via `agent-utilities`.
- **Resilient** — honours `429` `Retry-After`, retries transient `5xx`, and
  transparently follows DRF `next` pagination links.

## MCP

### Using as an MCP Server

The MCP Server runs in `stdio` (local) or `streamable-http` (networked) mode.
Each domain is a tool gated by a `{TAG}TOOL` environment variable (default `True`),
so you can scope the surface (e.g. set `CHATTOOL=False` to drop the chat domain).

#### Environment Variables

| Variable | Description |
| --- | --- |
| `CISO_ASSISTANT_URL` | Backend host URL, e.g. `https://ciso.arpa` or `http://localhost:8000`. |
| `CISO_ASSISTANT_TOKEN` | Pre-minted Knox token. |
| `CISO_ASSISTANT_USERNAME` / `CISO_ASSISTANT_PASSWORD` | Credentials exchanged for a token at `POST /api/iam/login/`. |
| `CISO_ASSISTANT_SSL_VERIFY` | Verify TLS (default `True`). |
| `<DOMAIN>TOOL` | Toggle a domain tool, e.g. `INCIDENTSTOOL`, `COMPLIANCETOOL`, `RISK_MANAGEMENTTOOL` (default `True`). |

#### Run in stdio mode (default):
```bash
export CISO_ASSISTANT_URL="https://ciso.arpa"
export CISO_ASSISTANT_TOKEN="your_token"
ciso-assistant-mcp --transport "stdio"
```

#### Run in HTTP mode:
```bash
export CISO_ASSISTANT_URL="https://ciso.arpa"
export CISO_ASSISTANT_TOKEN="your_token"
ciso-assistant-mcp --transport "streamable-http" --host "0.0.0.0" --port "8000"
```

### Tool Domains

`analytics_metrology`, `assets`, `auth_users`, `chat`, `compliance`, `crq`,
`ebios_rm`, `evidence`, `frameworks_libraries`, `governance`, `incidents`,
`integrations`, `privacy`, `resilience`, `risk_management`, `security_findings`,
`settings`, `tasks_timeline`, `third_party` — plus `custom_api` (a raw REST
escape hatch).

## A2A Agent

### Run A2A Server
```bash
export CISO_ASSISTANT_URL="https://ciso.arpa"
export CISO_ASSISTANT_TOKEN="your_token"
ciso-assistant-agent --provider openai --model-id gpt-4o --api-key sk-...
```

## Docker

### Build

```bash
docker build -t ciso-assistant-api .
```

### Run MCP Server

```bash
docker run -d \
  --name ciso-assistant-api \
  -p 8000:8000 \
  -e TRANSPORT=http \
  -e CISO_ASSISTANT_URL="https://ciso.arpa" \
  -e CISO_ASSISTANT_TOKEN="your_token" \
  knucklessg1/ciso-assistant-api:latest
```

### Deploy with Docker Compose

```yaml
services:
  ciso-assistant-api:
    image: knucklessg1/ciso-assistant-api:latest
    environment:
      - HOST=0.0.0.0
      - PORT=8000
      - TRANSPORT=http
      - CISO_ASSISTANT_URL=https://ciso.arpa
      - CISO_ASSISTANT_TOKEN=your_token
    ports:
      - 8000:8000
```

#### Configure `mcp.json` for AI Integration (e.g. Claude Desktop)

```json
{
  "mcpServers": {
    "ciso_assistant": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "ciso-assistant-api",
        "ciso-assistant-mcp"
      ],
      "env": {
        "CISO_ASSISTANT_URL": "https://ciso.arpa",
        "CISO_ASSISTANT_TOKEN": "your_token"
      }
    }
  }
}
```

## Install Python Package

```bash
python -m pip install ciso-assistant-api
```
```bash
uv pip install ciso-assistant-api
```

## Documentation

The complete documentation is published as the
[official documentation site](https://knuckles-team.github.io/ciso-assistant-api/) and is
the source of truth for installation, usage, and deployment.

| Page | Covers |
| --- | --- |
| [Overview](https://knuckles-team.github.io/ciso-assistant-api/overview/) | the action-routed tool surface and architecture |
| [Installation](https://knuckles-team.github.io/ciso-assistant-api/installation/) | pip, source, extras, prebuilt Docker image |
| [Usage (API / CLI / MCP)](https://knuckles-team.github.io/ciso-assistant-api/usage/) | the MCP tools, the `Api` client, the CLI |
| [Deployment](https://knuckles-team.github.io/ciso-assistant-api/deployment/) | run the MCP and agent servers, Compose, env config |

## Repository Owners

<img width="100%" height="180em" src="https://github-readme-stats.vercel.app/api?username=Knucklessg1&show_icons=true&hide_border=true&&count_private=true&include_all_commits=true" />

![GitHub followers](https://img.shields.io/github/followers/Knucklessg1)
![GitHub User's stars](https://img.shields.io/github/stars/Knucklessg1)
