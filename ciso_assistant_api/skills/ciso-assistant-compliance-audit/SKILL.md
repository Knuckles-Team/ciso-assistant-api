---
name: ciso-assistant-compliance-audit
description: >-
  Compliance audits on the CISO Assistant platform via the ciso-assistant-api MCP
  server — list and read compliance assessments (audits), their frameworks,
  progress, computed outcome and applied controls, surface requirement gaps, and
  natively ingest audits into the knowledge graph as typed :Audit nodes linked to
  their :Framework. Use when the agent must check an audit's completion, report a
  framework's compliance posture, or map audit state into the KG. Do NOT use for
  risk scenarios/treatment (use ciso-assistant-risk-management) or
  incidents/evidence (use ciso-assistant-incident-evidence).
license: MIT
tags: [ciso-assistant, grc, compliance, audit, mcp]
metadata:
  author: Genius
  version: '0.1.0'
---
# CISO Assistant Compliance Audit

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

\* Provide the token **or** the username/password pair. `MCP_TOOL_MODE`
(`condensed`|`verbose`|`both`) selects the condensed surface (used below) vs. the
one-to-one verbose tools.

## Tools & actions
Prefer the **condensed** tool; it takes `action` + a `params_json` **JSON string**.

| Condensed tool | Key actions |
|----------------|-------------|
| `ciso_assistant_compliance` | `api_compliance_assessments_list`, `api_compliance_assessments_retrieve`, `api_applied_controls_list`, `api_requirement_assessments_list` |
| `ciso_assistant_frameworks_libraries` | `api_frameworks_list`, `api_frameworks_retrieve` |
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
List frameworks (via `ciso_assistant_frameworks_libraries`):
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
