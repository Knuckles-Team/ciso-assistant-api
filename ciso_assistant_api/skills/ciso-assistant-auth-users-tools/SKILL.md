---
name: ciso-assistant-auth-users-tools
skill_type: skill
description: >-
  Operate the auth users area of CISO Assistant through the ciso-assistant-api MCP server: find, read, create, update and delete its records with one typed tool per API operation. Use when the task needs the auth users records of a governance, risk and compliance program. Do NOT use for areas owned by the other ciso-assistant skills.
license: MIT
tags: [ciso-assistant, grc, auth-users, mcp]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# CISO Assistant: auth users

Each tool maps to exactly one API operation and takes that operation's parameters. Read first (list, then retrieve), and ask for approval before any create, update or delete.

## Rules
- Scope work to one folder or perimeter and cite record ids.
- Never print credentials, tokens or attachment bytes.
- Delete tools (names ending in `_destroy`) need explicit approval and a stated reason.

## Steps

1. List the candidate records with `ciso_assistant_api_role_assignments_list`, passing the narrowest filters and a bounded limit. Verify the response holds records from the intended folder or perimeter before going further.
2. Read the exact record with `ciso_assistant_api_iam_auth_tokens_retrieve` using an id taken from the list. Verify the returned id equals the id you intend to cite.
3. After operator approval of the stated change, call `ciso_assistant_api_iam_auth_tokens_create` once with the approved parameters. Verify the response echoes the submitted fields and returns a new record id.
4. Remove a record only with `ciso_assistant_api_iam_auth_tokens_destroy`, after explicit approval and a stated reason. Verify with `ciso_assistant_api_iam_auth_tokens_retrieve` that the record is no longer returned.

## Failure recovery

| Failure | Cause | Recovery |
| --- | --- | --- |
| Tool returns an authentication or permission error | Connector credentials are missing, expired or lack rights on this area | Stop and report the error to the operator without printing any token; resume with `ciso_assistant_api_role_assignments_list` after the operator confirms refreshed credentials. |
| List result is empty | Filters or folder scope exclude the records | Call `ciso_assistant_api_role_assignments_list` with the filters removed, then narrow again using the folder id of a record you can already see. |
| Retrieve reports not found | The id is wrong or stale | Call `ciso_assistant_api_role_assignments_list` again and copy the id from the fresh result before calling `ciso_assistant_api_iam_auth_tokens_retrieve`. |
| Delete is refused or approval is missing | No explicit approval or reason was recorded | Do not call `ciso_assistant_api_iam_auth_tokens_destroy`; ask the operator for approval with a reason, then call `ciso_assistant_api_iam_auth_tokens_destroy` with that approval. |

## Accounts
- `ciso_assistant_api_accounts_saml_download_cert_retrieve`
- `ciso_assistant_api_accounts_saml_generate_keys_create`

## Csrf
- `ciso_assistant_api_csrf_retrieve`

## Iam
- `ciso_assistant_api_iam_auth_tokens_retrieve`
- `ciso_assistant_api_iam_current_user_retrieve`
- `ciso_assistant_api_iam_auth_tokens_create`
- `ciso_assistant_api_iam_change_password_create`
- `ciso_assistant_api_iam_login_create`
- `ciso_assistant_api_iam_logout_create`
- `ciso_assistant_api_iam_logoutall_create`
- `ciso_assistant_api_iam_password_reset_confirm_create`
- `ciso_assistant_api_iam_password_reset_create`
- `ciso_assistant_api_iam_revoke_sessions_create`
- `ciso_assistant_api_iam_session_token_create`
- `ciso_assistant_api_iam_set_password_create`
- `ciso_assistant_api_iam_auth_tokens_destroy`

## Role Assignments
- `ciso_assistant_api_role_assignments_list`
- `ciso_assistant_api_role_assignments_cascade_info_retrieve`
- `ciso_assistant_api_role_assignments_object_retrieve`
- `ciso_assistant_api_role_assignments_retrieve`
- `ciso_assistant_api_role_assignments_batch_action_create`
- `ciso_assistant_api_role_assignments_create`
- `ciso_assistant_api_role_assignments_update`
- `ciso_assistant_api_role_assignments_partial_update`
- `ciso_assistant_api_role_assignments_destroy`

## Teams
- `ciso_assistant_api_teams_list`
- `ciso_assistant_api_teams_cascade_info_retrieve`
- `ciso_assistant_api_teams_object_retrieve`
- `ciso_assistant_api_teams_retrieve`
- `ciso_assistant_api_teams_batch_action_create`
- `ciso_assistant_api_teams_create`
- `ciso_assistant_api_teams_update`
- `ciso_assistant_api_teams_partial_update`
- `ciso_assistant_api_teams_destroy`

## User Groups
- `ciso_assistant_api_user_groups_list`
- `ciso_assistant_api_user_groups_cascade_info_retrieve`
- `ciso_assistant_api_user_groups_object_retrieve`
- `ciso_assistant_api_user_groups_retrieve`
- `ciso_assistant_api_user_groups_batch_action_create`
- `ciso_assistant_api_user_groups_create`
- `ciso_assistant_api_user_groups_update`
- `ciso_assistant_api_user_groups_partial_update`
- `ciso_assistant_api_user_groups_destroy`

## User Preferences
- `ciso_assistant_api_user_preferences_retrieve`
- `ciso_assistant_api_user_preferences_partial_update`

## Users
- `ciso_assistant_api_users_list`
- `ciso_assistant_api_users_cascade_info_retrieve`
- `ciso_assistant_api_users_object_retrieve`
- `ciso_assistant_api_users_retrieve`
- `ciso_assistant_api_users_batch_action_create`
- `ciso_assistant_api_users_create`
- `ciso_assistant_api_users_update`
- `ciso_assistant_api_users_partial_update`
- `ciso_assistant_api_users_destroy`
