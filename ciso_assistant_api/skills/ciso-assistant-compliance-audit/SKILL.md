---
name: ciso-assistant-compliance-audit
skill_type: skill
description: >-
  Read CISO Assistant compliance audits via the ciso-assistant-api MCP server: assessments, frameworks, progress, computed outcome, applied controls and gaps, plus KG ingest as :Audit nodes. Use to check audit completion or framework posture. Do NOT use for risk (ciso-assistant-risk-management) or incidents (ciso-assistant-incident-evidence).
license: MIT
tags: [ciso-assistant, grc, compliance, audit, mcp]
metadata:
  author: Knuckles-Team
  version: '0.1.0'
---
# CISO Assistant Compliance Audit

Scope: Compliance audits on the CISO Assistant platform via the ciso-assistant-api MCP server — list and read compliance assessments (audits), their frameworks, progress, computed outcome and applied controls, surface requirement gaps, and natively ingest audits into the knowledge graph as typed :Audit nodes linked to their :Framework. Use when the agent must check an audit's completion, report a framework's compliance posture, or map audit state into the KG. Do NOT use for risk scenarios/treatment (use ciso-assistant-risk-management) or incidents/evidence (use ciso-assistant-incident-evidence).

Domain-typed access to the CISO Assistant **compliance** surface — compliance
assessments (audits), frameworks, and applied controls — for posture reporting and
KG mapping. Prefer these tools over raw HTTP; they return the records the ontology
(`:Audit`, `:Framework`, `:Control`) is built on.

## When to use
- List / read compliance assessments and their `progress` + `computed_outcome`.
- Report a framework's compliance posture across assessments.
- List applied controls backing an assessment and their status.
- Ingest audits into the KG as typed `:Audit` nodes (linked to `:Framework`).

## When NOT to use
- Risk assessments, scenarios, treatment decisions → `ciso-assistant-risk-management`.
- Incidents, evidence records and their attachments → `ciso-assistant-incident-evidence`.
- Endpoints with no dedicated tool → `ciso_assistant_api_request`.

## Steps

1. Confirm the instance is reachable by calling `ciso_assistant_api_frameworks_list` with `{"limit":100}`. Verify the response lists frameworks rather than an authentication error.
2. List the audits in scope with `ciso_assistant_api_compliance_assessments_list`, for example `{"status":"in_progress","ordering":"-updated_at"}`. Verify each row carries `progress` and `computed_outcome`.
3. Read one audit with `ciso_assistant_api_compliance_assessments_retrieve` and the assessment UUID. Verify the framework and the progress percent are present before reporting posture.
4. Check the supporting controls with `ciso_assistant_api_applied_controls_list` and `ciso_assistant_api_requirement_assessments_list`. Verify each gap you report names a requirement or control id.
5. Push audits into the graph with `ciso_ingest` and `{"kind":"compliance_assessments","params_json":"{\"limit\":100}"}`. Verify the result shows a non-null `ingested` count.

## Failure recovery

| Failure | Cause | Recovery |
| --- | --- | --- |
| Authentication error from any tool | `CISO_ASSISTANT_URL` is wrong, or neither the token nor the username/password pair is set | Set `CISO_ASSISTANT_URL` and either `CISO_ASSISTANT_TOKEN` or the username/password pair, then call `ciso_assistant_api_frameworks_list` to confirm. |
| Assessment list is empty | The `status` filter does not match any audit | Call `ciso_assistant_api_compliance_assessments_list` with `{"limit":100}` and no filter, then pick the status value seen in the rows. |
| `ciso_ingest` returns `"ingested": null` | No reachable KG engine | Report that nothing was persisted; do not claim graph state until the engine is reachable and `ciso_ingest` returns a count. |

## Prerequisites & environment
Connect via the `mcp-client` skill against the **`ciso-assistant-api`** MCP server.

| Variable | Required | Notes |
|----------|----------|-------|
| `CISO_ASSISTANT_URL` | ✅ | Backend host, e.g. `https://ciso.arpa` |
| `CISO_ASSISTANT_TOKEN` | ✅* | Pre-minted Knox token |
| `CISO_ASSISTANT_USERNAME` / `CISO_ASSISTANT_PASSWORD` | ✅* | Login flow exchanged at `POST /api/iam/login/` |
| `CISO_ASSISTANT_SSL_VERIFY` | optional | TLS verification toggle |

\* Provide the token **or** the username/password pair.

## Tools & actions
Each tool is one API operation and takes that operation's parameters directly.

| Tool group | Tools |
|----------------|-------------|
| Typed tools | `ciso_assistant_api_compliance_assessments_list`, `ciso_assistant_api_compliance_assessments_retrieve`, `ciso_assistant_api_applied_controls_list`, `ciso_assistant_api_requirement_assessments_list` |
| Typed tools | `ciso_assistant_api_frameworks_list`, `ciso_assistant_api_frameworks_retrieve` |
| `ciso_ingest` | native KG push: `kind` = `compliance_assessments` \| `applied_controls` |

## Recipes (`params_json`)
List in-progress compliance assessments:
```json
{"status":"in_progress","ordering":"-updated_at"}
```
Read one assessment (with framework + progress + outcome):
```json
{"id":"<assessment_uuid>"}
```
List frameworks :
```json
{"limit":100}
```
Ingest audits into the KG as typed `:Audit` nodes (`ciso_ingest`):
```json
{"kind":"compliance_assessments","params_json":"{\"limit\":100}"}
```

## Gotchas
- A compliance assessment IS the "audit" — the ontology maps it to `:Audit`; the
  framework it scores against is `:Framework` via `:assessesFramework`.
- `progress` is an integer percent; `computed_outcome` is the roll-up result — read
  both before reporting posture.
- `framework` on an assessment may be a nested object or a bare id; handle both.
- Object ids are UUID strings; pagination is DRF `limit`/`offset` (auto-followed).
- `ciso_ingest` is best-effort: `"ingested": null` means no reachable KG engine.

## Related
- `ciso-assistant-risk-management` — risk assessments, scenarios, controls.
- `ciso-assistant-incident-evidence` — incidents, evidence records + blob attachments.
- `mcp-client` — connect to and invoke the MCP server.
