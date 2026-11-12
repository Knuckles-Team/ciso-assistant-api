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
