---
name: ciso-assistant-assets-tools
skill_type: skill
description: >-
  Operate the assets area of CISO Assistant through the ciso-assistant-api MCP server: find, read, create, update and delete its records with one typed tool per API operation. Use when the task needs the assets records of a governance, risk and compliance program. Do NOT use for areas owned by the other ciso-assistant skills.
license: MIT
tags: [ciso-assistant, grc, assets, mcp]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# CISO Assistant: assets

Each tool maps to exactly one API operation and takes that operation's parameters. Read first (list, then retrieve), and ask for approval before any create, update or delete.

## Rules
- Scope work to one folder or perimeter and cite record ids.
- Never print credentials, tokens or attachment bytes.
- Delete tools (names ending in `_destroy`) need explicit approval and a stated reason.

## Asset Capabilities
- `ciso_assistant_api_asset_capabilities_list`
- `ciso_assistant_api_asset_capabilities_cascade_info_retrieve`
- `ciso_assistant_api_asset_capabilities_object_retrieve`
- `ciso_assistant_api_asset_capabilities_retrieve`
- `ciso_assistant_api_asset_capabilities_batch_action_create`
- `ciso_assistant_api_asset_capabilities_create`
- `ciso_assistant_api_asset_capabilities_update`
- `ciso_assistant_api_asset_capabilities_partial_update`
- `ciso_assistant_api_asset_capabilities_destroy`

## Asset Class
- `ciso_assistant_api_asset_class_list`
- `ciso_assistant_api_asset_class_cascade_info_retrieve`
- `ciso_assistant_api_asset_class_object_retrieve`
- `ciso_assistant_api_asset_class_retrieve`
- `ciso_assistant_api_asset_class_tree_retrieve`
- `ciso_assistant_api_asset_class_batch_action_create`
- `ciso_assistant_api_asset_class_create`
- `ciso_assistant_api_asset_class_update`
- `ciso_assistant_api_asset_class_partial_update`
- `ciso_assistant_api_asset_class_destroy`

## Assets
- `ciso_assistant_api_assets_list`
- `ciso_assistant_api_assets_asset_class_retrieve`
- `ciso_assistant_api_assets_autocomplete_retrieve`
- `ciso_assistant_api_assets_cascade_info_retrieve`
- `ciso_assistant_api_assets_disaster_recovery_objectives_retrieve`
- `ciso_assistant_api_assets_dora_criticality_assessment_retrieve`
- `ciso_assistant_api_assets_dora_discontinuing_impact_retrieve`
- `ciso_assistant_api_assets_dora_licenced_activity_retrieve`
- `ciso_assistant_api_assets_export_csv_retrieve`
- `ciso_assistant_api_assets_export_xlsx_retrieve`
- `ciso_assistant_api_assets_graph_retrieve`
- `ciso_assistant_api_assets_ids_retrieve`
- `ciso_assistant_api_assets_object_retrieve`
- `ciso_assistant_api_assets_retrieve`
- `ciso_assistant_api_assets_security_objectives_retrieve`
- `ciso_assistant_api_assets_type_retrieve`
- `ciso_assistant_api_assets_batch_action_create`
- `ciso_assistant_api_assets_batch_create_create`
- `ciso_assistant_api_assets_create`
- `ciso_assistant_api_assets_update`
- `ciso_assistant_api_assets_partial_update`
- `ciso_assistant_api_assets_destroy`
