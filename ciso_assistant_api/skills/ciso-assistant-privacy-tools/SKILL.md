---
name: ciso-assistant-privacy-tools
skill_type: skill
description: >-
  Operate the privacy area of CISO Assistant through the ciso-assistant-api MCP server: find, read, create, update and delete its records with one typed tool per API operation. Use when the task needs the privacy records of a governance, risk and compliance program. Do NOT use for areas owned by the other ciso-assistant skills.
license: MIT
tags: [ciso-assistant, grc, privacy, mcp]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# CISO Assistant: privacy

Each tool maps to exactly one API operation and takes that operation's parameters. Read first (list, then retrieve), and ask for approval before any create, update or delete.

## Rules
- Scope work to one folder or perimeter and cite record ids.
- Never print credentials, tokens or attachment bytes.
- Delete tools (names ending in `_destroy`) need explicit approval and a stated reason.

## Privacy Data Breaches
- `ciso_assistant_api_privacy_data_breaches_list`
- `ciso_assistant_api_privacy_data_breaches_breach_type_retrieve`
- `ciso_assistant_api_privacy_data_breaches_cascade_info_retrieve`
- `ciso_assistant_api_privacy_data_breaches_object_retrieve`
- `ciso_assistant_api_privacy_data_breaches_retrieve`
- `ciso_assistant_api_privacy_data_breaches_risk_level_retrieve`
- `ciso_assistant_api_privacy_data_breaches_status_retrieve`
- `ciso_assistant_api_privacy_data_breaches_batch_action_create`
- `ciso_assistant_api_privacy_data_breaches_create`
- `ciso_assistant_api_privacy_data_breaches_update`
- `ciso_assistant_api_privacy_data_breaches_partial_update`
- `ciso_assistant_api_privacy_data_breaches_destroy`

## Privacy Data Contractors
- `ciso_assistant_api_privacy_data_contractors_list`
- `ciso_assistant_api_privacy_data_contractors_cascade_info_retrieve`
- `ciso_assistant_api_privacy_data_contractors_country_retrieve`
- `ciso_assistant_api_privacy_data_contractors_object_retrieve`
- `ciso_assistant_api_privacy_data_contractors_relationship_type_retrieve`
- `ciso_assistant_api_privacy_data_contractors_retrieve`
- `ciso_assistant_api_privacy_data_contractors_batch_action_create`
- `ciso_assistant_api_privacy_data_contractors_create`
- `ciso_assistant_api_privacy_data_contractors_update`
- `ciso_assistant_api_privacy_data_contractors_partial_update`
- `ciso_assistant_api_privacy_data_contractors_destroy`

## Privacy Data Recipients
- `ciso_assistant_api_privacy_data_recipients_list`
- `ciso_assistant_api_privacy_data_recipients_cascade_info_retrieve`
- `ciso_assistant_api_privacy_data_recipients_category_retrieve`
- `ciso_assistant_api_privacy_data_recipients_object_retrieve`
- `ciso_assistant_api_privacy_data_recipients_retrieve`
- `ciso_assistant_api_privacy_data_recipients_batch_action_create`
- `ciso_assistant_api_privacy_data_recipients_create`
- `ciso_assistant_api_privacy_data_recipients_update`
- `ciso_assistant_api_privacy_data_recipients_partial_update`
- `ciso_assistant_api_privacy_data_recipients_destroy`

## Privacy Data Subjects
- `ciso_assistant_api_privacy_data_subjects_list`
- `ciso_assistant_api_privacy_data_subjects_cascade_info_retrieve`
- `ciso_assistant_api_privacy_data_subjects_category_retrieve`
- `ciso_assistant_api_privacy_data_subjects_object_retrieve`
- `ciso_assistant_api_privacy_data_subjects_retrieve`
- `ciso_assistant_api_privacy_data_subjects_batch_action_create`
- `ciso_assistant_api_privacy_data_subjects_create`
- `ciso_assistant_api_privacy_data_subjects_update`
- `ciso_assistant_api_privacy_data_subjects_partial_update`
- `ciso_assistant_api_privacy_data_subjects_destroy`

## Privacy Data Transfers
- `ciso_assistant_api_privacy_data_transfers_list`
- `ciso_assistant_api_privacy_data_transfers_cascade_info_retrieve`
- `ciso_assistant_api_privacy_data_transfers_country_retrieve`
- `ciso_assistant_api_privacy_data_transfers_object_retrieve`
- `ciso_assistant_api_privacy_data_transfers_retrieve`
- `ciso_assistant_api_privacy_data_transfers_transfer_mechanism_retrieve`
- `ciso_assistant_api_privacy_data_transfers_batch_action_create`
- `ciso_assistant_api_privacy_data_transfers_create`
- `ciso_assistant_api_privacy_data_transfers_update`
- `ciso_assistant_api_privacy_data_transfers_partial_update`
- `ciso_assistant_api_privacy_data_transfers_destroy`

## Privacy Personal Data
- `ciso_assistant_api_privacy_personal_data_list`
- `ciso_assistant_api_privacy_personal_data_cascade_info_retrieve`
- `ciso_assistant_api_privacy_personal_data_category_retrieve`
- `ciso_assistant_api_privacy_personal_data_deletion_policy_retrieve`
- `ciso_assistant_api_privacy_personal_data_is_sensitive_retrieve`
- `ciso_assistant_api_privacy_personal_data_object_retrieve`
- `ciso_assistant_api_privacy_personal_data_retrieve`
- `ciso_assistant_api_privacy_personal_data_batch_action_create`
- `ciso_assistant_api_privacy_personal_data_batch_create_create`
- `ciso_assistant_api_privacy_personal_data_create`
- `ciso_assistant_api_privacy_personal_data_update`
- `ciso_assistant_api_privacy_personal_data_partial_update`
- `ciso_assistant_api_privacy_personal_data_destroy`

## Privacy Processing Natures
- `ciso_assistant_api_privacy_processing_natures_list`
- `ciso_assistant_api_privacy_processing_natures_cascade_info_retrieve`
- `ciso_assistant_api_privacy_processing_natures_object_retrieve`
- `ciso_assistant_api_privacy_processing_natures_retrieve`
- `ciso_assistant_api_privacy_processing_natures_batch_action_create`
- `ciso_assistant_api_privacy_processing_natures_create`
- `ciso_assistant_api_privacy_processing_natures_update`
- `ciso_assistant_api_privacy_processing_natures_partial_update`
- `ciso_assistant_api_privacy_processing_natures_destroy`

## Privacy Processings
- `ciso_assistant_api_privacy_processings_list`
- `ciso_assistant_api_privacy_processings_agg_metrics_retrieve`
- `ciso_assistant_api_privacy_processings_assigned_to_retrieve`
- `ciso_assistant_api_privacy_processings_cascade_info_retrieve`
- `ciso_assistant_api_privacy_processings_export_csv_retrieve`
- `ciso_assistant_api_privacy_processings_export_xlsx_retrieve`
- `ciso_assistant_api_privacy_processings_metrics_retrieve`
- `ciso_assistant_api_privacy_processings_object_retrieve`
- `ciso_assistant_api_privacy_processings_retrieve`
- `ciso_assistant_api_privacy_processings_status_retrieve`
- `ciso_assistant_api_privacy_processings_batch_action_create`
- `ciso_assistant_api_privacy_processings_create`
- `ciso_assistant_api_privacy_processings_update`
- `ciso_assistant_api_privacy_processings_partial_update`
- `ciso_assistant_api_privacy_processings_destroy`

## Privacy Purposes
- `ciso_assistant_api_privacy_purposes_list`
- `ciso_assistant_api_privacy_purposes_article_9_condition_retrieve`
- `ciso_assistant_api_privacy_purposes_cascade_info_retrieve`
- `ciso_assistant_api_privacy_purposes_legal_basis_retrieve`
- `ciso_assistant_api_privacy_purposes_object_retrieve`
- `ciso_assistant_api_privacy_purposes_retrieve`
- `ciso_assistant_api_privacy_purposes_batch_action_create`
- `ciso_assistant_api_privacy_purposes_create`
- `ciso_assistant_api_privacy_purposes_update`
- `ciso_assistant_api_privacy_purposes_partial_update`
- `ciso_assistant_api_privacy_purposes_destroy`

## Privacy Right Requests
- `ciso_assistant_api_privacy_right_requests_list`
- `ciso_assistant_api_privacy_right_requests_cascade_info_retrieve`
- `ciso_assistant_api_privacy_right_requests_object_retrieve`
- `ciso_assistant_api_privacy_right_requests_owner_retrieve`
- `ciso_assistant_api_privacy_right_requests_request_type_retrieve`
- `ciso_assistant_api_privacy_right_requests_retrieve`
- `ciso_assistant_api_privacy_right_requests_status_retrieve`
- `ciso_assistant_api_privacy_right_requests_batch_action_create`
- `ciso_assistant_api_privacy_right_requests_create`
- `ciso_assistant_api_privacy_right_requests_update`
- `ciso_assistant_api_privacy_right_requests_partial_update`
- `ciso_assistant_api_privacy_right_requests_destroy`
