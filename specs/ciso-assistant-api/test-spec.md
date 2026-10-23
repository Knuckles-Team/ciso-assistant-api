# CONN-CISO-ASSISTANT-API — Test specification

Governing spec: [spec.md](spec.md).

| Test ID | Requirement | Level | Setup and input | Expected observation | Evidence |
|---|---|---|---|---|---|
| T-001 | `CONN-CISO-ASSISTANT-API-R001` | Unit | Read `pyproject.toml`. | Every SDK requirement has a floor of 0.3.10 or higher. | `tests/test_credential_refs.py::test_sdk_floor_is_declared` |
| T-002 | `CONN-CISO-ASSISTANT-API-R002` | Integration | `OPENBAO_ADDR` set, `OPENBAO_TOKEN_REF` unset, `env://` username and password references. | `get_client` returns an `Api` client. | `tests/test_credential_refs.py::test_env_refs_resolve_with_openbao_addr_and_no_token_ref` |
| T-003 | `CONN-CISO-ASSISTANT-API-R003` | Unit | Mocked HTTP session; username with and without `@`; a configured token. | Login hits the headless route, sends the right identity key, returns `meta.access_token`; a configured token makes no request. | `tests/test_auth.py::test_headless_login_returns_access_token` `tests/test_auth.py::test_configured_token_skips_login` |
| T-004 | `CONN-CISO-ASSISTANT-API-R004` | Unit | See the evidence test. | Every connector name in the package is `ciso-assistant-mcp`. | `tests/test_fleet_name.py::test_connector_name_is_the_fleet_name` |
| T-005 | `CONN-CISO-ASSISTANT-API-R005` | Unit | See the evidence test. | A 503 is retried through the SDK policy and the second answer returns. | `tests/test_sdk_centralization.py::test_transient_status_is_retried_by_the_sdk_policy` |
| T-006 | `CONN-CISO-ASSISTANT-API-R006` | Unit | See the evidence test. | A transport failure raises the same `RuntimeError` as before. | `tests/test_sdk_centralization.py::test_transport_failure_keeps_the_runtime_error_contract` |

## Negative and boundary cases

A blank `OPENBAO_TOKEN_REF` behaves as unset.

## Quality and release proof

Run `pytest tests/test_credential_refs.py`. Run `pipelines-hook spec-standard`.
