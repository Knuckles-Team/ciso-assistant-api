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
| `<DOMAIN>TOOL` | Toggle a domain tool, e.g. `INCIDENTSTOOL`, `COMPLIANCETOOL`, `RISK_MANAGEMENTTOOL` (default `True`). See the [Available MCP Tools](#available-mcp-tools) table for the authoritative names. |

The server also reads the standard MCP-transport, telemetry, governance, and agent-CLI
variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `TRANSPORT` | `stdio`, `streamable-http`, or `sse` | `stdio` |
| `HOST` | Bind host (HTTP transports) | `0.0.0.0` |
| `PORT` | Bind port (HTTP transports) | `8000` |
| `MCP_TOOL_MODE` | Tool surface: `condensed`, `verbose`, or `both` | `condensed` |
| `MCP_ENABLED_TOOLS` / `MCP_DISABLED_TOOLS` | Comma-separated tool allow/deny list | — |
| `MCP_ENABLED_TAGS` / `MCP_DISABLED_TAGS` | Comma-separated tag allow/deny list | — |
| `DEBUG` | Verbose logging | `False` |
| `PYTHONUNBUFFERED` | Unbuffered stdout (recommended in containers) | `1` |
| `ENABLE_OTEL` | Enable OpenTelemetry export | `True` |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | OTLP collector endpoint | — |
| `OTEL_EXPORTER_OTLP_PUBLIC_KEY` / `OTEL_EXPORTER_OTLP_SECRET_KEY` | OTLP auth keys | — |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | OTLP protocol (e.g. `http/protobuf`) | — |
| `EUNOMIA_TYPE` | Authorization mode: `none`, `embedded`, `remote` | `none` |
| `EUNOMIA_POLICY_FILE` | Embedded policy file | `mcp_policies.json` |
| `EUNOMIA_REMOTE_URL` | Remote Eunomia server URL | — |
| `MCP_URL` | (Agent only) URL of the MCP server the agent connects to | `http://localhost:8000/mcp` |
| `PROVIDER` | (Agent only) LLM provider (e.g. `openai`) | `openai` |
| `MODEL_ID` | (Agent only) Model id (e.g. `gpt-4o`) | `gpt-4o` |
| `ENABLE_WEB_UI` | (Agent only) Serve the AG-UI web interface | `True` |

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

### Available MCP Tools

_Auto-generated — do not edit (synced by the `mcp-readme-table` pre-commit hook)._

<!-- MCP-TOOLS-TABLE:START -->

| MCP Tool | Toggle Env Var | Description |
|----------|----------------|-------------|
| `ciso_assistant_analytics_metrology` | `ANALYTICS_METROLOGYTOOL` | Manage CISO Assistant analytics metrology operations. |
| `ciso_assistant_api_request` | `CUSTOM_APITOOL` | Execute an arbitrary CISO Assistant REST API request directly. |
| `ciso_assistant_assets` | `ASSETSTOOL` | Manage CISO Assistant assets operations. |
| `ciso_assistant_auth_users` | `AUTH_USERSTOOL` | Manage CISO Assistant auth users operations. |
| `ciso_assistant_chat` | `CHATTOOL` | Manage CISO Assistant chat operations. |
| `ciso_assistant_compliance` | `COMPLIANCETOOL` | Manage CISO Assistant compliance operations. |
| `ciso_assistant_crq` | `CRQTOOL` | Manage CISO Assistant crq operations. |
| `ciso_assistant_ebios_rm` | `EBIOS_RMTOOL` | Manage CISO Assistant ebios rm operations. |
| `ciso_assistant_evidence` | `EVIDENCETOOL` | Manage CISO Assistant evidence operations. |
| `ciso_assistant_frameworks_libraries` | `FRAMEWORKS_LIBRARIESTOOL` | Manage CISO Assistant frameworks libraries operations. |
| `ciso_assistant_governance` | `GOVERNANCETOOL` | Manage CISO Assistant governance operations. |
| `ciso_assistant_incidents` | `INCIDENTSTOOL` | Manage CISO Assistant incidents operations. |
| `ciso_assistant_integrations` | `INTEGRATIONSTOOL` | Manage CISO Assistant integrations operations. |
| `ciso_assistant_privacy` | `PRIVACYTOOL` | Manage CISO Assistant privacy operations. |
| `ciso_assistant_resilience` | `RESILIENCETOOL` | Manage CISO Assistant resilience operations. |
| `ciso_assistant_risk_management` | `RISK_MANAGEMENTTOOL` | Manage CISO Assistant risk management operations. |
| `ciso_assistant_security_findings` | `SECURITY_FINDINGSTOOL` | Manage CISO Assistant security findings operations. |
| `ciso_assistant_settings` | `SETTINGSTOOL` | Manage CISO Assistant settings operations. |
| `ciso_assistant_tasks_timeline` | `TASKS_TIMELINETOOL` | Manage CISO Assistant tasks timeline operations. |
| `ciso_assistant_third_party` | `THIRD_PARTYTOOL` | Manage CISO Assistant third party operations. |

_20 action-routed tools (default `MCP_TOOL_MODE=condensed`). Each is enabled unless its toggle is set false; set `MCP_TOOL_MODE=verbose` (or `both`) for the 1:1 per-operation surface. Auto-generated — do not edit._
<!-- MCP-TOOLS-TABLE:END -->

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
  knucklessg1/ciso-assistant-api:mcp
```

> The `:mcp` tag is the **slim MCP-server image** (built from
> `docker/Dockerfile --target mcp`, installing `ciso-assistant-api[mcp]`). The default
> `:latest` tag is the **full agent image** (`--target agent`, `ciso-assistant-api[agent]`)
> which also bundles the Pydantic AI agent and the epistemic-graph engine — use it
> when you run `ciso-assistant-agent` (the agent), not just the MCP server. See
> [Container images](#container-images-mcp-vs-agent).

### Deploy with Docker Compose

```yaml
services:
  ciso-assistant-api:
    image: knucklessg1/ciso-assistant-api:mcp
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

> **Install the slim `[mcp]` extra.** The example below installs
> `ciso-assistant-api[mcp]` — the MCP-server extra that pulls only the FastMCP /
> FastAPI tooling (`agent-utilities[mcp]`). It deliberately **excludes** the heavy
> agent runtime (the epistemic-graph engine, `pydantic-ai`, `dspy`, `llama-index`,
> `tree-sitter`), so `uvx`/container installs are dramatically smaller and faster.
> Use the full `[agent]` extra only when you need the integrated Pydantic AI agent
> (see [Installation](#install-python-package)).

```json
{
  "mcpServers": {
    "ciso_assistant": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "ciso-assistant-api[mcp]",
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

Pick the extra that matches what you want to run:

| Extra | Installs | Use when |
|-------|----------|----------|
| `ciso-assistant-api[mcp]` | Slim MCP server only (`agent-utilities[mcp]` — FastMCP/FastAPI) | You only run the **MCP server** (smallest install / image) |
| `ciso-assistant-api[agent]` | Full agent runtime (`agent-utilities[agent,logfire]` — Pydantic AI + the epistemic-graph engine) | You run the **integrated agent** |
| `ciso-assistant-api[all]` | Everything (`mcp` + `agent`) | Development / both surfaces |

```bash
# MCP server only (recommended for tool hosting — slim deps)
uv pip install "ciso-assistant-api[mcp]"

# Full agent runtime (Pydantic AI + epistemic-graph engine)
uv pip install "ciso-assistant-api[agent]"

# Everything (development)
uv pip install "ciso-assistant-api[all]"      # or: python -m pip install "ciso-assistant-api[all]"
```

### Container images (`:mcp` vs `:agent`)

One multi-stage `docker/Dockerfile` builds two right-sized images, selected by `--target`:

| Image tag | Build target | Contents | Entrypoint |
|-----------|--------------|----------|------------|
| `knucklessg1/ciso-assistant-api:mcp` | `--target mcp` | `ciso-assistant-api[mcp]` — **slim**, no engine/`pydantic-ai`/`dspy`/`llama-index`/`tree-sitter` | `ciso-assistant-mcp` |
| `knucklessg1/ciso-assistant-api:latest` | `--target agent` (default) | `ciso-assistant-api[agent]` — **full** agent runtime + epistemic-graph engine | `ciso-assistant-agent` |

```bash
docker build --target mcp   -t knucklessg1/ciso-assistant-api:mcp    docker/   # slim MCP server
docker build --target agent -t knucklessg1/ciso-assistant-api:latest docker/   # full agent
```

`docker/mcp.compose.yml` runs the slim `:mcp` server; `docker/agent.compose.yml` runs the
agent (`:latest`) with a co-located `:mcp` sidecar.

### Knowledge-graph database (`epistemic-graph`)

The **full agent** (`[agent]` / `:latest`) embeds the **epistemic-graph** engine (pulled in
transitively via `agent-utilities[agent]`). For production — or to share one knowledge graph
across multiple agents — run **epistemic-graph as its own database container** and point the
agent at it instead of embedding it. Deployment recipes (single-node + Raft HA), connection
config, and the full database architecture (with diagrams) are documented in the
[epistemic-graph deployment guide](https://knuckles-team.github.io/epistemic-graph/deployment/).
The slim `[mcp]` server does **not** require the database.

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


<!-- BEGIN agent-os-genesis-deploy (generated; do not edit between markers) -->

## Deploy with `agent-os-genesis`

This package can be provisioned for you — skill-guided — by the **`agent-os-genesis`**
universal skill (its *single-package deploy mode*): it picks your install method, seeds
secrets to OpenBao/Vault (or `.env`), trusts your enterprise CA, registers the MCP
server, and verifies it — the same machinery that stands up the whole Agent OS, narrowed
to just this package. Ask your agent to **"deploy `ciso-assistant-api` with agent-os-genesis"**.

| Install mode | Command |
|------|---------|
| Bare-metal, prod (PyPI) | `uvx ciso-assistant-mcp` · or `uv tool install ciso-assistant-api` |
| Bare-metal, dev (editable) | `uv pip install -e ".[all]"` · or `pip install -e ".[all]"` |
| Container, prod | deploy `knucklessg1/ciso-assistant-api:latest` via docker-compose / swarm / podman / podman-compose / kubernetes |
| Container, dev (editable) | deploy `docker/compose.dev.yml` (source-mounted at `/src`; edits live on restart) |

Secrets are read-existing + seeded via `vault_sync` — you are only prompted for what's missing.

<!-- END agent-os-genesis-deploy -->
