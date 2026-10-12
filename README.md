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

*Version: 2.1.0*

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

<!-- GOVERNED-CAPABILITY:START -->
## Governed capability boundary

The current provider owns its generated API/MCP surface, one canonical operations
skill, ontology source, connector source presets, exact local schema fingerprints,
and signed schema-v2 capability bundle. The committed source attestation proves only
offline structure and neutral fixtures; external-live certification remains a separate
deployment gate. Endpoints remain external, credentials use runtime secret references,
and TLS verification is mandatory.
<!-- GOVERNED-CAPABILITY:END -->

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
- **Knox token auth** — a referenced pre-minted Knox token *or* referenced
  username/password pair exchanged at `POST /api/iam/login/`, plus OIDC
  delegation (RFC 8693) through `agent-utilities`.
- **Resilient** — honours `429` `Retry-After`, retries transient `5xx`, and
  transparently follows DRF `next` pagination links.

## MCP

### Using as an MCP Server

The MCP Server runs in `stdio` (local) or `streamable-http` (networked) mode.
Each domain is a tool gated by a `{TAG}TOOL` environment variable (default `True`),
so the operator can scope the surface (e.g. set `CHATTOOL=False` to drop the chat domain).

#### Environment Variables

<!-- ENV-VARS-TABLE:START -->

#### Package environment variables

| Variable | Example | Description |
|----------|---------|-------------|
| `CISO_ASSISTANT_URL` | `https://service.example.invalid` | ─── CISO Assistant connection ─────────────────────────────────────────────── Remote deployments must use HTTPS. Loopback HTTP is accepted for local testing. |
| `CISO_ASSISTANT_TOKEN_REF` | `secret://connectors/ciso-assistant/token` | ─── Authentication references (never store secret values here) ───── Use a Knox token reference OR both username/password references. |
| `CISO_ASSISTANT_USERNAME_REF` | `secret://connectors/ciso-assistant/username` |  |
| `CISO_ASSISTANT_PASSWORD_REF` | `secret://connectors/ciso-assistant/password` |  |
| `CISO_ASSISTANT_TLS_PROFILE` | `enterprise-ca` | ─── TLS profile selectors ──────────────────────────────────────── Select a profile from AgentConfig, or reference one JSON TLS profile. |
| `CISO_ASSISTANT_TLS_PROFILE_REF` | `secret://connectors/ciso-assistant/tls-profile` |  |
| `FASTMCP_LOG_LEVEL` | `INFO` | ─── MCP transport / auth (agent-utilities) ──────────────────────────── |
| `TRANSPORT` | `stdio` |  |
| `AUTH_TYPE` | `none` |  |
| `ANALYTICS_METROLOGYTOOL` | `True` | analytics-metrology tools |
| `ASSETSTOOL` | `True` | assets tools |
| `AUTH_USERSTOOL` | `True` | auth-users tools |
| `CHATTOOL` | `True` | chat tools |
| `COMPLIANCETOOL` | `True` | compliance tools |
| `CRQTOOL` | `True` | crq tools |
| `CUSTOM_APITOOL` | `False` | arbitrary REST escape hatch (explicit opt-in) |
| `EBIOS_RMTOOL` | `True` | ebios-rm tools |
| `EVIDENCETOOL` | `True` | evidence tools |
| `FRAMEWORKS_LIBRARIESTOOL` | `True` | frameworks-libraries tools |
| `GOVERNANCETOOL` | `True` | governance tools |
| `INCIDENTSTOOL` | `True` | incidents tools |
| `INTEGRATIONSTOOL` | `True` | integrations tools |
| `KG_INGESTTOOL` | `True` | governed native graph ingestion |
| `PRIVACYTOOL` | `True` | privacy tools |
| `RESILIENCETOOL` | `True` | resilience tools |
| `RISK_MANAGEMENTTOOL` | `True` | risk-management tools |
| `SECURITY_FINDINGSTOOL` | `True` | security-findings tools |
| `SETTINGSTOOL` | `True` | settings tools |
| `TASKS_TIMELINETOOL` | `True` | tasks-timeline tools |
| `THIRD_PARTYTOOL` | `True` | third-party tools |
| `CISO_ASSISTANT_MCP_IMAGE` | — | Deployment image references must be operator-approved immutable digests. Leave unset until configuring an actual deployment; no image is implied here. |
| `CISO_ASSISTANT_AGENT_IMAGE` | — |  |

#### Inherited agent-utilities variables (apply to every connector)

| Variable | Example | Description |
|----------|---------|-------------|
| `HOST` | `127.0.0.1` | Loopback bind host (set an authenticated ingress explicitly) |
| `PORT` | `8000` | Bind port (HTTP transports) |
| `MCP_ENABLED_TOOLS` | — | Comma-separated tool allow-list |
| `MCP_DISABLED_TOOLS` | — | Comma-separated tool deny-list |
| `MCP_ENABLED_TAGS` | — | Comma-separated tag allow-list |
| `MCP_DISABLED_TAGS` | — | Comma-separated tag deny-list |
| `EUNOMIA_TYPE` | `none` | Authorization mode: `none` \| `embedded` \| `remote` |
| `EUNOMIA_POLICY_FILE` | `mcp_policies.json` | Embedded Eunomia policy file |
| `EUNOMIA_REMOTE_URL` | — | Remote Eunomia authorization server URL |
| `ENABLE_OTEL` | `False` | Enable OpenTelemetry export |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | — | OTLP collector endpoint |
| `MCP_CLIENT_AUTH` | — | Outbound MCP child auth: `oidc-client-credentials` \| `basic` \| `none` |
| `OIDC_CLIENT_ID` | — | OIDC client id (service-account auth) |
| `OIDC_CLIENT_SECRET_REF` | `secret://identity/oidc-client-secret` | Runtime secret reference for the OIDC service account |
| `MCP_BASIC_AUTH_USERNAME` | — | HTTP Basic username (`MCP_CLIENT_AUTH=basic`) |
| `MCP_BASIC_AUTH_PASSWORD_REF` | `secret://identity/mcp-basic-password` | Runtime secret reference for HTTP Basic auth (`MCP_CLIENT_AUTH=basic`) |
| `DEBUG` | `False` | Verbose logging |
| `PYTHONUNBUFFERED` | `1` | Unbuffered stdout (recommended in containers) |
| `MCP_URL` | `http://localhost:8000/mcp` | URL of the MCP server the agent connects to |
| `PROVIDER` | — | Operator-configured LLM provider for the agent |
| `MODEL_ID` | — | Operator-configured model id for the agent |
| `ENABLE_WEB_UI` | `True` | Serve the AG-UI web interface |

_32 package + 22 inherited variable(s). Auto-generated from `.env.example` + the shared agent-utilities set — do not edit._
<!-- ENV-VARS-TABLE:END -->

See [Configuration](docs/configuration.md) for AgentConfig, runtime secret, TLS,
privacy, and authenticated-network-transport requirements.

#### Run in stdio mode (default):
```bash
export CISO_ASSISTANT_URL="https://service.example.invalid"
export CISO_ASSISTANT_TOKEN_REF="secret://connectors/ciso-assistant/token"
ciso-assistant-mcp --transport "stdio"
```

#### Run in HTTP mode:
```bash
export CISO_ASSISTANT_URL="https://service.example.invalid"
export CISO_ASSISTANT_TOKEN_REF="secret://connectors/ciso-assistant/token"
ciso-assistant-mcp --transport "streamable-http" --host "127.0.0.1" --port "8000"
```

### Available MCP Tools

_Auto-generated — do not edit (synced by the `mcp-readme-table` pre-commit hook)._

<!-- MCP-TOOLS-TABLE:START -->

#### Intent tools

| MCP Tool | Kind | Description |
|----------|------|-------------|
| `ciso_assistant_analytics_metrology` | intent | Manage CISO Assistant analytics metrology operations. |
| `ciso_assistant_api_request` | intent | Execute an arbitrary CISO Assistant REST API request directly. |
| `ciso_assistant_assets` | intent | Manage CISO Assistant assets operations. |
| `ciso_assistant_auth_users` | intent | Manage CISO Assistant auth users operations. |
| `ciso_assistant_chat` | intent | Manage CISO Assistant chat operations. |
| `ciso_assistant_compliance` | intent | Manage CISO Assistant compliance operations. |
| `ciso_assistant_crq` | intent | Manage CISO Assistant crq operations. |
| `ciso_assistant_ebios_rm` | intent | Manage CISO Assistant ebios rm operations. |
| `ciso_assistant_evidence` | intent | Manage CISO Assistant evidence operations. |
| `ciso_assistant_frameworks_libraries` | intent | Manage CISO Assistant frameworks libraries operations. |
| `ciso_assistant_governance` | intent | Manage CISO Assistant governance operations. |
| `ciso_assistant_incidents` | intent | Manage CISO Assistant incidents operations. |
| `ciso_assistant_integrations` | intent | Manage CISO Assistant integrations operations. |
| `ciso_assistant_privacy` | intent | Manage CISO Assistant privacy operations. |
| `ciso_assistant_resilience` | intent | Manage CISO Assistant resilience operations. |
| `ciso_assistant_risk_management` | intent | Manage CISO Assistant risk management operations. |
| `ciso_assistant_security_findings` | intent | Manage CISO Assistant security findings operations. |
| `ciso_assistant_settings` | intent | Manage CISO Assistant settings operations. |
| `ciso_assistant_tasks_timeline` | intent | Manage CISO Assistant tasks timeline operations. |
| `ciso_assistant_third_party` | intent | Manage CISO Assistant third party operations. |
| `ciso_ingest` | intent | List a CISO Assistant GRC record kind and natively ingest it into epistemic-graph. |

_21 intent tool(s) · 0 operation(s). Call an operation as `act(action='<operation>', params={...})` (`ask` for reads); `find(action='describe', params={'action': '<operation>'})` returns its arguments. An operation is enabled unless its `<DOMAIN>TOOL` toggle is set false. Auto-generated — do not edit._
<!-- MCP-TOOLS-TABLE:END -->

## A2A Agent

### Run A2A Server
```bash
export CISO_ASSISTANT_URL="https://service.example.invalid"
export CISO_ASSISTANT_TOKEN_REF="secret://connectors/ciso-assistant/token"
ciso-assistant-agent --provider <configured-provider> --model-id <configured-model>
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
  -p 127.0.0.1:8000:8000 \
  -e TRANSPORT=streamable-http \
  -e CISO_ASSISTANT_URL="https://service.example.invalid" \
  -e CISO_ASSISTANT_TOKEN_REF="secret://connectors/ciso-assistant/token" \
  "${CISO_ASSISTANT_MCP_IMAGE:?set CISO_ASSISTANT_MCP_IMAGE}"
```

> The `:mcp` tag is the **engine-enabled MCP-server image** (built from
> `docker/Dockerfile --target mcp`, installing `ciso-assistant-api[mcp]`). The default
> the immutable agent image is the **full agent image** (`--target agent`, `ciso-assistant-api[agent]`)
> which adds the Pydantic AI agent and observability runtime — use it when the operator run
> `ciso-assistant-agent` (the agent), not just the MCP server. Both targets carry
> `epistemic-graph[full]` through the Agent Utilities base dependency. See
> [Container images](#container-images-mcp-vs-agent).

### Deploy with Docker Compose

```yaml
services:
  ciso-assistant-api:
    image: ${CISO_ASSISTANT_MCP_IMAGE:?set CISO_ASSISTANT_MCP_IMAGE}
    environment:
      - HOST=0.0.0.0
      - PORT=8000
      - TRANSPORT=streamable-http
      - CISO_ASSISTANT_URL=https://service.example.invalid
      - CISO_ASSISTANT_TOKEN_REF=secret://connectors/ciso-assistant/token
    ports:
      - 127.0.0.1:8000:8000
```

#### Configure `mcp.json` for AI Integration (e.g. Claude Desktop)

> **Install the `[mcp]` extra.** It includes FastMCP; the Agent Utilities base
> dependency guarantees `epistemic-graph[full]` for native graph
> ingestion. Use `[agent]` when the same process also needs the integrated
> Pydantic AI and observability runtime (see
> [Installation](#install-python-package)).

```json
{
  "mcpServers": {
    "ciso_assistant": {
      "command": "uvx",
      "args": [
        "--from",
        "ciso-assistant-api[mcp]",
        "ciso-assistant-mcp"
      ],
      "env": {
        "CISO_ASSISTANT_URL": "https://service.example.invalid",
        "CISO_ASSISTANT_TOKEN_REF": "secret://connectors/ciso-assistant/token"
      }
    }
  }
}
```

## Install Python Package

Pick the extra that matches what the operator want to run:

| Extra | Installs | Use when |
|-------|----------|----------|
| `ciso-assistant-api[mcp]` | MCP server plus `agent-utilities[mcp]`; the Agent Utilities base dependency includes `epistemic-graph[full]` | The operator run the **MCP server** with native graph ingestion |
| `ciso-assistant-api[agent]` | Full agent runtime (`agent-utilities[agent-runtime,logfire]` — Pydantic AI, observability, and the full epistemic-graph engine) | The operator run the **integrated agent** |
| `ciso-assistant-api[all]` | Everything (`mcp` + `agent`) | Development / both surfaces |

```bash
# MCP server with the full epistemic-graph engine contract
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
| `${CISO_ASSISTANT_MCP_IMAGE}` | `--target mcp` | `ciso-assistant-api[mcp]` — MCP + `epistemic-graph[full]`, no agent runtime | `ciso-assistant-mcp` |
| `${CISO_ASSISTANT_AGENT_IMAGE}` | `--target agent` (default) | `ciso-assistant-api[agent]` — **full** agent runtime + epistemic-graph engine | `ciso-assistant-agent` |

```bash
docker build --target mcp -t "${CISO_ASSISTANT_MCP_IMAGE}" docker/
docker build --target agent -t "${CISO_ASSISTANT_AGENT_IMAGE}" docker/
```

`docker/mcp.compose.yml` runs the engine-enabled `:mcp` server; `docker/agent.compose.yml` runs the
agent (`immutable agent digest`) with a co-located `:mcp` sidecar.

### Knowledge-graph database (`epistemic-graph`)

Both `[mcp]` and `[agent]` embed the **full epistemic-graph** engine contract
(pulled in transitively through the Agent Utilities engine extra). For production — or to
share one knowledge graph across multiple agents — run **epistemic-graph as its own database
container** and point the provider at it instead of embedding it. Deployment recipes
(single-node + Raft HA), connection
config, and the full database architecture (with diagrams) are documented in the
[epistemic-graph deployment guide](https://knuckles-team.github.io/epistemic-graph/deployment/).
The MCP server may use an embedded engine or an operator-configured remote engine.

## Documentation

The complete documentation is published as the
[official documentation site](https://knuckles-team.github.io/ciso-assistant-api/) and is
the source of truth for installation, usage, and deployment.

| Page | Covers |
| --- | --- |
| [Overview](https://knuckles-team.github.io/ciso-assistant-api/overview/) | the action-routed tool surface and architecture |
| [Installation](https://knuckles-team.github.io/ciso-assistant-api/installation/) | pip, source, extras, prebuilt Docker image |
| [Configuration](https://knuckles-team.github.io/ciso-assistant-api/configuration/) | AgentConfig, runtime secret references, TLS, privacy, and readiness |
| [Usage (API / CLI / MCP)](https://knuckles-team.github.io/ciso-assistant-api/usage/) | the MCP tools, the `Api` client, the CLI |
| [Deployment](https://knuckles-team.github.io/ciso-assistant-api/deployment/) | run the MCP and agent servers, Compose, env config |

<!-- BEGIN agent-utilities-deployment (generated; do not edit between markers) -->

## Deploy with `agent-utilities-deployment`

Provision this package with the consolidated **`agent-utilities-deployment`**
workflow. It selects an installed-package, editable-source, or immutable-container
path; records only runtime secret and TLS-profile references in `AgentConfig`; and
runs doctor, registration, policy, observability, and rollback gates. Ask your agent
to **"deploy `ciso-assistant-api` with agent-utilities-deployment"**.

| Install mode | Command |
|------|---------|
| Installed package | `uv tool install "ciso-assistant-api[mcp]"`, then run `ciso-assistant-mcp` |
| Editable source | `uv pip install -e ".[agent]"`, then run `ciso-assistant-mcp` |
| Immutable container | deploy `registry.example.invalid/ciso-assistant-api@sha256:<digest>` through the operator-selected orchestrator |

The repository embeds no deployment profile, credential value, certificate path, or
environment-specific endpoint. Supply those at runtime through `AgentConfig` and the
configured secret provider.

<!-- END agent-utilities-deployment -->
