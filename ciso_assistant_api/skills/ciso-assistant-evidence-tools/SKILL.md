---
name: ciso-assistant-evidence-tools
skill_type: skill
description: >-
  Operate the evidence area of CISO Assistant through the ciso-assistant-api MCP server: find, read, create, update and delete its records with one typed tool per API operation. Use when the task needs the evidence records of a governance, risk and compliance program. Do NOT use for areas owned by the other ciso-assistant skills.
license: MIT
tags: [ciso-assistant, grc, evidence, mcp]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# CISO Assistant: evidence

Each tool maps to exactly one API operation and takes that operation's parameters. Read first (list, then retrieve), and ask for approval before any create, update or delete.

## Rules
- Scope work to one folder or perimeter and cite record ids.
- Never print credentials, tokens or attachment bytes.
- Delete tools (names ending in `_destroy`) need explicit approval and a stated reason.

## Steps

1. List the candidate records with `ciso_assistant_api_document_revisions_list`, passing the narrowest filters and a bounded limit. Verify the response holds records from the intended folder or perimeter before going further.
2. Read the exact record with `ciso_assistant_api_document_attachments_retrieve` using an id taken from the list. Verify the returned id equals the id you intend to cite.
3. After operator approval of the stated change, call `ciso_assistant_api_document_attachments_create` once with the approved parameters. Verify the response echoes the submitted fields and returns a new record id.
4. Remove a record only with `ciso_assistant_api_document_attachments_destroy`, after explicit approval and a stated reason. Verify with `ciso_assistant_api_document_attachments_retrieve` that the record is no longer returned.

## Failure recovery

| Failure | Cause | Recovery |
| --- | --- | --- |
| Tool returns an authentication or permission error | Connector credentials are missing, expired or lack rights on this area | Stop and report the error to the operator without printing any token; resume with `ciso_assistant_api_document_revisions_list` after the operator confirms refreshed credentials. |
| List result is empty | Filters or folder scope exclude the records | Call `ciso_assistant_api_document_revisions_list` with the filters removed, then narrow again using the folder id of a record you can already see. |
| Retrieve reports not found | The id is wrong or stale | Call `ciso_assistant_api_document_revisions_list` again and copy the id from the fresh result before calling `ciso_assistant_api_document_attachments_retrieve`. |
| Delete is refused or approval is missing | No explicit approval or reason was recorded | Do not call `ciso_assistant_api_document_attachments_destroy`; ask the operator for approval with a reason, then call `ciso_assistant_api_document_attachments_destroy` with that approval. |

## Document Attachments
- `ciso_assistant_api_document_attachments_cascade_info_retrieve`
- `ciso_assistant_api_document_attachments_file_retrieve`
- `ciso_assistant_api_document_attachments_object_retrieve`
- `ciso_assistant_api_document_attachments_retrieve`
- `ciso_assistant_api_document_attachments_batch_action_create`
- `ciso_assistant_api_document_attachments_create`
- `ciso_assistant_api_document_attachments_update`
- `ciso_assistant_api_document_attachments_partial_update`
- `ciso_assistant_api_document_attachments_destroy`
- `ciso_assistant_api_document_attachments_retrieve_2`

## Document Revisions
- `ciso_assistant_api_document_revisions_list`
- `ciso_assistant_api_document_revisions_cascade_info_retrieve`
- `ciso_assistant_api_document_revisions_diff_retrieve`
- `ciso_assistant_api_document_revisions_edit_diff_retrieve`
- `ciso_assistant_api_document_revisions_edit_history_retrieve`
- `ciso_assistant_api_document_revisions_edit_snapshot_retrieve`
- `ciso_assistant_api_document_revisions_editing_status_retrieve`
- `ciso_assistant_api_document_revisions_export_pdf_retrieve`
- `ciso_assistant_api_document_revisions_object_retrieve`
- `ciso_assistant_api_document_revisions_retrieve`
- `ciso_assistant_api_document_revisions_status_retrieve`
- `ciso_assistant_api_document_revisions_approve_create`
- `ciso_assistant_api_document_revisions_batch_action_create`
- `ciso_assistant_api_document_revisions_create`
- `ciso_assistant_api_document_revisions_publish_create`
- `ciso_assistant_api_document_revisions_request_changes_create`
- `ciso_assistant_api_document_revisions_start_editing_create`
- `ciso_assistant_api_document_revisions_stop_editing_create`
- `ciso_assistant_api_document_revisions_submit_for_review_create`
- `ciso_assistant_api_document_revisions_take_over_editing_create`
- `ciso_assistant_api_document_revisions_update`
- `ciso_assistant_api_document_revisions_partial_update`
- `ciso_assistant_api_document_revisions_destroy`

## Evidence Revisions
- `ciso_assistant_api_evidence_revisions_list`
- `ciso_assistant_api_evidence_revisions_attachment_retrieve`
- `ciso_assistant_api_evidence_revisions_cascade_info_retrieve`
- `ciso_assistant_api_evidence_revisions_object_retrieve`
- `ciso_assistant_api_evidence_revisions_retrieve`
- `ciso_assistant_api_evidence_revisions_batch_action_create`
- `ciso_assistant_api_evidence_revisions_create`
- `ciso_assistant_api_evidence_revisions_delete_attachment_create`
- `ciso_assistant_api_evidence_revisions_upload_create`
- `ciso_assistant_api_evidence_revisions_update`
- `ciso_assistant_api_evidence_revisions_partial_update`
- `ciso_assistant_api_evidence_revisions_destroy`

## Evidences
- `ciso_assistant_api_evidences_list`
- `ciso_assistant_api_evidences_attachment_retrieve`
- `ciso_assistant_api_evidences_cascade_info_retrieve`
- `ciso_assistant_api_evidences_object_retrieve`
- `ciso_assistant_api_evidences_owner_retrieve`
- `ciso_assistant_api_evidences_retrieve`
- `ciso_assistant_api_evidences_status_retrieve`
- `ciso_assistant_api_evidences_batch_action_create`
- `ciso_assistant_api_evidences_batch_upload_create`
- `ciso_assistant_api_evidences_create`
- `ciso_assistant_api_evidences_upload_create`
- `ciso_assistant_api_evidences_update`
- `ciso_assistant_api_evidences_partial_update`
- `ciso_assistant_api_evidences_destroy`

## Managed Documents
- `ciso_assistant_api_managed_documents_list`
- `ciso_assistant_api_managed_documents_cascade_info_retrieve`
- `ciso_assistant_api_managed_documents_object_retrieve`
- `ciso_assistant_api_managed_documents_retrieve`
- `ciso_assistant_api_managed_documents_templates_retrieve`
- `ciso_assistant_api_managed_documents_batch_action_create`
- `ciso_assistant_api_managed_documents_create`
- `ciso_assistant_api_managed_documents_create_new_draft_create`
- `ciso_assistant_api_managed_documents_upload_image_create`
- `ciso_assistant_api_managed_documents_update`
- `ciso_assistant_api_managed_documents_partial_update`
- `ciso_assistant_api_managed_documents_destroy`
