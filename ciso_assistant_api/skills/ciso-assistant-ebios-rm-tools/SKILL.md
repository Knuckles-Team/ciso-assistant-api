---
name: ciso-assistant-ebios-rm-tools
skill_type: skill
description: >-
  Operate the ebios rm area of CISO Assistant through the ciso-assistant-api MCP server: find, read, create, update and delete its records with one typed tool per API operation. Use when the task needs the ebios rm records of a governance, risk and compliance program. Do NOT use for areas owned by the other ciso-assistant skills.
license: MIT
tags: [ciso-assistant, grc, ebios-rm, mcp]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# CISO Assistant: ebios rm

Each tool maps to exactly one API operation and takes that operation's parameters. Read first (list, then retrieve), and ask for approval before any create, update or delete.

## Rules
- Scope work to one folder or perimeter and cite record ids.
- Never print credentials, tokens or attachment bytes.
- Delete tools (names ending in `_destroy`) need explicit approval and a stated reason.

## Ebios Rm Attack Paths
- `ciso_assistant_api_ebios_rm_attack_paths_list`
- `ciso_assistant_api_ebios_rm_attack_paths_cascade_info_retrieve`
- `ciso_assistant_api_ebios_rm_attack_paths_object_retrieve`
- `ciso_assistant_api_ebios_rm_attack_paths_retrieve`
- `ciso_assistant_api_ebios_rm_attack_paths_batch_action_create`
- `ciso_assistant_api_ebios_rm_attack_paths_create`
- `ciso_assistant_api_ebios_rm_attack_paths_update`
- `ciso_assistant_api_ebios_rm_attack_paths_partial_update`
- `ciso_assistant_api_ebios_rm_attack_paths_destroy`

## Ebios Rm Elementary Actions
- `ciso_assistant_api_ebios_rm_elementary_actions_list`
- `ciso_assistant_api_ebios_rm_elementary_actions_attack_stage_retrieve`
- `ciso_assistant_api_ebios_rm_elementary_actions_cascade_info_retrieve`
- `ciso_assistant_api_ebios_rm_elementary_actions_icon_retrieve`
- `ciso_assistant_api_ebios_rm_elementary_actions_object_retrieve`
- `ciso_assistant_api_ebios_rm_elementary_actions_retrieve`
- `ciso_assistant_api_ebios_rm_elementary_actions_batch_action_create`
- `ciso_assistant_api_ebios_rm_elementary_actions_create`
- `ciso_assistant_api_ebios_rm_elementary_actions_update`
- `ciso_assistant_api_ebios_rm_elementary_actions_partial_update`
- `ciso_assistant_api_ebios_rm_elementary_actions_destroy`

## Ebios Rm Feared Events
- `ciso_assistant_api_ebios_rm_feared_events_list`
- `ciso_assistant_api_ebios_rm_feared_events_cascade_info_retrieve`
- `ciso_assistant_api_ebios_rm_feared_events_gravity_retrieve`
- `ciso_assistant_api_ebios_rm_feared_events_object_retrieve`
- `ciso_assistant_api_ebios_rm_feared_events_retrieve`
- `ciso_assistant_api_ebios_rm_feared_events_risk_matrix_retrieve`
- `ciso_assistant_api_ebios_rm_feared_events_batch_action_create`
- `ciso_assistant_api_ebios_rm_feared_events_batch_create_create`
- `ciso_assistant_api_ebios_rm_feared_events_create`
- `ciso_assistant_api_ebios_rm_feared_events_update`
- `ciso_assistant_api_ebios_rm_feared_events_partial_update`
- `ciso_assistant_api_ebios_rm_feared_events_destroy`

## Ebios Rm Kill Chains
- `ciso_assistant_api_ebios_rm_kill_chains_list`
- `ciso_assistant_api_ebios_rm_kill_chains_cascade_info_retrieve`
- `ciso_assistant_api_ebios_rm_kill_chains_logic_operator_retrieve`
- `ciso_assistant_api_ebios_rm_kill_chains_object_retrieve`
- `ciso_assistant_api_ebios_rm_kill_chains_retrieve`
- `ciso_assistant_api_ebios_rm_kill_chains_batch_action_create`
- `ciso_assistant_api_ebios_rm_kill_chains_create`
- `ciso_assistant_api_ebios_rm_kill_chains_update`
- `ciso_assistant_api_ebios_rm_kill_chains_partial_update`
- `ciso_assistant_api_ebios_rm_kill_chains_destroy`

## Ebios Rm Operating Modes
- `ciso_assistant_api_ebios_rm_operating_modes_list`
- `ciso_assistant_api_ebios_rm_operating_modes_build_graph_retrieve`
- `ciso_assistant_api_ebios_rm_operating_modes_cascade_info_retrieve`
- `ciso_assistant_api_ebios_rm_operating_modes_default_ref_id_retrieve`
- `ciso_assistant_api_ebios_rm_operating_modes_likelihood_retrieve`
- `ciso_assistant_api_ebios_rm_operating_modes_object_retrieve`
- `ciso_assistant_api_ebios_rm_operating_modes_retrieve`
- `ciso_assistant_api_ebios_rm_operating_modes_batch_action_create`
- `ciso_assistant_api_ebios_rm_operating_modes_create`
- `ciso_assistant_api_ebios_rm_operating_modes_save_graph_create`
- `ciso_assistant_api_ebios_rm_operating_modes_update`
- `ciso_assistant_api_ebios_rm_operating_modes_partial_update`
- `ciso_assistant_api_ebios_rm_operating_modes_destroy`

## Ebios Rm Operational Scenarios
- `ciso_assistant_api_ebios_rm_operational_scenarios_list`
- `ciso_assistant_api_ebios_rm_operational_scenarios_cascade_info_retrieve`
- `ciso_assistant_api_ebios_rm_operational_scenarios_likelihood_retrieve`
- `ciso_assistant_api_ebios_rm_operational_scenarios_object_retrieve`
- `ciso_assistant_api_ebios_rm_operational_scenarios_retrieve`
- `ciso_assistant_api_ebios_rm_operational_scenarios_risk_matrix_retrieve`
- `ciso_assistant_api_ebios_rm_operational_scenarios_batch_action_create`
- `ciso_assistant_api_ebios_rm_operational_scenarios_create`
- `ciso_assistant_api_ebios_rm_operational_scenarios_update`
- `ciso_assistant_api_ebios_rm_operational_scenarios_partial_update`
- `ciso_assistant_api_ebios_rm_operational_scenarios_destroy`

## Ebios Rm Ro To
- `ciso_assistant_api_ebios_rm_ro_to_list`
- `ciso_assistant_api_ebios_rm_ro_to_activity_retrieve`
- `ciso_assistant_api_ebios_rm_ro_to_cascade_info_retrieve`
- `ciso_assistant_api_ebios_rm_ro_to_motivation_retrieve`
- `ciso_assistant_api_ebios_rm_ro_to_object_retrieve`
- `ciso_assistant_api_ebios_rm_ro_to_pertinence_retrieve`
- `ciso_assistant_api_ebios_rm_ro_to_resources_retrieve`
- `ciso_assistant_api_ebios_rm_ro_to_retrieve`
- `ciso_assistant_api_ebios_rm_ro_to_batch_action_create`
- `ciso_assistant_api_ebios_rm_ro_to_create`
- `ciso_assistant_api_ebios_rm_ro_to_update`
- `ciso_assistant_api_ebios_rm_ro_to_partial_update`
- `ciso_assistant_api_ebios_rm_ro_to_destroy`

## Ebios Rm Stakeholders
- `ciso_assistant_api_ebios_rm_stakeholders_list`
- `ciso_assistant_api_ebios_rm_stakeholders_cascade_info_retrieve`
- `ciso_assistant_api_ebios_rm_stakeholders_category_retrieve`
- `ciso_assistant_api_ebios_rm_stakeholders_chart_data_retrieve`
- `ciso_assistant_api_ebios_rm_stakeholders_object_retrieve`
- `ciso_assistant_api_ebios_rm_stakeholders_retrieve`
- `ciso_assistant_api_ebios_rm_stakeholders_batch_action_create`
- `ciso_assistant_api_ebios_rm_stakeholders_create`
- `ciso_assistant_api_ebios_rm_stakeholders_update`
- `ciso_assistant_api_ebios_rm_stakeholders_partial_update`
- `ciso_assistant_api_ebios_rm_stakeholders_destroy`

## Ebios Rm Strategic Scenarios
- `ciso_assistant_api_ebios_rm_strategic_scenarios_list`
- `ciso_assistant_api_ebios_rm_strategic_scenarios_cascade_info_retrieve`
- `ciso_assistant_api_ebios_rm_strategic_scenarios_object_retrieve`
- `ciso_assistant_api_ebios_rm_strategic_scenarios_retrieve`
- `ciso_assistant_api_ebios_rm_strategic_scenarios_batch_action_create`
- `ciso_assistant_api_ebios_rm_strategic_scenarios_create`
- `ciso_assistant_api_ebios_rm_strategic_scenarios_update`
- `ciso_assistant_api_ebios_rm_strategic_scenarios_partial_update`
- `ciso_assistant_api_ebios_rm_strategic_scenarios_destroy`

## Ebios Rm Studies
- `ciso_assistant_api_ebios_rm_studies_list`
- `ciso_assistant_api_ebios_rm_studies_cascade_info_retrieve`
- `ciso_assistant_api_ebios_rm_studies_ecosystem_chart_data_retrieve`
- `ciso_assistant_api_ebios_rm_studies_ecosystem_circular_chart_data_retrieve`
- `ciso_assistant_api_ebios_rm_studies_export_xlsx_retrieve`
- `ciso_assistant_api_ebios_rm_studies_gravity_retrieve`
- `ciso_assistant_api_ebios_rm_studies_likelihood_retrieve`
- `ciso_assistant_api_ebios_rm_studies_object_retrieve`
- `ciso_assistant_api_ebios_rm_studies_quotation_method_retrieve`
- `ciso_assistant_api_ebios_rm_studies_report_data_retrieve`
- `ciso_assistant_api_ebios_rm_studies_retrieve`
- `ciso_assistant_api_ebios_rm_studies_risk_matrix_retrieve`
- `ciso_assistant_api_ebios_rm_studies_status_retrieve`
- `ciso_assistant_api_ebios_rm_studies_visual_analysis_retrieve`
- `ciso_assistant_api_ebios_rm_studies_batch_action_create`
- `ciso_assistant_api_ebios_rm_studies_create`
- `ciso_assistant_api_ebios_rm_studies_update`
- `ciso_assistant_api_ebios_rm_studies_partial_update`
- `ciso_assistant_api_ebios_rm_studies_workshop_step_partial_update`
- `ciso_assistant_api_ebios_rm_studies_destroy`
