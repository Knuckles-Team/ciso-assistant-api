---
name: ciso-assistant-risk-management
skill_type: skill
description: >-
  Work CISO Assistant risk via the ciso-assistant-api MCP server: read risk assessments, scenarios, applied controls, threats and vulnerabilities, judge residual level and treatment, ingest :RiskScenario / :Control nodes. Use to triage risk or decide treatment. Do NOT use for audits (ciso-assistant-compliance-audit) or incidents (ciso-assistant-incident-evidence).
license: MIT
tags: [ciso-assistant, grc, risk, controls, mcp]
metadata:
  author: Knuckles-Team
  version: '0.1.0'
---
# CISO Assistant Risk Management

Scope: Risk management on the CISO Assistant platform via the ciso-assistant-api MCP server — list and read risk assessments, risk scenarios, applied controls, threats and vulnerabilities, reason about inherent/current/residual levels and treatment, and natively ingest them into the knowledge graph as typed :RiskScenario / :Control nodes. Use when the agent must triage risk, decide a treatment, gate a risk as mitigated on a linked control, or map risk state into the KG. Do NOT use for compliance audits/frameworks (use ciso-assistant-compliance-audit) or incidents/evidence (use ciso-assistant-incident-evidence).

Domain-typed access to the CISO Assistant **risk** surface — risk assessments,
risk scenarios, applied controls, threats and vulnerabilities — for treatment
decisions and KG mapping. Prefer these tools over raw HTTP; they return the
GRC-shaped records the ontology (`:RiskScenario`, `:Control`, `:Threat`,
`:Vulnerability`) is built on.

## When to use
- List / triage risk scenarios and read their inherent/current/residual levels.
- Read a risk assessment and the scenarios it contains.
- List applied controls and their status/priority; decide if a risk is mitigated.
- Ingest risk scenarios / controls into the KG as typed nodes.

## When NOT to use
- Compliance assessments (audits), frameworks, requirements → `ciso-assistant-compliance-audit`.
- Incidents, evidence records and their attachments → `ciso-assistant-incident-evidence`.
- Endpoints with no dedicated tool → `ciso_assistant_api_request`.

## Steps

1. List the scenarios in scope with `ciso_assistant_api_risk_scenarios_list`, for example `{"ordering":"-updated_at","limit":25}`. Verify each row shows current and residual levels.
2. Read one scenario with `ciso_assistant_api_risk_scenarios_retrieve` and its UUID string. Verify the threats, assets and `applied_controls` fields are present.
3. Check treatment with `ciso_assistant_api_applied_controls_list`, for example `{"status":"to_do","ordering":"priority"}`. Verify a scenario is called mitigated only when it has a linked applied control.
4. Add context from `ciso_assistant_api_threats_list` and `ciso_assistant_api_vulnerabilities_list`. Verify the ids you cite exist in the returned rows.
5. Push records into the graph with `ciso_ingest` and `{"kind":"risk_scenarios","params_json":"{\"limit\":100}"}`. Verify the result shows a non-null `ingested` count.

## Failure recovery

| Failure | Cause | Recovery |
| --- | --- | --- |
| Authentication error from any tool | `CISO_ASSISTANT_URL` is wrong, or neither the token nor the username/password pair is set | Set `CISO_ASSISTANT_URL` and either `CISO_ASSISTANT_TOKEN` or the username/password pair, then call `ciso_assistant_api_risk_assessments_list` to confirm. |
| Retrieve reports not found | The id was passed as an integer or is stale | Pass the id as a UUID string copied from `ciso_assistant_api_risk_scenarios_list`. |
| Applied controls missing from risk output | Controls are served by the compliance tools, not the risk tools | Call `ciso_assistant_api_applied_controls_list` directly instead of looking in the risk results. |
| `ciso_ingest` returns `"ingested": null` | No reachable KG engine | Report that nothing was persisted; do not claim graph state until the engine is reachable and `ciso_ingest` returns a count. |

## Prerequisites & environment
Connect via the `mcp-client` skill against the **`ciso-assistant-api`** MCP server.

| Variable | Required | Notes |
|----------|----------|-------|
| `CISO_ASSISTANT_URL` | ✅ | Backend host, e.g. `https://ciso.arpa` |
| `CISO_ASSISTANT_TOKEN` | ✅* | Pre-minted Knox token |
| `CISO_ASSISTANT_USERNAME` / `CISO_ASSISTANT_PASSWORD` | ✅* | Login flow exchanged at `POST /api/iam/login/` |
| `CISO_ASSISTANT_SSL_VERIFY` | optional | TLS verification toggle |

\* Provide the token **or** the username/password pair. OIDC delegation is used
automatically when `ENABLE_DELEGATION` is active.

## Tools & actions
Each tool is one API operation and takes that operation's parameters directly.

| Tool group | Tools |
|----------------|-------------|
| Typed tools | `ciso_assistant_api_risk_assessments_list`, `ciso_assistant_api_risk_scenarios_list`, `ciso_assistant_api_risk_scenarios_retrieve`, `ciso_assistant_api_threats_list`, `ciso_assistant_api_vulnerabilities_list` |
| Typed tools | `ciso_assistant_api_applied_controls_list`, `ciso_assistant_api_applied_controls_retrieve` (controls live under the compliance client) |
| `ciso_ingest` | native KG push: `kind` = `risk_scenarios` \| `applied_controls` \| `risk_assessments` \| `vulnerabilities` |

## Recipes (`params_json`)
List open risk scenarios, most-recent first:
```json
{"ordering":"-updated_at","limit":25}
```
Read one risk scenario by id (with its threats/controls/assets):
```json
{"id":"<scenario_uuid>"}
```
List applied controls that are still to-do :
```json
{"status":"to_do","ordering":"priority"}
```
Ingest risk scenarios into the KG as typed `:RiskScenario` nodes (`ciso_ingest`):
```json
{"kind":"risk_scenarios","params_json":"{\"limit\":100}"}
```

## Gotchas
- Object ids are **UUID strings**, not ints — pass them as strings.
- List endpoints paginate DRF-style (`limit`/`offset`); the client follows `next`
  automatically and concatenates `results` into `Response.data`.
- Applied controls are served by the **compliance** client (the compliance tools),
  not the risk-management tool — a common mismatch.
- A scenario carries `current_level` / `residual_level`; do not call a risk mitigated
  unless it has a linked `applied_controls` entry.
- `ciso_ingest` is best-effort: `"ingested": null` means no reachable KG engine, not a
  data error.

## Related
- `ciso-assistant-compliance-audit` — compliance assessments, frameworks, controls.
- `ciso-assistant-incident-evidence` — incidents, evidence records + blob attachments.
- `mcp-client` — connect to and invoke the MCP server.
