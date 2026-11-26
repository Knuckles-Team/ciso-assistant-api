---
name: ciso-assistant-analytics-metrology-tools
skill_type: skill
description: >-
  Operate the analytics metrology area of CISO Assistant through the ciso-assistant-api MCP server: find, read, create, update and delete its records with one typed tool per API operation. Use when the task needs the analytics metrology records of a governance, risk and compliance program. Do NOT use for areas owned by the other ciso-assistant skills.
license: MIT
tags: [ciso-assistant, grc, analytics-metrology, mcp]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# CISO Assistant: analytics metrology

Each tool maps to exactly one API operation and takes that operation's parameters. Read first (list, then retrieve), and ask for approval before any create, update or delete.

## Rules
- Scope work to one folder or perimeter and cite record ids.
- Never print credentials, tokens or attachment bytes.
- Delete tools (names ending in `_destroy`) need explicit approval and a stated reason.

## Steps

1. List the candidate records with `ciso_assistant_api_metrology_builtin_metric_samples_list`, passing the narrowest filters and a bounded limit. Verify the response holds records from the intended folder or perimeter before going further.
2. Read the exact record with `ciso_assistant_api_metrology_builtin_metric_samples_retrieve` using an id taken from the list. Verify the returned id equals the id you intend to cite.
3. After operator approval of the stated change, call `ciso_assistant_api_metrology_builtin_metric_samples_create` once with the approved parameters. Verify the response echoes the submitted fields and returns a new record id.
4. Remove a record only with `ciso_assistant_api_metrology_builtin_metric_samples_destroy`, after explicit approval and a stated reason. Verify with `ciso_assistant_api_metrology_builtin_metric_samples_retrieve` that the record is no longer returned.

## Failure recovery

| Failure | Cause | Recovery |
| --- | --- | --- |
| Tool returns an authentication or permission error | Connector credentials are missing, expired or lack rights on this area | Stop and report the error to the operator without printing any token; resume with `ciso_assistant_api_metrology_builtin_metric_samples_list` after the operator confirms refreshed credentials. |
| List result is empty | Filters or folder scope exclude the records | Call `ciso_assistant_api_metrology_builtin_metric_samples_list` with the filters removed, then narrow again using the folder id of a record you can already see. |
| Retrieve reports not found | The id is wrong or stale | Call `ciso_assistant_api_metrology_builtin_metric_samples_list` again and copy the id from the fresh result before calling `ciso_assistant_api_metrology_builtin_metric_samples_retrieve`. |
| Delete is refused or approval is missing | No explicit approval or reason was recorded | Do not call `ciso_assistant_api_metrology_builtin_metric_samples_destroy`; ask the operator for approval with a reason, then call `ciso_assistant_api_metrology_builtin_metric_samples_destroy` with that approval. |

## Agg Data
- `ciso_assistant_api_agg_data_retrieve`

## Analytics
- `ciso_assistant_api_analytics_export_xlsx_retrieve`

## Composer Data
- `ciso_assistant_api_composer_data_retrieve`

## Get Audits Metrics
- `ciso_assistant_api_get_audits_metrics_retrieve`

## Get Combined Assessments Status
- `ciso_assistant_api_get_combined_assessments_status_retrieve`

## Get Counters
- `ciso_assistant_api_get_counters_retrieve`

## Get Governance Calendar Data
- `ciso_assistant_api_get_governance_calendar_data_retrieve`

## Get Metrics
- `ciso_assistant_api_get_metrics_retrieve`

## Metrology Builtin Metric Samples
- `ciso_assistant_api_metrology_builtin_metric_samples_list`
- `ciso_assistant_api_metrology_builtin_metric_samples_cascade_info_retrieve`
- `ciso_assistant_api_metrology_builtin_metric_samples_for_object_retrieve`
- `ciso_assistant_api_metrology_builtin_metric_samples_object_retrieve`
- `ciso_assistant_api_metrology_builtin_metric_samples_retrieve`
- `ciso_assistant_api_metrology_builtin_metric_samples_supported_models_retrieve`
- `ciso_assistant_api_metrology_builtin_metric_samples_batch_action_create`
- `ciso_assistant_api_metrology_builtin_metric_samples_create`
- `ciso_assistant_api_metrology_builtin_metric_samples_refresh_create`
- `ciso_assistant_api_metrology_builtin_metric_samples_update`
- `ciso_assistant_api_metrology_builtin_metric_samples_partial_update`
- `ciso_assistant_api_metrology_builtin_metric_samples_destroy`

## Metrology Custom Metric Samples
- `ciso_assistant_api_metrology_custom_metric_samples_list`
- `ciso_assistant_api_metrology_custom_metric_samples_cascade_info_retrieve`
- `ciso_assistant_api_metrology_custom_metric_samples_object_retrieve`
- `ciso_assistant_api_metrology_custom_metric_samples_retrieve`
- `ciso_assistant_api_metrology_custom_metric_samples_batch_action_create`
- `ciso_assistant_api_metrology_custom_metric_samples_create`
- `ciso_assistant_api_metrology_custom_metric_samples_update`
- `ciso_assistant_api_metrology_custom_metric_samples_partial_update`
- `ciso_assistant_api_metrology_custom_metric_samples_destroy`

## Metrology Dashboard Widgets
- `ciso_assistant_api_metrology_dashboard_widgets_list`
- `ciso_assistant_api_metrology_dashboard_widgets_aggregation_retrieve`
- `ciso_assistant_api_metrology_dashboard_widgets_cascade_info_retrieve`
- `ciso_assistant_api_metrology_dashboard_widgets_chart_type_retrieve`
- `ciso_assistant_api_metrology_dashboard_widgets_object_retrieve`
- `ciso_assistant_api_metrology_dashboard_widgets_retrieve`
- `ciso_assistant_api_metrology_dashboard_widgets_time_range_retrieve`
- `ciso_assistant_api_metrology_dashboard_widgets_batch_action_create`
- `ciso_assistant_api_metrology_dashboard_widgets_create`
- `ciso_assistant_api_metrology_dashboard_widgets_update`
- `ciso_assistant_api_metrology_dashboard_widgets_partial_update`
- `ciso_assistant_api_metrology_dashboard_widgets_destroy`

## Metrology Dashboards
- `ciso_assistant_api_metrology_dashboards_list`
- `ciso_assistant_api_metrology_dashboards_cascade_info_retrieve`
- `ciso_assistant_api_metrology_dashboards_object_retrieve`
- `ciso_assistant_api_metrology_dashboards_retrieve`
- `ciso_assistant_api_metrology_dashboards_batch_action_create`
- `ciso_assistant_api_metrology_dashboards_create`
- `ciso_assistant_api_metrology_dashboards_update`
- `ciso_assistant_api_metrology_dashboards_partial_update`
- `ciso_assistant_api_metrology_dashboards_destroy`

## Metrology Metric Definitions
- `ciso_assistant_api_metrology_metric_definitions_list`
- `ciso_assistant_api_metrology_metric_definitions_cascade_info_retrieve`
- `ciso_assistant_api_metrology_metric_definitions_category_retrieve`
- `ciso_assistant_api_metrology_metric_definitions_object_retrieve`
- `ciso_assistant_api_metrology_metric_definitions_provider_retrieve`
- `ciso_assistant_api_metrology_metric_definitions_retrieve`
- `ciso_assistant_api_metrology_metric_definitions_batch_action_create`
- `ciso_assistant_api_metrology_metric_definitions_create`
- `ciso_assistant_api_metrology_metric_definitions_update`
- `ciso_assistant_api_metrology_metric_definitions_partial_update`
- `ciso_assistant_api_metrology_metric_definitions_destroy`

## Metrology Metric Instances
- `ciso_assistant_api_metrology_metric_instances_list`
- `ciso_assistant_api_metrology_metric_instances_cascade_info_retrieve`
- `ciso_assistant_api_metrology_metric_instances_collection_frequency_retrieve`
- `ciso_assistant_api_metrology_metric_instances_object_retrieve`
- `ciso_assistant_api_metrology_metric_instances_retrieve`
- `ciso_assistant_api_metrology_metric_instances_status_retrieve`
- `ciso_assistant_api_metrology_metric_instances_batch_action_create`
- `ciso_assistant_api_metrology_metric_instances_create`
- `ciso_assistant_api_metrology_metric_instances_update`
- `ciso_assistant_api_metrology_metric_instances_partial_update`
- `ciso_assistant_api_metrology_metric_instances_destroy`
