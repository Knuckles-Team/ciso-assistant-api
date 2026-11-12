---
name: ciso-assistant-compliance-tools
skill_type: skill
description: >-
  Operate the compliance area of CISO Assistant through the ciso-assistant-api MCP server: find, read, create, update and delete its records with one typed tool per API operation. Use when the task needs the compliance records of a governance, risk and compliance program. Do NOT use for areas owned by the other ciso-assistant skills.
license: MIT
tags: [ciso-assistant, grc, compliance, mcp]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# CISO Assistant: compliance

Each tool maps to exactly one API operation and takes that operation's parameters. Read first (list, then retrieve), and ask for approval before any create, update or delete.

## Rules
- Scope work to one folder or perimeter and cite record ids.
- Never print credentials, tokens or attachment bytes.
- Delete tools (names ending in `_destroy`) need explicit approval and a stated reason.

## Applied Controls
- `ciso_assistant_api_applied_controls_list`
- `ciso_assistant_api_applied_controls_create`

## Applied Controls Analytics
- `ciso_assistant_api_applied_controls_analytics_retrieve`

## Applied Controls Autocomplete
- `ciso_assistant_api_applied_controls_autocomplete_retrieve`

## Applied Controls Batch Action
- `ciso_assistant_api_applied_controls_batch_action_create`

## Applied Controls Category
- `ciso_assistant_api_applied_controls_category_retrieve`

## Applied Controls Control Impact
- `ciso_assistant_api_applied_controls_control_impact_retrieve`

## Applied Controls Csf Function
- `ciso_assistant_api_applied_controls_csf_function_retrieve`

## Applied Controls Effort
- `ciso_assistant_api_applied_controls_effort_retrieve`

## Applied Controls Export Csv
- `ciso_assistant_api_applied_controls_export_csv_retrieve`

## Applied Controls Export Xlsx
- `ciso_assistant_api_applied_controls_export_xlsx_retrieve`

## Applied Controls Get Controls Info
- `ciso_assistant_api_applied_controls_get_controls_info_retrieve`

## Applied Controls Get Gantt Data
- `ciso_assistant_api_applied_controls_get_gantt_data_retrieve`

## Applied Controls Get Timeline Info
- `ciso_assistant_api_applied_controls_get_timeline_info_retrieve`

## Applied Controls Id
- `ciso_assistant_api_applied_controls_cascade_info_retrieve`
- `ciso_assistant_api_applied_controls_object_retrieve`
- `ciso_assistant_api_applied_controls_retrieve`
- `ciso_assistant_api_applied_controls_duplicate_create`
- `ciso_assistant_api_applied_controls_sync_to_reference_control_create`
- `ciso_assistant_api_applied_controls_update`
- `ciso_assistant_api_applied_controls_partial_update`
- `ciso_assistant_api_applied_controls_destroy`

## Applied Controls Ids
- `ciso_assistant_api_applied_controls_ids_retrieve`

## Applied Controls Impact Effort
- `ciso_assistant_api_applied_controls_impact_effort_retrieve`

## Applied Controls Impact Graph
- `ciso_assistant_api_applied_controls_impact_graph_retrieve`

## Applied Controls Linked Models
- `ciso_assistant_api_applied_controls_linked_models_retrieve`

## Applied Controls Merge
- `ciso_assistant_api_applied_controls_merge_create`

## Applied Controls Mss Xlsx
- `ciso_assistant_api_applied_controls_mss_xlsx_retrieve`

## Applied Controls Owner
- `ciso_assistant_api_applied_controls_owner_retrieve`

## Applied Controls Per Status
- `ciso_assistant_api_applied_controls_per_status_retrieve`

## Applied Controls Priority
- `ciso_assistant_api_applied_controls_priority_retrieve`

## Applied Controls Priority Chart Data
- `ciso_assistant_api_applied_controls_priority_chart_data_retrieve`

## Applied Controls Status
- `ciso_assistant_api_applied_controls_status_retrieve`

## Applied Controls Sunburst Data
- `ciso_assistant_api_applied_controls_sunburst_data_retrieve`

## Applied Controls To Review
- `ciso_assistant_api_applied_controls_to_review_retrieve`

## Applied Controls Todo
- `ciso_assistant_api_applied_controls_todo_retrieve`

## Applied Controls Updatables
- `ciso_assistant_api_applied_controls_updatables_retrieve`

## Compliance Assessments
- `ciso_assistant_api_compliance_assessments_list`
- `ciso_assistant_api_compliance_assessments_create`

## Compliance Assessments Analytics
- `ciso_assistant_api_compliance_assessments_analytics_retrieve`

## Compliance Assessments Auditee Dashboard
- `ciso_assistant_api_compliance_assessments_auditee_dashboard_retrieve`

## Compliance Assessments Batch Action
- `ciso_assistant_api_compliance_assessments_batch_action_create`

## Compliance Assessments Id
- `ciso_assistant_api_compliance_assessments_action_plan_budget_overview_list`
- `ciso_assistant_api_compliance_assessments_action_plan_list`
- `ciso_assistant_api_compliance_assessments_evidences_list_list`
- `ciso_assistant_api_compliance_assessments_action_plan_csv_retrieve`
- `ciso_assistant_api_compliance_assessments_action_plan_pdf_retrieve`
- `ciso_assistant_api_compliance_assessments_action_plan_xlsx_retrieve`
- `ciso_assistant_api_compliance_assessments_cascade_info_retrieve`
- `ciso_assistant_api_compliance_assessments_combined_tree_retrieve`
- `ciso_assistant_api_compliance_assessments_comparable_audits_retrieve`
- `ciso_assistant_api_compliance_assessments_compare_retrieve`
- `ciso_assistant_api_compliance_assessments_compliance_assessment_csv_retrieve`
- `ciso_assistant_api_compliance_assessments_compliance_timeline_retrieve`
- `ciso_assistant_api_compliance_assessments_controls_coverage_retrieve`
- `ciso_assistant_api_compliance_assessments_cyfun_xlsx_retrieve`
- `ciso_assistant_api_compliance_assessments_donut_data_retrieve`
- `ciso_assistant_api_compliance_assessments_evidence_coverage_retrieve`
- `ciso_assistant_api_compliance_assessments_exceptions_summary_retrieve`
- `ciso_assistant_api_compliance_assessments_export_retrieve`
- `ciso_assistant_api_compliance_assessments_frameworks_retrieve`
- `ciso_assistant_api_compliance_assessments_global_score_retrieve`
- `ciso_assistant_api_compliance_assessments_implementation_groups_breakdown_retrieve`
- `ciso_assistant_api_compliance_assessments_is_auditee_retrieve`
- `ciso_assistant_api_compliance_assessments_map_from_preview_retrieve`
- `ciso_assistant_api_compliance_assessments_object_retrieve`
- `ciso_assistant_api_compliance_assessments_progress_ts_retrieve`
- `ciso_assistant_api_compliance_assessments_requirements_list_retrieve`
- `ciso_assistant_api_compliance_assessments_retrieve`
- `ciso_assistant_api_compliance_assessments_section_compliance_retrieve`
- `ciso_assistant_api_compliance_assessments_soa_retrieve`
- `ciso_assistant_api_compliance_assessments_suggestions_applied_controls_retrieve`
- `ciso_assistant_api_compliance_assessments_sync_to_actions_retrieve`
- `ciso_assistant_api_compliance_assessments_threats_metrics_retrieve`
- `ciso_assistant_api_compliance_assessments_tree_retrieve`
- `ciso_assistant_api_compliance_assessments_word_report_retrieve`
- `ciso_assistant_api_compliance_assessments_xlsx_retrieve`
- `ciso_assistant_api_compliance_assessments_mailing_create`
- `ciso_assistant_api_compliance_assessments_map_from_create`
- `ciso_assistant_api_compliance_assessments_suggestions_applied_controls_create`
- `ciso_assistant_api_compliance_assessments_sync_to_actions_create`
- `ciso_assistant_api_compliance_assessments_update_requirement_create`
- `ciso_assistant_api_compliance_assessments_update`
- `ciso_assistant_api_compliance_assessments_partial_update`
- `ciso_assistant_api_compliance_assessments_destroy`
- `ciso_assistant_api_compliance_assessments_quality_check_retrieve_2`

## Compliance Assessments Per Status
- `ciso_assistant_api_compliance_assessments_per_status_retrieve`

## Compliance Assessments Quality Check
- `ciso_assistant_api_compliance_assessments_quality_check_retrieve`

## Compliance Assessments Recap
- `ciso_assistant_api_compliance_assessments_recap_retrieve`

## Compliance Assessments Score Calculation Method
- `ciso_assistant_api_compliance_assessments_score_calculation_method_retrieve`

## Compliance Assessments Status
- `ciso_assistant_api_compliance_assessments_status_retrieve`

## Mapping Libraries
- `ciso_assistant_api_mapping_libraries_list`

## Policies
- `ciso_assistant_api_policies_list`
- `ciso_assistant_api_policies_create`

## Policies Analytics
- `ciso_assistant_api_policies_analytics_retrieve`

## Policies Autocomplete
- `ciso_assistant_api_policies_autocomplete_retrieve`

## Policies Batch Action
- `ciso_assistant_api_policies_batch_action_create`

## Policies Category
- `ciso_assistant_api_policies_category_retrieve`

## Policies Control Impact
- `ciso_assistant_api_policies_control_impact_retrieve`

## Policies Csf Function
- `ciso_assistant_api_policies_csf_function_retrieve`

## Policies Effort
- `ciso_assistant_api_policies_effort_retrieve`

## Policies Export Csv
- `ciso_assistant_api_policies_export_csv_retrieve`

## Policies Export Xlsx
- `ciso_assistant_api_policies_export_xlsx_retrieve`

## Policies Get Controls Info
- `ciso_assistant_api_policies_get_controls_info_retrieve`

## Policies Get Gantt Data
- `ciso_assistant_api_policies_get_gantt_data_retrieve`

## Policies Get Timeline Info
- `ciso_assistant_api_policies_get_timeline_info_retrieve`

## Policies Id
- `ciso_assistant_api_policies_cascade_info_retrieve`
- `ciso_assistant_api_policies_object_retrieve`
- `ciso_assistant_api_policies_retrieve`
- `ciso_assistant_api_policies_duplicate_create`
- `ciso_assistant_api_policies_sync_to_reference_control_create`
- `ciso_assistant_api_policies_update`
- `ciso_assistant_api_policies_partial_update`
- `ciso_assistant_api_policies_destroy`

## Policies Ids
- `ciso_assistant_api_policies_ids_retrieve`

## Policies Impact Effort
- `ciso_assistant_api_policies_impact_effort_retrieve`

## Policies Impact Graph
- `ciso_assistant_api_policies_impact_graph_retrieve`

## Policies Linked Models
- `ciso_assistant_api_policies_linked_models_retrieve`

## Policies Merge
- `ciso_assistant_api_policies_merge_create`

## Policies Mss Xlsx
- `ciso_assistant_api_policies_mss_xlsx_retrieve`

## Policies Owner
- `ciso_assistant_api_policies_owner_retrieve`

## Policies Per Status
- `ciso_assistant_api_policies_per_status_retrieve`

## Policies Priority
- `ciso_assistant_api_policies_priority_retrieve`

## Policies Priority Chart Data
- `ciso_assistant_api_policies_priority_chart_data_retrieve`

## Policies Status
- `ciso_assistant_api_policies_status_retrieve`

## Policies Sunburst Data
- `ciso_assistant_api_policies_sunburst_data_retrieve`

## Policies To Review
- `ciso_assistant_api_policies_to_review_retrieve`

## Policies Todo
- `ciso_assistant_api_policies_todo_retrieve`

## Policies Updatables
- `ciso_assistant_api_policies_updatables_retrieve`

## Reference Controls
- `ciso_assistant_api_reference_controls_list`
- `ciso_assistant_api_reference_controls_cascade_info_retrieve`
- `ciso_assistant_api_reference_controls_category_retrieve`
- `ciso_assistant_api_reference_controls_csf_function_retrieve`
- `ciso_assistant_api_reference_controls_object_retrieve`
- `ciso_assistant_api_reference_controls_provider_retrieve`
- `ciso_assistant_api_reference_controls_retrieve`
- `ciso_assistant_api_reference_controls_syncable_applied_controls_retrieve`
- `ciso_assistant_api_reference_controls_batch_action_create`
- `ciso_assistant_api_reference_controls_create`
- `ciso_assistant_api_reference_controls_sync_applied_controls_create`
- `ciso_assistant_api_reference_controls_update`
- `ciso_assistant_api_reference_controls_partial_update`
- `ciso_assistant_api_reference_controls_destroy`

## Requirement Assessments
- `ciso_assistant_api_requirement_assessments_list`
- `ciso_assistant_api_requirement_assessments_cascade_info_retrieve`
- `ciso_assistant_api_requirement_assessments_extended_result_retrieve`
- `ciso_assistant_api_requirement_assessments_object_retrieve`
- `ciso_assistant_api_requirement_assessments_per_status_retrieve`
- `ciso_assistant_api_requirement_assessments_result_retrieve`
- `ciso_assistant_api_requirement_assessments_retrieve`
- `ciso_assistant_api_requirement_assessments_status_retrieve`
- `ciso_assistant_api_requirement_assessments_suggestions_applied_controls_retrieve`
- `ciso_assistant_api_requirement_assessments_to_review_retrieve`
- `ciso_assistant_api_requirement_assessments_todo_retrieve`
- `ciso_assistant_api_requirement_assessments_updatables_retrieve`
- `ciso_assistant_api_requirement_assessments_batch_action_create`
- `ciso_assistant_api_requirement_assessments_create`
- `ciso_assistant_api_requirement_assessments_suggestions_applied_controls_create`
- `ciso_assistant_api_requirement_assessments_update`
- `ciso_assistant_api_requirement_assessments_partial_update`
- `ciso_assistant_api_requirement_assessments_destroy`

## Requirement Assignments
- `ciso_assistant_api_requirement_assignments_list`
- `ciso_assistant_api_requirement_assignments_cascade_info_retrieve`
- `ciso_assistant_api_requirement_assignments_object_retrieve`
- `ciso_assistant_api_requirement_assignments_requirements_list_retrieve`
- `ciso_assistant_api_requirement_assignments_retrieve`
- `ciso_assistant_api_requirement_assignments_batch_action_create`
- `ciso_assistant_api_requirement_assignments_create`
- `ciso_assistant_api_requirement_assignments_set_status_create`
- `ciso_assistant_api_requirement_assignments_update`
- `ciso_assistant_api_requirement_assignments_partial_update`
- `ciso_assistant_api_requirement_assignments_destroy`

## Requirement Mapping Sets
- `ciso_assistant_api_requirement_mapping_sets_list`
- `ciso_assistant_api_requirement_mapping_sets_cascade_info_retrieve`
- `ciso_assistant_api_requirement_mapping_sets_graph_data_retrieve`
- `ciso_assistant_api_requirement_mapping_sets_object_retrieve`
- `ciso_assistant_api_requirement_mapping_sets_provider_retrieve`
- `ciso_assistant_api_requirement_mapping_sets_retrieve`
- `ciso_assistant_api_requirement_mapping_sets_batch_action_create`
- `ciso_assistant_api_requirement_mapping_sets_create`
- `ciso_assistant_api_requirement_mapping_sets_update`
- `ciso_assistant_api_requirement_mapping_sets_partial_update`
- `ciso_assistant_api_requirement_mapping_sets_destroy`
- `ciso_assistant_api_requirement_mapping_sets_graph_data_retrieve_2`

## Requirement Nodes
- `ciso_assistant_api_requirement_nodes_list`
- `ciso_assistant_api_requirement_nodes_cascade_info_retrieve`
- `ciso_assistant_api_requirement_nodes_inspect_requirement_retrieve`
- `ciso_assistant_api_requirement_nodes_object_retrieve`
- `ciso_assistant_api_requirement_nodes_retrieve`
- `ciso_assistant_api_requirement_nodes_serve_image_retrieve`
- `ciso_assistant_api_requirement_nodes_batch_action_create`
- `ciso_assistant_api_requirement_nodes_create`
- `ciso_assistant_api_requirement_nodes_upload_image_create`
- `ciso_assistant_api_requirement_nodes_update`
- `ciso_assistant_api_requirement_nodes_partial_update`
- `ciso_assistant_api_requirement_nodes_destroy`
