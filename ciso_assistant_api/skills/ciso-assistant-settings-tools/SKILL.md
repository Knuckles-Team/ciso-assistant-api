---
name: ciso-assistant-settings-tools
skill_type: skill
description: >-
  Operate the admin area of CISO Assistant through the ciso-assistant-api MCP server: find, read, create, update and delete its records with one typed tool per API operation. Use when the task needs the admin records of a governance, risk and compliance program. Do NOT use for areas owned by the other ciso-assistant skills.
license: MIT
tags: [ciso-assistant, grc, admin, mcp]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# CISO Assistant: admin

Each tool maps to exactly one API operation and takes that operation's parameters. Read first (list, then retrieve), and ask for approval before any create, update or delete.

## Rules
- Scope work to one folder or perimeter and cite record ids.
- Never print credentials, tokens or attachment bytes.
- Delete tools (names ending in `_destroy`) need explicit approval and a stated reason.

## Api Request
- `ciso_assistant_api_request`

## Settings Feature Flags
- `ciso_assistant_api_settings_feature_flags_retrieve`
- `ciso_assistant_api_settings_feature_flags_update`
- `ciso_assistant_api_settings_feature_flags_partial_update`

## Settings General
- `ciso_assistant_api_settings_general_default_custom_analytics_dashboard_retrieve`
- `ciso_assistant_api_settings_general_default_language_retrieve`
- `ciso_assistant_api_settings_general_ebios_radar_parameters_retrieve`
- `ciso_assistant_api_settings_general_interface_settings_retrieve`
- `ciso_assistant_api_settings_general_notifications_settings_retrieve`
- `ciso_assistant_api_settings_general_object_retrieve`
- `ciso_assistant_api_settings_general_retrieve`
- `ciso_assistant_api_settings_general_security_objective_scale_retrieve`
- `ciso_assistant_api_settings_general_force_language_create`
- `ciso_assistant_api_settings_general_set_default_dashboard_create`
- `ciso_assistant_api_settings_general_update`
- `ciso_assistant_api_settings_general_partial_update`
- `ciso_assistant_api_settings_general_default_language_retrieve_2`

## Settings Global
- `ciso_assistant_api_settings_global_list`
- `ciso_assistant_api_settings_global_retrieve`
- `ciso_assistant_api_settings_global_create`
- `ciso_assistant_api_settings_global_update`
- `ciso_assistant_api_settings_global_partial_update`
- `ciso_assistant_api_settings_global_destroy`

## Settings Sec Intel Feeds
- `ciso_assistant_api_settings_sec_intel_feeds_retrieve`
- `ciso_assistant_api_settings_sec_intel_feeds_update`
- `ciso_assistant_api_settings_sec_intel_feeds_partial_update`

## Settings Sso
- `ciso_assistant_api_settings_sso_cascade_info_retrieve`
- `ciso_assistant_api_settings_sso_info_retrieve`
- `ciso_assistant_api_settings_sso_object_retrieve`
- `ciso_assistant_api_settings_sso_provider_retrieve`
- `ciso_assistant_api_settings_sso_retrieve`
- `ciso_assistant_api_settings_sso_update`
- `ciso_assistant_api_settings_sso_partial_update`

## Settings Vulnerability Sla
- `ciso_assistant_api_settings_vulnerability_sla_retrieve`
- `ciso_assistant_api_settings_vulnerability_sla_update`
- `ciso_assistant_api_settings_vulnerability_sla_partial_update`
