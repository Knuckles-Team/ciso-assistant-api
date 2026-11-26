---
name: ciso-assistant-governance-tools
skill_type: skill
description: >-
  Operate the governance area of CISO Assistant through the ciso-assistant-api MCP server: find, read, create, update and delete its records with one typed tool per API operation. Use when the task needs the governance records of a governance, risk and compliance program. Do NOT use for areas owned by the other ciso-assistant skills.
license: MIT
tags: [ciso-assistant, grc, governance, mcp]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# CISO Assistant: governance

Each tool maps to exactly one API operation and takes that operation's parameters. Read first (list, then retrieve), and ask for approval before any create, update or delete.

## Rules
- Scope work to one folder or perimeter and cite record ids.
- Never print credentials, tokens or attachment bytes.
- Delete tools (names ending in `_destroy`) need explicit approval and a stated reason.

## Steps

1. List the candidate records with `ciso_assistant_api_comments_list`, passing the narrowest filters and a bounded limit. Verify the response holds records from the intended folder or perimeter before going further.
2. Read the exact record with `ciso_assistant_api_comments_retrieve` using an id taken from the list. Verify the returned id equals the id you intend to cite.
3. After operator approval of the stated change, call `ciso_assistant_api_comments_create` once with the approved parameters. Verify the response echoes the submitted fields and returns a new record id.
4. Remove a record only with `ciso_assistant_api_comments_destroy`, after explicit approval and a stated reason. Verify with `ciso_assistant_api_comments_retrieve` that the record is no longer returned.

## Failure recovery

| Failure | Cause | Recovery |
| --- | --- | --- |
| Tool returns an authentication or permission error | Connector credentials are missing, expired or lack rights on this area | Stop and report the error to the operator without printing any token; resume with `ciso_assistant_api_comments_list` after the operator confirms refreshed credentials. |
| List result is empty | Filters or folder scope exclude the records | Call `ciso_assistant_api_comments_list` with the filters removed, then narrow again using the folder id of a record you can already see. |
| Retrieve reports not found | The id is wrong or stale | Call `ciso_assistant_api_comments_list` again and copy the id from the fresh result before calling `ciso_assistant_api_comments_retrieve`. |
| Delete is refused or approval is missing | No explicit approval or reason was recorded | Do not call `ciso_assistant_api_comments_destroy`; ask the operator for approval with a reason, then call `ciso_assistant_api_comments_destroy` with that approval. |

## Comments
- `ciso_assistant_api_comments_list`
- `ciso_assistant_api_comments_cascade_info_retrieve`
- `ciso_assistant_api_comments_object_retrieve`
- `ciso_assistant_api_comments_retrieve`
- `ciso_assistant_api_comments_batch_action_create`
- `ciso_assistant_api_comments_create`
- `ciso_assistant_api_comments_update`
- `ciso_assistant_api_comments_partial_update`
- `ciso_assistant_api_comments_destroy`

## Folders
- `ciso_assistant_api_folders_list`
- `ciso_assistant_api_folders_users_list`
- `ciso_assistant_api_folders_cascade_info_retrieve`
- `ciso_assistant_api_folders_export_retrieve`
- `ciso_assistant_api_folders_get_accessible_objects_retrieve`
- `ciso_assistant_api_folders_ids_retrieve`
- `ciso_assistant_api_folders_my_assignments_retrieve`
- `ciso_assistant_api_folders_object_retrieve`
- `ciso_assistant_api_folders_org_tree_retrieve`
- `ciso_assistant_api_folders_quality_check_retrieve`
- `ciso_assistant_api_folders_retrieve`
- `ciso_assistant_api_folders_batch_action_create`
- `ciso_assistant_api_folders_create`
- `ciso_assistant_api_folders_import_create`
- `ciso_assistant_api_folders_import_dummy_create`
- `ciso_assistant_api_folders_update`
- `ciso_assistant_api_folders_partial_update`
- `ciso_assistant_api_folders_destroy`
- `ciso_assistant_api_folders_quality_check_retrieve_2`

## Journey Steps
- `ciso_assistant_api_journey_steps_list`
- `ciso_assistant_api_journey_steps_cascade_info_retrieve`
- `ciso_assistant_api_journey_steps_object_retrieve`
- `ciso_assistant_api_journey_steps_retrieve`
- `ciso_assistant_api_journey_steps_batch_action_create`
- `ciso_assistant_api_journey_steps_create`
- `ciso_assistant_api_journey_steps_update`
- `ciso_assistant_api_journey_steps_partial_update`
- `ciso_assistant_api_journey_steps_destroy`

## Journeys
- `ciso_assistant_api_journeys_list`
- `ciso_assistant_api_journeys_cascade_info_retrieve`
- `ciso_assistant_api_journeys_dashboard_retrieve`
- `ciso_assistant_api_journeys_object_retrieve`
- `ciso_assistant_api_journeys_retrieve`
- `ciso_assistant_api_journeys_batch_action_create`
- `ciso_assistant_api_journeys_create`
- `ciso_assistant_api_journeys_rename_create`
- `ciso_assistant_api_journeys_upgrade_create`
- `ciso_assistant_api_journeys_update`
- `ciso_assistant_api_journeys_partial_update`
- `ciso_assistant_api_journeys_destroy`

## Organisation Issues
- `ciso_assistant_api_organisation_issues_list`
- `ciso_assistant_api_organisation_issues_cascade_info_retrieve`
- `ciso_assistant_api_organisation_issues_category_retrieve`
- `ciso_assistant_api_organisation_issues_object_retrieve`
- `ciso_assistant_api_organisation_issues_origin_retrieve`
- `ciso_assistant_api_organisation_issues_retrieve`
- `ciso_assistant_api_organisation_issues_status_retrieve`
- `ciso_assistant_api_organisation_issues_batch_action_create`
- `ciso_assistant_api_organisation_issues_create`
- `ciso_assistant_api_organisation_issues_update`
- `ciso_assistant_api_organisation_issues_partial_update`
- `ciso_assistant_api_organisation_issues_destroy`

## Organisation Objectives
- `ciso_assistant_api_organisation_objectives_list`
- `ciso_assistant_api_organisation_objectives_cascade_info_retrieve`
- `ciso_assistant_api_organisation_objectives_health_retrieve`
- `ciso_assistant_api_organisation_objectives_is_active_retrieve`
- `ciso_assistant_api_organisation_objectives_object_retrieve`
- `ciso_assistant_api_organisation_objectives_retrieve`
- `ciso_assistant_api_organisation_objectives_status_retrieve`
- `ciso_assistant_api_organisation_objectives_batch_action_create`
- `ciso_assistant_api_organisation_objectives_create`
- `ciso_assistant_api_organisation_objectives_duplicate_create`
- `ciso_assistant_api_organisation_objectives_update`
- `ciso_assistant_api_organisation_objectives_partial_update`
- `ciso_assistant_api_organisation_objectives_destroy`

## Perimeters
- `ciso_assistant_api_perimeters_list`
- `ciso_assistant_api_perimeters_cascade_info_retrieve`
- `ciso_assistant_api_perimeters_ids_retrieve`
- `ciso_assistant_api_perimeters_lc_status_retrieve`
- `ciso_assistant_api_perimeters_names_retrieve`
- `ciso_assistant_api_perimeters_object_retrieve`
- `ciso_assistant_api_perimeters_quality_check_retrieve`
- `ciso_assistant_api_perimeters_retrieve`
- `ciso_assistant_api_perimeters_batch_action_create`
- `ciso_assistant_api_perimeters_create`
- `ciso_assistant_api_perimeters_update`
- `ciso_assistant_api_perimeters_partial_update`
- `ciso_assistant_api_perimeters_destroy`
- `ciso_assistant_api_perimeters_quality_check_retrieve_2`

## Quick Start
- `ciso_assistant_api_quick_start_create`

## Validation Flows
- `ciso_assistant_api_validation_flows_list`
- `ciso_assistant_api_validation_flows_cascade_info_retrieve`
- `ciso_assistant_api_validation_flows_default_ref_id_retrieve`
- `ciso_assistant_api_validation_flows_linked_models_retrieve`
- `ciso_assistant_api_validation_flows_object_retrieve`
- `ciso_assistant_api_validation_flows_retrieve`
- `ciso_assistant_api_validation_flows_status_retrieve`
- `ciso_assistant_api_validation_flows_batch_action_create`
- `ciso_assistant_api_validation_flows_create`
- `ciso_assistant_api_validation_flows_update`
- `ciso_assistant_api_validation_flows_partial_update`
- `ciso_assistant_api_validation_flows_destroy`
