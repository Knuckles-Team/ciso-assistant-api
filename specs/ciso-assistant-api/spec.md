# CONN-CISO-ASSISTANT-API — Credential reference resolution

## Outcome

The connector must resolve `env://` credential references when `OPENBAO_ADDR` is set and `OPENBAO_TOKEN_REF` is not.
The connector must start in a pod that carries the fleet-wide `OPENBAO_ADDR` without a per-service workaround.

## Scope and owner

The `ciso-assistant-api` repository owns CISO Assistant calls and its dependency floor on the SDK.
The shared connector SDK owns credential reference resolution.
The shared pipelines repository owns quality gates and delivery rendering.

Component: Connector integration
Code: ../../pyproject.toml ../../ciso_assistant_api/auth.py ../../ciso_assistant_api/api/api_client_base.py ../../tests/test_auth.py ../../tests/test_credential_refs.py

## Non-goals

This specification grants no service access and creates no credentials.
The connector must not log credential values.

## Why a new spec

The repository holds no local spec. The search of `specs/` found only the template.
The SDK owns the resolver rule (`SCION-CONNECTOR-CONTROL-R035`); this connector owns only its floor on that release.

## Requirements

See [requirements.md](requirements.md), [plan.md](plan.md), and [test-spec.md](test-spec.md).

## Scope and interfaces

In scope: the rows of [requirements.md](requirements.md). Out of scope: the SDK modules and the engine, which own the shared capabilities.

## User Scenarios & Testing

### User Story 1 - Credential reference resolution (Priority: P1)

The connector must resolve `env://` credential references when `OPENBAO_ADDR` is set and `OPENBAO_TOKEN_REF` is not.

**Acceptance Scenarios**:

1. **Given** the connector is configured, **When** the behaviour of row `CONN-CISO-ASSISTANT-API-R001` (sdk floor) is exercised, **Then** `tests/test_credential_refs.py::test_sdk_floor_is_declared` must pass.
2. **Given** the connector is configured, **When** the behaviour of row `CONN-CISO-ASSISTANT-API-R002` (wiring) is exercised, **Then** `tests/test_credential_refs.py::test_env_refs_resolve_with_openbao_addr_and_no_token_ref` must build a client through `get_client`.
3. **Given** the connector is configured, **When** the behaviour of row `CONN-CISO-ASSISTANT-API-R003` (headless login) is exercised, **Then** `tests/test_auth.py::test_headless_login_returns_access_token` and `tests/test_auth.py::test_configured_token_skips_login` must pass.

### Edge Cases

- If `CONN-CISO-ASSISTANT-API-R001` is not met, its proving test fails: sdk floor.
- If `CONN-CISO-ASSISTANT-API-R002` is not met, its proving test fails: wiring.
- If `CONN-CISO-ASSISTANT-API-R003` is not met, its proving test fails: headless login.

## Requirements

- **FR-001**: SDK floor. Rows: `CONN-CISO-ASSISTANT-API-R001`.
- **FR-002**: Wiring. Rows: `CONN-CISO-ASSISTANT-API-R002`.
- **FR-003**: Headless login. Rows: `CONN-CISO-ASSISTANT-API-R003`.
- **FR-004**: Fleet name. Rows: `CONN-CISO-ASSISTANT-API-R004`.

## Success Criteria

- **SC-001**: `tests/test_credential_refs.py::test_sdk_floor_is_declared` must pass. Rows: `CONN-CISO-ASSISTANT-API-R001`.
- **SC-002**: `tests/test_credential_refs.py::test_env_refs_resolve_with_openbao_addr_and_no_token_ref` must build a client through `get_client`. Rows: `CONN-CISO-ASSISTANT-API-R002`.
- **SC-003**: `tests/test_auth.py::test_headless_login_returns_access_token` and `tests/test_auth.py::test_configured_token_skips_login` must pass. Rows: `CONN-CISO-ASSISTANT-API-R003`.
- **SC-004**: Every connector name in the package is `ciso-assistant-mcp`. Rows: `CONN-CISO-ASSISTANT-API-R004`.

## Assumptions

- The external system is reachable with operator-supplied credentials.
- The SDK and engine contracts the rows cite are at the floors declared in `pyproject.toml`.

## Traceability

| Label | Rows | Design section | Test ID | Evidence |
|---|---|---|---|---|
| FR-001 | `CONN-CISO-ASSISTANT-API-R001` | [plan.md](plan.md) | T-001 | [test-spec.md](test-spec.md) |
| FR-002 | `CONN-CISO-ASSISTANT-API-R002` | [plan.md](plan.md) | T-002 | [test-spec.md](test-spec.md) |
| FR-003 | `CONN-CISO-ASSISTANT-API-R003` | [plan.md](plan.md) | T-003 | [test-spec.md](test-spec.md) |
| FR-004 | `CONN-CISO-ASSISTANT-API-R004` | [plan.md](plan.md) | T-004 | [test-spec.md](test-spec.md) |
