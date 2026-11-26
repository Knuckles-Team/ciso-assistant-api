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

## Steps

1. List the candidate records with `ciso_assistant_api_incidents_list`, passing the narrowest filters and a bounded limit. Verify the response holds records from the intended folder or perimeter before going further.
2. Read the exact record with `ciso_assistant_api_incidents_retrieve` using an id taken from the list. Verify the returned id equals the id you intend to cite.
3. After operator approval of the stated change, call `ciso_assistant_api_incidents_create` once with the approved parameters. Verify the response echoes the submitted fields and returns a new record id.
4. Remove a record only with `ciso_assistant_api_incidents_destroy`, after explicit approval and a stated reason. Verify with `ciso_assistant_api_incidents_retrieve` that the record is no longer returned.

## Failure recovery

| Failure | Cause | Recovery |
| --- | --- | --- |
| Tool returns an authentication or permission error | Connector credentials are missing, expired or lack rights on this area | Stop and report the error to the operator without printing any token; resume with `ciso_assistant_api_incidents_list` after the operator confirms refreshed credentials. |
| List result is empty | Filters or folder scope exclude the records | Call `ciso_assistant_api_incidents_list` with the filters removed, then narrow again using the folder id of a record you can already see. |
| Retrieve reports not found | The id is wrong or stale | Call `ciso_assistant_api_incidents_list` again and copy the id from the fresh result before calling `ciso_assistant_api_incidents_retrieve`. |
| Delete is refused or approval is missing | No explicit approval or reason was recorded | Do not call `ciso_assistant_api_incidents_destroy`; ask the operator for approval with a reason, then call `ciso_assistant_api_incidents_destroy` with that approval. |

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
