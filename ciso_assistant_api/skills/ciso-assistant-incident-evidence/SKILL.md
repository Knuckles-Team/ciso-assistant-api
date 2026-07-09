---
name: ciso-assistant-incident-evidence
skill_type: skill
description: >-
  Incident response and evidence handling on the CISO Assistant platform via the
  ciso-assistant-api MCP server — list and read security incidents (severity,
  status, detection and resolution timeline) and evidence records, ingest
  incidents into the knowledge graph as typed :Incident nodes, and store evidence
  attachment file bytes as content-addressed :Blob / :MediaAsset. Use when the
  agent must triage incidents, link affected assets/controls, or make evidence
  files durable and queryable in the KG. Do NOT use for risk scenarios/treatment
  (use ciso-assistant-risk-management) or compliance audits/frameworks (use
  ciso-assistant-compliance-audit).
license: MIT
tags: [ciso-assistant, grc, incident, evidence, blob, mcp]
metadata:
  author: Genius
  version: '0.1.0'
---
# CISO Assistant Incident & Evidence

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

\* Provide the token **or** the username/password pair. Blob ingestion also needs a
reachable epistemic-graph engine (best-effort; no-ops without one).

## Tools & actions
Prefer the **condensed** tool; it takes `action` + a `params_json` **JSON string**.

| Condensed tool | Key actions |
|----------------|-------------|
| `ciso_assistant_incidents` | `api_incidents_list`, `api_incidents_retrieve`, `api_incidents_severity_retrieve`, `api_timeline_entries_list` |
| `ciso_assistant_evidence` | `api_evidences_list`, `api_evidences_retrieve`, `api_evidences_attachment_retrieve` |
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
- Evidence bytes come from `api_evidences_attachment_retrieve` (id) — only records
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
