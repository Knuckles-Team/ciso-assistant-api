# CONN-CISO-ASSISTANT-API — Implementation plan

Governing spec: [spec.md](spec.md). Rows: [requirements.md](requirements.md).

## Summary

`get_client` in `ciso_assistant_api/auth.py` calls the SDK `resolve_secret_reference` for each credential reference. The fix raises the SDK floor. It adds no code and no second resolver. SDK 0.3.10 serves `env://` references when `OPENBAO_TOKEN_REF` is unset or blank. The connector image rebuilds on that release, so the deployment secret drops its `OPENBAO_ADDR=""` workaround.

## Technical Context

- **Language/Version**: Python 3.14 (floor 3.12)
- **Primary Dependencies**: scion-sdk, fastmcp
- **Storage**: N/A; the connector stores nothing
- **Testing**: pytest; the proof level each row names
- **Target Platform**: Linux containers
- **Project Type**: connector (MCP server)
- **Performance Goals**: N/A
- **Constraints**: one tool per API operation; shared capabilities come from the SDK
- **Scale/Scope**: 4 rows

## Constitution Check

- One owner per concept: pass. The connector owns one external system's calls, mappings and tools only.
- Connectors depend on the SDK and are called through arbora: pass.
- No ratchets: pass. The rows add no suppression.

## Project Structure

```text
pyproject.toml  existing
ciso_assistant_api/auth.py  existing
ciso_assistant_api/api/api_client_base.py  existing
tests/test_auth.py  existing
tests/test_fleet_name.py  existing
```

## Phase 0: Research

No unknowns. Each row names the code it touches.

## Phase 1: Design

### Interfaces and data model

No wire, schema, or tool change. Log lines carry no credential values.

### Live integration path

An MCP tool calls `get_client` in `ciso_assistant_api/auth.py`, which calls `resolve_secret_reference` in the SDK.

### Quality and release gates

Run `pytest tests/test_credential_refs.py`. No network is used.
Run `pipelines-hook spec-standard` and `pipelines-hook spec-status --write`.

### Risks, alternatives, and decisions

A floor bump is the smallest change. A local resolver would duplicate the SDK rule.

## Phase 2: Task approach

`tasks.md` holds one task line per row, producer first.

## Complexity Tracking

None. The constitution check passed.

## Build contract

The repository pre-commit hooks apply: `ruff`. Each row names its proving test. No suppression and no duplicate implementation.

## Production caller chain

1. `CONN-CISO-ASSISTANT-API-R001`: the `ciso-assistant-mcp` console script (`ciso_assistant_api.mcp_server:mcp_server`, line 79) -> `get_mcp_instance` (line 72) -> SDK `build_server("ciso_assistant_api")` -> `get_client` (`ciso_assistant_api/auth.py` line 53), whose secret resolution depends on the SDK floor declared in `pyproject.toml`.
2. `CONN-CISO-ASSISTANT-API-R002`: `ciso_assistant_api/mcp_server.py::register_server_surface` (line 32) passes `get_client` to `register_tool_surface` -> `get_client` (`ciso_assistant_api/auth.py` line 53) -> `_resolve_optional_secret` (line 120) -> `scion_sdk.credentials.resolution.resolve_secret_reference`.
3. `CONN-CISO-ASSISTANT-API-R003`: any API tool call -> `Api` client method in `ciso_assistant_api/api/` -> `_auth_headers` (`ciso_assistant_api/api/api_client_base.py` line 152) -> `_ensure_token` (line 116), which posts the headless login when no token is configured.
4. `CONN-CISO-ASSISTANT-API-R004`: the `ciso-assistant-mcp = ciso_assistant_api:connector` entry point in `pyproject.toml` -> `ciso_assistant_api/__init__.py::connector` (line 76) -> `IngestBinding` and `ConnectorContent` calls that carry the connector name.

## Cross-repo seams

none. The cited owner rows are library capabilities the connector calls in process; spec.md names them.
