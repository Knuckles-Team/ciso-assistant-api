---
name: ciso-assistant-chat-tools
skill_type: skill
description: >-
  Operate the chat area of CISO Assistant through the ciso-assistant-api MCP server: find, read, create, update and delete its records with one typed tool per API operation. Use when the task needs the chat records of a governance, risk and compliance program. Do NOT use for areas owned by the other ciso-assistant skills.
license: MIT
tags: [ciso-assistant, grc, chat, mcp]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# CISO Assistant: chat

Each tool maps to exactly one API operation and takes that operation's parameters. Read first (list, then retrieve), and ask for approval before any create, update or delete.

## Rules
- Scope work to one folder or perimeter and cite record ids.
- Never print credentials, tokens or attachment bytes.
- Delete tools (names ending in `_destroy`) need explicit approval and a stated reason.

## Chat Agent Actions
- `ciso_assistant_api_chat_agent_actions_list`
- `ciso_assistant_api_chat_agent_actions_cascade_info_retrieve`
- `ciso_assistant_api_chat_agent_actions_object_retrieve`
- `ciso_assistant_api_chat_agent_actions_retrieve`
- `ciso_assistant_api_chat_agent_actions_approve_create`
- `ciso_assistant_api_chat_agent_actions_batch_action_create`
- `ciso_assistant_api_chat_agent_actions_create`
- `ciso_assistant_api_chat_agent_actions_reject_create`

## Chat Agent Runs
- `ciso_assistant_api_chat_agent_runs_list`
- `ciso_assistant_api_chat_agent_runs_cascade_info_retrieve`
- `ciso_assistant_api_chat_agent_runs_object_retrieve`
- `ciso_assistant_api_chat_agent_runs_retrieve`
- `ciso_assistant_api_chat_agent_runs_batch_action_create`
- `ciso_assistant_api_chat_agent_runs_cancel_create`
- `ciso_assistant_api_chat_agent_runs_create`
- `ciso_assistant_api_chat_agent_runs_start_questionnaire_prefill_create`

## Chat Documents
- `ciso_assistant_api_chat_documents_list`
- `ciso_assistant_api_chat_documents_cascade_info_retrieve`
- `ciso_assistant_api_chat_documents_object_retrieve`
- `ciso_assistant_api_chat_documents_retrieve`
- `ciso_assistant_api_chat_documents_batch_action_create`
- `ciso_assistant_api_chat_documents_create`
- `ciso_assistant_api_chat_documents_update`
- `ciso_assistant_api_chat_documents_partial_update`
- `ciso_assistant_api_chat_documents_destroy`

## Chat Ollama Models
- `ciso_assistant_api_chat_ollama_models_retrieve`

## Chat Questionnaire Questions
- `ciso_assistant_api_chat_questionnaire_questions_list`
- `ciso_assistant_api_chat_questionnaire_questions_cascade_info_retrieve`
- `ciso_assistant_api_chat_questionnaire_questions_object_retrieve`
- `ciso_assistant_api_chat_questionnaire_questions_retrieve`
- `ciso_assistant_api_chat_questionnaire_questions_batch_action_create`
- `ciso_assistant_api_chat_questionnaire_questions_create`
- `ciso_assistant_api_chat_questionnaire_questions_create_and_retry_create`
- `ciso_assistant_api_chat_questionnaire_questions_retry_with_control_create`
- `ciso_assistant_api_chat_questionnaire_questions_suggest_control_create`
- `ciso_assistant_api_chat_questionnaire_questions_update`
- `ciso_assistant_api_chat_questionnaire_questions_partial_update`
- `ciso_assistant_api_chat_questionnaire_questions_destroy`

## Chat Questionnaire Runs
- `ciso_assistant_api_chat_questionnaire_runs_list`
- `ciso_assistant_api_chat_questionnaire_runs_cascade_info_retrieve`
- `ciso_assistant_api_chat_questionnaire_runs_export_retrieve`
- `ciso_assistant_api_chat_questionnaire_runs_object_retrieve`
- `ciso_assistant_api_chat_questionnaire_runs_retrieve`
- `ciso_assistant_api_chat_questionnaire_runs_batch_action_create`
- `ciso_assistant_api_chat_questionnaire_runs_create`
- `ciso_assistant_api_chat_questionnaire_runs_extract_questions_create`
- `ciso_assistant_api_chat_questionnaire_runs_upload_create`
- `ciso_assistant_api_chat_questionnaire_runs_update`
- `ciso_assistant_api_chat_questionnaire_runs_mapping_partial_update`
- `ciso_assistant_api_chat_questionnaire_runs_partial_update`
- `ciso_assistant_api_chat_questionnaire_runs_destroy`

## Chat Sessions
- `ciso_assistant_api_chat_sessions_list`
- `ciso_assistant_api_chat_sessions_cascade_info_retrieve`
- `ciso_assistant_api_chat_sessions_object_retrieve`
- `ciso_assistant_api_chat_sessions_retrieve`
- `ciso_assistant_api_chat_sessions_batch_action_create`
- `ciso_assistant_api_chat_sessions_create`
- `ciso_assistant_api_chat_sessions_message_create`
- `ciso_assistant_api_chat_sessions_upload_create`
- `ciso_assistant_api_chat_sessions_update`
- `ciso_assistant_api_chat_sessions_partial_update`
- `ciso_assistant_api_chat_sessions_destroy`

## Chat Status
- `ciso_assistant_api_chat_status_retrieve`
