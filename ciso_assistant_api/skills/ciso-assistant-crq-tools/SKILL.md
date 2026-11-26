---
name: ciso-assistant-crq-tools
skill_type: skill
description: >-
  Operate the crq area of CISO Assistant through the ciso-assistant-api MCP server: find, read, create, update and delete its records with one typed tool per API operation. Use when the task needs the crq records of a governance, risk and compliance program. Do NOT use for areas owned by the other ciso-assistant skills.
license: MIT
tags: [ciso-assistant, grc, crq, mcp]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# CISO Assistant: crq

Each tool maps to exactly one API operation and takes that operation's parameters. Read first (list, then retrieve), and ask for approval before any create, update or delete.

## Rules
- Scope work to one folder or perimeter and cite record ids.
- Never print credentials, tokens or attachment bytes.
- Delete tools (names ending in `_destroy`) need explicit approval and a stated reason.

## Steps

1. List the candidate records with `ciso_assistant_api_crq_quantitative_risk_hypotheses_list`, passing the narrowest filters and a bounded limit. Verify the response holds records from the intended folder or perimeter before going further.
2. Read the exact record with `ciso_assistant_api_crq_quantitative_risk_hypotheses_retrieve` using an id taken from the list. Verify the returned id equals the id you intend to cite.
3. After operator approval of the stated change, call `ciso_assistant_api_crq_quantitative_risk_hypotheses_create` once with the approved parameters. Verify the response echoes the submitted fields and returns a new record id.
4. Remove a record only with `ciso_assistant_api_crq_quantitative_risk_hypotheses_destroy`, after explicit approval and a stated reason. Verify with `ciso_assistant_api_crq_quantitative_risk_hypotheses_retrieve` that the record is no longer returned.

## Failure recovery

| Failure | Cause | Recovery |
| --- | --- | --- |
| Tool returns an authentication or permission error | Connector credentials are missing, expired or lack rights on this area | Stop and report the error to the operator without printing any token; resume with `ciso_assistant_api_crq_quantitative_risk_hypotheses_list` after the operator confirms refreshed credentials. |
| List result is empty | Filters or folder scope exclude the records | Call `ciso_assistant_api_crq_quantitative_risk_hypotheses_list` with the filters removed, then narrow again using the folder id of a record you can already see. |
| Retrieve reports not found | The id is wrong or stale | Call `ciso_assistant_api_crq_quantitative_risk_hypotheses_list` again and copy the id from the fresh result before calling `ciso_assistant_api_crq_quantitative_risk_hypotheses_retrieve`. |
| Delete is refused or approval is missing | No explicit approval or reason was recorded | Do not call `ciso_assistant_api_crq_quantitative_risk_hypotheses_destroy`; ask the operator for approval with a reason, then call `ciso_assistant_api_crq_quantitative_risk_hypotheses_destroy` with that approval. |

## Crq Quantitative Risk Hypotheses
- `ciso_assistant_api_crq_quantitative_risk_hypotheses_list`
- `ciso_assistant_api_crq_quantitative_risk_hypotheses_cascade_info_retrieve`
- `ciso_assistant_api_crq_quantitative_risk_hypotheses_default_ref_id_retrieve`
- `ciso_assistant_api_crq_quantitative_risk_hypotheses_lec_retrieve`
- `ciso_assistant_api_crq_quantitative_risk_hypotheses_object_retrieve`
- `ciso_assistant_api_crq_quantitative_risk_hypotheses_retrieve`
- `ciso_assistant_api_crq_quantitative_risk_hypotheses_risk_stage_retrieve`
- `ciso_assistant_api_crq_quantitative_risk_hypotheses_run_simulation_retrieve`
- `ciso_assistant_api_crq_quantitative_risk_hypotheses_batch_action_create`
- `ciso_assistant_api_crq_quantitative_risk_hypotheses_create`
- `ciso_assistant_api_crq_quantitative_risk_hypotheses_update`
- `ciso_assistant_api_crq_quantitative_risk_hypotheses_partial_update`
- `ciso_assistant_api_crq_quantitative_risk_hypotheses_destroy`

## Crq Quantitative Risk Scenarios
- `ciso_assistant_api_crq_quantitative_risk_scenarios_list`
- `ciso_assistant_api_crq_quantitative_risk_scenarios_cascade_info_retrieve`
- `ciso_assistant_api_crq_quantitative_risk_scenarios_default_ref_id_retrieve`
- `ciso_assistant_api_crq_quantitative_risk_scenarios_lec_retrieve`
- `ciso_assistant_api_crq_quantitative_risk_scenarios_object_retrieve`
- `ciso_assistant_api_crq_quantitative_risk_scenarios_priority_retrieve`
- `ciso_assistant_api_crq_quantitative_risk_scenarios_retrieve`
- `ciso_assistant_api_crq_quantitative_risk_scenarios_status_retrieve`
- `ciso_assistant_api_crq_quantitative_risk_scenarios_batch_action_create`
- `ciso_assistant_api_crq_quantitative_risk_scenarios_create`
- `ciso_assistant_api_crq_quantitative_risk_scenarios_update`
- `ciso_assistant_api_crq_quantitative_risk_scenarios_partial_update`
- `ciso_assistant_api_crq_quantitative_risk_scenarios_destroy`

## Crq Quantitative Risk Studies
- `ciso_assistant_api_crq_quantitative_risk_studies_action_plan_budget_overview_list`
- `ciso_assistant_api_crq_quantitative_risk_studies_action_plan_list`
- `ciso_assistant_api_crq_quantitative_risk_studies_list`
- `ciso_assistant_api_crq_quantitative_risk_studies_ale_comparison_retrieve`
- `ciso_assistant_api_crq_quantitative_risk_studies_cascade_info_retrieve`
- `ciso_assistant_api_crq_quantitative_risk_studies_combined_ale_retrieve`
- `ciso_assistant_api_crq_quantitative_risk_studies_combined_lec_retrieve`
- `ciso_assistant_api_crq_quantitative_risk_studies_distribution_model_retrieve`
- `ciso_assistant_api_crq_quantitative_risk_studies_executive_summary_retrieve`
- `ciso_assistant_api_crq_quantitative_risk_studies_key_metrics_retrieve`
- `ciso_assistant_api_crq_quantitative_risk_studies_object_retrieve`
- `ciso_assistant_api_crq_quantitative_risk_studies_retrieve`
- `ciso_assistant_api_crq_quantitative_risk_studies_status_retrieve`
- `ciso_assistant_api_crq_quantitative_risk_studies_batch_action_create`
- `ciso_assistant_api_crq_quantitative_risk_studies_create`
- `ciso_assistant_api_crq_quantitative_risk_studies_retrigger_all_simulations_create`
- `ciso_assistant_api_crq_quantitative_risk_studies_update`
- `ciso_assistant_api_crq_quantitative_risk_studies_partial_update`
- `ciso_assistant_api_crq_quantitative_risk_studies_destroy`
