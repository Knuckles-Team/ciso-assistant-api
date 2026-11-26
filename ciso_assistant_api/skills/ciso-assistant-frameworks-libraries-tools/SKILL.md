---
name: ciso-assistant-frameworks-libraries-tools
skill_type: skill
description: >-
  Operate the frameworks libraries area of CISO Assistant through the ciso-assistant-api MCP server: find, read, create, update and delete its records with one typed tool per API operation. Use when the task needs the frameworks libraries records of a governance, risk and compliance program. Do NOT use for areas owned by the other ciso-assistant skills.
license: MIT
tags: [ciso-assistant, grc, frameworks-libraries, mcp]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# CISO Assistant: frameworks libraries

Each tool maps to exactly one API operation and takes that operation's parameters. Read first (list, then retrieve), and ask for approval before any create, update or delete.

## Rules
- Scope work to one folder or perimeter and cite record ids.
- Never print credentials, tokens or attachment bytes.
- Delete tools (names ending in `_destroy`) need explicit approval and a stated reason.

## Steps

1. List the candidate records with `ciso_assistant_api_filtering_labels_list`, passing the narrowest filters and a bounded limit. Verify the response holds records from the intended folder or perimeter before going further.
2. Read the exact record with `ciso_assistant_api_filtering_labels_retrieve` using an id taken from the list. Verify the returned id equals the id you intend to cite.
3. After operator approval of the stated change, call `ciso_assistant_api_filtering_labels_create` once with the approved parameters. Verify the response echoes the submitted fields and returns a new record id.
4. Remove a record only with `ciso_assistant_api_filtering_labels_destroy`, after explicit approval and a stated reason. Verify with `ciso_assistant_api_filtering_labels_retrieve` that the record is no longer returned.

## Failure recovery

| Failure | Cause | Recovery |
| --- | --- | --- |
| Tool returns an authentication or permission error | Connector credentials are missing, expired or lack rights on this area | Stop and report the error to the operator without printing any token; resume with `ciso_assistant_api_filtering_labels_list` after the operator confirms refreshed credentials. |
| List result is empty | Filters or folder scope exclude the records | Call `ciso_assistant_api_filtering_labels_list` with the filters removed, then narrow again using the folder id of a record you can already see. |
| Retrieve reports not found | The id is wrong or stale | Call `ciso_assistant_api_filtering_labels_list` again and copy the id from the fresh result before calling `ciso_assistant_api_filtering_labels_retrieve`. |
| Delete is refused or approval is missing | No explicit approval or reason was recorded | Do not call `ciso_assistant_api_filtering_labels_destroy`; ask the operator for approval with a reason, then call `ciso_assistant_api_filtering_labels_destroy` with that approval. |

## Filtering Labels
- `ciso_assistant_api_filtering_labels_list`
- `ciso_assistant_api_filtering_labels_cascade_info_retrieve`
- `ciso_assistant_api_filtering_labels_object_retrieve`
- `ciso_assistant_api_filtering_labels_retrieve`
- `ciso_assistant_api_filtering_labels_batch_action_create`
- `ciso_assistant_api_filtering_labels_create`
- `ciso_assistant_api_filtering_labels_update`
- `ciso_assistant_api_filtering_labels_partial_update`
- `ciso_assistant_api_filtering_labels_destroy`

## Frameworks
- `ciso_assistant_api_frameworks_list`
- `ciso_assistant_api_frameworks_create`

## Frameworks Batch Action
- `ciso_assistant_api_frameworks_batch_action_create`

## Frameworks Id
- `ciso_assistant_api_frameworks_cascade_info_retrieve`
- `ciso_assistant_api_frameworks_excel_template_retrieve`
- `ciso_assistant_api_frameworks_export_yaml_retrieve`
- `ciso_assistant_api_frameworks_mapping_stats_retrieve`
- `ciso_assistant_api_frameworks_mappings_retrieve`
- `ciso_assistant_api_frameworks_object_retrieve`
- `ciso_assistant_api_frameworks_report_retrieve`
- `ciso_assistant_api_frameworks_retrieve`
- `ciso_assistant_api_frameworks_serve_image_retrieve`
- `ciso_assistant_api_frameworks_tree_retrieve`
- `ciso_assistant_api_frameworks_discard_draft_create`
- `ciso_assistant_api_frameworks_duplicate_create`
- `ciso_assistant_api_frameworks_publish_draft_create`
- `ciso_assistant_api_frameworks_publish_draft_preview_create`
- `ciso_assistant_api_frameworks_start_editing_create`
- `ciso_assistant_api_frameworks_upload_image_create`
- `ciso_assistant_api_frameworks_update`
- `ciso_assistant_api_frameworks_partial_update`
- `ciso_assistant_api_frameworks_save_draft_partial_update`
- `ciso_assistant_api_frameworks_destroy`

## Frameworks Names
- `ciso_assistant_api_frameworks_names_retrieve`

## Frameworks Provider
- `ciso_assistant_api_frameworks_provider_retrieve`

## Frameworks Used
- `ciso_assistant_api_frameworks_used_retrieve`

## Library Filtering Labels
- `ciso_assistant_api_library_filtering_labels_list`
- `ciso_assistant_api_library_filtering_labels_cascade_info_retrieve`
- `ciso_assistant_api_library_filtering_labels_object_retrieve`
- `ciso_assistant_api_library_filtering_labels_retrieve`
- `ciso_assistant_api_library_filtering_labels_batch_action_create`
- `ciso_assistant_api_library_filtering_labels_create`
- `ciso_assistant_api_library_filtering_labels_update`
- `ciso_assistant_api_library_filtering_labels_partial_update`
- `ciso_assistant_api_library_filtering_labels_destroy`

## Loaded Libraries
- `ciso_assistant_api_loaded_libraries_list`
- `ciso_assistant_api_loaded_libraries_available_updates_retrieve`
- `ciso_assistant_api_loaded_libraries_cascade_info_retrieve`
- `ciso_assistant_api_loaded_libraries_content_retrieve`
- `ciso_assistant_api_loaded_libraries_object_retrieve`
- `ciso_assistant_api_loaded_libraries_retrieve`
- `ciso_assistant_api_loaded_libraries_tree_retrieve`
- `ciso_assistant_api_loaded_libraries_update_retrieve`
- `ciso_assistant_api_loaded_libraries_batch_action_create`
- `ciso_assistant_api_loaded_libraries_create`
- `ciso_assistant_api_loaded_libraries_update`
- `ciso_assistant_api_loaded_libraries_partial_update`
- `ciso_assistant_api_loaded_libraries_destroy`

## Presets
- `ciso_assistant_api_presets_list`
- `ciso_assistant_api_presets_cascade_info_retrieve`
- `ciso_assistant_api_presets_object_retrieve`
- `ciso_assistant_api_presets_retrieve`
- `ciso_assistant_api_presets_apply_create`
- `ciso_assistant_api_presets_batch_action_create`
- `ciso_assistant_api_presets_create`
- `ciso_assistant_api_presets_create_blank_create`
- `ciso_assistant_api_presets_discard_draft_create`
- `ciso_assistant_api_presets_duplicate_create`
- `ciso_assistant_api_presets_publish_draft_create`
- `ciso_assistant_api_presets_publish_draft_preview_create`
- `ciso_assistant_api_presets_start_editing_create`
- `ciso_assistant_api_presets_update`
- `ciso_assistant_api_presets_partial_update`
- `ciso_assistant_api_presets_save_draft_partial_update`
- `ciso_assistant_api_presets_destroy`

## Stored Libraries
- `ciso_assistant_api_stored_libraries_list`
- `ciso_assistant_api_stored_libraries_cascade_info_retrieve`
- `ciso_assistant_api_stored_libraries_content_retrieve`
- `ciso_assistant_api_stored_libraries_locale_retrieve`
- `ciso_assistant_api_stored_libraries_object_retrieve`
- `ciso_assistant_api_stored_libraries_object_type_retrieve`
- `ciso_assistant_api_stored_libraries_provider_retrieve`
- `ciso_assistant_api_stored_libraries_retrieve`
- `ciso_assistant_api_stored_libraries_tree_retrieve`
- `ciso_assistant_api_stored_libraries_batch_action_create`
- `ciso_assistant_api_stored_libraries_create`
- `ciso_assistant_api_stored_libraries_import_create`
- `ciso_assistant_api_stored_libraries_unload_create`
- `ciso_assistant_api_stored_libraries_upload_create`
- `ciso_assistant_api_stored_libraries_update`
- `ciso_assistant_api_stored_libraries_partial_update`
- `ciso_assistant_api_stored_libraries_destroy`

## Terminologies
- `ciso_assistant_api_terminologies_list`
- `ciso_assistant_api_terminologies_cascade_info_retrieve`
- `ciso_assistant_api_terminologies_field_path_retrieve`
- `ciso_assistant_api_terminologies_object_retrieve`
- `ciso_assistant_api_terminologies_retrieve`
- `ciso_assistant_api_terminologies_batch_action_create`
- `ciso_assistant_api_terminologies_create`
- `ciso_assistant_api_terminologies_update`
- `ciso_assistant_api_terminologies_partial_update`
- `ciso_assistant_api_terminologies_destroy`
