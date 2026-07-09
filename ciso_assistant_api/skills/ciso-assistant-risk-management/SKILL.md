---
name: ciso-assistant-risk-management
skill_type: skill
description: >-
  Risk management on the CISO Assistant platform via the ciso-assistant-api MCP
  server — list and read risk assessments, risk scenarios, applied controls,
  threats and vulnerabilities, reason about inherent/current/residual levels and
  treatment, and natively ingest them into the knowledge graph as typed
  :RiskScenario / :Control nodes. Use when the agent must triage risk, decide a
  treatment, gate a risk as mitigated on a linked control, or map risk state into
  the KG. Do NOT use for compliance audits/frameworks (use
  ciso-assistant-compliance-audit) or incidents/evidence (use
  ciso-assistant-incident-evidence).
license: MIT
tags: [ciso-assistant, grc, risk, controls, mcp]
metadata:
  author: Genius
  version: '0.1.0'
---
# CISO Assistant Risk Management

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
- Arbitrary endpoints the condensed tools don't cover → the verbose 1:1 tools
  (set `MCP_TOOL_MODE=verbose`).

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

`MCP_TOOL_MODE` (`condensed`|`verbose`|`both`) selects the condensed surface (used
below) vs. the one-to-one verbose tools.

## Tools & actions
Prefer the **condensed** tool; it takes `action` + a `params_json` **JSON string**
whose keys are passed straight to the client method.

| Condensed tool | Key actions |
|----------------|-------------|
| `ciso_assistant_risk_management` | `api_risk_assessments_list`, `api_risk_scenarios_list`, `api_risk_scenarios_retrieve`, `api_threats_list`, `api_vulnerabilities_list` |
| `ciso_assistant_compliance` | `api_applied_controls_list`, `api_applied_controls_retrieve` (controls live under the compliance client) |
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
List applied controls that are still to-do (via `ciso_assistant_compliance`):
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
- Applied controls are served by the **compliance** client (`ciso_assistant_compliance`),
  not the risk-management tool — a common mismatch.
- A scenario carries `current_level` / `residual_level`; do not call a risk mitigated
  unless it has a linked `applied_controls` entry.
- `ciso_ingest` is best-effort: `"ingested": null` means no reachable KG engine, not a
  data error.

## Related
- `ciso-assistant-compliance-audit` — compliance assessments, frameworks, controls.
- `ciso-assistant-incident-evidence` — incidents, evidence records + blob attachments.
- `mcp-client` — connect to and invoke the MCP server.
