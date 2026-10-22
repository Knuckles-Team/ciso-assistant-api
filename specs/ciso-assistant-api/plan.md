# CONN-CISO-ASSISTANT-API — Design and implementation plan

Governing spec: [spec.md](spec.md).

## Existing system and reuse

`get_client` in `ciso_assistant_api/auth.py` calls the SDK `resolve_secret_reference` for each credential reference.
The fix raises the SDK floor. It adds no code and no second resolver.

## Architecture

SDK 0.3.10 serves `env://` references when `OPENBAO_TOKEN_REF` is unset or blank.
The connector image rebuilds on that release, so the deployment secret drops its `OPENBAO_ADDR=""` workaround.

## Interfaces and data model

No wire, schema, or tool change. Log lines carry no credential values.

## Live integration path

An MCP tool calls `get_client` in `ciso_assistant_api/auth.py`, which calls `resolve_secret_reference` in the SDK.

## Quality and release gates

Run `pytest tests/test_credential_refs.py`. No network is used.
Run `pipelines-hook spec-standard` and `pipelines-hook spec-status --write`.

## Risks, alternatives, and decisions

A floor bump is the smallest change. A local resolver would duplicate the SDK rule.
