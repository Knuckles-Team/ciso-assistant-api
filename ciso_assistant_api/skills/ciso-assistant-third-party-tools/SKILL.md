---
name: ciso-assistant-third-party-tools
skill_type: skill
description: >-
  Operate the third party area of CISO Assistant through the ciso-assistant-api MCP server: find, read, create, update and delete its records with one typed tool per API operation. Use when the task needs the third party records of a governance, risk and compliance program. Do NOT use for areas owned by the other ciso-assistant skills.
license: MIT
tags: [ciso-assistant, grc, third-party, mcp]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# CISO Assistant: third party

Each tool maps to exactly one API operation and takes that operation's parameters. Read first (list, then retrieve), and ask for approval before any create, update or delete.

## Rules
- Scope work to one folder or perimeter and cite record ids.
- Never print credentials, tokens or attachment bytes.
- Delete tools (names ending in `_destroy`) need explicit approval and a stated reason.

## Actors
- `ciso_assistant_api_actors_list`
- `ciso_assistant_api_actors_cascade_info_retrieve`
- `ciso_assistant_api_actors_object_retrieve`
- `ciso_assistant_api_actors_retrieve`

## Contracts
- `ciso_assistant_api_contracts_list`
- `ciso_assistant_api_contracts_cascade_info_retrieve`
- `ciso_assistant_api_contracts_currency_retrieve`
- `ciso_assistant_api_contracts_dora_contractual_arrangement_retrieve`
- `ciso_assistant_api_contracts_export_csv_retrieve`
- `ciso_assistant_api_contracts_export_xlsx_retrieve`
- `ciso_assistant_api_contracts_governing_law_country_retrieve`
- `ciso_assistant_api_contracts_object_retrieve`
- `ciso_assistant_api_contracts_retrieve`
- `ciso_assistant_api_contracts_status_retrieve`
- `ciso_assistant_api_contracts_termination_reason_retrieve`
- `ciso_assistant_api_contracts_batch_action_create`
- `ciso_assistant_api_contracts_create`
- `ciso_assistant_api_contracts_update`
- `ciso_assistant_api_contracts_partial_update`
- `ciso_assistant_api_contracts_destroy`

## Entities
- `ciso_assistant_api_entities_list`
- `ciso_assistant_api_entities_cascade_info_retrieve`
- `ciso_assistant_api_entities_country_retrieve`
- `ciso_assistant_api_entities_currency_retrieve`
- `ciso_assistant_api_entities_dora_entity_hierarchy_retrieve`
- `ciso_assistant_api_entities_dora_entity_type_retrieve`
- `ciso_assistant_api_entities_dora_provider_person_type_retrieve`
- `ciso_assistant_api_entities_dora_roi_lint_retrieve`
- `ciso_assistant_api_entities_export_csv_retrieve`
- `ciso_assistant_api_entities_export_ecosystem_retrieve`
- `ciso_assistant_api_entities_export_xlsx_retrieve`
- `ciso_assistant_api_entities_generate_dora_roi_retrieve`
- `ciso_assistant_api_entities_graph_retrieve`
- `ciso_assistant_api_entities_object_retrieve`
- `ciso_assistant_api_entities_retrieve`
- `ciso_assistant_api_entities_batch_action_create`
- `ciso_assistant_api_entities_batch_create_create`
- `ciso_assistant_api_entities_create`
- `ciso_assistant_api_entities_update`
- `ciso_assistant_api_entities_partial_update`
- `ciso_assistant_api_entities_destroy`

## Entity Assessments
- `ciso_assistant_api_entity_assessments_list`
- `ciso_assistant_api_entity_assessments_cascade_info_retrieve`
- `ciso_assistant_api_entity_assessments_conclusion_retrieve`
- `ciso_assistant_api_entity_assessments_metrics_retrieve`
- `ciso_assistant_api_entity_assessments_object_retrieve`
- `ciso_assistant_api_entity_assessments_retrieve`
- `ciso_assistant_api_entity_assessments_status_retrieve`
- `ciso_assistant_api_entity_assessments_batch_action_create`
- `ciso_assistant_api_entity_assessments_create`
- `ciso_assistant_api_entity_assessments_update`
- `ciso_assistant_api_entity_assessments_partial_update`
- `ciso_assistant_api_entity_assessments_destroy`

## Representatives
- `ciso_assistant_api_representatives_list`
- `ciso_assistant_api_representatives_cascade_info_retrieve`
- `ciso_assistant_api_representatives_object_retrieve`
- `ciso_assistant_api_representatives_retrieve`
- `ciso_assistant_api_representatives_batch_action_create`
- `ciso_assistant_api_representatives_create`
- `ciso_assistant_api_representatives_update`
- `ciso_assistant_api_representatives_partial_update`
- `ciso_assistant_api_representatives_destroy`

## Solutions
- `ciso_assistant_api_solutions_list`
- `ciso_assistant_api_solutions_cascade_info_retrieve`
- `ciso_assistant_api_solutions_data_location_processing_retrieve`
- `ciso_assistant_api_solutions_data_location_storage_retrieve`
- `ciso_assistant_api_solutions_dora_alternative_providers_identified_retrieve`
- `ciso_assistant_api_solutions_dora_data_sensitiveness_retrieve`
- `ciso_assistant_api_solutions_dora_discontinuing_impact_retrieve`
- `ciso_assistant_api_solutions_dora_has_exit_plan_retrieve`
- `ciso_assistant_api_solutions_dora_ict_service_type_retrieve`
- `ciso_assistant_api_solutions_dora_non_substitutability_reason_retrieve`
- `ciso_assistant_api_solutions_dora_reintegration_possibility_retrieve`
- `ciso_assistant_api_solutions_dora_reliance_level_retrieve`
- `ciso_assistant_api_solutions_dora_substitutability_retrieve`
- `ciso_assistant_api_solutions_export_csv_retrieve`
- `ciso_assistant_api_solutions_export_xlsx_retrieve`
- `ciso_assistant_api_solutions_object_retrieve`
- `ciso_assistant_api_solutions_retrieve`
- `ciso_assistant_api_solutions_batch_action_create`
- `ciso_assistant_api_solutions_create`
- `ciso_assistant_api_solutions_update`
- `ciso_assistant_api_solutions_partial_update`
- `ciso_assistant_api_solutions_destroy`
