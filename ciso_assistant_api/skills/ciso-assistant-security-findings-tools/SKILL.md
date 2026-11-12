---
name: ciso-assistant-security-findings-tools
skill_type: skill
description: >-
  Operate the security findings area of CISO Assistant through the ciso-assistant-api MCP server: find, read, create, update and delete its records with one typed tool per API operation. Use when the task needs the security findings records of a governance, risk and compliance program. Do NOT use for areas owned by the other ciso-assistant skills.
license: MIT
tags: [ciso-assistant, grc, security-findings, mcp]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# CISO Assistant: security findings

Each tool maps to exactly one API operation and takes that operation's parameters. Read first (list, then retrieve), and ask for approval before any create, update or delete.

## Rules
- Scope work to one folder or perimeter and cite record ids.
- Never print credentials, tokens or attachment bytes.
- Delete tools (names ending in `_destroy`) need explicit approval and a stated reason.

## Findings
- `ciso_assistant_api_findings_list`
- `ciso_assistant_api_findings_cascade_info_retrieve`
- `ciso_assistant_api_findings_object_retrieve`
- `ciso_assistant_api_findings_owner_retrieve`
- `ciso_assistant_api_findings_priority_retrieve`
- `ciso_assistant_api_findings_retrieve`
- `ciso_assistant_api_findings_sankey_data_retrieve`
- `ciso_assistant_api_findings_severity_retrieve`
- `ciso_assistant_api_findings_status_retrieve`
- `ciso_assistant_api_findings_batch_action_create`
- `ciso_assistant_api_findings_create`
- `ciso_assistant_api_findings_update`
- `ciso_assistant_api_findings_partial_update`
- `ciso_assistant_api_findings_destroy`

## Findings Assessments
- `ciso_assistant_api_findings_assessments_list`
- `ciso_assistant_api_findings_assessments_cascade_info_retrieve`
- `ciso_assistant_api_findings_assessments_category_retrieve`
- `ciso_assistant_api_findings_assessments_md_retrieve`
- `ciso_assistant_api_findings_assessments_metrics_retrieve`
- `ciso_assistant_api_findings_assessments_object_retrieve`
- `ciso_assistant_api_findings_assessments_pdf_retrieve`
- `ciso_assistant_api_findings_assessments_retrieve`
- `ciso_assistant_api_findings_assessments_status_retrieve`
- `ciso_assistant_api_findings_assessments_sunburst_data_retrieve`
- `ciso_assistant_api_findings_assessments_xlsx_retrieve`
- `ciso_assistant_api_findings_assessments_batch_action_create`
- `ciso_assistant_api_findings_assessments_create`
- `ciso_assistant_api_findings_assessments_update`
- `ciso_assistant_api_findings_assessments_partial_update`
- `ciso_assistant_api_findings_assessments_destroy`

## Security Advisories
- `ciso_assistant_api_security_advisories_list`
- `ciso_assistant_api_security_advisories_autocomplete_retrieve`
- `ciso_assistant_api_security_advisories_cascade_info_retrieve`
- `ciso_assistant_api_security_advisories_object_retrieve`
- `ciso_assistant_api_security_advisories_retrieve`
- `ciso_assistant_api_security_advisories_source_retrieve`
- `ciso_assistant_api_security_advisories_batch_action_create`
- `ciso_assistant_api_security_advisories_create`
- `ciso_assistant_api_security_advisories_enrich_create`
- `ciso_assistant_api_security_advisories_sync_euvd_create`
- `ciso_assistant_api_security_advisories_sync_kev_create`
- `ciso_assistant_api_security_advisories_update`
- `ciso_assistant_api_security_advisories_partial_update`
- `ciso_assistant_api_security_advisories_destroy`

## Security Exceptions
- `ciso_assistant_api_security_exceptions_list`
- `ciso_assistant_api_security_exceptions_cascade_info_retrieve`
- `ciso_assistant_api_security_exceptions_export_csv_retrieve`
- `ciso_assistant_api_security_exceptions_export_xlsx_retrieve`
- `ciso_assistant_api_security_exceptions_object_retrieve`
- `ciso_assistant_api_security_exceptions_retrieve`
- `ciso_assistant_api_security_exceptions_sankey_data_retrieve`
- `ciso_assistant_api_security_exceptions_severity_retrieve`
- `ciso_assistant_api_security_exceptions_status_retrieve`
- `ciso_assistant_api_security_exceptions_batch_action_create`
- `ciso_assistant_api_security_exceptions_create`
- `ciso_assistant_api_security_exceptions_update`
- `ciso_assistant_api_security_exceptions_partial_update`
- `ciso_assistant_api_security_exceptions_destroy`
