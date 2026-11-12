# CONN-CISO-ASSISTANT-API-CONNECTOR-CONTENT — Implementation plan

Governing spec: [spec.md](spec.md). Rows: [requirements.md](requirements.md).

## Summary

`pyproject.toml` declares `ciso-assistant-mcp` as the connector identity. `create_mcp_server` resolves the packaged content of `ciso_assistant_api` from it.

## Technical Context

- **Language/Version**: Python 3.14 (floor 3.12)
- **Primary Dependencies**: scion-sdk, fastmcp
- **Storage**: N/A; the connector stores nothing
- **Testing**: pytest; the proof level each row names
- **Target Platform**: Linux containers
- **Project Type**: connector (MCP server)
- **Performance Goals**: N/A
- **Constraints**: one tool per API operation; shared capabilities come from the SDK
- **Scale/Scope**: 2 rows

## Constitution Check

- One owner per concept: pass. The connector owns one external system's calls, mappings and tools only.
- Connectors depend on the SDK and are called through arbora: pass.
- No ratchets: pass. The rows add no suppression.

## Project Structure

```text
pyproject.toml  existing
tests/test_default_content_surfaces.py  existing
ciso_assistant_api/mcp_server.py  existing
ciso_assistant_api/ontology/certification.json  existing
```

## Phase 0: Research

No unknowns. Each row names the code it touches.

## Phase 1: Design

The rows are delivered in place; the design is the caller chain below.

## Phase 2: Task approach

`tasks.md` holds one task line per row, producer first.

## Complexity Tracking

None. The constitution check passed.

## Build contract

The repository pre-commit hooks apply: `ruff`. Each row names its proving test. No suppression and no duplicate implementation.

## Production caller chain

1. `CONN-CISO-ASSISTANT-API-CONNECTOR-CONTENT-R001`: the `ciso-assistant-mcp = ciso_assistant_api:connector` entry point in `pyproject.toml` -> `ciso_assistant_api/__init__.py::connector` (line 76) -> SDK `build_server("ciso_assistant_api")` called by `ciso_assistant_api/mcp_server.py::get_mcp_instance` (line 72), serving the packaged skills, prompts and ontology.
2. `CONN-CISO-ASSISTANT-API-CONNECTOR-CONTENT-R002`: arbora `fleet.call` -> typed tools `ciso_assistant_api_applied_controls_list` and `ciso_assistant_api_risk_scenarios_list` registered by `register_server_surface` (`ciso_assistant_api/mcp_server.py`) -> `ciso_assistant_api/api/` client; the new `ontology/access_contracts.ttl` does not exist yet.

## Cross-repo seams

none. The cited owner rows are library capabilities the connector calls in process; spec.md names them.
