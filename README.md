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

*Version: 2.0.0*

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
so you can scope the surface (e.g. set `CHATTOOL=False` to drop the chat domain).

#### Environment Variables

<!-- ENV-VARS-TABLE:START -->

#### Package environment variables

| Variable | Example | Description |
|----------|---------|-------------|
| `CISO_ASSISTANT_URL` | `https://service.example.invalid` | Remote deployments must use HTTPS. Loopback HTTP is accepted for local testing. |
| `CISO_ASSISTANT_TOKEN_REF` | `secret://connectors/ciso-assistant/token` | Use a Knox token reference OR both username/password references. |
| `CISO_ASSISTANT_USERNAME_REF` | `secret://connectors/ciso-assistant/username` |  |
| `CISO_ASSISTANT_PASSWORD_REF` | `secret://connectors/ciso-assistant/password` |  |
| `CISO_ASSISTANT_TLS_PROFILE` | `enterprise-ca` | Select a profile from AgentConfig, or reference one JSON TLS profile. |
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

#### Inherited agent-utilities variables (apply to every connector)

| Variable | Example | Description |
|----------|---------|-------------|
| `HOST` | `127.0.0.1` | Loopback bind host (set an authenticated ingress explicitly) |
| `PORT` | `8000` | Bind port (HTTP transports) |
| `MCP_TOOL_MODE` | `intent` | Tool surface: `intent` \| `condensed` \| `verbose` \| `both` |
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
| `PROVIDER` | `openai` | LLM provider for the agent |
| `MODEL_ID` | `gpt-4o` | Model id for the agent |
| `ENABLE_WEB_UI` | `True` | Serve the AG-UI web interface |

_30 package + 23 inherited variable(s). Auto-generated from `.env.example` + the shared agent-utilities set — do not edit._
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

#### Condensed action-routed tools (`MCP_TOOL_MODE=condensed`)

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
| `ciso_ingest` | `KG_INGESTTOOL` | List a CISO Assistant GRC record kind and natively ingest it into epistemic-graph. |

#### Verbose 1:1 API-mapped tools (`MCP_TOOL_MODE=verbose` or `both`)

<details>
<summary>1565 per-operation tools — one per public API method (click to expand)</summary>

| MCP Tool | Toggle Env Var | Description |
|----------|----------------|-------------|
| `ciso_assistant_api_accounts_saml_download_cert_retrieve` | `AUTH_USERSTOOL` | api_accounts_saml_download_cert_retrieve |
| `ciso_assistant_api_accounts_saml_generate_keys_create` | `AUTH_USERSTOOL` | Endpoint to generate a key pair (private key + self-signed X.509 certificate). |
| `ciso_assistant_api_actors_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_actors_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_actors_object_retrieve` | `GRANULARTOOL` | api_actors_object_retrieve |
| `ciso_assistant_api_actors_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_agg_data_retrieve` | `ANALYTICS_METROLOGYTOOL` | api_agg_data_retrieve |
| `ciso_assistant_api_analytics_export_xlsx_retrieve` | `ANALYTICS_METROLOGYTOOL` | Export all analytics dashboard data as a multi-sheet XLSX file. |
| `ciso_assistant_api_answers_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_answers_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_answers_create` | `GRANULARTOOL` | API endpoint for Answer CRUD. |
| `ciso_assistant_api_answers_destroy` | `GRANULARTOOL` | API endpoint for Answer CRUD. |
| `ciso_assistant_api_answers_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_answers_object_retrieve` | `GRANULARTOOL` | API endpoint for Answer CRUD. |
| `ciso_assistant_api_answers_partial_update` | `GRANULARTOOL` | API endpoint for Answer CRUD. |
| `ciso_assistant_api_answers_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_answers_update` | `GRANULARTOOL` | API endpoint for Answer CRUD. |
| `ciso_assistant_api_applied_controls_analytics_retrieve` | `COMPLIANCETOOL` | Aggregated analytics over the filtered applied-controls queryset. |
| `ciso_assistant_api_applied_controls_autocomplete_retrieve` | `COMPLIANCETOOL` | Minimal endpoint for autocomplete selects. |
| `ciso_assistant_api_applied_controls_batch_action_create` | `COMPLIANCETOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_applied_controls_cascade_info_retrieve` | `COMPLIANCETOOL` | Cascade preview: |
| `ciso_assistant_api_applied_controls_category_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_applied_controls_control_impact_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_applied_controls_create` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_applied_controls_csf_function_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_applied_controls_destroy` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_applied_controls_duplicate_create` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_applied_controls_effort_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_applied_controls_export_csv_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_applied_controls_export_xlsx_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_applied_controls_get_controls_info_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_applied_controls_get_gantt_data_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_applied_controls_get_timeline_info_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_applied_controls_ids_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_applied_controls_impact_effort_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_applied_controls_impact_graph_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_applied_controls_linked_models_retrieve` | `COMPLIANCETOOL` | Return available model types that can be linked to applied controls |
| `ciso_assistant_api_applied_controls_list` | `COMPLIANCETOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_applied_controls_merge_create` | `COMPLIANCETOOL` | Merge N source applied controls into 1 target. See |
| `ciso_assistant_api_applied_controls_mss_xlsx_retrieve` | `COMPLIANCETOOL` | Export filtered applied controls in ANSSI MonServiceSécurisé format |
| `ciso_assistant_api_applied_controls_object_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_applied_controls_owner_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_applied_controls_partial_update` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_applied_controls_per_status_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_applied_controls_priority_chart_data_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_applied_controls_priority_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_applied_controls_retrieve` | `COMPLIANCETOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_applied_controls_status_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_applied_controls_sunburst_data_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_applied_controls_sync_to_reference_control_create` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_applied_controls_to_review_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_applied_controls_todo_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_applied_controls_updatables_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_applied_controls_update` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_asset_capabilities_batch_action_create` | `ASSETSTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_asset_capabilities_cascade_info_retrieve` | `ASSETSTOOL` | Cascade preview: |
| `ciso_assistant_api_asset_capabilities_create` | `ASSETSTOOL` | api_asset_capabilities_create |
| `ciso_assistant_api_asset_capabilities_destroy` | `ASSETSTOOL` | api_asset_capabilities_destroy |
| `ciso_assistant_api_asset_capabilities_list` | `ASSETSTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_asset_capabilities_object_retrieve` | `ASSETSTOOL` | api_asset_capabilities_object_retrieve |
| `ciso_assistant_api_asset_capabilities_partial_update` | `ASSETSTOOL` | api_asset_capabilities_partial_update |
| `ciso_assistant_api_asset_capabilities_retrieve` | `ASSETSTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_asset_capabilities_update` | `ASSETSTOOL` | api_asset_capabilities_update |
| `ciso_assistant_api_asset_class_batch_action_create` | `ASSETSTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_asset_class_cascade_info_retrieve` | `ASSETSTOOL` | Cascade preview: |
| `ciso_assistant_api_asset_class_create` | `ASSETSTOOL` | api_asset_class_create |
| `ciso_assistant_api_asset_class_destroy` | `ASSETSTOOL` | api_asset_class_destroy |
| `ciso_assistant_api_asset_class_list` | `ASSETSTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_asset_class_object_retrieve` | `ASSETSTOOL` | api_asset_class_object_retrieve |
| `ciso_assistant_api_asset_class_partial_update` | `ASSETSTOOL` | api_asset_class_partial_update |
| `ciso_assistant_api_asset_class_retrieve` | `ASSETSTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_asset_class_tree_retrieve` | `ASSETSTOOL` | api_asset_class_tree_retrieve |
| `ciso_assistant_api_asset_class_update` | `ASSETSTOOL` | api_asset_class_update |
| `ciso_assistant_api_assets_asset_class_retrieve` | `ASSETSTOOL` | API endpoint that allows assets to be viewed or edited. |
| `ciso_assistant_api_assets_autocomplete_retrieve` | `ASSETSTOOL` | Minimal endpoint for autocomplete selects — skips graph traversal. |
| `ciso_assistant_api_assets_batch_action_create` | `ASSETSTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_assets_batch_create_create` | `ASSETSTOOL` | Batch create multiple assets from a text list with parent-child relationships. |
| `ciso_assistant_api_assets_cascade_info_retrieve` | `ASSETSTOOL` | Cascade preview: |
| `ciso_assistant_api_assets_create` | `ASSETSTOOL` | API endpoint that allows assets to be viewed or edited. |
| `ciso_assistant_api_assets_destroy` | `ASSETSTOOL` | API endpoint that allows assets to be viewed or edited. |
| `ciso_assistant_api_assets_disaster_recovery_objectives_retrieve` | `ASSETSTOOL` | API endpoint that allows assets to be viewed or edited. |
| `ciso_assistant_api_assets_dora_criticality_assessment_retrieve` | `ASSETSTOOL` | API endpoint that allows assets to be viewed or edited. |
| `ciso_assistant_api_assets_dora_discontinuing_impact_retrieve` | `ASSETSTOOL` | API endpoint that allows assets to be viewed or edited. |
| `ciso_assistant_api_assets_dora_licenced_activity_retrieve` | `ASSETSTOOL` | API endpoint that allows assets to be viewed or edited. |
| `ciso_assistant_api_assets_export_csv_retrieve` | `ASSETSTOOL` | API endpoint that allows assets to be viewed or edited. |
| `ciso_assistant_api_assets_export_xlsx_retrieve` | `ASSETSTOOL` | API endpoint that allows assets to be viewed or edited. |
| `ciso_assistant_api_assets_graph_retrieve` | `ASSETSTOOL` | API endpoint that allows assets to be viewed or edited. |
| `ciso_assistant_api_assets_ids_retrieve` | `ASSETSTOOL` | API endpoint that allows assets to be viewed or edited. |
| `ciso_assistant_api_assets_list` | `ASSETSTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_assets_object_retrieve` | `ASSETSTOOL` | API endpoint that allows assets to be viewed or edited. |
| `ciso_assistant_api_assets_partial_update` | `ASSETSTOOL` | API endpoint that allows assets to be viewed or edited. |
| `ciso_assistant_api_assets_retrieve` | `ASSETSTOOL` | Populate `optimized_data` for the single retrieved asset so the |
| `ciso_assistant_api_assets_security_objectives_retrieve` | `ASSETSTOOL` | API endpoint that allows assets to be viewed or edited. |
| `ciso_assistant_api_assets_type_retrieve` | `ASSETSTOOL` | API endpoint that allows assets to be viewed or edited. |
| `ciso_assistant_api_assets_update` | `ASSETSTOOL` | API endpoint that allows assets to be viewed or edited. |
| `ciso_assistant_api_build_retrieve` | `GRANULARTOOL` | API endpoint that returns the build version of the application. |
| `ciso_assistant_api_campaigns_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_campaigns_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_campaigns_create` | `GRANULARTOOL` | api_campaigns_create |
| `ciso_assistant_api_campaigns_destroy` | `GRANULARTOOL` | api_campaigns_destroy |
| `ciso_assistant_api_campaigns_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_campaigns_metrics_retrieve` | `GRANULARTOOL` | api_campaigns_metrics_retrieve |
| `ciso_assistant_api_campaigns_object_retrieve` | `GRANULARTOOL` | api_campaigns_object_retrieve |
| `ciso_assistant_api_campaigns_partial_update` | `GRANULARTOOL` | api_campaigns_partial_update |
| `ciso_assistant_api_campaigns_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_campaigns_status_retrieve` | `GRANULARTOOL` | api_campaigns_status_retrieve |
| `ciso_assistant_api_campaigns_update` | `GRANULARTOOL` | api_campaigns_update |
| `ciso_assistant_api_chat_agent_actions_approve_create` | `CHATTOOL` | api_chat_agent_actions_approve_create |
| `ciso_assistant_api_chat_agent_actions_batch_action_create` | `CHATTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_chat_agent_actions_cascade_info_retrieve` | `CHATTOOL` | Cascade preview: |
| `ciso_assistant_api_chat_agent_actions_create` | `CHATTOOL` | api_chat_agent_actions_create |
| `ciso_assistant_api_chat_agent_actions_list` | `CHATTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_chat_agent_actions_object_retrieve` | `CHATTOOL` | api_chat_agent_actions_object_retrieve |
| `ciso_assistant_api_chat_agent_actions_reject_create` | `CHATTOOL` | api_chat_agent_actions_reject_create |
| `ciso_assistant_api_chat_agent_actions_retrieve` | `CHATTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_chat_agent_runs_batch_action_create` | `CHATTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_chat_agent_runs_cancel_create` | `CHATTOOL` | Mark an active run as cancelled. The worker checks before each step. |
| `ciso_assistant_api_chat_agent_runs_cascade_info_retrieve` | `CHATTOOL` | Cascade preview: |
| `ciso_assistant_api_chat_agent_runs_create` | `CHATTOOL` | api_chat_agent_runs_create |
| `ciso_assistant_api_chat_agent_runs_list` | `CHATTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_chat_agent_runs_object_retrieve` | `CHATTOOL` | api_chat_agent_runs_object_retrieve |
| `ciso_assistant_api_chat_agent_runs_retrieve` | `CHATTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_chat_agent_runs_start_questionnaire_prefill_create` | `CHATTOOL` | Create + enqueue an AgentRun for prefilling a questionnaire. |
| `ciso_assistant_api_chat_documents_batch_action_create` | `CHATTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_chat_documents_cascade_info_retrieve` | `CHATTOOL` | Cascade preview: |
| `ciso_assistant_api_chat_documents_create` | `CHATTOOL` | ViewSet for managing indexed documents. |
| `ciso_assistant_api_chat_documents_destroy` | `CHATTOOL` | ViewSet for managing indexed documents. |
| `ciso_assistant_api_chat_documents_list` | `CHATTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_chat_documents_object_retrieve` | `CHATTOOL` | ViewSet for managing indexed documents. |
| `ciso_assistant_api_chat_documents_partial_update` | `CHATTOOL` | ViewSet for managing indexed documents. |
| `ciso_assistant_api_chat_documents_retrieve` | `CHATTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_chat_documents_update` | `CHATTOOL` | ViewSet for managing indexed documents. |
| `ciso_assistant_api_chat_ollama_models_retrieve` | `CHATTOOL` | List available models from the Ollama server. |
| `ciso_assistant_api_chat_questionnaire_questions_batch_action_create` | `CHATTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_chat_questionnaire_questions_cascade_info_retrieve` | `CHATTOOL` | Cascade preview: |
| `ciso_assistant_api_chat_questionnaire_questions_create` | `CHATTOOL` | api_chat_questionnaire_questions_create |
| `ciso_assistant_api_chat_questionnaire_questions_create_and_retry_create` | `CHATTOOL` | Create an AppliedControl in the question's folder from a (possibly |
| `ciso_assistant_api_chat_questionnaire_questions_destroy` | `CHATTOOL` | api_chat_questionnaire_questions_destroy |
| `ciso_assistant_api_chat_questionnaire_questions_list` | `CHATTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_chat_questionnaire_questions_object_retrieve` | `CHATTOOL` | api_chat_questionnaire_questions_object_retrieve |
| `ciso_assistant_api_chat_questionnaire_questions_partial_update` | `CHATTOOL` | api_chat_questionnaire_questions_partial_update |
| `ciso_assistant_api_chat_questionnaire_questions_retrieve` | `CHATTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_chat_questionnaire_questions_retry_with_control_create` | `CHATTOOL` | Re-run a single question's answer pipeline with a chosen |
| `ciso_assistant_api_chat_questionnaire_questions_suggest_control_create` | `CHATTOOL` | Synchronous LLM call: draft an AppliedControl that would let us |
| `ciso_assistant_api_chat_questionnaire_questions_update` | `CHATTOOL` | api_chat_questionnaire_questions_update |
| `ciso_assistant_api_chat_questionnaire_runs_batch_action_create` | `CHATTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_chat_questionnaire_runs_cascade_info_retrieve` | `CHATTOOL` | Cascade preview: |
| `ciso_assistant_api_chat_questionnaire_runs_create` | `CHATTOOL` | Experimental: questionnaire prefill runs. |
| `ciso_assistant_api_chat_questionnaire_runs_destroy` | `CHATTOOL` | Experimental: questionnaire prefill runs. |
| `ciso_assistant_api_chat_questionnaire_runs_export_retrieve` | `CHATTOOL` | Stream a copy of the original xlsx with response/comment columns |
| `ciso_assistant_api_chat_questionnaire_runs_extract_questions_create` | `CHATTOOL` | Materialize QuestionnaireQuestion rows from parsed_data + column_mapping. |
| `ciso_assistant_api_chat_questionnaire_runs_list` | `CHATTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_chat_questionnaire_runs_mapping_partial_update` | `CHATTOOL` | Persist the user's column-mapping choice for this run. |
| `ciso_assistant_api_chat_questionnaire_runs_object_retrieve` | `CHATTOOL` | Experimental: questionnaire prefill runs. |
| `ciso_assistant_api_chat_questionnaire_runs_partial_update` | `CHATTOOL` | Experimental: questionnaire prefill runs. |
| `ciso_assistant_api_chat_questionnaire_runs_retrieve` | `CHATTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_chat_questionnaire_runs_update` | `CHATTOOL` | Experimental: questionnaire prefill runs. |
| `ciso_assistant_api_chat_questionnaire_runs_upload_create` | `CHATTOOL` | Multipart upload entry point: file + folder + optional title. |
| `ciso_assistant_api_chat_sessions_batch_action_create` | `CHATTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_chat_sessions_cascade_info_retrieve` | `CHATTOOL` | Cascade preview: |
| `ciso_assistant_api_chat_sessions_create` | `CHATTOOL` | ViewSet for chat sessions with streaming message endpoint. |
| `ciso_assistant_api_chat_sessions_destroy` | `CHATTOOL` | ViewSet for chat sessions with streaming message endpoint. |
| `ciso_assistant_api_chat_sessions_list` | `CHATTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_chat_sessions_message_create` | `CHATTOOL` | Send a message and get a streaming SSE response. |
| `ciso_assistant_api_chat_sessions_object_retrieve` | `CHATTOOL` | ViewSet for chat sessions with streaming message endpoint. |
| `ciso_assistant_api_chat_sessions_partial_update` | `CHATTOOL` | ViewSet for chat sessions with streaming message endpoint. |
| `ciso_assistant_api_chat_sessions_retrieve` | `CHATTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_chat_sessions_update` | `CHATTOOL` | ViewSet for chat sessions with streaming message endpoint. |
| `ciso_assistant_api_chat_sessions_upload_create` | `CHATTOOL` | Upload a document to be indexed for RAG in this session's folder context. |
| `ciso_assistant_api_chat_status_retrieve` | `CHATTOOL` | Check chat service health: Ollama availability, index status. |
| `ciso_assistant_api_comments_batch_action_create` | `GOVERNANCETOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_comments_cascade_info_retrieve` | `GOVERNANCETOOL` | Cascade preview: |
| `ciso_assistant_api_comments_create` | `GOVERNANCETOOL` | api_comments_create |
| `ciso_assistant_api_comments_destroy` | `GOVERNANCETOOL` | api_comments_destroy |
| `ciso_assistant_api_comments_list` | `GOVERNANCETOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_comments_object_retrieve` | `GOVERNANCETOOL` | api_comments_object_retrieve |
| `ciso_assistant_api_comments_partial_update` | `GOVERNANCETOOL` | api_comments_partial_update |
| `ciso_assistant_api_comments_retrieve` | `GOVERNANCETOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_comments_update` | `GOVERNANCETOOL` | api_comments_update |
| `ciso_assistant_api_compliance_assessments_action_plan_budget_overview_list` | `COMPLIANCETOOL` | Mixin that computes budget aggregation over an applied controls queryset. |
| `ciso_assistant_api_compliance_assessments_action_plan_csv_retrieve` | `COMPLIANCETOOL` | API endpoint that allows compliance assessments to be viewed or edited. |
| `ciso_assistant_api_compliance_assessments_action_plan_list` | `COMPLIANCETOOL` | api_compliance_assessments_action_plan_list |
| `ciso_assistant_api_compliance_assessments_action_plan_pdf_retrieve` | `COMPLIANCETOOL` | API endpoint that allows compliance assessments to be viewed or edited. |
| `ciso_assistant_api_compliance_assessments_action_plan_xlsx_retrieve` | `COMPLIANCETOOL` | API endpoint that allows compliance assessments to be viewed or edited. |
| `ciso_assistant_api_compliance_assessments_analytics_retrieve` | `COMPLIANCETOOL` | Returns compliance analytics data grouped by framework and domain |
| `ciso_assistant_api_compliance_assessments_auditee_dashboard_retrieve` | `COMPLIANCETOOL` | Returns per-assignment progress data for the auditee's dashboard. |
| `ciso_assistant_api_compliance_assessments_batch_action_create` | `COMPLIANCETOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_compliance_assessments_cascade_info_retrieve` | `COMPLIANCETOOL` | Cascade preview: |
| `ciso_assistant_api_compliance_assessments_combined_tree_retrieve` | `COMPLIANCETOOL` | Requirement tree with domain-tree inheritance applied as an overlay. |
| `ciso_assistant_api_compliance_assessments_comparable_audits_retrieve` | `COMPLIANCETOOL` | Get list of compliance assessments that can be compared with this one |
| `ciso_assistant_api_compliance_assessments_compare_retrieve` | `COMPLIANCETOOL` | Compare two compliance assessments that use the same framework |
| `ciso_assistant_api_compliance_assessments_compliance_assessment_csv_retrieve` | `COMPLIANCETOOL` | API endpoint that allows compliance assessments to be viewed or edited. |
| `ciso_assistant_api_compliance_assessments_compliance_timeline_retrieve` | `COMPLIANCETOOL` | Returns compliance metrics over time from HistoricalMetric snapshots. |
| `ciso_assistant_api_compliance_assessments_controls_coverage_retrieve` | `COMPLIANCETOOL` | Controls coverage analysis for this compliance assessment. |
| `ciso_assistant_api_compliance_assessments_create` | `COMPLIANCETOOL` | API endpoint that allows compliance assessments to be viewed or edited. |
| `ciso_assistant_api_compliance_assessments_cyfun_xlsx_retrieve` | `COMPLIANCETOOL` | API endpoint that allows compliance assessments to be viewed or edited. |
| `ciso_assistant_api_compliance_assessments_destroy` | `COMPLIANCETOOL` | API endpoint that allows compliance assessments to be viewed or edited. |
| `ciso_assistant_api_compliance_assessments_donut_data_retrieve` | `COMPLIANCETOOL` | API endpoint that allows compliance assessments to be viewed or edited. |
| `ciso_assistant_api_compliance_assessments_evidence_coverage_retrieve` | `COMPLIANCETOOL` | Evidence coverage analysis — direct (on RA) and indirect (via applied controls). |
| `ciso_assistant_api_compliance_assessments_evidences_list_list` | `COMPLIANCETOOL` | api_compliance_assessments_evidences_list_list |
| `ciso_assistant_api_compliance_assessments_exceptions_summary_retrieve` | `COMPLIANCETOOL` | Security exceptions summary for this compliance assessment. |
| `ciso_assistant_api_compliance_assessments_export_retrieve` | `COMPLIANCETOOL` | API endpoint that allows compliance assessments to be viewed or edited. |
| `ciso_assistant_api_compliance_assessments_frameworks_retrieve` | `COMPLIANCETOOL` | API endpoint that allows compliance assessments to be viewed or edited. |
| `ciso_assistant_api_compliance_assessments_global_score_retrieve` | `COMPLIANCETOOL` | Returns the global score of the compliance assessment |
| `ciso_assistant_api_compliance_assessments_implementation_groups_breakdown_retrieve` | `COMPLIANCETOOL` | Breakdown of compliance results by implementation group. |
| `ciso_assistant_api_compliance_assessments_is_auditee_retrieve` | `COMPLIANCETOOL` | Returns whether the current user is an auditee for this compliance assessment. |
| `ciso_assistant_api_compliance_assessments_list` | `COMPLIANCETOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_compliance_assessments_mailing_create` | `COMPLIANCETOOL` | API endpoint that allows compliance assessments to be viewed or edited. |
| `ciso_assistant_api_compliance_assessments_map_from_create` | `COMPLIANCETOOL` | Map data from a source audit into this one. |
| `ciso_assistant_api_compliance_assessments_map_from_preview_retrieve` | `COMPLIANCETOOL` | Preview the effect of mapping data from a source audit into this one. |
| `ciso_assistant_api_compliance_assessments_object_retrieve` | `COMPLIANCETOOL` | API endpoint that allows compliance assessments to be viewed or edited. |
| `ciso_assistant_api_compliance_assessments_partial_update` | `COMPLIANCETOOL` | API endpoint that allows compliance assessments to be viewed or edited. |
| `ciso_assistant_api_compliance_assessments_per_status_retrieve` | `COMPLIANCETOOL` | API endpoint that allows compliance assessments to be viewed or edited. |
| `ciso_assistant_api_compliance_assessments_progress_ts_retrieve` | `COMPLIANCETOOL` | API endpoint that allows compliance assessments to be viewed or edited. |
| `ciso_assistant_api_compliance_assessments_quality_check_retrieve` | `COMPLIANCETOOL` | Returns the quality check of every compliance assessment |
| `ciso_assistant_api_compliance_assessments_quality_check_retrieve_2` | `COMPLIANCETOOL` | Returns the quality check of a specific assessment |
| `ciso_assistant_api_compliance_assessments_recap_retrieve` | `COMPLIANCETOOL` | API endpoint that allows compliance assessments to be viewed or edited. |
| `ciso_assistant_api_compliance_assessments_requirements_list_retrieve` | `COMPLIANCETOOL` | Returns the list of requirement assessments for the different audit modes |
| `ciso_assistant_api_compliance_assessments_retrieve` | `COMPLIANCETOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_compliance_assessments_score_calculation_method_retrieve` | `COMPLIANCETOOL` | API endpoint that allows compliance assessments to be viewed or edited. |
| `ciso_assistant_api_compliance_assessments_section_compliance_retrieve` | `COMPLIANCETOOL` | Aggregates compliance results and scores per top-level requirement group. |
| `ciso_assistant_api_compliance_assessments_soa_retrieve` | `COMPLIANCETOOL` | Returns the requirement tree enriched with applied controls and |
| `ciso_assistant_api_compliance_assessments_status_retrieve` | `COMPLIANCETOOL` | API endpoint that allows compliance assessments to be viewed or edited. |
| `ciso_assistant_api_compliance_assessments_suggestions_applied_controls_create` | `COMPLIANCETOOL` | api_compliance_assessments_suggestions_applied_controls_create |
| `ciso_assistant_api_compliance_assessments_suggestions_applied_controls_retrieve` | `COMPLIANCETOOL` | api_compliance_assessments_suggestions_applied_controls_retrieve |
| `ciso_assistant_api_compliance_assessments_sync_to_actions_create` | `COMPLIANCETOOL` | API endpoint that allows compliance assessments to be viewed or edited. |
| `ciso_assistant_api_compliance_assessments_sync_to_actions_retrieve` | `COMPLIANCETOOL` | API endpoint that allows compliance assessments to be viewed or edited. |
| `ciso_assistant_api_compliance_assessments_threats_metrics_retrieve` | `COMPLIANCETOOL` | API endpoint that allows compliance assessments to be viewed or edited. |
| `ciso_assistant_api_compliance_assessments_tree_retrieve` | `COMPLIANCETOOL` | API endpoint that allows compliance assessments to be viewed or edited. |
| `ciso_assistant_api_compliance_assessments_update` | `COMPLIANCETOOL` | API endpoint that allows compliance assessments to be viewed or edited. |
| `ciso_assistant_api_compliance_assessments_update_requirement_create` | `COMPLIANCETOOL` | API endpoint that allows compliance assessments to be viewed or edited. |
| `ciso_assistant_api_compliance_assessments_word_report_retrieve` | `COMPLIANCETOOL` | Word report generation (Exec) |
| `ciso_assistant_api_compliance_assessments_xlsx_retrieve` | `COMPLIANCETOOL` | API endpoint that allows compliance assessments to be viewed or edited. |
| `ciso_assistant_api_composer_data_retrieve` | `ANALYTICS_METROLOGYTOOL` | api_composer_data_retrieve |
| `ciso_assistant_api_content_types_retrieve` | `GRANULARTOOL` | api_content_types_retrieve |
| `ciso_assistant_api_contracts_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_contracts_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_contracts_create` | `GRANULARTOOL` | API endpoint that allows contracts to be viewed or edited. |
| `ciso_assistant_api_contracts_currency_retrieve` | `GRANULARTOOL` | API endpoint that allows contracts to be viewed or edited. |
| `ciso_assistant_api_contracts_destroy` | `GRANULARTOOL` | API endpoint that allows contracts to be viewed or edited. |
| `ciso_assistant_api_contracts_dora_contractual_arrangement_retrieve` | `GRANULARTOOL` | API endpoint that allows contracts to be viewed or edited. |
| `ciso_assistant_api_contracts_export_csv_retrieve` | `GRANULARTOOL` | API endpoint that allows contracts to be viewed or edited. |
| `ciso_assistant_api_contracts_export_xlsx_retrieve` | `GRANULARTOOL` | API endpoint that allows contracts to be viewed or edited. |
| `ciso_assistant_api_contracts_governing_law_country_retrieve` | `GRANULARTOOL` | API endpoint that allows contracts to be viewed or edited. |
| `ciso_assistant_api_contracts_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_contracts_object_retrieve` | `GRANULARTOOL` | API endpoint that allows contracts to be viewed or edited. |
| `ciso_assistant_api_contracts_partial_update` | `GRANULARTOOL` | API endpoint that allows contracts to be viewed or edited. |
| `ciso_assistant_api_contracts_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_contracts_status_retrieve` | `GRANULARTOOL` | API endpoint that allows contracts to be viewed or edited. |
| `ciso_assistant_api_contracts_termination_reason_retrieve` | `GRANULARTOOL` | API endpoint that allows contracts to be viewed or edited. |
| `ciso_assistant_api_contracts_update` | `GRANULARTOOL` | API endpoint that allows contracts to be viewed or edited. |
| `ciso_assistant_api_crq_quantitative_risk_hypotheses_batch_action_create` | `CRQTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_crq_quantitative_risk_hypotheses_cascade_info_retrieve` | `CRQTOOL` | Cascade preview: |
| `ciso_assistant_api_crq_quantitative_risk_hypotheses_create` | `CRQTOOL` | api_crq_quantitative_risk_hypotheses_create |
| `ciso_assistant_api_crq_quantitative_risk_hypotheses_default_ref_id_retrieve` | `CRQTOOL` | api_crq_quantitative_risk_hypotheses_default_ref_id_retrieve |
| `ciso_assistant_api_crq_quantitative_risk_hypotheses_destroy` | `CRQTOOL` | api_crq_quantitative_risk_hypotheses_destroy |
| `ciso_assistant_api_crq_quantitative_risk_hypotheses_lec_retrieve` | `CRQTOOL` | Returns the Loss Exceedance Curve data from stored simulation results. |
| `ciso_assistant_api_crq_quantitative_risk_hypotheses_list` | `CRQTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_crq_quantitative_risk_hypotheses_object_retrieve` | `CRQTOOL` | api_crq_quantitative_risk_hypotheses_object_retrieve |
| `ciso_assistant_api_crq_quantitative_risk_hypotheses_partial_update` | `CRQTOOL` | api_crq_quantitative_risk_hypotheses_partial_update |
| `ciso_assistant_api_crq_quantitative_risk_hypotheses_retrieve` | `CRQTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_crq_quantitative_risk_hypotheses_risk_stage_retrieve` | `CRQTOOL` | api_crq_quantitative_risk_hypotheses_risk_stage_retrieve |
| `ciso_assistant_api_crq_quantitative_risk_hypotheses_run_simulation_retrieve` | `CRQTOOL` | Triggers a Monte Carlo simulation for a specific risk hypothesis. |
| `ciso_assistant_api_crq_quantitative_risk_hypotheses_update` | `CRQTOOL` | api_crq_quantitative_risk_hypotheses_update |
| `ciso_assistant_api_crq_quantitative_risk_scenarios_batch_action_create` | `CRQTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_crq_quantitative_risk_scenarios_cascade_info_retrieve` | `CRQTOOL` | Cascade preview: |
| `ciso_assistant_api_crq_quantitative_risk_scenarios_create` | `CRQTOOL` | api_crq_quantitative_risk_scenarios_create |
| `ciso_assistant_api_crq_quantitative_risk_scenarios_default_ref_id_retrieve` | `CRQTOOL` | api_crq_quantitative_risk_scenarios_default_ref_id_retrieve |
| `ciso_assistant_api_crq_quantitative_risk_scenarios_destroy` | `CRQTOOL` | api_crq_quantitative_risk_scenarios_destroy |
| `ciso_assistant_api_crq_quantitative_risk_scenarios_lec_retrieve` | `CRQTOOL` | Returns combined Loss Exceedance Curve data for the scenario: |
| `ciso_assistant_api_crq_quantitative_risk_scenarios_list` | `CRQTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_crq_quantitative_risk_scenarios_object_retrieve` | `CRQTOOL` | api_crq_quantitative_risk_scenarios_object_retrieve |
| `ciso_assistant_api_crq_quantitative_risk_scenarios_partial_update` | `CRQTOOL` | api_crq_quantitative_risk_scenarios_partial_update |
| `ciso_assistant_api_crq_quantitative_risk_scenarios_priority_retrieve` | `CRQTOOL` | api_crq_quantitative_risk_scenarios_priority_retrieve |
| `ciso_assistant_api_crq_quantitative_risk_scenarios_retrieve` | `CRQTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_crq_quantitative_risk_scenarios_status_retrieve` | `CRQTOOL` | api_crq_quantitative_risk_scenarios_status_retrieve |
| `ciso_assistant_api_crq_quantitative_risk_scenarios_update` | `CRQTOOL` | api_crq_quantitative_risk_scenarios_update |
| `ciso_assistant_api_crq_quantitative_risk_studies_action_plan_budget_overview_list` | `CRQTOOL` | Mixin that computes budget aggregation over an applied controls queryset. |
| `ciso_assistant_api_crq_quantitative_risk_studies_action_plan_list` | `CRQTOOL` | Action plan for quantitative risk studies. |
| `ciso_assistant_api_crq_quantitative_risk_studies_ale_comparison_retrieve` | `CRQTOOL` | Returns data for ALE comparison chart showing: |
| `ciso_assistant_api_crq_quantitative_risk_studies_batch_action_create` | `CRQTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_crq_quantitative_risk_studies_cascade_info_retrieve` | `CRQTOOL` | Cascade preview: |
| `ciso_assistant_api_crq_quantitative_risk_studies_combined_ale_retrieve` | `CRQTOOL` | Returns combined ALE metrics for the quantitative risk study: |
| `ciso_assistant_api_crq_quantitative_risk_studies_combined_lec_retrieve` | `CRQTOOL` | Returns combined Loss Exceedance Curve data for the quantitative risk study: |
| `ciso_assistant_api_crq_quantitative_risk_studies_create` | `CRQTOOL` | api_crq_quantitative_risk_studies_create |
| `ciso_assistant_api_crq_quantitative_risk_studies_destroy` | `CRQTOOL` | api_crq_quantitative_risk_studies_destroy |
| `ciso_assistant_api_crq_quantitative_risk_studies_distribution_model_retrieve` | `CRQTOOL` | api_crq_quantitative_risk_studies_distribution_model_retrieve |
| `ciso_assistant_api_crq_quantitative_risk_studies_executive_summary_retrieve` | `CRQTOOL` | Returns executive summary data for the quantitative risk study. |
| `ciso_assistant_api_crq_quantitative_risk_studies_key_metrics_retrieve` | `CRQTOOL` | Returns key metrics data for quantitative risk scenarios scoped per study. |
| `ciso_assistant_api_crq_quantitative_risk_studies_list` | `CRQTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_crq_quantitative_risk_studies_object_retrieve` | `CRQTOOL` | api_crq_quantitative_risk_studies_object_retrieve |
| `ciso_assistant_api_crq_quantitative_risk_studies_partial_update` | `CRQTOOL` | api_crq_quantitative_risk_studies_partial_update |
| `ciso_assistant_api_crq_quantitative_risk_studies_retrieve` | `CRQTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_crq_quantitative_risk_studies_retrigger_all_simulations_create` | `CRQTOOL` | Retriggers all simulations for the quantitative risk study. |
| `ciso_assistant_api_crq_quantitative_risk_studies_status_retrieve` | `CRQTOOL` | api_crq_quantitative_risk_studies_status_retrieve |
| `ciso_assistant_api_crq_quantitative_risk_studies_update` | `CRQTOOL` | api_crq_quantitative_risk_studies_update |
| `ciso_assistant_api_csrf_retrieve` | `AUTH_USERSTOOL` | API endpoint that returns the CSRF token. |
| `ciso_assistant_api_cwes_autocomplete_retrieve` | `GRANULARTOOL` | API endpoint that allows CWEs to be viewed or edited. |
| `ciso_assistant_api_cwes_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_cwes_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_cwes_create` | `GRANULARTOOL` | API endpoint that allows CWEs to be viewed or edited. |
| `ciso_assistant_api_cwes_destroy` | `GRANULARTOOL` | API endpoint that allows CWEs to be viewed or edited. |
| `ciso_assistant_api_cwes_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_cwes_object_retrieve` | `GRANULARTOOL` | API endpoint that allows CWEs to be viewed or edited. |
| `ciso_assistant_api_cwes_partial_update` | `GRANULARTOOL` | API endpoint that allows CWEs to be viewed or edited. |
| `ciso_assistant_api_cwes_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_cwes_sync_catalog_create` | `GRANULARTOOL` | Sync CWE catalog from MITRE. |
| `ciso_assistant_api_cwes_update` | `GRANULARTOOL` | API endpoint that allows CWEs to be viewed or edited. |
| `ciso_assistant_api_data_wizard_load_file_create` | `GRANULARTOOL` | api_data_wizard_load_file_create |
| `ciso_assistant_api_document_attachments_batch_action_create` | `EVIDENCETOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_document_attachments_cascade_info_retrieve` | `EVIDENCETOOL` | Cascade preview: |
| `ciso_assistant_api_document_attachments_create` | `EVIDENCETOOL` | API endpoint for serving document attachment files. |
| `ciso_assistant_api_document_attachments_destroy` | `EVIDENCETOOL` | API endpoint for serving document attachment files. |
| `ciso_assistant_api_document_attachments_file_retrieve` | `EVIDENCETOOL` | Serve the attachment file with correct content type. |
| `ciso_assistant_api_document_attachments_object_retrieve` | `EVIDENCETOOL` | API endpoint for serving document attachment files. |
| `ciso_assistant_api_document_attachments_partial_update` | `EVIDENCETOOL` | API endpoint for serving document attachment files. |
| `ciso_assistant_api_document_attachments_retrieve` | `EVIDENCETOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_document_attachments_retrieve_2` | `EVIDENCETOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_document_attachments_update` | `EVIDENCETOOL` | API endpoint for serving document attachment files. |
| `ciso_assistant_api_document_revisions_approve_create` | `EVIDENCETOOL` | Approve a revision: transition from in_review to validated. |
| `ciso_assistant_api_document_revisions_batch_action_create` | `EVIDENCETOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_document_revisions_cascade_info_retrieve` | `EVIDENCETOOL` | Cascade preview: |
| `ciso_assistant_api_document_revisions_create` | `EVIDENCETOOL` | API endpoint that allows document revisions to be viewed or edited. |
| `ciso_assistant_api_document_revisions_destroy` | `EVIDENCETOOL` | API endpoint that allows document revisions to be viewed or edited. |
| `ciso_assistant_api_document_revisions_diff_retrieve` | `EVIDENCETOOL` | Compute unified diff between this revision and another of the same document. |
| `ciso_assistant_api_document_revisions_edit_diff_retrieve` | `EVIDENCETOOL` | Compute unified diff between two DocumentEdit content snapshots. |
| `ciso_assistant_api_document_revisions_edit_history_retrieve` | `EVIDENCETOOL` | Return the edit history for this revision. |
| `ciso_assistant_api_document_revisions_edit_snapshot_retrieve` | `EVIDENCETOOL` | Return the content snapshot of a specific edit. |
| `ciso_assistant_api_document_revisions_editing_status_retrieve` | `EVIDENCETOOL` | Check who is currently editing. |
| `ciso_assistant_api_document_revisions_export_pdf_retrieve` | `EVIDENCETOOL` | Export revision content as a PDF document. |
| `ciso_assistant_api_document_revisions_list` | `EVIDENCETOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_document_revisions_object_retrieve` | `EVIDENCETOOL` | API endpoint that allows document revisions to be viewed or edited. |
| `ciso_assistant_api_document_revisions_partial_update` | `EVIDENCETOOL` | API endpoint that allows document revisions to be viewed or edited. |
| `ciso_assistant_api_document_revisions_publish_create` | `EVIDENCETOOL` | Publish a validated revision: deprecate previous, generate PDF. |
| `ciso_assistant_api_document_revisions_request_changes_create` | `EVIDENCETOOL` | Request changes on an in-review revision. |
| `ciso_assistant_api_document_revisions_retrieve` | `EVIDENCETOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_document_revisions_start_editing_create` | `EVIDENCETOOL` | Mark the current user as editing this revision. |
| `ciso_assistant_api_document_revisions_status_retrieve` | `EVIDENCETOOL` | API endpoint that allows document revisions to be viewed or edited. |
| `ciso_assistant_api_document_revisions_stop_editing_create` | `EVIDENCETOOL` | Release the editing lock. |
| `ciso_assistant_api_document_revisions_submit_for_review_create` | `EVIDENCETOOL` | Transition from draft or change_requested to in_review. |
| `ciso_assistant_api_document_revisions_take_over_editing_create` | `EVIDENCETOOL` | Force-acquire the editing lock, overriding the current editor. |
| `ciso_assistant_api_document_revisions_update` | `EVIDENCETOOL` | API endpoint that allows document revisions to be viewed or edited. |
| `ciso_assistant_api_ebios_rm_attack_paths_batch_action_create` | `EBIOS_RMTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_ebios_rm_attack_paths_cascade_info_retrieve` | `EBIOS_RMTOOL` | Cascade preview: |
| `ciso_assistant_api_ebios_rm_attack_paths_create` | `EBIOS_RMTOOL` | api_ebios_rm_attack_paths_create |
| `ciso_assistant_api_ebios_rm_attack_paths_destroy` | `EBIOS_RMTOOL` | api_ebios_rm_attack_paths_destroy |
| `ciso_assistant_api_ebios_rm_attack_paths_list` | `EBIOS_RMTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_ebios_rm_attack_paths_object_retrieve` | `EBIOS_RMTOOL` | api_ebios_rm_attack_paths_object_retrieve |
| `ciso_assistant_api_ebios_rm_attack_paths_partial_update` | `EBIOS_RMTOOL` | api_ebios_rm_attack_paths_partial_update |
| `ciso_assistant_api_ebios_rm_attack_paths_retrieve` | `EBIOS_RMTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_ebios_rm_attack_paths_update` | `EBIOS_RMTOOL` | api_ebios_rm_attack_paths_update |
| `ciso_assistant_api_ebios_rm_elementary_actions_attack_stage_retrieve` | `EBIOS_RMTOOL` | api_ebios_rm_elementary_actions_attack_stage_retrieve |
| `ciso_assistant_api_ebios_rm_elementary_actions_batch_action_create` | `EBIOS_RMTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_ebios_rm_elementary_actions_cascade_info_retrieve` | `EBIOS_RMTOOL` | Cascade preview: |
| `ciso_assistant_api_ebios_rm_elementary_actions_create` | `EBIOS_RMTOOL` | api_ebios_rm_elementary_actions_create |
| `ciso_assistant_api_ebios_rm_elementary_actions_destroy` | `EBIOS_RMTOOL` | api_ebios_rm_elementary_actions_destroy |
| `ciso_assistant_api_ebios_rm_elementary_actions_icon_retrieve` | `EBIOS_RMTOOL` | api_ebios_rm_elementary_actions_icon_retrieve |
| `ciso_assistant_api_ebios_rm_elementary_actions_list` | `EBIOS_RMTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_ebios_rm_elementary_actions_object_retrieve` | `EBIOS_RMTOOL` | api_ebios_rm_elementary_actions_object_retrieve |
| `ciso_assistant_api_ebios_rm_elementary_actions_partial_update` | `EBIOS_RMTOOL` | api_ebios_rm_elementary_actions_partial_update |
| `ciso_assistant_api_ebios_rm_elementary_actions_retrieve` | `EBIOS_RMTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_ebios_rm_elementary_actions_update` | `EBIOS_RMTOOL` | api_ebios_rm_elementary_actions_update |
| `ciso_assistant_api_ebios_rm_feared_events_batch_action_create` | `EBIOS_RMTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_ebios_rm_feared_events_batch_create_create` | `EBIOS_RMTOOL` | Batch create multiple feared events from a text list. |
| `ciso_assistant_api_ebios_rm_feared_events_cascade_info_retrieve` | `EBIOS_RMTOOL` | Cascade preview: |
| `ciso_assistant_api_ebios_rm_feared_events_create` | `EBIOS_RMTOOL` | api_ebios_rm_feared_events_create |
| `ciso_assistant_api_ebios_rm_feared_events_destroy` | `EBIOS_RMTOOL` | api_ebios_rm_feared_events_destroy |
| `ciso_assistant_api_ebios_rm_feared_events_gravity_retrieve` | `EBIOS_RMTOOL` | api_ebios_rm_feared_events_gravity_retrieve |
| `ciso_assistant_api_ebios_rm_feared_events_list` | `EBIOS_RMTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_ebios_rm_feared_events_object_retrieve` | `EBIOS_RMTOOL` | api_ebios_rm_feared_events_object_retrieve |
| `ciso_assistant_api_ebios_rm_feared_events_partial_update` | `EBIOS_RMTOOL` | api_ebios_rm_feared_events_partial_update |
| `ciso_assistant_api_ebios_rm_feared_events_retrieve` | `EBIOS_RMTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_ebios_rm_feared_events_risk_matrix_retrieve` | `EBIOS_RMTOOL` | api_ebios_rm_feared_events_risk_matrix_retrieve |
| `ciso_assistant_api_ebios_rm_feared_events_update` | `EBIOS_RMTOOL` | api_ebios_rm_feared_events_update |
| `ciso_assistant_api_ebios_rm_kill_chains_batch_action_create` | `EBIOS_RMTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_ebios_rm_kill_chains_cascade_info_retrieve` | `EBIOS_RMTOOL` | Cascade preview: |
| `ciso_assistant_api_ebios_rm_kill_chains_create` | `EBIOS_RMTOOL` | api_ebios_rm_kill_chains_create |
| `ciso_assistant_api_ebios_rm_kill_chains_destroy` | `EBIOS_RMTOOL` | api_ebios_rm_kill_chains_destroy |
| `ciso_assistant_api_ebios_rm_kill_chains_list` | `EBIOS_RMTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_ebios_rm_kill_chains_logic_operator_retrieve` | `EBIOS_RMTOOL` | api_ebios_rm_kill_chains_logic_operator_retrieve |
| `ciso_assistant_api_ebios_rm_kill_chains_object_retrieve` | `EBIOS_RMTOOL` | api_ebios_rm_kill_chains_object_retrieve |
| `ciso_assistant_api_ebios_rm_kill_chains_partial_update` | `EBIOS_RMTOOL` | api_ebios_rm_kill_chains_partial_update |
| `ciso_assistant_api_ebios_rm_kill_chains_retrieve` | `EBIOS_RMTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_ebios_rm_kill_chains_update` | `EBIOS_RMTOOL` | api_ebios_rm_kill_chains_update |
| `ciso_assistant_api_ebios_rm_operating_modes_batch_action_create` | `EBIOS_RMTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_ebios_rm_operating_modes_build_graph_retrieve` | `EBIOS_RMTOOL` | api_ebios_rm_operating_modes_build_graph_retrieve |
| `ciso_assistant_api_ebios_rm_operating_modes_cascade_info_retrieve` | `EBIOS_RMTOOL` | Cascade preview: |
| `ciso_assistant_api_ebios_rm_operating_modes_create` | `EBIOS_RMTOOL` | api_ebios_rm_operating_modes_create |
| `ciso_assistant_api_ebios_rm_operating_modes_default_ref_id_retrieve` | `EBIOS_RMTOOL` | api_ebios_rm_operating_modes_default_ref_id_retrieve |
| `ciso_assistant_api_ebios_rm_operating_modes_destroy` | `EBIOS_RMTOOL` | api_ebios_rm_operating_modes_destroy |
| `ciso_assistant_api_ebios_rm_operating_modes_likelihood_retrieve` | `EBIOS_RMTOOL` | api_ebios_rm_operating_modes_likelihood_retrieve |
| `ciso_assistant_api_ebios_rm_operating_modes_list` | `EBIOS_RMTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_ebios_rm_operating_modes_object_retrieve` | `EBIOS_RMTOOL` | api_ebios_rm_operating_modes_object_retrieve |
| `ciso_assistant_api_ebios_rm_operating_modes_partial_update` | `EBIOS_RMTOOL` | api_ebios_rm_operating_modes_partial_update |
| `ciso_assistant_api_ebios_rm_operating_modes_retrieve` | `EBIOS_RMTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_ebios_rm_operating_modes_save_graph_create` | `EBIOS_RMTOOL` | api_ebios_rm_operating_modes_save_graph_create |
| `ciso_assistant_api_ebios_rm_operating_modes_update` | `EBIOS_RMTOOL` | api_ebios_rm_operating_modes_update |
| `ciso_assistant_api_ebios_rm_operational_scenarios_batch_action_create` | `EBIOS_RMTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_ebios_rm_operational_scenarios_cascade_info_retrieve` | `EBIOS_RMTOOL` | Cascade preview: |
| `ciso_assistant_api_ebios_rm_operational_scenarios_create` | `EBIOS_RMTOOL` | api_ebios_rm_operational_scenarios_create |
| `ciso_assistant_api_ebios_rm_operational_scenarios_destroy` | `EBIOS_RMTOOL` | api_ebios_rm_operational_scenarios_destroy |
| `ciso_assistant_api_ebios_rm_operational_scenarios_likelihood_retrieve` | `EBIOS_RMTOOL` | api_ebios_rm_operational_scenarios_likelihood_retrieve |
| `ciso_assistant_api_ebios_rm_operational_scenarios_list` | `EBIOS_RMTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_ebios_rm_operational_scenarios_object_retrieve` | `EBIOS_RMTOOL` | api_ebios_rm_operational_scenarios_object_retrieve |
| `ciso_assistant_api_ebios_rm_operational_scenarios_partial_update` | `EBIOS_RMTOOL` | api_ebios_rm_operational_scenarios_partial_update |
| `ciso_assistant_api_ebios_rm_operational_scenarios_retrieve` | `EBIOS_RMTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_ebios_rm_operational_scenarios_risk_matrix_retrieve` | `EBIOS_RMTOOL` | api_ebios_rm_operational_scenarios_risk_matrix_retrieve |
| `ciso_assistant_api_ebios_rm_operational_scenarios_update` | `EBIOS_RMTOOL` | api_ebios_rm_operational_scenarios_update |
| `ciso_assistant_api_ebios_rm_ro_to_activity_retrieve` | `EBIOS_RMTOOL` | api_ebios_rm_ro_to_activity_retrieve |
| `ciso_assistant_api_ebios_rm_ro_to_batch_action_create` | `EBIOS_RMTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_ebios_rm_ro_to_cascade_info_retrieve` | `EBIOS_RMTOOL` | Cascade preview: |
| `ciso_assistant_api_ebios_rm_ro_to_create` | `EBIOS_RMTOOL` | api_ebios_rm_ro_to_create |
| `ciso_assistant_api_ebios_rm_ro_to_destroy` | `EBIOS_RMTOOL` | api_ebios_rm_ro_to_destroy |
| `ciso_assistant_api_ebios_rm_ro_to_list` | `EBIOS_RMTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_ebios_rm_ro_to_motivation_retrieve` | `EBIOS_RMTOOL` | api_ebios_rm_ro_to_motivation_retrieve |
| `ciso_assistant_api_ebios_rm_ro_to_object_retrieve` | `EBIOS_RMTOOL` | api_ebios_rm_ro_to_object_retrieve |
| `ciso_assistant_api_ebios_rm_ro_to_partial_update` | `EBIOS_RMTOOL` | api_ebios_rm_ro_to_partial_update |
| `ciso_assistant_api_ebios_rm_ro_to_pertinence_retrieve` | `EBIOS_RMTOOL` | api_ebios_rm_ro_to_pertinence_retrieve |
| `ciso_assistant_api_ebios_rm_ro_to_resources_retrieve` | `EBIOS_RMTOOL` | api_ebios_rm_ro_to_resources_retrieve |
| `ciso_assistant_api_ebios_rm_ro_to_retrieve` | `EBIOS_RMTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_ebios_rm_ro_to_update` | `EBIOS_RMTOOL` | api_ebios_rm_ro_to_update |
| `ciso_assistant_api_ebios_rm_stakeholders_batch_action_create` | `EBIOS_RMTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_ebios_rm_stakeholders_cascade_info_retrieve` | `EBIOS_RMTOOL` | Cascade preview: |
| `ciso_assistant_api_ebios_rm_stakeholders_category_retrieve` | `EBIOS_RMTOOL` | api_ebios_rm_stakeholders_category_retrieve |
| `ciso_assistant_api_ebios_rm_stakeholders_chart_data_retrieve` | `EBIOS_RMTOOL` | api_ebios_rm_stakeholders_chart_data_retrieve |
| `ciso_assistant_api_ebios_rm_stakeholders_create` | `EBIOS_RMTOOL` | api_ebios_rm_stakeholders_create |
| `ciso_assistant_api_ebios_rm_stakeholders_destroy` | `EBIOS_RMTOOL` | api_ebios_rm_stakeholders_destroy |
| `ciso_assistant_api_ebios_rm_stakeholders_list` | `EBIOS_RMTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_ebios_rm_stakeholders_object_retrieve` | `EBIOS_RMTOOL` | api_ebios_rm_stakeholders_object_retrieve |
| `ciso_assistant_api_ebios_rm_stakeholders_partial_update` | `EBIOS_RMTOOL` | api_ebios_rm_stakeholders_partial_update |
| `ciso_assistant_api_ebios_rm_stakeholders_retrieve` | `EBIOS_RMTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_ebios_rm_stakeholders_update` | `EBIOS_RMTOOL` | api_ebios_rm_stakeholders_update |
| `ciso_assistant_api_ebios_rm_strategic_scenarios_batch_action_create` | `EBIOS_RMTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_ebios_rm_strategic_scenarios_cascade_info_retrieve` | `EBIOS_RMTOOL` | Cascade preview: |
| `ciso_assistant_api_ebios_rm_strategic_scenarios_create` | `EBIOS_RMTOOL` | api_ebios_rm_strategic_scenarios_create |
| `ciso_assistant_api_ebios_rm_strategic_scenarios_destroy` | `EBIOS_RMTOOL` | api_ebios_rm_strategic_scenarios_destroy |
| `ciso_assistant_api_ebios_rm_strategic_scenarios_list` | `EBIOS_RMTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_ebios_rm_strategic_scenarios_object_retrieve` | `EBIOS_RMTOOL` | api_ebios_rm_strategic_scenarios_object_retrieve |
| `ciso_assistant_api_ebios_rm_strategic_scenarios_partial_update` | `EBIOS_RMTOOL` | api_ebios_rm_strategic_scenarios_partial_update |
| `ciso_assistant_api_ebios_rm_strategic_scenarios_retrieve` | `EBIOS_RMTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_ebios_rm_strategic_scenarios_update` | `EBIOS_RMTOOL` | api_ebios_rm_strategic_scenarios_update |
| `ciso_assistant_api_ebios_rm_studies_batch_action_create` | `EBIOS_RMTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_ebios_rm_studies_cascade_info_retrieve` | `EBIOS_RMTOOL` | Cascade preview: |
| `ciso_assistant_api_ebios_rm_studies_create` | `EBIOS_RMTOOL` | API endpoint that allows ebios rm studies to be viewed or edited. |
| `ciso_assistant_api_ebios_rm_studies_destroy` | `EBIOS_RMTOOL` | API endpoint that allows ebios rm studies to be viewed or edited. |
| `ciso_assistant_api_ebios_rm_studies_ecosystem_chart_data_retrieve` | `EBIOS_RMTOOL` | API endpoint that allows ebios rm studies to be viewed or edited. |
| `ciso_assistant_api_ebios_rm_studies_ecosystem_circular_chart_data_retrieve` | `EBIOS_RMTOOL` | API endpoint that allows ebios rm studies to be viewed or edited. |
| `ciso_assistant_api_ebios_rm_studies_export_xlsx_retrieve` | `EBIOS_RMTOOL` | Export EBIOS RM study data to Excel with multiple sheets. |
| `ciso_assistant_api_ebios_rm_studies_gravity_retrieve` | `EBIOS_RMTOOL` | API endpoint that allows ebios rm studies to be viewed or edited. |
| `ciso_assistant_api_ebios_rm_studies_likelihood_retrieve` | `EBIOS_RMTOOL` | API endpoint that allows ebios rm studies to be viewed or edited. |
| `ciso_assistant_api_ebios_rm_studies_list` | `EBIOS_RMTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_ebios_rm_studies_object_retrieve` | `EBIOS_RMTOOL` | API endpoint that allows ebios rm studies to be viewed or edited. |
| `ciso_assistant_api_ebios_rm_studies_partial_update` | `EBIOS_RMTOOL` | API endpoint that allows ebios rm studies to be viewed or edited. |
| `ciso_assistant_api_ebios_rm_studies_quotation_method_retrieve` | `EBIOS_RMTOOL` | API endpoint that allows ebios rm studies to be viewed or edited. |
| `ciso_assistant_api_ebios_rm_studies_report_data_retrieve` | `EBIOS_RMTOOL` | Endpoint to prepare comprehensive report data for an EBIOS RM study. |
| `ciso_assistant_api_ebios_rm_studies_retrieve` | `EBIOS_RMTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_ebios_rm_studies_risk_matrix_retrieve` | `EBIOS_RMTOOL` | API endpoint that allows ebios rm studies to be viewed or edited. |
| `ciso_assistant_api_ebios_rm_studies_status_retrieve` | `EBIOS_RMTOOL` | API endpoint that allows ebios rm studies to be viewed or edited. |
| `ciso_assistant_api_ebios_rm_studies_update` | `EBIOS_RMTOOL` | API endpoint that allows ebios rm studies to be viewed or edited. |
| `ciso_assistant_api_ebios_rm_studies_visual_analysis_retrieve` | `EBIOS_RMTOOL` | API endpoint that allows ebios rm studies to be viewed or edited. |
| `ciso_assistant_api_ebios_rm_studies_workshop_step_partial_update` | `EBIOS_RMTOOL` | API endpoint that allows ebios rm studies to be viewed or edited. |
| `ciso_assistant_api_entities_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_entities_batch_create_create` | `GRANULARTOOL` | Batch create multiple entities from a text list. |
| `ciso_assistant_api_entities_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_entities_country_retrieve` | `GRANULARTOOL` | API endpoint that allows entities to be viewed or edited. |
| `ciso_assistant_api_entities_create` | `GRANULARTOOL` | API endpoint that allows entities to be viewed or edited. |
| `ciso_assistant_api_entities_currency_retrieve` | `GRANULARTOOL` | API endpoint that allows entities to be viewed or edited. |
| `ciso_assistant_api_entities_destroy` | `GRANULARTOOL` | Convert Django's ProtectedError into a 409 Conflict with the list of |
| `ciso_assistant_api_entities_dora_entity_hierarchy_retrieve` | `GRANULARTOOL` | API endpoint that allows entities to be viewed or edited. |
| `ciso_assistant_api_entities_dora_entity_type_retrieve` | `GRANULARTOOL` | API endpoint that allows entities to be viewed or edited. |
| `ciso_assistant_api_entities_dora_provider_person_type_retrieve` | `GRANULARTOOL` | API endpoint that allows entities to be viewed or edited. |
| `ciso_assistant_api_entities_dora_roi_lint_retrieve` | `GRANULARTOOL` | Validate DORA ROI requirements and return linting results. |
| `ciso_assistant_api_entities_export_csv_retrieve` | `GRANULARTOOL` | API endpoint that allows entities to be viewed or edited. |
| `ciso_assistant_api_entities_export_ecosystem_retrieve` | `GRANULARTOOL` | Export the TPRM ecosystem as a multi-sheet Excel file with three sheets |
| `ciso_assistant_api_entities_export_xlsx_retrieve` | `GRANULARTOOL` | API endpoint that allows entities to be viewed or edited. |
| `ciso_assistant_api_entities_generate_dora_roi_retrieve` | `GRANULARTOOL` | Generate DORA Register of Information (ROI) as a zip file containing CSV data. |
| `ciso_assistant_api_entities_graph_retrieve` | `GRANULARTOOL` | Generate graph data for entities, showing: |
| `ciso_assistant_api_entities_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_entities_object_retrieve` | `GRANULARTOOL` | API endpoint that allows entities to be viewed or edited. |
| `ciso_assistant_api_entities_partial_update` | `GRANULARTOOL` | API endpoint that allows entities to be viewed or edited. |
| `ciso_assistant_api_entities_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_entities_update` | `GRANULARTOOL` | API endpoint that allows entities to be viewed or edited. |
| `ciso_assistant_api_entity_assessments_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_entity_assessments_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_entity_assessments_conclusion_retrieve` | `GRANULARTOOL` | API endpoint that allows entity assessments to be viewed or edited. |
| `ciso_assistant_api_entity_assessments_create` | `GRANULARTOOL` | API endpoint that allows entity assessments to be viewed or edited. |
| `ciso_assistant_api_entity_assessments_destroy` | `GRANULARTOOL` | API endpoint that allows entity assessments to be viewed or edited. |
| `ciso_assistant_api_entity_assessments_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_entity_assessments_metrics_retrieve` | `GRANULARTOOL` | API endpoint that allows entity assessments to be viewed or edited. |
| `ciso_assistant_api_entity_assessments_object_retrieve` | `GRANULARTOOL` | API endpoint that allows entity assessments to be viewed or edited. |
| `ciso_assistant_api_entity_assessments_partial_update` | `GRANULARTOOL` | API endpoint that allows entity assessments to be viewed or edited. |
| `ciso_assistant_api_entity_assessments_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_entity_assessments_status_retrieve` | `GRANULARTOOL` | API endpoint that allows entity assessments to be viewed or edited. |
| `ciso_assistant_api_entity_assessments_update` | `GRANULARTOOL` | API endpoint that allows entity assessments to be viewed or edited. |
| `ciso_assistant_api_evidence_revisions_attachment_retrieve` | `EVIDENCETOOL` | API endpoint that allows evidence revisions to be viewed or edited. |
| `ciso_assistant_api_evidence_revisions_batch_action_create` | `EVIDENCETOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_evidence_revisions_cascade_info_retrieve` | `EVIDENCETOOL` | Cascade preview: |
| `ciso_assistant_api_evidence_revisions_create` | `EVIDENCETOOL` | API endpoint that allows evidence revisions to be viewed or edited. |
| `ciso_assistant_api_evidence_revisions_delete_attachment_create` | `EVIDENCETOOL` | API endpoint that allows evidence revisions to be viewed or edited. |
| `ciso_assistant_api_evidence_revisions_destroy` | `EVIDENCETOOL` | API endpoint that allows evidence revisions to be viewed or edited. |
| `ciso_assistant_api_evidence_revisions_list` | `EVIDENCETOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_evidence_revisions_object_retrieve` | `EVIDENCETOOL` | API endpoint that allows evidence revisions to be viewed or edited. |
| `ciso_assistant_api_evidence_revisions_partial_update` | `EVIDENCETOOL` | API endpoint that allows evidence revisions to be viewed or edited. |
| `ciso_assistant_api_evidence_revisions_retrieve` | `EVIDENCETOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_evidence_revisions_update` | `EVIDENCETOOL` | API endpoint that allows evidence revisions to be viewed or edited. |
| `ciso_assistant_api_evidence_revisions_upload_create` | `EVIDENCETOOL` | api_evidence_revisions_upload_create |
| `ciso_assistant_api_evidences_attachment_retrieve` | `EVIDENCETOOL` | API endpoint that allows evidences to be viewed or edited. |
| `ciso_assistant_api_evidences_batch_action_create` | `EVIDENCETOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_evidences_batch_upload_create` | `EVIDENCETOOL` | Bulk-upload evidences from a multipart payload. |
| `ciso_assistant_api_evidences_cascade_info_retrieve` | `EVIDENCETOOL` | Cascade preview: |
| `ciso_assistant_api_evidences_create` | `EVIDENCETOOL` | API endpoint that allows evidences to be viewed or edited. |
| `ciso_assistant_api_evidences_destroy` | `EVIDENCETOOL` | API endpoint that allows evidences to be viewed or edited. |
| `ciso_assistant_api_evidences_list` | `EVIDENCETOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_evidences_object_retrieve` | `EVIDENCETOOL` | API endpoint that allows evidences to be viewed or edited. |
| `ciso_assistant_api_evidences_owner_retrieve` | `EVIDENCETOOL` | API endpoint that allows evidences to be viewed or edited. |
| `ciso_assistant_api_evidences_partial_update` | `EVIDENCETOOL` | API endpoint that allows evidences to be viewed or edited. |
| `ciso_assistant_api_evidences_retrieve` | `EVIDENCETOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_evidences_status_retrieve` | `EVIDENCETOOL` | API endpoint that allows evidences to be viewed or edited. |
| `ciso_assistant_api_evidences_update` | `EVIDENCETOOL` | API endpoint that allows evidences to be viewed or edited. |
| `ciso_assistant_api_evidences_upload_create` | `EVIDENCETOOL` | api_evidences_upload_create |
| `ciso_assistant_api_filtering_labels_batch_action_create` | `FRAMEWORKS_LIBRARIESTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_filtering_labels_cascade_info_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | Cascade preview: |
| `ciso_assistant_api_filtering_labels_create` | `FRAMEWORKS_LIBRARIESTOOL` | API endpoint that allows labels to be viewed or edited. |
| `ciso_assistant_api_filtering_labels_destroy` | `FRAMEWORKS_LIBRARIESTOOL` | API endpoint that allows labels to be viewed or edited. |
| `ciso_assistant_api_filtering_labels_list` | `FRAMEWORKS_LIBRARIESTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_filtering_labels_object_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | API endpoint that allows labels to be viewed or edited. |
| `ciso_assistant_api_filtering_labels_partial_update` | `FRAMEWORKS_LIBRARIESTOOL` | API endpoint that allows labels to be viewed or edited. |
| `ciso_assistant_api_filtering_labels_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_filtering_labels_update` | `FRAMEWORKS_LIBRARIESTOOL` | API endpoint that allows labels to be viewed or edited. |
| `ciso_assistant_api_findings_assessments_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_findings_assessments_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_findings_assessments_category_retrieve` | `GRANULARTOOL` | api_findings_assessments_category_retrieve |
| `ciso_assistant_api_findings_assessments_create` | `GRANULARTOOL` | api_findings_assessments_create |
| `ciso_assistant_api_findings_assessments_destroy` | `GRANULARTOOL` | api_findings_assessments_destroy |
| `ciso_assistant_api_findings_assessments_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_findings_assessments_md_retrieve` | `GRANULARTOOL` | api_findings_assessments_md_retrieve |
| `ciso_assistant_api_findings_assessments_metrics_retrieve` | `GRANULARTOOL` | api_findings_assessments_metrics_retrieve |
| `ciso_assistant_api_findings_assessments_object_retrieve` | `GRANULARTOOL` | api_findings_assessments_object_retrieve |
| `ciso_assistant_api_findings_assessments_partial_update` | `GRANULARTOOL` | api_findings_assessments_partial_update |
| `ciso_assistant_api_findings_assessments_pdf_retrieve` | `GRANULARTOOL` | api_findings_assessments_pdf_retrieve |
| `ciso_assistant_api_findings_assessments_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_findings_assessments_status_retrieve` | `GRANULARTOOL` | api_findings_assessments_status_retrieve |
| `ciso_assistant_api_findings_assessments_sunburst_data_retrieve` | `GRANULARTOOL` | Returns FindingsAssessment data structured for sunburst visualization: |
| `ciso_assistant_api_findings_assessments_update` | `GRANULARTOOL` | api_findings_assessments_update |
| `ciso_assistant_api_findings_assessments_xlsx_retrieve` | `GRANULARTOOL` | api_findings_assessments_xlsx_retrieve |
| `ciso_assistant_api_findings_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_findings_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_findings_create` | `GRANULARTOOL` | api_findings_create |
| `ciso_assistant_api_findings_destroy` | `GRANULARTOOL` | api_findings_destroy |
| `ciso_assistant_api_findings_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_findings_object_retrieve` | `GRANULARTOOL` | api_findings_object_retrieve |
| `ciso_assistant_api_findings_owner_retrieve` | `GRANULARTOOL` | api_findings_owner_retrieve |
| `ciso_assistant_api_findings_partial_update` | `GRANULARTOOL` | api_findings_partial_update |
| `ciso_assistant_api_findings_priority_retrieve` | `GRANULARTOOL` | api_findings_priority_retrieve |
| `ciso_assistant_api_findings_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_findings_sankey_data_retrieve` | `GRANULARTOOL` | Returns findings data structured for Sankey diagram: |
| `ciso_assistant_api_findings_severity_retrieve` | `GRANULARTOOL` | api_findings_severity_retrieve |
| `ciso_assistant_api_findings_status_retrieve` | `GRANULARTOOL` | api_findings_status_retrieve |
| `ciso_assistant_api_findings_update` | `GRANULARTOOL` | api_findings_update |
| `ciso_assistant_api_folders_batch_action_create` | `GOVERNANCETOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_folders_cascade_info_retrieve` | `GOVERNANCETOOL` | Cascade preview: |
| `ciso_assistant_api_folders_create` | `GOVERNANCETOOL` | API endpoint that allows folders to be viewed or edited. |
| `ciso_assistant_api_folders_destroy` | `GOVERNANCETOOL` | API endpoint that allows folders to be viewed or edited. |
| `ciso_assistant_api_folders_export_retrieve` | `GOVERNANCETOOL` | Export the domain as a zip file containing a JSON dump of all objects and their relationships |
| `ciso_assistant_api_folders_get_accessible_objects_retrieve` | `GOVERNANCETOOL` | Return the list of folders, perimeters, frameworks and risk matrices |
| `ciso_assistant_api_folders_ids_retrieve` | `GOVERNANCETOOL` | API endpoint that allows folders to be viewed or edited. |
| `ciso_assistant_api_folders_import_create` | `GOVERNANCETOOL` | Handle file upload and initiate import process. |
| `ciso_assistant_api_folders_import_dummy_create` | `GOVERNANCETOOL` | API endpoint that allows folders to be viewed or edited. |
| `ciso_assistant_api_folders_list` | `GOVERNANCETOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_folders_my_assignments_retrieve` | `GOVERNANCETOOL` | API endpoint that allows folders to be viewed or edited. |
| `ciso_assistant_api_folders_object_retrieve` | `GOVERNANCETOOL` | API endpoint that allows folders to be viewed or edited. |
| `ciso_assistant_api_folders_org_tree_retrieve` | `GOVERNANCETOOL` | Return the tree of domains and perimeters. |
| `ciso_assistant_api_folders_partial_update` | `GOVERNANCETOOL` | API endpoint that allows folders to be viewed or edited. |
| `ciso_assistant_api_folders_quality_check_retrieve` | `GOVERNANCETOOL` | Returns the quality check of assessments grouped by folder. |
| `ciso_assistant_api_folders_quality_check_retrieve_2` | `GOVERNANCETOOL` | Returns the quality check of assessments for a specific folder. |
| `ciso_assistant_api_folders_retrieve` | `GOVERNANCETOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_folders_update` | `GOVERNANCETOOL` | API endpoint that allows folders to be viewed or edited. |
| `ciso_assistant_api_folders_users_list` | `GOVERNANCETOOL` | api_folders_users_list |
| `ciso_assistant_api_frameworks_batch_action_create` | `FRAMEWORKS_LIBRARIESTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_frameworks_cascade_info_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | Cascade preview: |
| `ciso_assistant_api_frameworks_create` | `FRAMEWORKS_LIBRARIESTOOL` | API endpoint that allows frameworks to be viewed or edited. |
| `ciso_assistant_api_frameworks_destroy` | `FRAMEWORKS_LIBRARIESTOOL` | API endpoint that allows frameworks to be viewed or edited. |
| `ciso_assistant_api_frameworks_discard_draft_create` | `FRAMEWORKS_LIBRARIESTOOL` | Discard editing_draft without affecting relational data. |
| `ciso_assistant_api_frameworks_duplicate_create` | `FRAMEWORKS_LIBRARIESTOOL` | Deep-clone a framework with all requirement nodes, questions, and choices. |
| `ciso_assistant_api_frameworks_excel_template_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | API endpoint that allows frameworks to be viewed or edited. |
| `ciso_assistant_api_frameworks_export_yaml_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | Export a framework as a library-compatible YAML file. |
| `ciso_assistant_api_frameworks_list` | `FRAMEWORKS_LIBRARIESTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_frameworks_mapping_stats_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | API endpoint that allows frameworks to be viewed or edited. |
| `ciso_assistant_api_frameworks_mappings_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | API endpoint that allows frameworks to be viewed or edited. |
| `ciso_assistant_api_frameworks_names_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | API endpoint that allows frameworks to be viewed or edited. |
| `ciso_assistant_api_frameworks_object_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | API endpoint that allows frameworks to be viewed or edited. |
| `ciso_assistant_api_frameworks_partial_update` | `FRAMEWORKS_LIBRARIESTOOL` | API endpoint that allows frameworks to be viewed or edited. |
| `ciso_assistant_api_frameworks_provider_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | API endpoint that allows frameworks to be viewed or edited. |
| `ciso_assistant_api_frameworks_publish_draft_create` | `FRAMEWORKS_LIBRARIESTOOL` | Publish editing_draft → relational DB, snapshot history, bump version. |
| `ciso_assistant_api_frameworks_publish_draft_preview_create` | `FRAMEWORKS_LIBRARIESTOOL` | Preview the impact of publishing the current draft. |
| `ciso_assistant_api_frameworks_report_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | Cross-assessment report for one framework. |
| `ciso_assistant_api_frameworks_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_frameworks_save_draft_partial_update` | `FRAMEWORKS_LIBRARIESTOOL` | Update editing_draft with the current WIP from the frontend. |
| `ciso_assistant_api_frameworks_serve_image_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | Serve an image attachment belonging to this framework. |
| `ciso_assistant_api_frameworks_start_editing_create` | `FRAMEWORKS_LIBRARIESTOOL` | Serialize the framework tree into editing_draft to begin editing. |
| `ciso_assistant_api_frameworks_tree_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | API endpoint that allows frameworks to be viewed or edited. |
| `ciso_assistant_api_frameworks_update` | `FRAMEWORKS_LIBRARIESTOOL` | API endpoint that allows frameworks to be viewed or edited. |
| `ciso_assistant_api_frameworks_upload_image_create` | `FRAMEWORKS_LIBRARIESTOOL` | Upload an image to this framework (for splash screen markdown in draft mode). |
| `ciso_assistant_api_frameworks_used_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | API endpoint that allows frameworks to be viewed or edited. |
| `ciso_assistant_api_get_audits_metrics_retrieve` | `ANALYTICS_METROLOGYTOOL` | API endpoint that returns the expensive audit metrics (progress avg + audits stats). |
| `ciso_assistant_api_get_combined_assessments_status_retrieve` | `ANALYTICS_METROLOGYTOOL` | API endpoint that returns combined assessment counts per status |
| `ciso_assistant_api_get_counters_retrieve` | `ANALYTICS_METROLOGYTOOL` | API endpoint that returns the counters |
| `ciso_assistant_api_get_governance_calendar_data_retrieve` | `ANALYTICS_METROLOGYTOOL` | API endpoint that returns governance activity calendar data |
| `ciso_assistant_api_get_metrics_retrieve` | `ANALYTICS_METROLOGYTOOL` | API endpoint that returns the counters |
| `ciso_assistant_api_health_retrieve` | `GRANULARTOOL` | api_health_retrieve |
| `ciso_assistant_api_iam_auth_tokens_create` | `AUTH_USERSTOOL` | api_iam_auth_tokens_create |
| `ciso_assistant_api_iam_auth_tokens_destroy` | `AUTH_USERSTOOL` | api_iam_auth_tokens_destroy |
| `ciso_assistant_api_iam_auth_tokens_retrieve` | `AUTH_USERSTOOL` | Get all personal access tokens for the user. |
| `ciso_assistant_api_iam_change_password_create` | `AUTH_USERSTOOL` | An endpoint for changing password. |
| `ciso_assistant_api_iam_current_user_retrieve` | `AUTH_USERSTOOL` | api_iam_current_user_retrieve |
| `ciso_assistant_api_iam_login_create` | `AUTH_USERSTOOL` | api_iam_login_create |
| `ciso_assistant_api_iam_logout_create` | `AUTH_USERSTOOL` | api_iam_logout_create |
| `ciso_assistant_api_iam_logoutall_create` | `AUTH_USERSTOOL` | Log the user out of all sessions |
| `ciso_assistant_api_iam_password_reset_confirm_create` | `AUTH_USERSTOOL` | API Endpoint for reset password confirm |
| `ciso_assistant_api_iam_password_reset_create` | `AUTH_USERSTOOL` | api_iam_password_reset_create |
| `ciso_assistant_api_iam_revoke_sessions_create` | `AUTH_USERSTOOL` | An endpoint for revoking all other user sessions (except the current one). |
| `ciso_assistant_api_iam_session_token_create` | `AUTH_USERSTOOL` | API Endpoint for getting the session token from an access token |
| `ciso_assistant_api_iam_set_password_create` | `AUTH_USERSTOOL` | An endpoint for setting a password as an administrator. |
| `ciso_assistant_api_incidents_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_incidents_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_incidents_create` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_incidents_destroy` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_incidents_detection_breakdown_retrieve` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_incidents_detection_retrieve` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_incidents_export_csv_retrieve` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_incidents_export_xlsx_retrieve` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_incidents_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_incidents_md_retrieve` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_incidents_monthly_metrics_retrieve` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_incidents_object_retrieve` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_incidents_partial_update` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_incidents_pdf_retrieve` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_incidents_qualifications_breakdown_retrieve` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_incidents_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_incidents_severity_breakdown_retrieve` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_incidents_severity_retrieve` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_incidents_status_retrieve` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_incidents_summary_stats_retrieve` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_incidents_update` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_integrations_configs_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_integrations_configs_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_integrations_configs_create` | `GRANULARTOOL` | API endpoint for creating, viewing, updating, and deleting Integration Configurations. |
| `ciso_assistant_api_integrations_configs_destroy` | `GRANULARTOOL` | API endpoint for creating, viewing, updating, and deleting Integration Configurations. |
| `ciso_assistant_api_integrations_configs_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_integrations_configs_object_retrieve` | `GRANULARTOOL` | API endpoint for creating, viewing, updating, and deleting Integration Configurations. |
| `ciso_assistant_api_integrations_configs_partial_update` | `GRANULARTOOL` | API endpoint for creating, viewing, updating, and deleting Integration Configurations. |
| `ciso_assistant_api_integrations_configs_remote_objects_retrieve` | `GRANULARTOOL` | API endpoint for creating, viewing, updating, and deleting Integration Configurations. |
| `ciso_assistant_api_integrations_configs_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_integrations_configs_rpc_create` | `GRANULARTOOL` | Generic endpoint for interactive integration commands. |
| `ciso_assistant_api_integrations_configs_test_connection_create` | `GRANULARTOOL` | Custom action to test the connection for a saved integration configuration. |
| `ciso_assistant_api_integrations_configs_update` | `GRANULARTOOL` | API endpoint for creating, viewing, updating, and deleting Integration Configurations. |
| `ciso_assistant_api_integrations_providers_list` | `GRANULARTOOL` | An API endpoint to list all available (and active) Integration Providers. |
| `ciso_assistant_api_integrations_sync_mappings_destroy` | `GRANULARTOOL` | An API endpoint to delete a SyncMapping. |
| `ciso_assistant_api_integrations_test_connection_create` | `GRANULARTOOL` | An endpoint to test connection credentials without saving them. |
| `ciso_assistant_api_journey_steps_batch_action_create` | `GOVERNANCETOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_journey_steps_cascade_info_retrieve` | `GOVERNANCETOOL` | Cascade preview: |
| `ciso_assistant_api_journey_steps_create` | `GOVERNANCETOOL` | api_journey_steps_create |
| `ciso_assistant_api_journey_steps_destroy` | `GOVERNANCETOOL` | api_journey_steps_destroy |
| `ciso_assistant_api_journey_steps_list` | `GOVERNANCETOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_journey_steps_object_retrieve` | `GOVERNANCETOOL` | api_journey_steps_object_retrieve |
| `ciso_assistant_api_journey_steps_partial_update` | `GOVERNANCETOOL` | api_journey_steps_partial_update |
| `ciso_assistant_api_journey_steps_retrieve` | `GOVERNANCETOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_journey_steps_update` | `GOVERNANCETOOL` | api_journey_steps_update |
| `ciso_assistant_api_journeys_batch_action_create` | `GOVERNANCETOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_journeys_cascade_info_retrieve` | `GOVERNANCETOOL` | Cascade preview: |
| `ciso_assistant_api_journeys_create` | `GOVERNANCETOOL` | api_journeys_create |
| `ciso_assistant_api_journeys_dashboard_retrieve` | `GOVERNANCETOOL` | api_journeys_dashboard_retrieve |
| `ciso_assistant_api_journeys_destroy` | `GOVERNANCETOOL` | api_journeys_destroy |
| `ciso_assistant_api_journeys_list` | `GOVERNANCETOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_journeys_object_retrieve` | `GOVERNANCETOOL` | api_journeys_object_retrieve |
| `ciso_assistant_api_journeys_partial_update` | `GOVERNANCETOOL` | api_journeys_partial_update |
| `ciso_assistant_api_journeys_rename_create` | `GOVERNANCETOOL` | api_journeys_rename_create |
| `ciso_assistant_api_journeys_retrieve` | `GOVERNANCETOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_journeys_update` | `GOVERNANCETOOL` | api_journeys_update |
| `ciso_assistant_api_journeys_upgrade_create` | `GOVERNANCETOOL` | api_journeys_upgrade_create |
| `ciso_assistant_api_library_filtering_labels_batch_action_create` | `FRAMEWORKS_LIBRARIESTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_library_filtering_labels_cascade_info_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | Cascade preview: |
| `ciso_assistant_api_library_filtering_labels_create` | `FRAMEWORKS_LIBRARIESTOOL` | API endpoint that allows library labels to be viewed or edited. |
| `ciso_assistant_api_library_filtering_labels_destroy` | `FRAMEWORKS_LIBRARIESTOOL` | API endpoint that allows library labels to be viewed or edited. |
| `ciso_assistant_api_library_filtering_labels_list` | `FRAMEWORKS_LIBRARIESTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_library_filtering_labels_object_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | API endpoint that allows library labels to be viewed or edited. |
| `ciso_assistant_api_library_filtering_labels_partial_update` | `FRAMEWORKS_LIBRARIESTOOL` | API endpoint that allows library labels to be viewed or edited. |
| `ciso_assistant_api_library_filtering_labels_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_library_filtering_labels_update` | `FRAMEWORKS_LIBRARIESTOOL` | API endpoint that allows library labels to be viewed or edited. |
| `ciso_assistant_api_loaded_libraries_available_updates_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | api_loaded_libraries_available_updates_retrieve |
| `ciso_assistant_api_loaded_libraries_batch_action_create` | `FRAMEWORKS_LIBRARIESTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_loaded_libraries_cascade_info_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | Cascade preview: |
| `ciso_assistant_api_loaded_libraries_content_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | api_loaded_libraries_content_retrieve |
| `ciso_assistant_api_loaded_libraries_create` | `FRAMEWORKS_LIBRARIESTOOL` | api_loaded_libraries_create |
| `ciso_assistant_api_loaded_libraries_destroy` | `FRAMEWORKS_LIBRARIESTOOL` | api_loaded_libraries_destroy |
| `ciso_assistant_api_loaded_libraries_list` | `FRAMEWORKS_LIBRARIESTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_loaded_libraries_object_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | api_loaded_libraries_object_retrieve |
| `ciso_assistant_api_loaded_libraries_partial_update` | `FRAMEWORKS_LIBRARIESTOOL` | api_loaded_libraries_partial_update |
| `ciso_assistant_api_loaded_libraries_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_loaded_libraries_tree_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | api_loaded_libraries_tree_retrieve |
| `ciso_assistant_api_loaded_libraries_update` | `FRAMEWORKS_LIBRARIESTOOL` | api_loaded_libraries_update |
| `ciso_assistant_api_loaded_libraries_update_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | api_loaded_libraries_update_retrieve |
| `ciso_assistant_api_managed_documents_batch_action_create` | `EVIDENCETOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_managed_documents_cascade_info_retrieve` | `EVIDENCETOOL` | Cascade preview: |
| `ciso_assistant_api_managed_documents_create` | `EVIDENCETOOL` | API endpoint that allows managed documents to be viewed or edited. |
| `ciso_assistant_api_managed_documents_create_new_draft_create` | `EVIDENCETOOL` | Create a new draft revision cloned from the current revision. |
| `ciso_assistant_api_managed_documents_destroy` | `EVIDENCETOOL` | API endpoint that allows managed documents to be viewed or edited. |
| `ciso_assistant_api_managed_documents_list` | `EVIDENCETOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_managed_documents_object_retrieve` | `EVIDENCETOOL` | API endpoint that allows managed documents to be viewed or edited. |
| `ciso_assistant_api_managed_documents_partial_update` | `EVIDENCETOOL` | API endpoint that allows managed documents to be viewed or edited. |
| `ciso_assistant_api_managed_documents_retrieve` | `EVIDENCETOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_managed_documents_templates_retrieve` | `EVIDENCETOOL` | List available document templates. Accepts optional ?lang= query parameter. |
| `ciso_assistant_api_managed_documents_update` | `EVIDENCETOOL` | API endpoint that allows managed documents to be viewed or edited. |
| `ciso_assistant_api_managed_documents_upload_image_create` | `EVIDENCETOOL` | Upload an image file and attach it to this document. |
| `ciso_assistant_api_mapping_libraries_list` | `COMPLIANCETOOL` | api_mapping_libraries_list |
| `ciso_assistant_api_metrology_builtin_metric_samples_batch_action_create` | `ANALYTICS_METROLOGYTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_metrology_builtin_metric_samples_cascade_info_retrieve` | `ANALYTICS_METROLOGYTOOL` | Cascade preview: |
| `ciso_assistant_api_metrology_builtin_metric_samples_create` | `ANALYTICS_METROLOGYTOOL` | api_metrology_builtin_metric_samples_create |
| `ciso_assistant_api_metrology_builtin_metric_samples_destroy` | `ANALYTICS_METROLOGYTOOL` | api_metrology_builtin_metric_samples_destroy |
| `ciso_assistant_api_metrology_builtin_metric_samples_for_object_retrieve` | `ANALYTICS_METROLOGYTOOL` | api_metrology_builtin_metric_samples_for_object_retrieve |
| `ciso_assistant_api_metrology_builtin_metric_samples_list` | `ANALYTICS_METROLOGYTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_metrology_builtin_metric_samples_object_retrieve` | `ANALYTICS_METROLOGYTOOL` | api_metrology_builtin_metric_samples_object_retrieve |
| `ciso_assistant_api_metrology_builtin_metric_samples_partial_update` | `ANALYTICS_METROLOGYTOOL` | api_metrology_builtin_metric_samples_partial_update |
| `ciso_assistant_api_metrology_builtin_metric_samples_refresh_create` | `ANALYTICS_METROLOGYTOOL` | api_metrology_builtin_metric_samples_refresh_create |
| `ciso_assistant_api_metrology_builtin_metric_samples_retrieve` | `ANALYTICS_METROLOGYTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_metrology_builtin_metric_samples_supported_models_retrieve` | `ANALYTICS_METROLOGYTOOL` | api_metrology_builtin_metric_samples_supported_models_retrieve |
| `ciso_assistant_api_metrology_builtin_metric_samples_update` | `ANALYTICS_METROLOGYTOOL` | api_metrology_builtin_metric_samples_update |
| `ciso_assistant_api_metrology_custom_metric_samples_batch_action_create` | `ANALYTICS_METROLOGYTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_metrology_custom_metric_samples_cascade_info_retrieve` | `ANALYTICS_METROLOGYTOOL` | Cascade preview: |
| `ciso_assistant_api_metrology_custom_metric_samples_create` | `ANALYTICS_METROLOGYTOOL` | api_metrology_custom_metric_samples_create |
| `ciso_assistant_api_metrology_custom_metric_samples_destroy` | `ANALYTICS_METROLOGYTOOL` | api_metrology_custom_metric_samples_destroy |
| `ciso_assistant_api_metrology_custom_metric_samples_list` | `ANALYTICS_METROLOGYTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_metrology_custom_metric_samples_object_retrieve` | `ANALYTICS_METROLOGYTOOL` | api_metrology_custom_metric_samples_object_retrieve |
| `ciso_assistant_api_metrology_custom_metric_samples_partial_update` | `ANALYTICS_METROLOGYTOOL` | api_metrology_custom_metric_samples_partial_update |
| `ciso_assistant_api_metrology_custom_metric_samples_retrieve` | `ANALYTICS_METROLOGYTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_metrology_custom_metric_samples_update` | `ANALYTICS_METROLOGYTOOL` | api_metrology_custom_metric_samples_update |
| `ciso_assistant_api_metrology_dashboard_widgets_aggregation_retrieve` | `ANALYTICS_METROLOGYTOOL` | api_metrology_dashboard_widgets_aggregation_retrieve |
| `ciso_assistant_api_metrology_dashboard_widgets_batch_action_create` | `ANALYTICS_METROLOGYTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_metrology_dashboard_widgets_cascade_info_retrieve` | `ANALYTICS_METROLOGYTOOL` | Cascade preview: |
| `ciso_assistant_api_metrology_dashboard_widgets_chart_type_retrieve` | `ANALYTICS_METROLOGYTOOL` | api_metrology_dashboard_widgets_chart_type_retrieve |
| `ciso_assistant_api_metrology_dashboard_widgets_create` | `ANALYTICS_METROLOGYTOOL` | api_metrology_dashboard_widgets_create |
| `ciso_assistant_api_metrology_dashboard_widgets_destroy` | `ANALYTICS_METROLOGYTOOL` | api_metrology_dashboard_widgets_destroy |
| `ciso_assistant_api_metrology_dashboard_widgets_list` | `ANALYTICS_METROLOGYTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_metrology_dashboard_widgets_object_retrieve` | `ANALYTICS_METROLOGYTOOL` | api_metrology_dashboard_widgets_object_retrieve |
| `ciso_assistant_api_metrology_dashboard_widgets_partial_update` | `ANALYTICS_METROLOGYTOOL` | api_metrology_dashboard_widgets_partial_update |
| `ciso_assistant_api_metrology_dashboard_widgets_retrieve` | `ANALYTICS_METROLOGYTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_metrology_dashboard_widgets_time_range_retrieve` | `ANALYTICS_METROLOGYTOOL` | api_metrology_dashboard_widgets_time_range_retrieve |
| `ciso_assistant_api_metrology_dashboard_widgets_update` | `ANALYTICS_METROLOGYTOOL` | api_metrology_dashboard_widgets_update |
| `ciso_assistant_api_metrology_dashboards_batch_action_create` | `ANALYTICS_METROLOGYTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_metrology_dashboards_cascade_info_retrieve` | `ANALYTICS_METROLOGYTOOL` | Cascade preview: |
| `ciso_assistant_api_metrology_dashboards_create` | `ANALYTICS_METROLOGYTOOL` | api_metrology_dashboards_create |
| `ciso_assistant_api_metrology_dashboards_destroy` | `ANALYTICS_METROLOGYTOOL` | api_metrology_dashboards_destroy |
| `ciso_assistant_api_metrology_dashboards_list` | `ANALYTICS_METROLOGYTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_metrology_dashboards_object_retrieve` | `ANALYTICS_METROLOGYTOOL` | api_metrology_dashboards_object_retrieve |
| `ciso_assistant_api_metrology_dashboards_partial_update` | `ANALYTICS_METROLOGYTOOL` | api_metrology_dashboards_partial_update |
| `ciso_assistant_api_metrology_dashboards_retrieve` | `ANALYTICS_METROLOGYTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_metrology_dashboards_update` | `ANALYTICS_METROLOGYTOOL` | api_metrology_dashboards_update |
| `ciso_assistant_api_metrology_metric_definitions_batch_action_create` | `ANALYTICS_METROLOGYTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_metrology_metric_definitions_cascade_info_retrieve` | `ANALYTICS_METROLOGYTOOL` | Cascade preview: |
| `ciso_assistant_api_metrology_metric_definitions_category_retrieve` | `ANALYTICS_METROLOGYTOOL` | api_metrology_metric_definitions_category_retrieve |
| `ciso_assistant_api_metrology_metric_definitions_create` | `ANALYTICS_METROLOGYTOOL` | api_metrology_metric_definitions_create |
| `ciso_assistant_api_metrology_metric_definitions_destroy` | `ANALYTICS_METROLOGYTOOL` | api_metrology_metric_definitions_destroy |
| `ciso_assistant_api_metrology_metric_definitions_list` | `ANALYTICS_METROLOGYTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_metrology_metric_definitions_object_retrieve` | `ANALYTICS_METROLOGYTOOL` | api_metrology_metric_definitions_object_retrieve |
| `ciso_assistant_api_metrology_metric_definitions_partial_update` | `ANALYTICS_METROLOGYTOOL` | api_metrology_metric_definitions_partial_update |
| `ciso_assistant_api_metrology_metric_definitions_provider_retrieve` | `ANALYTICS_METROLOGYTOOL` | api_metrology_metric_definitions_provider_retrieve |
| `ciso_assistant_api_metrology_metric_definitions_retrieve` | `ANALYTICS_METROLOGYTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_metrology_metric_definitions_update` | `ANALYTICS_METROLOGYTOOL` | api_metrology_metric_definitions_update |
| `ciso_assistant_api_metrology_metric_instances_batch_action_create` | `ANALYTICS_METROLOGYTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_metrology_metric_instances_cascade_info_retrieve` | `ANALYTICS_METROLOGYTOOL` | Cascade preview: |
| `ciso_assistant_api_metrology_metric_instances_collection_frequency_retrieve` | `ANALYTICS_METROLOGYTOOL` | api_metrology_metric_instances_collection_frequency_retrieve |
| `ciso_assistant_api_metrology_metric_instances_create` | `ANALYTICS_METROLOGYTOOL` | api_metrology_metric_instances_create |
| `ciso_assistant_api_metrology_metric_instances_destroy` | `ANALYTICS_METROLOGYTOOL` | api_metrology_metric_instances_destroy |
| `ciso_assistant_api_metrology_metric_instances_list` | `ANALYTICS_METROLOGYTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_metrology_metric_instances_object_retrieve` | `ANALYTICS_METROLOGYTOOL` | api_metrology_metric_instances_object_retrieve |
| `ciso_assistant_api_metrology_metric_instances_partial_update` | `ANALYTICS_METROLOGYTOOL` | api_metrology_metric_instances_partial_update |
| `ciso_assistant_api_metrology_metric_instances_retrieve` | `ANALYTICS_METROLOGYTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_metrology_metric_instances_status_retrieve` | `ANALYTICS_METROLOGYTOOL` | api_metrology_metric_instances_status_retrieve |
| `ciso_assistant_api_metrology_metric_instances_update` | `ANALYTICS_METROLOGYTOOL` | api_metrology_metric_instances_update |
| `ciso_assistant_api_organisation_issues_batch_action_create` | `GOVERNANCETOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_organisation_issues_cascade_info_retrieve` | `GOVERNANCETOOL` | Cascade preview: |
| `ciso_assistant_api_organisation_issues_category_retrieve` | `GOVERNANCETOOL` | api_organisation_issues_category_retrieve |
| `ciso_assistant_api_organisation_issues_create` | `GOVERNANCETOOL` | api_organisation_issues_create |
| `ciso_assistant_api_organisation_issues_destroy` | `GOVERNANCETOOL` | api_organisation_issues_destroy |
| `ciso_assistant_api_organisation_issues_list` | `GOVERNANCETOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_organisation_issues_object_retrieve` | `GOVERNANCETOOL` | api_organisation_issues_object_retrieve |
| `ciso_assistant_api_organisation_issues_origin_retrieve` | `GOVERNANCETOOL` | api_organisation_issues_origin_retrieve |
| `ciso_assistant_api_organisation_issues_partial_update` | `GOVERNANCETOOL` | api_organisation_issues_partial_update |
| `ciso_assistant_api_organisation_issues_retrieve` | `GOVERNANCETOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_organisation_issues_status_retrieve` | `GOVERNANCETOOL` | api_organisation_issues_status_retrieve |
| `ciso_assistant_api_organisation_issues_update` | `GOVERNANCETOOL` | api_organisation_issues_update |
| `ciso_assistant_api_organisation_objectives_batch_action_create` | `GOVERNANCETOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_organisation_objectives_cascade_info_retrieve` | `GOVERNANCETOOL` | Cascade preview: |
| `ciso_assistant_api_organisation_objectives_create` | `GOVERNANCETOOL` | api_organisation_objectives_create |
| `ciso_assistant_api_organisation_objectives_destroy` | `GOVERNANCETOOL` | api_organisation_objectives_destroy |
| `ciso_assistant_api_organisation_objectives_duplicate_create` | `GOVERNANCETOOL` | api_organisation_objectives_duplicate_create |
| `ciso_assistant_api_organisation_objectives_health_retrieve` | `GOVERNANCETOOL` | api_organisation_objectives_health_retrieve |
| `ciso_assistant_api_organisation_objectives_is_active_retrieve` | `GOVERNANCETOOL` | api_organisation_objectives_is_active_retrieve |
| `ciso_assistant_api_organisation_objectives_list` | `GOVERNANCETOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_organisation_objectives_object_retrieve` | `GOVERNANCETOOL` | api_organisation_objectives_object_retrieve |
| `ciso_assistant_api_organisation_objectives_partial_update` | `GOVERNANCETOOL` | api_organisation_objectives_partial_update |
| `ciso_assistant_api_organisation_objectives_retrieve` | `GOVERNANCETOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_organisation_objectives_status_retrieve` | `GOVERNANCETOOL` | api_organisation_objectives_status_retrieve |
| `ciso_assistant_api_organisation_objectives_update` | `GOVERNANCETOOL` | api_organisation_objectives_update |
| `ciso_assistant_api_perimeters_batch_action_create` | `GOVERNANCETOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_perimeters_cascade_info_retrieve` | `GOVERNANCETOOL` | Cascade preview: |
| `ciso_assistant_api_perimeters_create` | `GOVERNANCETOOL` | API endpoint that allows perimeters to be viewed or edited. |
| `ciso_assistant_api_perimeters_destroy` | `GOVERNANCETOOL` | API endpoint that allows perimeters to be viewed or edited. |
| `ciso_assistant_api_perimeters_ids_retrieve` | `GOVERNANCETOOL` | API endpoint that allows perimeters to be viewed or edited. |
| `ciso_assistant_api_perimeters_lc_status_retrieve` | `GOVERNANCETOOL` | API endpoint that allows perimeters to be viewed or edited. |
| `ciso_assistant_api_perimeters_list` | `GOVERNANCETOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_perimeters_names_retrieve` | `GOVERNANCETOOL` | API endpoint that allows perimeters to be viewed or edited. |
| `ciso_assistant_api_perimeters_object_retrieve` | `GOVERNANCETOOL` | API endpoint that allows perimeters to be viewed or edited. |
| `ciso_assistant_api_perimeters_partial_update` | `GOVERNANCETOOL` | API endpoint that allows perimeters to be viewed or edited. |
| `ciso_assistant_api_perimeters_quality_check_retrieve` | `GOVERNANCETOOL` | Returns the quality check of the perimeters |
| `ciso_assistant_api_perimeters_quality_check_retrieve_2` | `GOVERNANCETOOL` | Returns the quality check of the perimeter |
| `ciso_assistant_api_perimeters_retrieve` | `GOVERNANCETOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_perimeters_update` | `GOVERNANCETOOL` | API endpoint that allows perimeters to be viewed or edited. |
| `ciso_assistant_api_pmbok_accreditations_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_pmbok_accreditations_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_pmbok_accreditations_category_retrieve` | `GRANULARTOOL` | api_pmbok_accreditations_category_retrieve |
| `ciso_assistant_api_pmbok_accreditations_create` | `GRANULARTOOL` | api_pmbok_accreditations_create |
| `ciso_assistant_api_pmbok_accreditations_destroy` | `GRANULARTOOL` | api_pmbok_accreditations_destroy |
| `ciso_assistant_api_pmbok_accreditations_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_pmbok_accreditations_object_retrieve` | `GRANULARTOOL` | api_pmbok_accreditations_object_retrieve |
| `ciso_assistant_api_pmbok_accreditations_partial_update` | `GRANULARTOOL` | api_pmbok_accreditations_partial_update |
| `ciso_assistant_api_pmbok_accreditations_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_pmbok_accreditations_status_retrieve` | `GRANULARTOOL` | api_pmbok_accreditations_status_retrieve |
| `ciso_assistant_api_pmbok_accreditations_update` | `GRANULARTOOL` | api_pmbok_accreditations_update |
| `ciso_assistant_api_pmbok_generic_collections_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_pmbok_generic_collections_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_pmbok_generic_collections_create` | `GRANULARTOOL` | api_pmbok_generic_collections_create |
| `ciso_assistant_api_pmbok_generic_collections_destroy` | `GRANULARTOOL` | api_pmbok_generic_collections_destroy |
| `ciso_assistant_api_pmbok_generic_collections_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_pmbok_generic_collections_object_retrieve` | `GRANULARTOOL` | api_pmbok_generic_collections_object_retrieve |
| `ciso_assistant_api_pmbok_generic_collections_partial_update` | `GRANULARTOOL` | api_pmbok_generic_collections_partial_update |
| `ciso_assistant_api_pmbok_generic_collections_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_pmbok_generic_collections_status_retrieve` | `GRANULARTOOL` | api_pmbok_generic_collections_status_retrieve |
| `ciso_assistant_api_pmbok_generic_collections_update` | `GRANULARTOOL` | api_pmbok_generic_collections_update |
| `ciso_assistant_api_pmbok_projects_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_pmbok_projects_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_pmbok_projects_create` | `GRANULARTOOL` | api_pmbok_projects_create |
| `ciso_assistant_api_pmbok_projects_currencies_retrieve` | `GRANULARTOOL` | api_pmbok_projects_currencies_retrieve |
| `ciso_assistant_api_pmbok_projects_destroy` | `GRANULARTOOL` | api_pmbok_projects_destroy |
| `ciso_assistant_api_pmbok_projects_kind_retrieve` | `GRANULARTOOL` | api_pmbok_projects_kind_retrieve |
| `ciso_assistant_api_pmbok_projects_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_pmbok_projects_object_retrieve` | `GRANULARTOOL` | api_pmbok_projects_object_retrieve |
| `ciso_assistant_api_pmbok_projects_partial_update` | `GRANULARTOOL` | api_pmbok_projects_partial_update |
| `ciso_assistant_api_pmbok_projects_priority_retrieve` | `GRANULARTOOL` | api_pmbok_projects_priority_retrieve |
| `ciso_assistant_api_pmbok_projects_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_pmbok_projects_update` | `GRANULARTOOL` | api_pmbok_projects_update |
| `ciso_assistant_api_pmbok_responsibility_assignments_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_pmbok_responsibility_assignments_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_pmbok_responsibility_assignments_object_retrieve` | `GRANULARTOOL` | api_pmbok_responsibility_assignments_object_retrieve |
| `ciso_assistant_api_pmbok_responsibility_assignments_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_pmbok_responsibility_matrices_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_pmbok_responsibility_matrices_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_pmbok_responsibility_matrices_create` | `GRANULARTOOL` | api_pmbok_responsibility_matrices_create |
| `ciso_assistant_api_pmbok_responsibility_matrices_cycle_cell_create` | `GRANULARTOOL` | api_pmbok_responsibility_matrices_cycle_cell_create |
| `ciso_assistant_api_pmbok_responsibility_matrices_destroy` | `GRANULARTOOL` | api_pmbok_responsibility_matrices_destroy |
| `ciso_assistant_api_pmbok_responsibility_matrices_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_pmbok_responsibility_matrices_object_retrieve` | `GRANULARTOOL` | api_pmbok_responsibility_matrices_object_retrieve |
| `ciso_assistant_api_pmbok_responsibility_matrices_partial_update` | `GRANULARTOOL` | api_pmbok_responsibility_matrices_partial_update |
| `ciso_assistant_api_pmbok_responsibility_matrices_preset_retrieve` | `GRANULARTOOL` | api_pmbok_responsibility_matrices_preset_retrieve |
| `ciso_assistant_api_pmbok_responsibility_matrices_reorder_activities_create` | `GRANULARTOOL` | api_pmbok_responsibility_matrices_reorder_activities_create |
| `ciso_assistant_api_pmbok_responsibility_matrices_reorder_actors_create` | `GRANULARTOOL` | api_pmbok_responsibility_matrices_reorder_actors_create |
| `ciso_assistant_api_pmbok_responsibility_matrices_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_pmbok_responsibility_matrices_update` | `GRANULARTOOL` | api_pmbok_responsibility_matrices_update |
| `ciso_assistant_api_pmbok_responsibility_matrix_activities_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_pmbok_responsibility_matrix_activities_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_pmbok_responsibility_matrix_activities_create` | `GRANULARTOOL` | api_pmbok_responsibility_matrix_activities_create |
| `ciso_assistant_api_pmbok_responsibility_matrix_activities_destroy` | `GRANULARTOOL` | api_pmbok_responsibility_matrix_activities_destroy |
| `ciso_assistant_api_pmbok_responsibility_matrix_activities_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_pmbok_responsibility_matrix_activities_object_retrieve` | `GRANULARTOOL` | api_pmbok_responsibility_matrix_activities_object_retrieve |
| `ciso_assistant_api_pmbok_responsibility_matrix_activities_partial_update` | `GRANULARTOOL` | api_pmbok_responsibility_matrix_activities_partial_update |
| `ciso_assistant_api_pmbok_responsibility_matrix_activities_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_pmbok_responsibility_matrix_activities_update` | `GRANULARTOOL` | api_pmbok_responsibility_matrix_activities_update |
| `ciso_assistant_api_pmbok_responsibility_matrix_actors_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_pmbok_responsibility_matrix_actors_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_pmbok_responsibility_matrix_actors_create` | `GRANULARTOOL` | api_pmbok_responsibility_matrix_actors_create |
| `ciso_assistant_api_pmbok_responsibility_matrix_actors_destroy` | `GRANULARTOOL` | api_pmbok_responsibility_matrix_actors_destroy |
| `ciso_assistant_api_pmbok_responsibility_matrix_actors_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_pmbok_responsibility_matrix_actors_object_retrieve` | `GRANULARTOOL` | api_pmbok_responsibility_matrix_actors_object_retrieve |
| `ciso_assistant_api_pmbok_responsibility_matrix_actors_partial_update` | `GRANULARTOOL` | api_pmbok_responsibility_matrix_actors_partial_update |
| `ciso_assistant_api_pmbok_responsibility_matrix_actors_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_pmbok_responsibility_matrix_actors_update` | `GRANULARTOOL` | api_pmbok_responsibility_matrix_actors_update |
| `ciso_assistant_api_pmbok_responsibility_roles_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_pmbok_responsibility_roles_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_pmbok_responsibility_roles_object_retrieve` | `GRANULARTOOL` | api_pmbok_responsibility_roles_object_retrieve |
| `ciso_assistant_api_pmbok_responsibility_roles_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_pmbok_responsibility_roles_taxonomy_retrieve` | `GRANULARTOOL` | api_pmbok_responsibility_roles_taxonomy_retrieve |
| `ciso_assistant_api_policies_analytics_retrieve` | `COMPLIANCETOOL` | Aggregated analytics over the filtered applied-controls queryset. |
| `ciso_assistant_api_policies_autocomplete_retrieve` | `COMPLIANCETOOL` | Minimal endpoint for autocomplete selects. |
| `ciso_assistant_api_policies_batch_action_create` | `COMPLIANCETOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_policies_cascade_info_retrieve` | `COMPLIANCETOOL` | Cascade preview: |
| `ciso_assistant_api_policies_category_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_policies_control_impact_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_policies_create` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_policies_csf_function_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_policies_destroy` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_policies_duplicate_create` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_policies_effort_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_policies_export_csv_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_policies_export_xlsx_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_policies_get_controls_info_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_policies_get_gantt_data_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_policies_get_timeline_info_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_policies_ids_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_policies_impact_effort_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_policies_impact_graph_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_policies_linked_models_retrieve` | `COMPLIANCETOOL` | Return available model types that can be linked to applied controls |
| `ciso_assistant_api_policies_list` | `COMPLIANCETOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_policies_merge_create` | `COMPLIANCETOOL` | Merge N source applied controls into 1 target. See |
| `ciso_assistant_api_policies_mss_xlsx_retrieve` | `COMPLIANCETOOL` | Export filtered applied controls in ANSSI MonServiceSécurisé format |
| `ciso_assistant_api_policies_object_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_policies_owner_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_policies_partial_update` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_policies_per_status_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_policies_priority_chart_data_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_policies_priority_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_policies_retrieve` | `COMPLIANCETOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_policies_status_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_policies_sunburst_data_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_policies_sync_to_reference_control_create` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_policies_to_review_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_policies_todo_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_policies_updatables_retrieve` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_policies_update` | `COMPLIANCETOOL` | API endpoint that allows applied controls to be viewed or edited. |
| `ciso_assistant_api_presets_apply_create` | `FRAMEWORKS_LIBRARIESTOOL` | api_presets_apply_create |
| `ciso_assistant_api_presets_batch_action_create` | `FRAMEWORKS_LIBRARIESTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_presets_cascade_info_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | Cascade preview: |
| `ciso_assistant_api_presets_create` | `FRAMEWORKS_LIBRARIESTOOL` | api_presets_create |
| `ciso_assistant_api_presets_create_blank_create` | `FRAMEWORKS_LIBRARIESTOOL` | api_presets_create_blank_create |
| `ciso_assistant_api_presets_destroy` | `FRAMEWORKS_LIBRARIESTOOL` | api_presets_destroy |
| `ciso_assistant_api_presets_discard_draft_create` | `FRAMEWORKS_LIBRARIESTOOL` | api_presets_discard_draft_create |
| `ciso_assistant_api_presets_duplicate_create` | `FRAMEWORKS_LIBRARIESTOOL` | api_presets_duplicate_create |
| `ciso_assistant_api_presets_list` | `FRAMEWORKS_LIBRARIESTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_presets_object_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | api_presets_object_retrieve |
| `ciso_assistant_api_presets_partial_update` | `FRAMEWORKS_LIBRARIESTOOL` | api_presets_partial_update |
| `ciso_assistant_api_presets_publish_draft_create` | `FRAMEWORKS_LIBRARIESTOOL` | api_presets_publish_draft_create |
| `ciso_assistant_api_presets_publish_draft_preview_create` | `FRAMEWORKS_LIBRARIESTOOL` | api_presets_publish_draft_preview_create |
| `ciso_assistant_api_presets_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_presets_save_draft_partial_update` | `FRAMEWORKS_LIBRARIESTOOL` | api_presets_save_draft_partial_update |
| `ciso_assistant_api_presets_start_editing_create` | `FRAMEWORKS_LIBRARIESTOOL` | api_presets_start_editing_create |
| `ciso_assistant_api_presets_update` | `FRAMEWORKS_LIBRARIESTOOL` | api_presets_update |
| `ciso_assistant_api_privacy_data_breaches_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_privacy_data_breaches_breach_type_retrieve` | `GRANULARTOOL` | API endpoint that allows data breaches to be viewed or edited. |
| `ciso_assistant_api_privacy_data_breaches_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_privacy_data_breaches_create` | `GRANULARTOOL` | API endpoint that allows data breaches to be viewed or edited. |
| `ciso_assistant_api_privacy_data_breaches_destroy` | `GRANULARTOOL` | API endpoint that allows data breaches to be viewed or edited. |
| `ciso_assistant_api_privacy_data_breaches_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_privacy_data_breaches_object_retrieve` | `GRANULARTOOL` | API endpoint that allows data breaches to be viewed or edited. |
| `ciso_assistant_api_privacy_data_breaches_partial_update` | `GRANULARTOOL` | API endpoint that allows data breaches to be viewed or edited. |
| `ciso_assistant_api_privacy_data_breaches_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_privacy_data_breaches_risk_level_retrieve` | `GRANULARTOOL` | API endpoint that allows data breaches to be viewed or edited. |
| `ciso_assistant_api_privacy_data_breaches_status_retrieve` | `GRANULARTOOL` | API endpoint that allows data breaches to be viewed or edited. |
| `ciso_assistant_api_privacy_data_breaches_update` | `GRANULARTOOL` | API endpoint that allows data breaches to be viewed or edited. |
| `ciso_assistant_api_privacy_data_contractors_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_privacy_data_contractors_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_privacy_data_contractors_country_retrieve` | `GRANULARTOOL` | API endpoint that allows data contractors to be viewed or edited. |
| `ciso_assistant_api_privacy_data_contractors_create` | `GRANULARTOOL` | API endpoint that allows data contractors to be viewed or edited. |
| `ciso_assistant_api_privacy_data_contractors_destroy` | `GRANULARTOOL` | API endpoint that allows data contractors to be viewed or edited. |
| `ciso_assistant_api_privacy_data_contractors_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_privacy_data_contractors_object_retrieve` | `GRANULARTOOL` | API endpoint that allows data contractors to be viewed or edited. |
| `ciso_assistant_api_privacy_data_contractors_partial_update` | `GRANULARTOOL` | API endpoint that allows data contractors to be viewed or edited. |
| `ciso_assistant_api_privacy_data_contractors_relationship_type_retrieve` | `GRANULARTOOL` | API endpoint that allows data contractors to be viewed or edited. |
| `ciso_assistant_api_privacy_data_contractors_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_privacy_data_contractors_update` | `GRANULARTOOL` | API endpoint that allows data contractors to be viewed or edited. |
| `ciso_assistant_api_privacy_data_recipients_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_privacy_data_recipients_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_privacy_data_recipients_category_retrieve` | `GRANULARTOOL` | API endpoint that allows data recipients to be viewed or edited. |
| `ciso_assistant_api_privacy_data_recipients_create` | `GRANULARTOOL` | API endpoint that allows data recipients to be viewed or edited. |
| `ciso_assistant_api_privacy_data_recipients_destroy` | `GRANULARTOOL` | API endpoint that allows data recipients to be viewed or edited. |
| `ciso_assistant_api_privacy_data_recipients_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_privacy_data_recipients_object_retrieve` | `GRANULARTOOL` | API endpoint that allows data recipients to be viewed or edited. |
| `ciso_assistant_api_privacy_data_recipients_partial_update` | `GRANULARTOOL` | API endpoint that allows data recipients to be viewed or edited. |
| `ciso_assistant_api_privacy_data_recipients_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_privacy_data_recipients_update` | `GRANULARTOOL` | API endpoint that allows data recipients to be viewed or edited. |
| `ciso_assistant_api_privacy_data_subjects_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_privacy_data_subjects_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_privacy_data_subjects_category_retrieve` | `GRANULARTOOL` | API endpoint that allows data subjects to be viewed or edited. |
| `ciso_assistant_api_privacy_data_subjects_create` | `GRANULARTOOL` | API endpoint that allows data subjects to be viewed or edited. |
| `ciso_assistant_api_privacy_data_subjects_destroy` | `GRANULARTOOL` | API endpoint that allows data subjects to be viewed or edited. |
| `ciso_assistant_api_privacy_data_subjects_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_privacy_data_subjects_object_retrieve` | `GRANULARTOOL` | API endpoint that allows data subjects to be viewed or edited. |
| `ciso_assistant_api_privacy_data_subjects_partial_update` | `GRANULARTOOL` | API endpoint that allows data subjects to be viewed or edited. |
| `ciso_assistant_api_privacy_data_subjects_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_privacy_data_subjects_update` | `GRANULARTOOL` | API endpoint that allows data subjects to be viewed or edited. |
| `ciso_assistant_api_privacy_data_transfers_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_privacy_data_transfers_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_privacy_data_transfers_country_retrieve` | `GRANULARTOOL` | API endpoint that allows data transfers to be viewed or edited. |
| `ciso_assistant_api_privacy_data_transfers_create` | `GRANULARTOOL` | API endpoint that allows data transfers to be viewed or edited. |
| `ciso_assistant_api_privacy_data_transfers_destroy` | `GRANULARTOOL` | API endpoint that allows data transfers to be viewed or edited. |
| `ciso_assistant_api_privacy_data_transfers_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_privacy_data_transfers_object_retrieve` | `GRANULARTOOL` | API endpoint that allows data transfers to be viewed or edited. |
| `ciso_assistant_api_privacy_data_transfers_partial_update` | `GRANULARTOOL` | API endpoint that allows data transfers to be viewed or edited. |
| `ciso_assistant_api_privacy_data_transfers_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_privacy_data_transfers_transfer_mechanism_retrieve` | `GRANULARTOOL` | API endpoint that allows data transfers to be viewed or edited. |
| `ciso_assistant_api_privacy_data_transfers_update` | `GRANULARTOOL` | API endpoint that allows data transfers to be viewed or edited. |
| `ciso_assistant_api_privacy_personal_data_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_privacy_personal_data_batch_create_create` | `GRANULARTOOL` | Batch create multiple personal data entries for a processing. |
| `ciso_assistant_api_privacy_personal_data_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_privacy_personal_data_category_retrieve` | `GRANULARTOOL` | API endpoint that allows personal data to be viewed or edited. |
| `ciso_assistant_api_privacy_personal_data_create` | `GRANULARTOOL` | API endpoint that allows personal data to be viewed or edited. |
| `ciso_assistant_api_privacy_personal_data_deletion_policy_retrieve` | `GRANULARTOOL` | API endpoint that allows personal data to be viewed or edited. |
| `ciso_assistant_api_privacy_personal_data_destroy` | `GRANULARTOOL` | API endpoint that allows personal data to be viewed or edited. |
| `ciso_assistant_api_privacy_personal_data_is_sensitive_retrieve` | `GRANULARTOOL` | API endpoint that allows personal data to be viewed or edited. |
| `ciso_assistant_api_privacy_personal_data_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_privacy_personal_data_object_retrieve` | `GRANULARTOOL` | API endpoint that allows personal data to be viewed or edited. |
| `ciso_assistant_api_privacy_personal_data_partial_update` | `GRANULARTOOL` | API endpoint that allows personal data to be viewed or edited. |
| `ciso_assistant_api_privacy_personal_data_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_privacy_personal_data_update` | `GRANULARTOOL` | API endpoint that allows personal data to be viewed or edited. |
| `ciso_assistant_api_privacy_processing_natures_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_privacy_processing_natures_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_privacy_processing_natures_create` | `GRANULARTOOL` | api_privacy_processing_natures_create |
| `ciso_assistant_api_privacy_processing_natures_destroy` | `GRANULARTOOL` | api_privacy_processing_natures_destroy |
| `ciso_assistant_api_privacy_processing_natures_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_privacy_processing_natures_object_retrieve` | `GRANULARTOOL` | api_privacy_processing_natures_object_retrieve |
| `ciso_assistant_api_privacy_processing_natures_partial_update` | `GRANULARTOOL` | api_privacy_processing_natures_partial_update |
| `ciso_assistant_api_privacy_processing_natures_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_privacy_processing_natures_update` | `GRANULARTOOL` | api_privacy_processing_natures_update |
| `ciso_assistant_api_privacy_processings_agg_metrics_retrieve` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_privacy_processings_assigned_to_retrieve` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_privacy_processings_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_privacy_processings_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_privacy_processings_create` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_privacy_processings_destroy` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_privacy_processings_export_csv_retrieve` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_privacy_processings_export_xlsx_retrieve` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_privacy_processings_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_privacy_processings_metrics_retrieve` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_privacy_processings_object_retrieve` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_privacy_processings_partial_update` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_privacy_processings_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_privacy_processings_status_retrieve` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_privacy_processings_update` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_privacy_purposes_article_9_condition_retrieve` | `GRANULARTOOL` | API endpoint that allows purposes to be viewed or edited. |
| `ciso_assistant_api_privacy_purposes_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_privacy_purposes_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_privacy_purposes_create` | `GRANULARTOOL` | API endpoint that allows purposes to be viewed or edited. |
| `ciso_assistant_api_privacy_purposes_destroy` | `GRANULARTOOL` | API endpoint that allows purposes to be viewed or edited. |
| `ciso_assistant_api_privacy_purposes_legal_basis_retrieve` | `GRANULARTOOL` | API endpoint that allows purposes to be viewed or edited. |
| `ciso_assistant_api_privacy_purposes_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_privacy_purposes_object_retrieve` | `GRANULARTOOL` | API endpoint that allows purposes to be viewed or edited. |
| `ciso_assistant_api_privacy_purposes_partial_update` | `GRANULARTOOL` | API endpoint that allows purposes to be viewed or edited. |
| `ciso_assistant_api_privacy_purposes_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_privacy_purposes_update` | `GRANULARTOOL` | API endpoint that allows purposes to be viewed or edited. |
| `ciso_assistant_api_privacy_right_requests_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_privacy_right_requests_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_privacy_right_requests_create` | `GRANULARTOOL` | API endpoint that allows right requests to be viewed or edited. |
| `ciso_assistant_api_privacy_right_requests_destroy` | `GRANULARTOOL` | API endpoint that allows right requests to be viewed or edited. |
| `ciso_assistant_api_privacy_right_requests_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_privacy_right_requests_object_retrieve` | `GRANULARTOOL` | API endpoint that allows right requests to be viewed or edited. |
| `ciso_assistant_api_privacy_right_requests_owner_retrieve` | `GRANULARTOOL` | API endpoint that allows right requests to be viewed or edited. |
| `ciso_assistant_api_privacy_right_requests_partial_update` | `GRANULARTOOL` | API endpoint that allows right requests to be viewed or edited. |
| `ciso_assistant_api_privacy_right_requests_request_type_retrieve` | `GRANULARTOOL` | API endpoint that allows right requests to be viewed or edited. |
| `ciso_assistant_api_privacy_right_requests_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_privacy_right_requests_status_retrieve` | `GRANULARTOOL` | API endpoint that allows right requests to be viewed or edited. |
| `ciso_assistant_api_privacy_right_requests_update` | `GRANULARTOOL` | API endpoint that allows right requests to be viewed or edited. |
| `ciso_assistant_api_question_choices_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_question_choices_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_question_choices_create` | `GRANULARTOOL` | API endpoint for QuestionChoice CRUD. |
| `ciso_assistant_api_question_choices_destroy` | `GRANULARTOOL` | API endpoint for QuestionChoice CRUD. |
| `ciso_assistant_api_question_choices_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_question_choices_object_retrieve` | `GRANULARTOOL` | API endpoint for QuestionChoice CRUD. |
| `ciso_assistant_api_question_choices_partial_update` | `GRANULARTOOL` | API endpoint for QuestionChoice CRUD. |
| `ciso_assistant_api_question_choices_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_question_choices_update` | `GRANULARTOOL` | API endpoint for QuestionChoice CRUD. |
| `ciso_assistant_api_questions_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_questions_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_questions_create` | `GRANULARTOOL` | API endpoint for Question CRUD. |
| `ciso_assistant_api_questions_destroy` | `GRANULARTOOL` | API endpoint for Question CRUD. |
| `ciso_assistant_api_questions_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_questions_object_retrieve` | `GRANULARTOOL` | API endpoint for Question CRUD. |
| `ciso_assistant_api_questions_partial_update` | `GRANULARTOOL` | API endpoint for Question CRUD. |
| `ciso_assistant_api_questions_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_questions_update` | `GRANULARTOOL` | API endpoint for Question CRUD. |
| `ciso_assistant_api_quick_start_create` | `GOVERNANCETOOL` | api_quick_start_create |
| `ciso_assistant_api_reference_controls_batch_action_create` | `COMPLIANCETOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_reference_controls_cascade_info_retrieve` | `COMPLIANCETOOL` | Cascade preview: |
| `ciso_assistant_api_reference_controls_category_retrieve` | `COMPLIANCETOOL` | API endpoint that allows reference controls to be viewed or edited. |
| `ciso_assistant_api_reference_controls_create` | `COMPLIANCETOOL` | API endpoint that allows reference controls to be viewed or edited. |
| `ciso_assistant_api_reference_controls_csf_function_retrieve` | `COMPLIANCETOOL` | API endpoint that allows reference controls to be viewed or edited. |
| `ciso_assistant_api_reference_controls_destroy` | `COMPLIANCETOOL` | API endpoint that allows reference controls to be viewed or edited. |
| `ciso_assistant_api_reference_controls_list` | `COMPLIANCETOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_reference_controls_object_retrieve` | `COMPLIANCETOOL` | API endpoint that allows reference controls to be viewed or edited. |
| `ciso_assistant_api_reference_controls_partial_update` | `COMPLIANCETOOL` | API endpoint that allows reference controls to be viewed or edited. |
| `ciso_assistant_api_reference_controls_provider_retrieve` | `COMPLIANCETOOL` | API endpoint that allows reference controls to be viewed or edited. |
| `ciso_assistant_api_reference_controls_retrieve` | `COMPLIANCETOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_reference_controls_sync_applied_controls_create` | `COMPLIANCETOOL` | API endpoint that allows reference controls to be viewed or edited. |
| `ciso_assistant_api_reference_controls_syncable_applied_controls_retrieve` | `COMPLIANCETOOL` | API endpoint that allows reference controls to be viewed or edited. |
| `ciso_assistant_api_reference_controls_update` | `COMPLIANCETOOL` | API endpoint that allows reference controls to be viewed or edited. |
| `ciso_assistant_api_representatives_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_representatives_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_representatives_create` | `GRANULARTOOL` | API endpoint that allows representatives to be viewed or edited. |
| `ciso_assistant_api_representatives_destroy` | `GRANULARTOOL` | API endpoint that allows representatives to be viewed or edited. |
| `ciso_assistant_api_representatives_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_representatives_object_retrieve` | `GRANULARTOOL` | API endpoint that allows representatives to be viewed or edited. |
| `ciso_assistant_api_representatives_partial_update` | `GRANULARTOOL` | API endpoint that allows representatives to be viewed or edited. |
| `ciso_assistant_api_representatives_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_representatives_update` | `GRANULARTOOL` | API endpoint that allows representatives to be viewed or edited. |
| `ciso_assistant_api_requirement_assessments_batch_action_create` | `COMPLIANCETOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_requirement_assessments_cascade_info_retrieve` | `COMPLIANCETOOL` | Cascade preview: |
| `ciso_assistant_api_requirement_assessments_create` | `COMPLIANCETOOL` | API endpoint that allows requirement assessments to be viewed or edited. |
| `ciso_assistant_api_requirement_assessments_destroy` | `COMPLIANCETOOL` | API endpoint that allows requirement assessments to be viewed or edited. |
| `ciso_assistant_api_requirement_assessments_extended_result_retrieve` | `COMPLIANCETOOL` | API endpoint that allows requirement assessments to be viewed or edited. |
| `ciso_assistant_api_requirement_assessments_list` | `COMPLIANCETOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_requirement_assessments_object_retrieve` | `COMPLIANCETOOL` | API endpoint that allows requirement assessments to be viewed or edited. |
| `ciso_assistant_api_requirement_assessments_partial_update` | `COMPLIANCETOOL` | API endpoint that allows requirement assessments to be viewed or edited. |
| `ciso_assistant_api_requirement_assessments_per_status_retrieve` | `COMPLIANCETOOL` | API endpoint that allows requirement assessments to be viewed or edited. |
| `ciso_assistant_api_requirement_assessments_result_retrieve` | `COMPLIANCETOOL` | API endpoint that allows requirement assessments to be viewed or edited. |
| `ciso_assistant_api_requirement_assessments_retrieve` | `COMPLIANCETOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_requirement_assessments_status_retrieve` | `COMPLIANCETOOL` | API endpoint that allows requirement assessments to be viewed or edited. |
| `ciso_assistant_api_requirement_assessments_suggestions_applied_controls_create` | `COMPLIANCETOOL` | api_requirement_assessments_suggestions_applied_controls_create |
| `ciso_assistant_api_requirement_assessments_suggestions_applied_controls_retrieve` | `COMPLIANCETOOL` | api_requirement_assessments_suggestions_applied_controls_retrieve |
| `ciso_assistant_api_requirement_assessments_to_review_retrieve` | `COMPLIANCETOOL` | API endpoint that allows requirement assessments to be viewed or edited. |
| `ciso_assistant_api_requirement_assessments_todo_retrieve` | `COMPLIANCETOOL` | API endpoint that allows requirement assessments to be viewed or edited. |
| `ciso_assistant_api_requirement_assessments_updatables_retrieve` | `COMPLIANCETOOL` | API endpoint that allows requirement assessments to be viewed or edited. |
| `ciso_assistant_api_requirement_assessments_update` | `COMPLIANCETOOL` | API endpoint that allows requirement assessments to be viewed or edited. |
| `ciso_assistant_api_requirement_assignments_batch_action_create` | `COMPLIANCETOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_requirement_assignments_cascade_info_retrieve` | `COMPLIANCETOOL` | Cascade preview: |
| `ciso_assistant_api_requirement_assignments_create` | `COMPLIANCETOOL` | API endpoint that allows requirement assignments to be viewed or edited. |
| `ciso_assistant_api_requirement_assignments_destroy` | `COMPLIANCETOOL` | API endpoint that allows requirement assignments to be viewed or edited. |
| `ciso_assistant_api_requirement_assignments_list` | `COMPLIANCETOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_requirement_assignments_object_retrieve` | `COMPLIANCETOOL` | API endpoint that allows requirement assignments to be viewed or edited. |
| `ciso_assistant_api_requirement_assignments_partial_update` | `COMPLIANCETOOL` | API endpoint that allows requirement assignments to be viewed or edited. |
| `ciso_assistant_api_requirement_assignments_requirements_list_retrieve` | `COMPLIANCETOOL` | Returns the scoped requirements list for this assignment. |
| `ciso_assistant_api_requirement_assignments_retrieve` | `COMPLIANCETOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_requirement_assignments_set_status_create` | `COMPLIANCETOOL` | Transition assignment to a new status. |
| `ciso_assistant_api_requirement_assignments_update` | `COMPLIANCETOOL` | API endpoint that allows requirement assignments to be viewed or edited. |
| `ciso_assistant_api_requirement_mapping_sets_batch_action_create` | `COMPLIANCETOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_requirement_mapping_sets_cascade_info_retrieve` | `COMPLIANCETOOL` | Cascade preview: |
| `ciso_assistant_api_requirement_mapping_sets_create` | `COMPLIANCETOOL` | api_requirement_mapping_sets_create |
| `ciso_assistant_api_requirement_mapping_sets_destroy` | `COMPLIANCETOOL` | api_requirement_mapping_sets_destroy |
| `ciso_assistant_api_requirement_mapping_sets_graph_data_retrieve` | `COMPLIANCETOOL` | api_requirement_mapping_sets_graph_data_retrieve |
| `ciso_assistant_api_requirement_mapping_sets_graph_data_retrieve_2` | `COMPLIANCETOOL` | api_requirement_mapping_sets_graph_data_retrieve_2 |
| `ciso_assistant_api_requirement_mapping_sets_list` | `COMPLIANCETOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_requirement_mapping_sets_object_retrieve` | `COMPLIANCETOOL` | api_requirement_mapping_sets_object_retrieve |
| `ciso_assistant_api_requirement_mapping_sets_partial_update` | `COMPLIANCETOOL` | api_requirement_mapping_sets_partial_update |
| `ciso_assistant_api_requirement_mapping_sets_provider_retrieve` | `COMPLIANCETOOL` | api_requirement_mapping_sets_provider_retrieve |
| `ciso_assistant_api_requirement_mapping_sets_retrieve` | `COMPLIANCETOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_requirement_mapping_sets_update` | `COMPLIANCETOOL` | api_requirement_mapping_sets_update |
| `ciso_assistant_api_requirement_nodes_batch_action_create` | `COMPLIANCETOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_requirement_nodes_cascade_info_retrieve` | `COMPLIANCETOOL` | Cascade preview: |
| `ciso_assistant_api_requirement_nodes_create` | `COMPLIANCETOOL` | API endpoint that allows requirements to be viewed or edited. |
| `ciso_assistant_api_requirement_nodes_destroy` | `COMPLIANCETOOL` | API endpoint that allows requirements to be viewed or edited. |
| `ciso_assistant_api_requirement_nodes_inspect_requirement_retrieve` | `COMPLIANCETOOL` | API endpoint that allows requirements to be viewed or edited. |
| `ciso_assistant_api_requirement_nodes_list` | `COMPLIANCETOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_requirement_nodes_object_retrieve` | `COMPLIANCETOOL` | API endpoint that allows requirements to be viewed or edited. |
| `ciso_assistant_api_requirement_nodes_partial_update` | `COMPLIANCETOOL` | API endpoint that allows requirements to be viewed or edited. |
| `ciso_assistant_api_requirement_nodes_retrieve` | `COMPLIANCETOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_requirement_nodes_serve_image_retrieve` | `COMPLIANCETOOL` | Serve an image attachment belonging to this requirement node. |
| `ciso_assistant_api_requirement_nodes_update` | `COMPLIANCETOOL` | API endpoint that allows requirements to be viewed or edited. |
| `ciso_assistant_api_requirement_nodes_upload_image_create` | `COMPLIANCETOOL` | Upload an image file and attach it to this requirement node. |
| `ciso_assistant_api_resilience_asset_assessments_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_resilience_asset_assessments_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_resilience_asset_assessments_create` | `GRANULARTOOL` | api_resilience_asset_assessments_create |
| `ciso_assistant_api_resilience_asset_assessments_dependency_graph_retrieve` | `GRANULARTOOL` | Returns graph data for visualizing asset dependencies. |
| `ciso_assistant_api_resilience_asset_assessments_destroy` | `GRANULARTOOL` | api_resilience_asset_assessments_destroy |
| `ciso_assistant_api_resilience_asset_assessments_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_resilience_asset_assessments_metrics_retrieve` | `GRANULARTOOL` | api_resilience_asset_assessments_metrics_retrieve |
| `ciso_assistant_api_resilience_asset_assessments_object_retrieve` | `GRANULARTOOL` | api_resilience_asset_assessments_object_retrieve |
| `ciso_assistant_api_resilience_asset_assessments_partial_update` | `GRANULARTOOL` | api_resilience_asset_assessments_partial_update |
| `ciso_assistant_api_resilience_asset_assessments_quali_impact_retrieve` | `GRANULARTOOL` | api_resilience_asset_assessments_quali_impact_retrieve |
| `ciso_assistant_api_resilience_asset_assessments_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_resilience_asset_assessments_risk_matrix_retrieve` | `GRANULARTOOL` | api_resilience_asset_assessments_risk_matrix_retrieve |
| `ciso_assistant_api_resilience_asset_assessments_update` | `GRANULARTOOL` | api_resilience_asset_assessments_update |
| `ciso_assistant_api_resilience_business_impact_analysis_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_resilience_business_impact_analysis_build_table_retrieve` | `GRANULARTOOL` | api_resilience_business_impact_analysis_build_table_retrieve |
| `ciso_assistant_api_resilience_business_impact_analysis_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_resilience_business_impact_analysis_create` | `GRANULARTOOL` | api_resilience_business_impact_analysis_create |
| `ciso_assistant_api_resilience_business_impact_analysis_destroy` | `GRANULARTOOL` | api_resilience_business_impact_analysis_destroy |
| `ciso_assistant_api_resilience_business_impact_analysis_export_csv_retrieve` | `GRANULARTOOL` | api_resilience_business_impact_analysis_export_csv_retrieve |
| `ciso_assistant_api_resilience_business_impact_analysis_export_xlsx_retrieve` | `GRANULARTOOL` | api_resilience_business_impact_analysis_export_xlsx_retrieve |
| `ciso_assistant_api_resilience_business_impact_analysis_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_resilience_business_impact_analysis_metrics_retrieve` | `GRANULARTOOL` | api_resilience_business_impact_analysis_metrics_retrieve |
| `ciso_assistant_api_resilience_business_impact_analysis_object_retrieve` | `GRANULARTOOL` | api_resilience_business_impact_analysis_object_retrieve |
| `ciso_assistant_api_resilience_business_impact_analysis_partial_update` | `GRANULARTOOL` | api_resilience_business_impact_analysis_partial_update |
| `ciso_assistant_api_resilience_business_impact_analysis_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_resilience_business_impact_analysis_status_retrieve` | `GRANULARTOOL` | api_resilience_business_impact_analysis_status_retrieve |
| `ciso_assistant_api_resilience_business_impact_analysis_update` | `GRANULARTOOL` | api_resilience_business_impact_analysis_update |
| `ciso_assistant_api_resilience_business_impact_analysis_xlsx_retrieve` | `GRANULARTOOL` | api_resilience_business_impact_analysis_xlsx_retrieve |
| `ciso_assistant_api_resilience_dora_incident_reports_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_resilience_dora_incident_reports_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_resilience_dora_incident_reports_classification_criterion_retrieve` | `GRANULARTOOL` | api_resilience_dora_incident_reports_classification_criterion_retrieve |
| `ciso_assistant_api_resilience_dora_incident_reports_create` | `GRANULARTOOL` | api_resilience_dora_incident_reports_create |
| `ciso_assistant_api_resilience_dora_incident_reports_destroy` | `GRANULARTOOL` | api_resilience_dora_incident_reports_destroy |
| `ciso_assistant_api_resilience_dora_incident_reports_export_json_retrieve` | `GRANULARTOOL` | api_resilience_dora_incident_reports_export_json_retrieve |
| `ciso_assistant_api_resilience_dora_incident_reports_incident_classification_retrieve` | `GRANULARTOOL` | api_resilience_dora_incident_reports_incident_classification_retrieve |
| `ciso_assistant_api_resilience_dora_incident_reports_incident_discovery_retrieve` | `GRANULARTOOL` | api_resilience_dora_incident_reports_incident_discovery_retrieve |
| `ciso_assistant_api_resilience_dora_incident_reports_incident_submission_retrieve` | `GRANULARTOOL` | api_resilience_dora_incident_reports_incident_submission_retrieve |
| `ciso_assistant_api_resilience_dora_incident_reports_info_duration_service_downtime_actual_or_estimate_retrieve` | `GRANULARTOOL` | api_resilience_dora_incident_reports_info_duration_service_downtime_actual_or_estimate_retrieve |
| `ciso_assistant_api_resilience_dora_incident_reports_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_resilience_dora_incident_reports_main_entity_retrieve` | `GRANULARTOOL` | api_resilience_dora_incident_reports_main_entity_retrieve |
| `ciso_assistant_api_resilience_dora_incident_reports_object_retrieve` | `GRANULARTOOL` | api_resilience_dora_incident_reports_object_retrieve |
| `ciso_assistant_api_resilience_dora_incident_reports_partial_update` | `GRANULARTOOL` | api_resilience_dora_incident_reports_partial_update |
| `ciso_assistant_api_resilience_dora_incident_reports_report_currency_retrieve` | `GRANULARTOOL` | api_resilience_dora_incident_reports_report_currency_retrieve |
| `ciso_assistant_api_resilience_dora_incident_reports_reporting_authority_retrieve` | `GRANULARTOOL` | api_resilience_dora_incident_reports_reporting_authority_retrieve |
| `ciso_assistant_api_resilience_dora_incident_reports_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_resilience_dora_incident_reports_root_cause_additional_retrieve` | `GRANULARTOOL` | api_resilience_dora_incident_reports_root_cause_additional_retrieve |
| `ciso_assistant_api_resilience_dora_incident_reports_root_cause_detailed_retrieve` | `GRANULARTOOL` | api_resilience_dora_incident_reports_root_cause_detailed_retrieve |
| `ciso_assistant_api_resilience_dora_incident_reports_root_cause_hl_retrieve` | `GRANULARTOOL` | api_resilience_dora_incident_reports_root_cause_hl_retrieve |
| `ciso_assistant_api_resilience_dora_incident_reports_threat_techniques_retrieve` | `GRANULARTOOL` | api_resilience_dora_incident_reports_threat_techniques_retrieve |
| `ciso_assistant_api_resilience_dora_incident_reports_update` | `GRANULARTOOL` | api_resilience_dora_incident_reports_update |
| `ciso_assistant_api_resilience_dora_incident_reports_validate_report_retrieve` | `GRANULARTOOL` | api_resilience_dora_incident_reports_validate_report_retrieve |
| `ciso_assistant_api_resilience_escalation_thresholds_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_resilience_escalation_thresholds_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_resilience_escalation_thresholds_create` | `GRANULARTOOL` | api_resilience_escalation_thresholds_create |
| `ciso_assistant_api_resilience_escalation_thresholds_destroy` | `GRANULARTOOL` | api_resilience_escalation_thresholds_destroy |
| `ciso_assistant_api_resilience_escalation_thresholds_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_resilience_escalation_thresholds_object_retrieve` | `GRANULARTOOL` | api_resilience_escalation_thresholds_object_retrieve |
| `ciso_assistant_api_resilience_escalation_thresholds_partial_update` | `GRANULARTOOL` | api_resilience_escalation_thresholds_partial_update |
| `ciso_assistant_api_resilience_escalation_thresholds_quali_impact_retrieve` | `GRANULARTOOL` | api_resilience_escalation_thresholds_quali_impact_retrieve |
| `ciso_assistant_api_resilience_escalation_thresholds_quant_unit_retrieve` | `GRANULARTOOL` | api_resilience_escalation_thresholds_quant_unit_retrieve |
| `ciso_assistant_api_resilience_escalation_thresholds_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_resilience_escalation_thresholds_risk_matrix_retrieve` | `GRANULARTOOL` | api_resilience_escalation_thresholds_risk_matrix_retrieve |
| `ciso_assistant_api_resilience_escalation_thresholds_update` | `GRANULARTOOL` | api_resilience_escalation_thresholds_update |
| `ciso_assistant_api_risk_acceptances_accept_create` | `GRANULARTOOL` | API endpoint that allows risk acceptance to be viewed or edited. |
| `ciso_assistant_api_risk_acceptances_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_risk_acceptances_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_risk_acceptances_create` | `GRANULARTOOL` | API endpoint that allows risk acceptance to be viewed or edited. |
| `ciso_assistant_api_risk_acceptances_destroy` | `GRANULARTOOL` | API endpoint that allows risk acceptance to be viewed or edited. |
| `ciso_assistant_api_risk_acceptances_draft_create` | `GRANULARTOOL` | API endpoint that allows risk acceptance to be viewed or edited. |
| `ciso_assistant_api_risk_acceptances_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_risk_acceptances_object_retrieve` | `GRANULARTOOL` | API endpoint that allows risk acceptance to be viewed or edited. |
| `ciso_assistant_api_risk_acceptances_partial_update` | `GRANULARTOOL` | API endpoint that allows risk acceptance to be viewed or edited. |
| `ciso_assistant_api_risk_acceptances_reject_create` | `GRANULARTOOL` | API endpoint that allows risk acceptance to be viewed or edited. |
| `ciso_assistant_api_risk_acceptances_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_risk_acceptances_revoke_create` | `GRANULARTOOL` | API endpoint that allows risk acceptance to be viewed or edited. |
| `ciso_assistant_api_risk_acceptances_state_retrieve` | `GRANULARTOOL` | API endpoint that allows risk acceptance to be viewed or edited. |
| `ciso_assistant_api_risk_acceptances_submit_create` | `GRANULARTOOL` | API endpoint that allows risk acceptance to be viewed or edited. |
| `ciso_assistant_api_risk_acceptances_to_review_retrieve` | `GRANULARTOOL` | API endpoint that allows risk acceptance to be viewed or edited. |
| `ciso_assistant_api_risk_acceptances_update` | `GRANULARTOOL` | API endpoint that allows risk acceptance to be viewed or edited. |
| `ciso_assistant_api_risk_acceptances_waiting_retrieve` | `GRANULARTOOL` | API endpoint that allows risk acceptance to be viewed or edited. |
| `ciso_assistant_api_risk_assessments_action_plan_budget_overview_list` | `GRANULARTOOL` | Mixin that computes budget aggregation over an applied controls queryset. |
| `ciso_assistant_api_risk_assessments_action_plan_excel_retrieve` | `GRANULARTOOL` | API endpoint that allows risk assessments to be viewed or edited. |
| `ciso_assistant_api_risk_assessments_action_plan_list` | `GRANULARTOOL` | api_risk_assessments_action_plan_list |
| `ciso_assistant_api_risk_assessments_action_plan_pdf_retrieve` | `GRANULARTOOL` | API endpoint that allows risk assessments to be viewed or edited. |
| `ciso_assistant_api_risk_assessments_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_risk_assessments_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_risk_assessments_convert_to_quantitative_create` | `GRANULARTOOL` | Convert a qualitative risk assessment to a quantitative risk study. |
| `ciso_assistant_api_risk_assessments_create` | `GRANULARTOOL` | API endpoint that allows risk assessments to be viewed or edited. |
| `ciso_assistant_api_risk_assessments_destroy` | `GRANULARTOOL` | API endpoint that allows risk assessments to be viewed or edited. |
| `ciso_assistant_api_risk_assessments_duplicate_create` | `GRANULARTOOL` | API endpoint that allows risk assessments to be viewed or edited. |
| `ciso_assistant_api_risk_assessments_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_risk_assessments_object_retrieve` | `GRANULARTOOL` | API endpoint that allows risk assessments to be viewed or edited. |
| `ciso_assistant_api_risk_assessments_partial_update` | `GRANULARTOOL` | API endpoint that allows risk assessments to be viewed or edited. |
| `ciso_assistant_api_risk_assessments_per_status_retrieve` | `GRANULARTOOL` | API endpoint that allows risk assessments to be viewed or edited. |
| `ciso_assistant_api_risk_assessments_quality_check_retrieve` | `GRANULARTOOL` | Returns the quality check of the risk assessments |
| `ciso_assistant_api_risk_assessments_quality_check_retrieve_2` | `GRANULARTOOL` | Returns the quality check of the risk_assessment |
| `ciso_assistant_api_risk_assessments_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_risk_assessments_risk_analytics_retrieve` | `GRANULARTOOL` | Analytics data for a single risk assessment. |
| `ciso_assistant_api_risk_assessments_risk_assessment_csv_retrieve` | `GRANULARTOOL` | API endpoint that allows risk assessments to be viewed or edited. |
| `ciso_assistant_api_risk_assessments_risk_assessment_pdf_retrieve` | `GRANULARTOOL` | API endpoint that allows risk assessments to be viewed or edited. |
| `ciso_assistant_api_risk_assessments_risk_assessment_xlsx_retrieve` | `GRANULARTOOL` | API endpoint that allows risk assessments to be viewed or edited. |
| `ciso_assistant_api_risk_assessments_risk_timeline_retrieve` | `GRANULARTOOL` | Returns risk metrics over time from BuiltinMetricSample snapshots. |
| `ciso_assistant_api_risk_assessments_status_retrieve` | `GRANULARTOOL` | API endpoint that allows risk assessments to be viewed or edited. |
| `ciso_assistant_api_risk_assessments_sync_from_ebios_rm_create` | `GRANULARTOOL` | Synchronize an existing risk assessment with its linked EBIOS RM study. |
| `ciso_assistant_api_risk_assessments_sync_preview_retrieve` | `GRANULARTOOL` | Preview what a sync from EBIOS RM would produce. |
| `ciso_assistant_api_risk_assessments_sync_to_actions_create` | `GRANULARTOOL` | API endpoint that allows risk assessments to be viewed or edited. |
| `ciso_assistant_api_risk_assessments_update` | `GRANULARTOOL` | API endpoint that allows risk assessments to be viewed or edited. |
| `ciso_assistant_api_risk_matrices_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_risk_matrices_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_risk_matrices_colors_retrieve` | `GRANULARTOOL` | API endpoint that allows risk matrices to be viewed or edited. |
| `ciso_assistant_api_risk_matrices_create` | `GRANULARTOOL` | API endpoint that allows risk matrices to be viewed or edited. |
| `ciso_assistant_api_risk_matrices_create_draft_create` | `GRANULARTOOL` | Create a new unpublished RiskMatrix with an editing_draft for the visual editor. |
| `ciso_assistant_api_risk_matrices_create_draft_from_create` | `GRANULARTOOL` | Clone an existing matrix into a new unpublished RiskMatrix with editing_draft. |
| `ciso_assistant_api_risk_matrices_destroy` | `GRANULARTOOL` | API endpoint that allows risk matrices to be viewed or edited. |
| `ciso_assistant_api_risk_matrices_discard_draft_create` | `GRANULARTOOL` | Discard editing_draft without affecting json_definition. |
| `ciso_assistant_api_risk_matrices_export_yaml_retrieve` | `GRANULARTOOL` | Export a matrix as a library-compatible YAML file. |
| `ciso_assistant_api_risk_matrices_ids_retrieve` | `GRANULARTOOL` | API endpoint that allows risk matrices to be viewed or edited. |
| `ciso_assistant_api_risk_matrices_impact_retrieve` | `GRANULARTOOL` | API endpoint that allows risk matrices to be viewed or edited. |
| `ciso_assistant_api_risk_matrices_import_yaml_create` | `GRANULARTOOL` | Import a library YAML file and create a new draft matrix from it. |
| `ciso_assistant_api_risk_matrices_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_risk_matrices_object_retrieve` | `GRANULARTOOL` | API endpoint that allows risk matrices to be viewed or edited. |
| `ciso_assistant_api_risk_matrices_partial_update` | `GRANULARTOOL` | API endpoint that allows risk matrices to be viewed or edited. |
| `ciso_assistant_api_risk_matrices_probability_retrieve` | `GRANULARTOOL` | API endpoint that allows risk matrices to be viewed or edited. |
| `ciso_assistant_api_risk_matrices_provider_retrieve` | `GRANULARTOOL` | API endpoint that allows risk matrices to be viewed or edited. |
| `ciso_assistant_api_risk_matrices_publish_draft_create` | `GRANULARTOOL` | Publish editing_draft → json_definition, snapshot history, bump version. |
| `ciso_assistant_api_risk_matrices_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_risk_matrices_risk_retrieve` | `GRANULARTOOL` | API endpoint that allows risk matrices to be viewed or edited. |
| `ciso_assistant_api_risk_matrices_save_draft_partial_update` | `GRANULARTOOL` | Update editing_draft with current WIP. Metadata stays draft-scoped until publish. |
| `ciso_assistant_api_risk_matrices_start_editing_create` | `GRANULARTOOL` | Copy json_definition into editing_draft to begin editing. |
| `ciso_assistant_api_risk_matrices_update` | `GRANULARTOOL` | API endpoint that allows risk matrices to be viewed or edited. |
| `ciso_assistant_api_risk_matrices_used_retrieve` | `GRANULARTOOL` | API endpoint that allows risk matrices to be viewed or edited. |
| `ciso_assistant_api_risk_scenarios_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_risk_scenarios_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_risk_scenarios_count_per_level_retrieve` | `GRANULARTOOL` | API endpoint that allows risk scenarios to be viewed or edited. |
| `ciso_assistant_api_risk_scenarios_create` | `GRANULARTOOL` | API endpoint that allows risk scenarios to be viewed or edited. |
| `ciso_assistant_api_risk_scenarios_default_ref_id_retrieve` | `GRANULARTOOL` | API endpoint that allows risk scenarios to be viewed or edited. |
| `ciso_assistant_api_risk_scenarios_destroy` | `GRANULARTOOL` | API endpoint that allows risk scenarios to be viewed or edited. |
| `ciso_assistant_api_risk_scenarios_export_csv_retrieve` | `GRANULARTOOL` | API endpoint that allows risk scenarios to be viewed or edited. |
| `ciso_assistant_api_risk_scenarios_export_xlsx_retrieve` | `GRANULARTOOL` | API endpoint that allows risk scenarios to be viewed or edited. |
| `ciso_assistant_api_risk_scenarios_impact_retrieve` | `GRANULARTOOL` | API endpoint that allows risk scenarios to be viewed or edited. |
| `ciso_assistant_api_risk_scenarios_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_risk_scenarios_object_retrieve` | `GRANULARTOOL` | API endpoint that allows risk scenarios to be viewed or edited. |
| `ciso_assistant_api_risk_scenarios_partial_update` | `GRANULARTOOL` | API endpoint that allows risk scenarios to be viewed or edited. |
| `ciso_assistant_api_risk_scenarios_per_status_retrieve` | `GRANULARTOOL` | API endpoint that allows risk scenarios to be viewed or edited. |
| `ciso_assistant_api_risk_scenarios_probability_retrieve` | `GRANULARTOOL` | API endpoint that allows risk scenarios to be viewed or edited. |
| `ciso_assistant_api_risk_scenarios_qualifications_count_retrieve` | `GRANULARTOOL` | API endpoint that allows risk scenarios to be viewed or edited. |
| `ciso_assistant_api_risk_scenarios_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_risk_scenarios_strength_of_knowledge_retrieve` | `GRANULARTOOL` | API endpoint that allows risk scenarios to be viewed or edited. |
| `ciso_assistant_api_risk_scenarios_sync_to_actions_create` | `GRANULARTOOL` | API endpoint that allows risk scenarios to be viewed or edited. |
| `ciso_assistant_api_risk_scenarios_treatment_retrieve` | `GRANULARTOOL` | API endpoint that allows risk scenarios to be viewed or edited. |
| `ciso_assistant_api_risk_scenarios_update` | `GRANULARTOOL` | API endpoint that allows risk scenarios to be viewed or edited. |
| `ciso_assistant_api_role_assignments_batch_action_create` | `AUTH_USERSTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_role_assignments_cascade_info_retrieve` | `AUTH_USERSTOOL` | Cascade preview: |
| `ciso_assistant_api_role_assignments_create` | `AUTH_USERSTOOL` | API endpoint that allows role assignments to be viewed or edited. |
| `ciso_assistant_api_role_assignments_destroy` | `AUTH_USERSTOOL` | API endpoint that allows role assignments to be viewed or edited. |
| `ciso_assistant_api_role_assignments_list` | `AUTH_USERSTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_role_assignments_object_retrieve` | `AUTH_USERSTOOL` | API endpoint that allows role assignments to be viewed or edited. |
| `ciso_assistant_api_role_assignments_partial_update` | `AUTH_USERSTOOL` | API endpoint that allows role assignments to be viewed or edited. |
| `ciso_assistant_api_role_assignments_retrieve` | `AUTH_USERSTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_role_assignments_update` | `AUTH_USERSTOOL` | API endpoint that allows role assignments to be viewed or edited. |
| `ciso_assistant_api_search_retrieve` | `GRANULARTOOL` | Universal fuzzy search across all searchable models. |
| `ciso_assistant_api_security_advisories_autocomplete_retrieve` | `GRANULARTOOL` | API endpoint that allows security advisories to be viewed or edited. |
| `ciso_assistant_api_security_advisories_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_security_advisories_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_security_advisories_create` | `GRANULARTOOL` | API endpoint that allows security advisories to be viewed or edited. |
| `ciso_assistant_api_security_advisories_destroy` | `GRANULARTOOL` | API endpoint that allows security advisories to be viewed or edited. |
| `ciso_assistant_api_security_advisories_enrich_create` | `GRANULARTOOL` | Enrich this advisory with data from its source (NVD or EUVD). |
| `ciso_assistant_api_security_advisories_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_security_advisories_object_retrieve` | `GRANULARTOOL` | API endpoint that allows security advisories to be viewed or edited. |
| `ciso_assistant_api_security_advisories_partial_update` | `GRANULARTOOL` | API endpoint that allows security advisories to be viewed or edited. |
| `ciso_assistant_api_security_advisories_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_security_advisories_source_retrieve` | `GRANULARTOOL` | API endpoint that allows security advisories to be viewed or edited. |
| `ciso_assistant_api_security_advisories_sync_euvd_create` | `GRANULARTOOL` | Sync EUVD exploited vulnerabilities synchronously. |
| `ciso_assistant_api_security_advisories_sync_kev_create` | `GRANULARTOOL` | Sync KEV feed synchronously. Scheduled async via Huey periodic tasks. |
| `ciso_assistant_api_security_advisories_update` | `GRANULARTOOL` | API endpoint that allows security advisories to be viewed or edited. |
| `ciso_assistant_api_security_exceptions_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_security_exceptions_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_security_exceptions_create` | `GRANULARTOOL` | API endpoint that allows security exceptions to be viewed or edited. |
| `ciso_assistant_api_security_exceptions_destroy` | `GRANULARTOOL` | API endpoint that allows security exceptions to be viewed or edited. |
| `ciso_assistant_api_security_exceptions_export_csv_retrieve` | `GRANULARTOOL` | API endpoint that allows security exceptions to be viewed or edited. |
| `ciso_assistant_api_security_exceptions_export_xlsx_retrieve` | `GRANULARTOOL` | API endpoint that allows security exceptions to be viewed or edited. |
| `ciso_assistant_api_security_exceptions_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_security_exceptions_object_retrieve` | `GRANULARTOOL` | API endpoint that allows security exceptions to be viewed or edited. |
| `ciso_assistant_api_security_exceptions_partial_update` | `GRANULARTOOL` | API endpoint that allows security exceptions to be viewed or edited. |
| `ciso_assistant_api_security_exceptions_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_security_exceptions_sankey_data_retrieve` | `GRANULARTOOL` | API endpoint that allows security exceptions to be viewed or edited. |
| `ciso_assistant_api_security_exceptions_severity_retrieve` | `GRANULARTOOL` | API endpoint that allows security exceptions to be viewed or edited. |
| `ciso_assistant_api_security_exceptions_status_retrieve` | `GRANULARTOOL` | API endpoint that allows security exceptions to be viewed or edited. |
| `ciso_assistant_api_security_exceptions_update` | `GRANULARTOOL` | API endpoint that allows security exceptions to be viewed or edited. |
| `ciso_assistant_api_serdes_attachment_metadata_retrieve` | `GRANULARTOOL` | GET endpoint that returns paginated metadata for all attachments. |
| `ciso_assistant_api_serdes_batch_download_attachments_create` | `GRANULARTOOL` | POST endpoint that streams multiple attachments in a custom binary format. |
| `ciso_assistant_api_serdes_batch_upload_attachments_create` | `GRANULARTOOL` | POST endpoint that accepts multiple attachments in custom binary format. |
| `ciso_assistant_api_serdes_dump_db_retrieve` | `GRANULARTOOL` | api_serdes_dump_db_retrieve |
| `ciso_assistant_api_serdes_full_restore_create` | `GRANULARTOOL` | POST endpoint for atomic database + attachments restore. |
| `ciso_assistant_api_serdes_load_backup_create` | `GRANULARTOOL` | api_serdes_load_backup_create |
| `ciso_assistant_api_settings_feature_flags_partial_update` | `GRANULARTOOL` | api_settings_feature_flags_partial_update |
| `ciso_assistant_api_settings_feature_flags_retrieve` | `GRANULARTOOL` | api_settings_feature_flags_retrieve |
| `ciso_assistant_api_settings_feature_flags_update` | `GRANULARTOOL` | api_settings_feature_flags_update |
| `ciso_assistant_api_settings_general_default_custom_analytics_dashboard_retrieve` | `GRANULARTOOL` | Return a {dashboard_uuid: dashboard_name} map of dashboards |
| `ciso_assistant_api_settings_general_default_language_retrieve` | `GRANULARTOOL` | Returns the configured default language. Falls back to English if unset or invalid. |
| `ciso_assistant_api_settings_general_default_language_retrieve_2` | `GRANULARTOOL` | api_settings_general_default_language_retrieve_2 |
| `ciso_assistant_api_settings_general_ebios_radar_parameters_retrieve` | `GRANULARTOOL` | api_settings_general_ebios_radar_parameters_retrieve |
| `ciso_assistant_api_settings_general_force_language_create` | `GRANULARTOOL` | api_settings_general_force_language_create |
| `ciso_assistant_api_settings_general_interface_settings_retrieve` | `GRANULARTOOL` | api_settings_general_interface_settings_retrieve |
| `ciso_assistant_api_settings_general_notifications_settings_retrieve` | `GRANULARTOOL` | api_settings_general_notifications_settings_retrieve |
| `ciso_assistant_api_settings_general_object_retrieve` | `GRANULARTOOL` | api_settings_general_object_retrieve |
| `ciso_assistant_api_settings_general_partial_update` | `GRANULARTOOL` | api_settings_general_partial_update |
| `ciso_assistant_api_settings_general_retrieve` | `GRANULARTOOL` | api_settings_general_retrieve |
| `ciso_assistant_api_settings_general_security_objective_scale_retrieve` | `GRANULARTOOL` | api_settings_general_security_objective_scale_retrieve |
| `ciso_assistant_api_settings_general_set_default_dashboard_create` | `GRANULARTOOL` | Partial update of the default_custom_analytics_dashboard key. |
| `ciso_assistant_api_settings_general_update` | `GRANULARTOOL` | api_settings_general_update |
| `ciso_assistant_api_settings_global_create` | `GRANULARTOOL` | api_settings_global_create |
| `ciso_assistant_api_settings_global_destroy` | `GRANULARTOOL` | api_settings_global_destroy |
| `ciso_assistant_api_settings_global_list` | `GRANULARTOOL` | api_settings_global_list |
| `ciso_assistant_api_settings_global_partial_update` | `GRANULARTOOL` | api_settings_global_partial_update |
| `ciso_assistant_api_settings_global_retrieve` | `GRANULARTOOL` | api_settings_global_retrieve |
| `ciso_assistant_api_settings_global_update` | `GRANULARTOOL` | api_settings_global_update |
| `ciso_assistant_api_settings_sec_intel_feeds_partial_update` | `GRANULARTOOL` | api_settings_sec_intel_feeds_partial_update |
| `ciso_assistant_api_settings_sec_intel_feeds_retrieve` | `GRANULARTOOL` | api_settings_sec_intel_feeds_retrieve |
| `ciso_assistant_api_settings_sec_intel_feeds_update` | `GRANULARTOOL` | api_settings_sec_intel_feeds_update |
| `ciso_assistant_api_settings_sso_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_settings_sso_info_retrieve` | `GRANULARTOOL` | API endpoint that returns the CSRF token. |
| `ciso_assistant_api_settings_sso_object_retrieve` | `GRANULARTOOL` | api_settings_sso_object_retrieve |
| `ciso_assistant_api_settings_sso_partial_update` | `GRANULARTOOL` | api_settings_sso_partial_update |
| `ciso_assistant_api_settings_sso_provider_retrieve` | `GRANULARTOOL` | api_settings_sso_provider_retrieve |
| `ciso_assistant_api_settings_sso_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_settings_sso_update` | `GRANULARTOOL` | api_settings_sso_update |
| `ciso_assistant_api_settings_vulnerability_sla_partial_update` | `GRANULARTOOL` | api_settings_vulnerability_sla_partial_update |
| `ciso_assistant_api_settings_vulnerability_sla_retrieve` | `GRANULARTOOL` | api_settings_vulnerability_sla_retrieve |
| `ciso_assistant_api_settings_vulnerability_sla_update` | `GRANULARTOOL` | api_settings_vulnerability_sla_update |
| `ciso_assistant_api_solutions_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_solutions_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_solutions_create` | `GRANULARTOOL` | API endpoint that allows solutions to be viewed or edited. |
| `ciso_assistant_api_solutions_data_location_processing_retrieve` | `GRANULARTOOL` | API endpoint that allows solutions to be viewed or edited. |
| `ciso_assistant_api_solutions_data_location_storage_retrieve` | `GRANULARTOOL` | API endpoint that allows solutions to be viewed or edited. |
| `ciso_assistant_api_solutions_destroy` | `GRANULARTOOL` | API endpoint that allows solutions to be viewed or edited. |
| `ciso_assistant_api_solutions_dora_alternative_providers_identified_retrieve` | `GRANULARTOOL` | API endpoint that allows solutions to be viewed or edited. |
| `ciso_assistant_api_solutions_dora_data_sensitiveness_retrieve` | `GRANULARTOOL` | API endpoint that allows solutions to be viewed or edited. |
| `ciso_assistant_api_solutions_dora_discontinuing_impact_retrieve` | `GRANULARTOOL` | API endpoint that allows solutions to be viewed or edited. |
| `ciso_assistant_api_solutions_dora_has_exit_plan_retrieve` | `GRANULARTOOL` | API endpoint that allows solutions to be viewed or edited. |
| `ciso_assistant_api_solutions_dora_ict_service_type_retrieve` | `GRANULARTOOL` | API endpoint that allows solutions to be viewed or edited. |
| `ciso_assistant_api_solutions_dora_non_substitutability_reason_retrieve` | `GRANULARTOOL` | API endpoint that allows solutions to be viewed or edited. |
| `ciso_assistant_api_solutions_dora_reintegration_possibility_retrieve` | `GRANULARTOOL` | API endpoint that allows solutions to be viewed or edited. |
| `ciso_assistant_api_solutions_dora_reliance_level_retrieve` | `GRANULARTOOL` | API endpoint that allows solutions to be viewed or edited. |
| `ciso_assistant_api_solutions_dora_substitutability_retrieve` | `GRANULARTOOL` | API endpoint that allows solutions to be viewed or edited. |
| `ciso_assistant_api_solutions_export_csv_retrieve` | `GRANULARTOOL` | API endpoint that allows solutions to be viewed or edited. |
| `ciso_assistant_api_solutions_export_xlsx_retrieve` | `GRANULARTOOL` | API endpoint that allows solutions to be viewed or edited. |
| `ciso_assistant_api_solutions_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_solutions_object_retrieve` | `GRANULARTOOL` | API endpoint that allows solutions to be viewed or edited. |
| `ciso_assistant_api_solutions_partial_update` | `GRANULARTOOL` | API endpoint that allows solutions to be viewed or edited. |
| `ciso_assistant_api_solutions_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_solutions_update` | `GRANULARTOOL` | API endpoint that allows solutions to be viewed or edited. |
| `ciso_assistant_api_stored_libraries_batch_action_create` | `FRAMEWORKS_LIBRARIESTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_stored_libraries_cascade_info_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | Cascade preview: |
| `ciso_assistant_api_stored_libraries_content_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | api_stored_libraries_content_retrieve |
| `ciso_assistant_api_stored_libraries_create` | `FRAMEWORKS_LIBRARIESTOOL` | api_stored_libraries_create |
| `ciso_assistant_api_stored_libraries_destroy` | `FRAMEWORKS_LIBRARIESTOOL` | api_stored_libraries_destroy |
| `ciso_assistant_api_stored_libraries_import_create` | `FRAMEWORKS_LIBRARIESTOOL` | api_stored_libraries_import_create |
| `ciso_assistant_api_stored_libraries_list` | `FRAMEWORKS_LIBRARIESTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_stored_libraries_locale_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | api_stored_libraries_locale_retrieve |
| `ciso_assistant_api_stored_libraries_object_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | api_stored_libraries_object_retrieve |
| `ciso_assistant_api_stored_libraries_object_type_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | api_stored_libraries_object_type_retrieve |
| `ciso_assistant_api_stored_libraries_partial_update` | `FRAMEWORKS_LIBRARIESTOOL` | api_stored_libraries_partial_update |
| `ciso_assistant_api_stored_libraries_provider_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | api_stored_libraries_provider_retrieve |
| `ciso_assistant_api_stored_libraries_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_stored_libraries_tree_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | api_stored_libraries_tree_retrieve |
| `ciso_assistant_api_stored_libraries_unload_create` | `FRAMEWORKS_LIBRARIESTOOL` | api_stored_libraries_unload_create |
| `ciso_assistant_api_stored_libraries_update` | `FRAMEWORKS_LIBRARIESTOOL` | api_stored_libraries_update |
| `ciso_assistant_api_stored_libraries_upload_create` | `FRAMEWORKS_LIBRARIESTOOL` | api_stored_libraries_upload_create |
| `ciso_assistant_api_task_nodes_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_task_nodes_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_task_nodes_create` | `GRANULARTOOL` | api_task_nodes_create |
| `ciso_assistant_api_task_nodes_destroy` | `GRANULARTOOL` | api_task_nodes_destroy |
| `ciso_assistant_api_task_nodes_evidences_list` | `GRANULARTOOL` | api_task_nodes_evidences_list |
| `ciso_assistant_api_task_nodes_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_task_nodes_object_retrieve` | `GRANULARTOOL` | api_task_nodes_object_retrieve |
| `ciso_assistant_api_task_nodes_partial_update` | `GRANULARTOOL` | api_task_nodes_partial_update |
| `ciso_assistant_api_task_nodes_remove_evidence_create` | `GRANULARTOOL` | api_task_nodes_remove_evidence_create |
| `ciso_assistant_api_task_nodes_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_task_nodes_status_retrieve` | `GRANULARTOOL` | api_task_nodes_status_retrieve |
| `ciso_assistant_api_task_nodes_update` | `GRANULARTOOL` | api_task_nodes_update |
| `ciso_assistant_api_task_templates_assigned_to_retrieve` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_task_templates_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_task_templates_calendar_retrieve` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_task_templates_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_task_templates_create` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_task_templates_destroy` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_task_templates_export_csv_retrieve` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_task_templates_export_xlsx_retrieve` | `GRANULARTOOL` | Export task templates with a summary sheet and individual sheets for each template's task nodes. |
| `ciso_assistant_api_task_templates_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_task_templates_object_retrieve` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_task_templates_partial_update` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_task_templates_per_status_retrieve` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_task_templates_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_task_templates_status_retrieve` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_task_templates_update` | `GRANULARTOOL` | Generic export mixin for CSV/XLSX exports. |
| `ciso_assistant_api_task_templates_yearly_review_retrieve` | `GRANULARTOOL` | Get recurrent task templates grouped by folder for yearly review. |
| `ciso_assistant_api_teams_batch_action_create` | `AUTH_USERSTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_teams_cascade_info_retrieve` | `AUTH_USERSTOOL` | Cascade preview: |
| `ciso_assistant_api_teams_create` | `AUTH_USERSTOOL` | api_teams_create |
| `ciso_assistant_api_teams_destroy` | `AUTH_USERSTOOL` | api_teams_destroy |
| `ciso_assistant_api_teams_list` | `AUTH_USERSTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_teams_object_retrieve` | `AUTH_USERSTOOL` | api_teams_object_retrieve |
| `ciso_assistant_api_teams_partial_update` | `AUTH_USERSTOOL` | api_teams_partial_update |
| `ciso_assistant_api_teams_retrieve` | `AUTH_USERSTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_teams_update` | `AUTH_USERSTOOL` | api_teams_update |
| `ciso_assistant_api_terminologies_batch_action_create` | `FRAMEWORKS_LIBRARIESTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_terminologies_cascade_info_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | Cascade preview: |
| `ciso_assistant_api_terminologies_create` | `FRAMEWORKS_LIBRARIESTOOL` | api_terminologies_create |
| `ciso_assistant_api_terminologies_destroy` | `FRAMEWORKS_LIBRARIESTOOL` | api_terminologies_destroy |
| `ciso_assistant_api_terminologies_field_path_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | api_terminologies_field_path_retrieve |
| `ciso_assistant_api_terminologies_list` | `FRAMEWORKS_LIBRARIESTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_terminologies_object_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | api_terminologies_object_retrieve |
| `ciso_assistant_api_terminologies_partial_update` | `FRAMEWORKS_LIBRARIESTOOL` | api_terminologies_partial_update |
| `ciso_assistant_api_terminologies_retrieve` | `FRAMEWORKS_LIBRARIESTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_terminologies_update` | `FRAMEWORKS_LIBRARIESTOOL` | api_terminologies_update |
| `ciso_assistant_api_threats_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_threats_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_threats_create` | `GRANULARTOOL` | API endpoint that allows threats to be viewed or edited. |
| `ciso_assistant_api_threats_destroy` | `GRANULARTOOL` | API endpoint that allows threats to be viewed or edited. |
| `ciso_assistant_api_threats_ids_retrieve` | `GRANULARTOOL` | API endpoint that allows threats to be viewed or edited. |
| `ciso_assistant_api_threats_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_threats_object_retrieve` | `GRANULARTOOL` | API endpoint that allows threats to be viewed or edited. |
| `ciso_assistant_api_threats_partial_update` | `GRANULARTOOL` | API endpoint that allows threats to be viewed or edited. |
| `ciso_assistant_api_threats_provider_retrieve` | `GRANULARTOOL` | API endpoint that allows threats to be viewed or edited. |
| `ciso_assistant_api_threats_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_threats_threats_count_retrieve` | `GRANULARTOOL` | API endpoint that allows threats to be viewed or edited. |
| `ciso_assistant_api_threats_update` | `GRANULARTOOL` | API endpoint that allows threats to be viewed or edited. |
| `ciso_assistant_api_timeline_entries_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_timeline_entries_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_timeline_entries_create` | `GRANULARTOOL` | api_timeline_entries_create |
| `ciso_assistant_api_timeline_entries_destroy` | `GRANULARTOOL` | api_timeline_entries_destroy |
| `ciso_assistant_api_timeline_entries_entry_type_retrieve` | `GRANULARTOOL` | api_timeline_entries_entry_type_retrieve |
| `ciso_assistant_api_timeline_entries_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_timeline_entries_object_retrieve` | `GRANULARTOOL` | api_timeline_entries_object_retrieve |
| `ciso_assistant_api_timeline_entries_partial_update` | `GRANULARTOOL` | api_timeline_entries_partial_update |
| `ciso_assistant_api_timeline_entries_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_timeline_entries_update` | `GRANULARTOOL` | api_timeline_entries_update |
| `ciso_assistant_api_user_groups_batch_action_create` | `AUTH_USERSTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_user_groups_cascade_info_retrieve` | `AUTH_USERSTOOL` | Cascade preview: |
| `ciso_assistant_api_user_groups_create` | `AUTH_USERSTOOL` | API endpoint that allows user groups to be viewed or edited |
| `ciso_assistant_api_user_groups_destroy` | `AUTH_USERSTOOL` | API endpoint that allows user groups to be viewed or edited |
| `ciso_assistant_api_user_groups_list` | `AUTH_USERSTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_user_groups_object_retrieve` | `AUTH_USERSTOOL` | API endpoint that allows user groups to be viewed or edited |
| `ciso_assistant_api_user_groups_partial_update` | `AUTH_USERSTOOL` | API endpoint that allows user groups to be viewed or edited |
| `ciso_assistant_api_user_groups_retrieve` | `AUTH_USERSTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_user_groups_update` | `AUTH_USERSTOOL` | API endpoint that allows user groups to be viewed or edited |
| `ciso_assistant_api_user_preferences_partial_update` | `AUTH_USERSTOOL` | api_user_preferences_partial_update |
| `ciso_assistant_api_user_preferences_retrieve` | `AUTH_USERSTOOL` | api_user_preferences_retrieve |
| `ciso_assistant_api_users_batch_action_create` | `AUTH_USERSTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_users_cascade_info_retrieve` | `AUTH_USERSTOOL` | Cascade preview: |
| `ciso_assistant_api_users_create` | `AUTH_USERSTOOL` | API endpoint that allows users to be viewed or edited |
| `ciso_assistant_api_users_destroy` | `AUTH_USERSTOOL` | API endpoint that allows users to be viewed or edited |
| `ciso_assistant_api_users_list` | `AUTH_USERSTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_users_object_retrieve` | `AUTH_USERSTOOL` | API endpoint that allows users to be viewed or edited |
| `ciso_assistant_api_users_partial_update` | `AUTH_USERSTOOL` | API endpoint that allows users to be viewed or edited |
| `ciso_assistant_api_users_retrieve` | `AUTH_USERSTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_users_update` | `AUTH_USERSTOOL` | API endpoint that allows users to be viewed or edited |
| `ciso_assistant_api_validation_flows_batch_action_create` | `GOVERNANCETOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_validation_flows_cascade_info_retrieve` | `GOVERNANCETOOL` | Cascade preview: |
| `ciso_assistant_api_validation_flows_create` | `GOVERNANCETOOL` | API endpoint that allows validation flows to be viewed or edited. |
| `ciso_assistant_api_validation_flows_default_ref_id_retrieve` | `GOVERNANCETOOL` | API endpoint that allows validation flows to be viewed or edited. |
| `ciso_assistant_api_validation_flows_destroy` | `GOVERNANCETOOL` | API endpoint that allows validation flows to be viewed or edited. |
| `ciso_assistant_api_validation_flows_linked_models_retrieve` | `GOVERNANCETOOL` | Return available model types that can be linked to validation flows |
| `ciso_assistant_api_validation_flows_list` | `GOVERNANCETOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_validation_flows_object_retrieve` | `GOVERNANCETOOL` | API endpoint that allows validation flows to be viewed or edited. |
| `ciso_assistant_api_validation_flows_partial_update` | `GOVERNANCETOOL` | API endpoint that allows validation flows to be viewed or edited. |
| `ciso_assistant_api_validation_flows_retrieve` | `GOVERNANCETOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_validation_flows_status_retrieve` | `GOVERNANCETOOL` | API endpoint that allows validation flows to be viewed or edited. |
| `ciso_assistant_api_validation_flows_update` | `GOVERNANCETOOL` | API endpoint that allows validation flows to be viewed or edited. |
| `ciso_assistant_api_vulnerabilities_autocomplete_retrieve` | `GRANULARTOOL` | API endpoint that allows vulnerabilities to be viewed or edited. |
| `ciso_assistant_api_vulnerabilities_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_vulnerabilities_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_vulnerabilities_create` | `GRANULARTOOL` | API endpoint that allows vulnerabilities to be viewed or edited. |
| `ciso_assistant_api_vulnerabilities_destroy` | `GRANULARTOOL` | API endpoint that allows vulnerabilities to be viewed or edited. |
| `ciso_assistant_api_vulnerabilities_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_vulnerabilities_object_retrieve` | `GRANULARTOOL` | API endpoint that allows vulnerabilities to be viewed or edited. |
| `ciso_assistant_api_vulnerabilities_partial_update` | `GRANULARTOOL` | API endpoint that allows vulnerabilities to be viewed or edited. |
| `ciso_assistant_api_vulnerabilities_refresh_due_dates_create` | `GRANULARTOOL` | Recalculate due_date for all vulnerabilities based on current SLA policy. |
| `ciso_assistant_api_vulnerabilities_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_vulnerabilities_sankey_data_retrieve` | `GRANULARTOOL` | Returns vulnerability data structured for Sankey diagram: |
| `ciso_assistant_api_vulnerabilities_severity_retrieve` | `GRANULARTOOL` | API endpoint that allows vulnerabilities to be viewed or edited. |
| `ciso_assistant_api_vulnerabilities_status_retrieve` | `GRANULARTOOL` | API endpoint that allows vulnerabilities to be viewed or edited. |
| `ciso_assistant_api_vulnerabilities_treemap_data_retrieve` | `GRANULARTOOL` | Returns vulnerability data structured for treemap visualization: |
| `ciso_assistant_api_vulnerabilities_update` | `GRANULARTOOL` | API endpoint that allows vulnerabilities to be viewed or edited. |
| `ciso_assistant_api_webhooks_audit_sinks_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_webhooks_audit_sinks_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_webhooks_audit_sinks_create` | `GRANULARTOOL` | Admin-managed audit-log forwarding destinations (kind=AUDIT_SINK). Folder/IAM |
| `ciso_assistant_api_webhooks_audit_sinks_destroy` | `GRANULARTOOL` | Admin-managed audit-log forwarding destinations (kind=AUDIT_SINK). Folder/IAM |
| `ciso_assistant_api_webhooks_audit_sinks_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_webhooks_audit_sinks_object_retrieve` | `GRANULARTOOL` | Admin-managed audit-log forwarding destinations (kind=AUDIT_SINK). Folder/IAM |
| `ciso_assistant_api_webhooks_audit_sinks_partial_update` | `GRANULARTOOL` | Admin-managed audit-log forwarding destinations (kind=AUDIT_SINK). Folder/IAM |
| `ciso_assistant_api_webhooks_audit_sinks_replay_create` | `GRANULARTOOL` | Re-emit historical audit events to this sink. Body: {since, until?} (ISO |
| `ciso_assistant_api_webhooks_audit_sinks_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_webhooks_audit_sinks_update` | `GRANULARTOOL` | Admin-managed audit-log forwarding destinations (kind=AUDIT_SINK). Folder/IAM |
| `ciso_assistant_api_webhooks_endpoints_batch_action_create` | `GRANULARTOOL` | Perform a batch action on multiple objects. |
| `ciso_assistant_api_webhooks_endpoints_cascade_info_retrieve` | `GRANULARTOOL` | Cascade preview: |
| `ciso_assistant_api_webhooks_endpoints_create` | `GRANULARTOOL` | API endpoint to create, list, retrieve, update, and delete |
| `ciso_assistant_api_webhooks_endpoints_destroy` | `GRANULARTOOL` | API endpoint to create, list, retrieve, update, and delete |
| `ciso_assistant_api_webhooks_endpoints_list` | `GRANULARTOOL` | Override the list method to inject optimized data into the serializer context. |
| `ciso_assistant_api_webhooks_endpoints_object_retrieve` | `GRANULARTOOL` | API endpoint to create, list, retrieve, update, and delete |
| `ciso_assistant_api_webhooks_endpoints_partial_update` | `GRANULARTOOL` | API endpoint to create, list, retrieve, update, and delete |
| `ciso_assistant_api_webhooks_endpoints_retrieve` | `GRANULARTOOL` | Return a single object with unauthorized related fields masked. |
| `ciso_assistant_api_webhooks_endpoints_update` | `GRANULARTOOL` | API endpoint to create, list, retrieve, update, and delete |
| `ciso_assistant_api_webhooks_event_types_retrieve` | `GRANULARTOOL` | Returns a list of all registered event type strings. |
| `ciso_assistant_serdes_attachment_metadata_retrieve` | `GRANULARTOOL` | GET endpoint that returns paginated metadata for all attachments. |
| `ciso_assistant_serdes_batch_download_attachments_create` | `GRANULARTOOL` | POST endpoint that streams multiple attachments in a custom binary format. |
| `ciso_assistant_serdes_batch_upload_attachments_create` | `GRANULARTOOL` | POST endpoint that accepts multiple attachments in custom binary format. |
| `ciso_assistant_serdes_dump_db_retrieve` | `GRANULARTOOL` | serdes_dump_db_retrieve |
| `ciso_assistant_serdes_full_restore_create` | `GRANULARTOOL` | POST endpoint for atomic database + attachments restore. |
| `ciso_assistant_serdes_load_backup_create` | `GRANULARTOOL` | serdes_load_backup_create |

</details>

_21 action-routed tool(s) · 1565 verbose 1:1 tool(s). Each is enabled unless its `<DOMAIN>TOOL` toggle is set false; `MCP_TOOL_MODE` selects the surface (**`intent` default** — the six verb-tools, granular set loaded on demand · `condensed` action-routed · `verbose` 1:1 · `both`). Auto-generated — do not edit._
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
> which adds the Pydantic AI agent and observability runtime — use it when you run
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

Pick the extra that matches what you want to run:

| Extra | Installs | Use when |
|-------|----------|----------|
| `ciso-assistant-api[mcp]` | MCP server plus `agent-utilities[mcp]`; the Agent Utilities base dependency includes `epistemic-graph[full]` | You run the **MCP server** with native graph ingestion |
| `ciso-assistant-api[agent]` | Full agent runtime (`agent-utilities[agent-runtime,logfire]` — Pydantic AI, observability, and the full epistemic-graph engine) | You run the **integrated agent** |
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
