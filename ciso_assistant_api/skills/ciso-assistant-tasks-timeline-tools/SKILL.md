---
name: ciso-assistant-tasks-timeline-tools
skill_type: skill
description: >-
  Operate the tasks timeline area of CISO Assistant through the ciso-assistant-api MCP server: find, read, create, update and delete its records with one typed tool per API operation. Use when the task needs the tasks timeline records of a governance, risk and compliance program. Do NOT use for areas owned by the other ciso-assistant skills.
license: MIT
tags: [ciso-assistant, grc, tasks-timeline, mcp]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# CISO Assistant: tasks timeline

Each tool maps to exactly one API operation and takes that operation's parameters. Read first (list, then retrieve), and ask for approval before any create, update or delete.

## Rules
- Scope work to one folder or perimeter and cite record ids.
- Never print credentials, tokens or attachment bytes.
- Delete tools (names ending in `_destroy`) need explicit approval and a stated reason.

## Steps

1. List the candidate records with `ciso_assistant_api_answers_list`, passing the narrowest filters and a bounded limit. Verify the response holds records from the intended folder or perimeter before going further.
2. Read the exact record with `ciso_assistant_api_answers_retrieve` using an id taken from the list. Verify the returned id equals the id you intend to cite.
3. After operator approval of the stated change, call `ciso_assistant_api_answers_create` once with the approved parameters. Verify the response echoes the submitted fields and returns a new record id.
4. Remove a record only with `ciso_assistant_api_answers_destroy`, after explicit approval and a stated reason. Verify with `ciso_assistant_api_answers_retrieve` that the record is no longer returned.

## Failure recovery

| Failure | Cause | Recovery |
| --- | --- | --- |
| Tool returns an authentication or permission error | Connector credentials are missing, expired or lack rights on this area | Stop and report the error to the operator without printing any token; resume with `ciso_assistant_api_answers_list` after the operator confirms refreshed credentials. |
| List result is empty | Filters or folder scope exclude the records | Call `ciso_assistant_api_answers_list` with the filters removed, then narrow again using the folder id of a record you can already see. |
| Retrieve reports not found | The id is wrong or stale | Call `ciso_assistant_api_answers_list` again and copy the id from the fresh result before calling `ciso_assistant_api_answers_retrieve`. |
| Delete is refused or approval is missing | No explicit approval or reason was recorded | Do not call `ciso_assistant_api_answers_destroy`; ask the operator for approval with a reason, then call `ciso_assistant_api_answers_destroy` with that approval. |

## Answers
- `ciso_assistant_api_answers_list`
- `ciso_assistant_api_answers_cascade_info_retrieve`
- `ciso_assistant_api_answers_object_retrieve`
- `ciso_assistant_api_answers_retrieve`
- `ciso_assistant_api_answers_batch_action_create`
- `ciso_assistant_api_answers_create`
- `ciso_assistant_api_answers_update`
- `ciso_assistant_api_answers_partial_update`
- `ciso_assistant_api_answers_destroy`

## Campaigns
- `ciso_assistant_api_campaigns_list`
- `ciso_assistant_api_campaigns_cascade_info_retrieve`
- `ciso_assistant_api_campaigns_metrics_retrieve`
- `ciso_assistant_api_campaigns_object_retrieve`
- `ciso_assistant_api_campaigns_retrieve`
- `ciso_assistant_api_campaigns_status_retrieve`
- `ciso_assistant_api_campaigns_batch_action_create`
- `ciso_assistant_api_campaigns_create`
- `ciso_assistant_api_campaigns_update`
- `ciso_assistant_api_campaigns_partial_update`
- `ciso_assistant_api_campaigns_destroy`

## Question Choices
- `ciso_assistant_api_question_choices_list`
- `ciso_assistant_api_question_choices_cascade_info_retrieve`
- `ciso_assistant_api_question_choices_object_retrieve`
- `ciso_assistant_api_question_choices_retrieve`
- `ciso_assistant_api_question_choices_batch_action_create`
- `ciso_assistant_api_question_choices_create`
- `ciso_assistant_api_question_choices_update`
- `ciso_assistant_api_question_choices_partial_update`
- `ciso_assistant_api_question_choices_destroy`

## Questions
- `ciso_assistant_api_questions_list`
- `ciso_assistant_api_questions_cascade_info_retrieve`
- `ciso_assistant_api_questions_object_retrieve`
- `ciso_assistant_api_questions_retrieve`
- `ciso_assistant_api_questions_batch_action_create`
- `ciso_assistant_api_questions_create`
- `ciso_assistant_api_questions_update`
- `ciso_assistant_api_questions_partial_update`
- `ciso_assistant_api_questions_destroy`

## Task Nodes
- `ciso_assistant_api_task_nodes_evidences_list`
- `ciso_assistant_api_task_nodes_list`
- `ciso_assistant_api_task_nodes_cascade_info_retrieve`
- `ciso_assistant_api_task_nodes_object_retrieve`
- `ciso_assistant_api_task_nodes_retrieve`
- `ciso_assistant_api_task_nodes_status_retrieve`
- `ciso_assistant_api_task_nodes_batch_action_create`
- `ciso_assistant_api_task_nodes_create`
- `ciso_assistant_api_task_nodes_remove_evidence_create`
- `ciso_assistant_api_task_nodes_update`
- `ciso_assistant_api_task_nodes_partial_update`
- `ciso_assistant_api_task_nodes_destroy`

## Task Templates
- `ciso_assistant_api_task_templates_list`
- `ciso_assistant_api_task_templates_assigned_to_retrieve`
- `ciso_assistant_api_task_templates_calendar_retrieve`
- `ciso_assistant_api_task_templates_cascade_info_retrieve`
- `ciso_assistant_api_task_templates_export_csv_retrieve`
- `ciso_assistant_api_task_templates_export_xlsx_retrieve`
- `ciso_assistant_api_task_templates_object_retrieve`
- `ciso_assistant_api_task_templates_per_status_retrieve`
- `ciso_assistant_api_task_templates_retrieve`
- `ciso_assistant_api_task_templates_status_retrieve`
- `ciso_assistant_api_task_templates_yearly_review_retrieve`
- `ciso_assistant_api_task_templates_batch_action_create`
- `ciso_assistant_api_task_templates_create`
- `ciso_assistant_api_task_templates_update`
- `ciso_assistant_api_task_templates_partial_update`
- `ciso_assistant_api_task_templates_destroy`
