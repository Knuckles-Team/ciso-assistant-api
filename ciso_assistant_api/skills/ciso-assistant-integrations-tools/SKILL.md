---
name: ciso-assistant-integrations-tools
skill_type: skill
description: >-
  Operate the integrations area of CISO Assistant through the ciso-assistant-api MCP server: find, read, create, update and delete its records with one typed tool per API operation. Use when the task needs the integrations records of a governance, risk and compliance program. Do NOT use for areas owned by the other ciso-assistant skills.
license: MIT
tags: [ciso-assistant, grc, integrations, mcp]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# CISO Assistant: integrations

Each tool maps to exactly one API operation and takes that operation's parameters. Read first (list, then retrieve), and ask for approval before any create, update or delete.

## Rules
- Scope work to one folder or perimeter and cite record ids.
- Never print credentials, tokens or attachment bytes.
- Delete tools (names ending in `_destroy`) need explicit approval and a stated reason.

## Attachment Metadata
- `ciso_assistant_serdes_attachment_metadata_retrieve`

## Batch Download Attachments
- `ciso_assistant_serdes_batch_download_attachments_create`

## Batch Upload Attachments
- `ciso_assistant_serdes_batch_upload_attachments_create`

## Build
- `ciso_assistant_api_build_retrieve`

## Content Types
- `ciso_assistant_api_content_types_retrieve`

## Data Wizard
- `ciso_assistant_api_data_wizard_load_file_create`

## Dump Db
- `ciso_assistant_serdes_dump_db_retrieve`

## Full Restore
- `ciso_assistant_serdes_full_restore_create`

## Health
- `ciso_assistant_api_health_retrieve`

## Integrations
- `ciso_assistant_api_integrations_configs_list`
- `ciso_assistant_api_integrations_providers_list`
- `ciso_assistant_api_integrations_configs_cascade_info_retrieve`
- `ciso_assistant_api_integrations_configs_object_retrieve`
- `ciso_assistant_api_integrations_configs_remote_objects_retrieve`
- `ciso_assistant_api_integrations_configs_retrieve`
- `ciso_assistant_api_integrations_configs_batch_action_create`
- `ciso_assistant_api_integrations_configs_create`
- `ciso_assistant_api_integrations_configs_rpc_create`
- `ciso_assistant_api_integrations_configs_test_connection_create`
- `ciso_assistant_api_integrations_test_connection_create`
- `ciso_assistant_api_integrations_configs_update`
- `ciso_assistant_api_integrations_configs_partial_update`
- `ciso_assistant_api_integrations_configs_destroy`
- `ciso_assistant_api_integrations_sync_mappings_destroy`

## Load Backup
- `ciso_assistant_serdes_load_backup_create`

## Search
- `ciso_assistant_api_search_retrieve`

## Serdes
- `ciso_assistant_api_serdes_attachment_metadata_retrieve`
- `ciso_assistant_api_serdes_dump_db_retrieve`
- `ciso_assistant_api_serdes_batch_download_attachments_create`
- `ciso_assistant_api_serdes_batch_upload_attachments_create`
- `ciso_assistant_api_serdes_full_restore_create`
- `ciso_assistant_api_serdes_load_backup_create`

## Webhooks
- `ciso_assistant_api_webhooks_audit_sinks_list`
- `ciso_assistant_api_webhooks_endpoints_list`
- `ciso_assistant_api_webhooks_audit_sinks_cascade_info_retrieve`
- `ciso_assistant_api_webhooks_audit_sinks_object_retrieve`
- `ciso_assistant_api_webhooks_audit_sinks_retrieve`
- `ciso_assistant_api_webhooks_endpoints_cascade_info_retrieve`
- `ciso_assistant_api_webhooks_endpoints_object_retrieve`
- `ciso_assistant_api_webhooks_endpoints_retrieve`
- `ciso_assistant_api_webhooks_event_types_retrieve`
- `ciso_assistant_api_webhooks_audit_sinks_batch_action_create`
- `ciso_assistant_api_webhooks_audit_sinks_create`
- `ciso_assistant_api_webhooks_audit_sinks_replay_create`
- `ciso_assistant_api_webhooks_endpoints_batch_action_create`
- `ciso_assistant_api_webhooks_endpoints_create`
- `ciso_assistant_api_webhooks_audit_sinks_update`
- `ciso_assistant_api_webhooks_endpoints_update`
- `ciso_assistant_api_webhooks_audit_sinks_partial_update`
- `ciso_assistant_api_webhooks_endpoints_partial_update`
- `ciso_assistant_api_webhooks_audit_sinks_destroy`
- `ciso_assistant_api_webhooks_endpoints_destroy`
