---
name: ciso-assistant-incidents-tools
skill_type: skill
description: >-
  Operate the incidents area of CISO Assistant through the ciso-assistant-api MCP server: find, read, create, update and delete its records with one typed tool per API operation. Use when the task needs the incidents records of a governance, risk and compliance program. Do NOT use for areas owned by the other ciso-assistant skills.
license: MIT
tags: [ciso-assistant, grc, incidents, mcp]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# CISO Assistant: incidents

Each tool maps to exactly one API operation and takes that operation's parameters. Read first (list, then retrieve), and ask for approval before any create, update or delete.

## Rules
- Scope work to one folder or perimeter and cite record ids.
- Never print credentials, tokens or attachment bytes.
- Delete tools (names ending in `_destroy`) need explicit approval and a stated reason.

## Incidents
- `ciso_assistant_api_incidents_list`
- `ciso_assistant_api_incidents_cascade_info_retrieve`
- `ciso_assistant_api_incidents_detection_breakdown_retrieve`
- `ciso_assistant_api_incidents_detection_retrieve`
- `ciso_assistant_api_incidents_export_csv_retrieve`
- `ciso_assistant_api_incidents_export_xlsx_retrieve`
- `ciso_assistant_api_incidents_md_retrieve`
- `ciso_assistant_api_incidents_monthly_metrics_retrieve`
- `ciso_assistant_api_incidents_object_retrieve`
- `ciso_assistant_api_incidents_pdf_retrieve`
- `ciso_assistant_api_incidents_qualifications_breakdown_retrieve`
- `ciso_assistant_api_incidents_retrieve`
- `ciso_assistant_api_incidents_severity_breakdown_retrieve`
- `ciso_assistant_api_incidents_severity_retrieve`
- `ciso_assistant_api_incidents_status_retrieve`
- `ciso_assistant_api_incidents_summary_stats_retrieve`
- `ciso_assistant_api_incidents_batch_action_create`
- `ciso_assistant_api_incidents_create`
- `ciso_assistant_api_incidents_update`
- `ciso_assistant_api_incidents_partial_update`
- `ciso_assistant_api_incidents_destroy`

## Timeline Entries
- `ciso_assistant_api_timeline_entries_list`
- `ciso_assistant_api_timeline_entries_cascade_info_retrieve`
- `ciso_assistant_api_timeline_entries_entry_type_retrieve`
- `ciso_assistant_api_timeline_entries_object_retrieve`
- `ciso_assistant_api_timeline_entries_retrieve`
- `ciso_assistant_api_timeline_entries_batch_action_create`
- `ciso_assistant_api_timeline_entries_create`
- `ciso_assistant_api_timeline_entries_update`
- `ciso_assistant_api_timeline_entries_partial_update`
- `ciso_assistant_api_timeline_entries_destroy`
