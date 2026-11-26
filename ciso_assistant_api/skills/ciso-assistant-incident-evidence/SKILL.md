---
name: ciso-assistant-incident-evidence
skill_type: skill
description: >-
  Handle CISO Assistant incidents and evidence via the ciso-assistant-api MCP server: read incidents (severity, status, timeline) and evidence, ingest :Incident nodes, store attachments as :Blob. Use to triage incidents or make evidence queryable. Do NOT use for risk (ciso-assistant-risk-management) or audits (ciso-assistant-compliance-audit).
license: MIT
tags: [ciso-assistant, grc, incident, evidence, blob, mcp]
metadata:
  author: Knuckles-Team
  version: '0.1.0'
---
# CISO Assistant Incident & Evidence

Scope: Incident response and evidence handling on the CISO Assistant platform via the ciso-assistant-api MCP server — list and read security incidents (severity, status, detection and resolution timeline) and evidence records, ingest incidents into the knowledge graph as typed :Incident nodes, and store evidence attachment file bytes as content-addressed :Blob / :MediaAsset. Use when the agent must triage incidents, link affected assets/controls, or make evidence files durable and queryable in the KG. Do NOT use for risk scenarios/treatment (use ciso-assistant-risk-management) or compliance audits/frameworks (use ciso-assistant-compliance-audit).

Domain-typed access to the CISO Assistant **incident** and **evidence** surfaces —
security incidents plus their evidence records and file attachments — for response
and durable KG capture. Prefer these tools over raw HTTP; they return the records
the ontology (`:Incident`, `:Evidence`, `:Asset`) is built on, and evidence files
land as reusable `:Blob` / `:MediaAsset` nodes.

## When to use
- List / triage incidents by severity and status; read detection/resolution times.
- Link an incident's affected assets and applied controls.
- List evidence records and their attachment/expiry.
- Ingest incidents into the KG (`:Incident`) and store evidence file bytes as blobs.

## When NOT to use
- Risk assessments, scenarios, treatment decisions → `ciso-assistant-risk-management`.
- Compliance assessments (audits), frameworks → `ciso-assistant-compliance-audit`.
- Endpoints with no dedicated tool → `ciso_assistant_api_request`.

## Steps

1. List the incidents in scope with `ciso_assistant_api_incidents_list`, for example `{"severity":"1","status":"open","ordering":"-reported_at"}`. Verify each row has a severity code and a status code.
2. Read one incident with `ciso_assistant_api_incidents_retrieve` and its UUID. Verify the detection and resolution times are present, using `ciso_assistant_api_timeline_entries_list` if the incident omits them.
3. List evidence with `ciso_assistant_api_evidences_list`. Verify which records have an `attachment` field set, since only those have a file.
4. Fetch an attachment with `ciso_assistant_api_evidences_attachment_retrieve` and the evidence id. Verify the response carries file content for that record.
5. Persist records with `ciso_ingest`, using `{"kind":"incidents"}` or `{"kind":"evidences","ingest_attachments":true}`. Verify the result shows non-null `ingested` and `stored` counts.

## Failure recovery

| Failure | Cause | Recovery |
| --- | --- | --- |
| Authentication error from any tool | `CISO_ASSISTANT_URL` is wrong, or neither the token nor the username/password pair is set | Set `CISO_ASSISTANT_URL` and either `CISO_ASSISTANT_TOKEN` or the username/password pair, then call `ciso_assistant_api_incidents_list` to confirm. |
| Incident list is empty | Severity or status was passed as a display string instead of the enum code | Call `ciso_assistant_api_incidents_list` with `{"limit":50}` and reuse the severity and status codes shown in the rows. |
| Attachment fetch returns no file | The evidence record has no `attachment` set | Skip that record and pick one from `ciso_assistant_api_evidences_list` whose `attachment` is present. |
| `ciso_ingest` returns `"ingested": null` or `"stored": 0` | No reachable KG engine | Report that nothing was persisted; do not claim graph state until the engine is reachable and `ciso_ingest` returns a count. |

## Prerequisites & environment
Connect via the `mcp-client` skill against the **`ciso-assistant-api`** MCP server.

| Variable | Required | Notes |
|----------|----------|-------|
| `CISO_ASSISTANT_URL` | ✅ | Backend host, e.g. `https://ciso.arpa` |
| `CISO_ASSISTANT_TOKEN` | ✅* | Pre-minted Knox token |
| `CISO_ASSISTANT_USERNAME` / `CISO_ASSISTANT_PASSWORD` | ✅* | Login flow exchanged at `POST /api/iam/login/` |
| `CISO_ASSISTANT_SSL_VERIFY` | optional | TLS verification toggle |

\* Provide the token **or** the username/password pair. Blob ingestion also needs a
reachable medulla engine (best-effort; no-ops without one).

## Tools & actions
Each tool is one API operation and takes that operation's parameters directly.

| Tool group | Tools |
|----------------|-------------|
| Typed tools | `ciso_assistant_api_incidents_list`, `ciso_assistant_api_incidents_retrieve`, `ciso_assistant_api_incidents_severity_retrieve`, `ciso_assistant_api_timeline_entries_list` |
| Typed tools | `ciso_assistant_api_evidences_list`, `ciso_assistant_api_evidences_retrieve`, `ciso_assistant_api_evidences_attachment_retrieve` |
| `ciso_ingest` | native KG push: `kind` = `incidents` \| `evidences` (evidences also stores attachment blobs when `ingest_attachments=true`) |

## Recipes (`params_json`)
List high-severity open incidents:
```json
{"severity":"1","status":"open","ordering":"-reported_at"}
```
Read one incident (assets, controls, timeline):
```json
{"id":"<incident_uuid>"}
```
List evidence records with attachments:
```json
{"limit":50}
```
Ingest incidents into the KG as typed `:Incident` nodes (`ciso_ingest`):
```json
{"kind":"incidents","params_json":"{\"limit\":100}"}
```
Ingest evidences AND store their attachment file blobs (`ciso_ingest`):
```json
{"kind":"evidences","ingest_attachments":true,"params_json":"{\"limit\":50}"}
```

## Gotchas
- Incident `severity` and `status` are enum codes (e.g. severity `1` = highest),
  not display strings.
- Evidence bytes come from `ciso_assistant_api_evidences_attachment_retrieve` (id) — only records
  whose `attachment` field is set have a file; skip the rest.
- Blob ingestion is content-addressed and deduped; re-ingesting the same file is a
  cheap no-op, not a duplicate.
- `ciso_ingest kind=evidences` writes the evidence text as a `:Document` and, with
  `ingest_attachments=true`, the file as a `:Blob` / `:MediaAsset`; link them via
  `:hasAttachment`.
- Everything KG-side is best-effort: `"ingested": null` / `"stored": 0` means no
  reachable engine, not a data error.

## Related
- `ciso-assistant-risk-management` — risk assessments, scenarios, controls.
- `ciso-assistant-compliance-audit` — compliance assessments, frameworks, controls.
- `mcp-client` — connect to and invoke the MCP server.
