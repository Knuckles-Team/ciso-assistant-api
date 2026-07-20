---
name: ciso-assistant-operations
description: Operate CISO Assistant governance, risk, compliance, incident, evidence, control, framework, and knowledge-graph workflows through the ciso-assistant-api MCP server. Use when an agent needs to inspect or correlate risk scenarios, assessments, controls, audits, incidents, evidence, frameworks, threats, or vulnerabilities; ingest supported records into epistemic-graph; or plan a governed mutation after explicit approval.
---

# CISO Assistant Operations

Use the action-routed `ciso-assistant-api` MCP tools. Prefer the condensed surface
and treat the generated operation catalog as authoritative when an action is not
listed below.

## Establish the boundary

1. Confirm `CISO_ASSISTANT_URL` identifies the intended instance.
2. Require credentials through `CISO_ASSISTANT_TOKEN_REF`, or both
   `CISO_ASSISTANT_USERNAME_REF` and `CISO_ASSISTANT_PASSWORD_REF`.
3. Use the shared AgentConfig TLS profile. Never disable certificate or hostname
   verification.
4. Start with read-only discovery. Request explicit approval before create,
   update, delete, treatment, acceptance, or status-transition actions.
5. Keep credentials, raw identity attributes, local paths, and attachment bytes
   out of prompts, logs, traces, graph properties, and reports.

## Select the workflow

| Need | Tool | Representative actions |
| --- | --- | --- |
| Risks, threats, vulnerabilities | `ciso_assistant_risk_management` | `api_risk_assessments_list`, `api_risk_scenarios_list`, `api_risk_scenarios_retrieve`, `api_threats_list`, `api_vulnerabilities_list` |
| Audits, controls, requirements | `ciso_assistant_compliance` | `api_compliance_assessments_list`, `api_compliance_assessments_retrieve`, `api_applied_controls_list`, `api_requirement_assessments_list` |
| Frameworks | `ciso_assistant_frameworks_libraries` | `api_frameworks_list`, `api_frameworks_retrieve` |
| Incidents and timelines | `ciso_assistant_incidents` | `api_incidents_list`, `api_incidents_retrieve`, `api_timeline_entries_list` |
| Evidence and attachments | `ciso_assistant_evidence` | `api_evidences_list`, `api_evidences_retrieve`, `api_evidences_attachment_retrieve` |
| Governed KG materialization | `ciso_ingest` | `risk_scenarios`, `risk_assessments`, `applied_controls`, `vulnerabilities`, `compliance_assessments`, `incidents`, `evidences` |

Pass tool parameters as the action router requires. For condensed tools this is
normally an `action` plus a JSON-encoded `params_json` string.

## Execute safely

1. List narrowly with server-side filters and bounded limits.
2. Retrieve exact UUIDs before correlating or mutating records.
3. Preserve source identifiers and provenance, but replace user identity values
   with approved opaque references before persistence.
4. Distinguish observed fields from interpretation. Do not infer mitigation from
   a residual score alone; verify linked controls and their state.
5. Treat compliance progress and computed outcome as separate facts.
6. Treat incident severity/status as source enum values unless the source also
   supplies display labels.
7. Before ingestion, state the target graph and record kinds. The MCP ingestion
   boundary excludes raw attachment bytes; do not imply they were persisted.
8. Verify counts and representative relationships after ingestion. A null or
   zero graph result can indicate an unavailable engine rather than an empty
   source.

## Common read recipes

List recent risk scenarios:

```json
{"ordering":"-updated_at","limit":25}
```

Retrieve one source object:

```json
{"id":"<source_uuid>"}
```

List in-progress compliance assessments:

```json
{"status":"in_progress","ordering":"-updated_at","limit":25}
```

List open incidents by severity:

```json
{"severity":"<source_enum>","status":"open","ordering":"-reported_at","limit":25}
```

Ingest one supported record family with `ciso_ingest`:

```json
{"kind":"risk_scenarios","params_json":"{\"limit\":100}"}
```

## Report results

Report the source instance only as an operator-approved logical label. Include
filters, record counts, unresolved references, ingestion counts, and any policy
gate. Do not include credentials, raw user identifiers, local filesystem paths,
private attachment content, or environment-specific topology.

This skill describes the current human-authored provider surface. Connector
activation in a governed fleet still requires the centrally generated and signed
schema-v2 capability evidence; do not claim certification from this source skill.
