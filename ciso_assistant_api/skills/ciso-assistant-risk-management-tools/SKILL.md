---
name: ciso-assistant-risk-management-tools
skill_type: skill
description: >-
  Operate the risk management area of CISO Assistant through the ciso-assistant-api MCP server: find, read, create, update and delete its records with one typed tool per API operation. Use when the task needs the risk management records of a governance, risk and compliance program. Do NOT use for areas owned by the other ciso-assistant skills.
license: MIT
tags: [ciso-assistant, grc, risk-management, mcp]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# CISO Assistant: risk management

Each tool maps to exactly one API operation and takes that operation's parameters. Read first (list, then retrieve), and ask for approval before any create, update or delete.

## Rules
- Scope work to one folder or perimeter and cite record ids.
- Never print credentials, tokens or attachment bytes.
- Delete tools (names ending in `_destroy`) need explicit approval and a stated reason.

## Cwes
- `ciso_assistant_api_cwes_list`
- `ciso_assistant_api_cwes_autocomplete_retrieve`
- `ciso_assistant_api_cwes_cascade_info_retrieve`
- `ciso_assistant_api_cwes_object_retrieve`
- `ciso_assistant_api_cwes_retrieve`
- `ciso_assistant_api_cwes_batch_action_create`
- `ciso_assistant_api_cwes_create`
- `ciso_assistant_api_cwes_sync_catalog_create`
- `ciso_assistant_api_cwes_update`
- `ciso_assistant_api_cwes_partial_update`
- `ciso_assistant_api_cwes_destroy`

## Kg Ingest
- `ciso_ingest`

## Risk Acceptances
- `ciso_assistant_api_risk_acceptances_list`
- `ciso_assistant_api_risk_acceptances_cascade_info_retrieve`
- `ciso_assistant_api_risk_acceptances_object_retrieve`
- `ciso_assistant_api_risk_acceptances_retrieve`
- `ciso_assistant_api_risk_acceptances_state_retrieve`
- `ciso_assistant_api_risk_acceptances_to_review_retrieve`
- `ciso_assistant_api_risk_acceptances_waiting_retrieve`
- `ciso_assistant_api_risk_acceptances_accept_create`
- `ciso_assistant_api_risk_acceptances_batch_action_create`
- `ciso_assistant_api_risk_acceptances_create`
- `ciso_assistant_api_risk_acceptances_draft_create`
- `ciso_assistant_api_risk_acceptances_reject_create`
- `ciso_assistant_api_risk_acceptances_revoke_create`
- `ciso_assistant_api_risk_acceptances_submit_create`
- `ciso_assistant_api_risk_acceptances_update`
- `ciso_assistant_api_risk_acceptances_partial_update`
- `ciso_assistant_api_risk_acceptances_destroy`

## Risk Assessments
- `ciso_assistant_api_risk_assessments_list`
- `ciso_assistant_api_risk_assessments_create`

## Risk Assessments Batch Action
- `ciso_assistant_api_risk_assessments_batch_action_create`

## Risk Assessments Id
- `ciso_assistant_api_risk_assessments_action_plan_budget_overview_list`
- `ciso_assistant_api_risk_assessments_action_plan_list`
- `ciso_assistant_api_risk_assessments_action_plan_excel_retrieve`
- `ciso_assistant_api_risk_assessments_action_plan_pdf_retrieve`
- `ciso_assistant_api_risk_assessments_cascade_info_retrieve`
- `ciso_assistant_api_risk_assessments_object_retrieve`
- `ciso_assistant_api_risk_assessments_retrieve`
- `ciso_assistant_api_risk_assessments_risk_analytics_retrieve`
- `ciso_assistant_api_risk_assessments_risk_assessment_csv_retrieve`
- `ciso_assistant_api_risk_assessments_risk_assessment_pdf_retrieve`
- `ciso_assistant_api_risk_assessments_risk_assessment_xlsx_retrieve`
- `ciso_assistant_api_risk_assessments_risk_timeline_retrieve`
- `ciso_assistant_api_risk_assessments_sync_preview_retrieve`
- `ciso_assistant_api_risk_assessments_convert_to_quantitative_create`
- `ciso_assistant_api_risk_assessments_duplicate_create`
- `ciso_assistant_api_risk_assessments_sync_from_ebios_rm_create`
- `ciso_assistant_api_risk_assessments_sync_to_actions_create`
- `ciso_assistant_api_risk_assessments_update`
- `ciso_assistant_api_risk_assessments_partial_update`
- `ciso_assistant_api_risk_assessments_destroy`
- `ciso_assistant_api_risk_assessments_quality_check_retrieve_2`

## Risk Assessments Per Status
- `ciso_assistant_api_risk_assessments_per_status_retrieve`

## Risk Assessments Quality Check
- `ciso_assistant_api_risk_assessments_quality_check_retrieve`

## Risk Assessments Status
- `ciso_assistant_api_risk_assessments_status_retrieve`

## Risk Matrices
- `ciso_assistant_api_risk_matrices_list`
- `ciso_assistant_api_risk_matrices_cascade_info_retrieve`
- `ciso_assistant_api_risk_matrices_colors_retrieve`
- `ciso_assistant_api_risk_matrices_export_yaml_retrieve`
- `ciso_assistant_api_risk_matrices_ids_retrieve`
- `ciso_assistant_api_risk_matrices_impact_retrieve`
- `ciso_assistant_api_risk_matrices_object_retrieve`
- `ciso_assistant_api_risk_matrices_probability_retrieve`
- `ciso_assistant_api_risk_matrices_provider_retrieve`
- `ciso_assistant_api_risk_matrices_retrieve`
- `ciso_assistant_api_risk_matrices_risk_retrieve`
- `ciso_assistant_api_risk_matrices_used_retrieve`
- `ciso_assistant_api_risk_matrices_batch_action_create`
- `ciso_assistant_api_risk_matrices_create`
- `ciso_assistant_api_risk_matrices_create_draft_create`
- `ciso_assistant_api_risk_matrices_create_draft_from_create`
- `ciso_assistant_api_risk_matrices_discard_draft_create`
- `ciso_assistant_api_risk_matrices_import_yaml_create`
- `ciso_assistant_api_risk_matrices_publish_draft_create`
- `ciso_assistant_api_risk_matrices_start_editing_create`
- `ciso_assistant_api_risk_matrices_update`
- `ciso_assistant_api_risk_matrices_partial_update`
- `ciso_assistant_api_risk_matrices_save_draft_partial_update`
- `ciso_assistant_api_risk_matrices_destroy`

## Risk Scenarios
- `ciso_assistant_api_risk_scenarios_list`
- `ciso_assistant_api_risk_scenarios_cascade_info_retrieve`
- `ciso_assistant_api_risk_scenarios_count_per_level_retrieve`
- `ciso_assistant_api_risk_scenarios_default_ref_id_retrieve`
- `ciso_assistant_api_risk_scenarios_export_csv_retrieve`
- `ciso_assistant_api_risk_scenarios_export_xlsx_retrieve`
- `ciso_assistant_api_risk_scenarios_impact_retrieve`
- `ciso_assistant_api_risk_scenarios_object_retrieve`
- `ciso_assistant_api_risk_scenarios_per_status_retrieve`
- `ciso_assistant_api_risk_scenarios_probability_retrieve`
- `ciso_assistant_api_risk_scenarios_qualifications_count_retrieve`
- `ciso_assistant_api_risk_scenarios_retrieve`
- `ciso_assistant_api_risk_scenarios_strength_of_knowledge_retrieve`
- `ciso_assistant_api_risk_scenarios_treatment_retrieve`
- `ciso_assistant_api_risk_scenarios_batch_action_create`
- `ciso_assistant_api_risk_scenarios_create`
- `ciso_assistant_api_risk_scenarios_sync_to_actions_create`
- `ciso_assistant_api_risk_scenarios_update`
- `ciso_assistant_api_risk_scenarios_partial_update`
- `ciso_assistant_api_risk_scenarios_destroy`

## Threats
- `ciso_assistant_api_threats_list`
- `ciso_assistant_api_threats_cascade_info_retrieve`
- `ciso_assistant_api_threats_ids_retrieve`
- `ciso_assistant_api_threats_object_retrieve`
- `ciso_assistant_api_threats_provider_retrieve`
- `ciso_assistant_api_threats_retrieve`
- `ciso_assistant_api_threats_threats_count_retrieve`
- `ciso_assistant_api_threats_batch_action_create`
- `ciso_assistant_api_threats_create`
- `ciso_assistant_api_threats_update`
- `ciso_assistant_api_threats_partial_update`
- `ciso_assistant_api_threats_destroy`

## Vulnerabilities
- `ciso_assistant_api_vulnerabilities_list`
- `ciso_assistant_api_vulnerabilities_autocomplete_retrieve`
- `ciso_assistant_api_vulnerabilities_cascade_info_retrieve`
- `ciso_assistant_api_vulnerabilities_object_retrieve`
- `ciso_assistant_api_vulnerabilities_retrieve`
- `ciso_assistant_api_vulnerabilities_sankey_data_retrieve`
- `ciso_assistant_api_vulnerabilities_severity_retrieve`
- `ciso_assistant_api_vulnerabilities_status_retrieve`
- `ciso_assistant_api_vulnerabilities_treemap_data_retrieve`
- `ciso_assistant_api_vulnerabilities_batch_action_create`
- `ciso_assistant_api_vulnerabilities_create`
- `ciso_assistant_api_vulnerabilities_refresh_due_dates_create`
- `ciso_assistant_api_vulnerabilities_update`
- `ciso_assistant_api_vulnerabilities_partial_update`
- `ciso_assistant_api_vulnerabilities_destroy`
