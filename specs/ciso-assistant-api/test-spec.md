# CONN-CISO-ASSISTANT-API — Test specification

Governing spec: [spec.md](spec.md).

| Test ID | Requirement | Level | Setup and input | Expected observation | Evidence |
|---|---|---|---|---|---|
| T-001 | `CONN-CISO-ASSISTANT-API-R001` | Unit | Read `pyproject.toml`. | Every SDK requirement uses scion-sdk with a floor of 0.5.6 or higher and preserves the credential resolver contract. | `tests/test_credential_refs.py::test_sdk_floor_is_declared` |
| T-002 | `CONN-CISO-ASSISTANT-API-R002` | Integration | `OPENBAO_ADDR` set, `OPENBAO_TOKEN_REF` unset, `env://` username and password references. | `get_client` returns an `Api` client. | `tests/test_credential_refs.py::test_env_refs_resolve_with_openbao_addr_and_no_token_ref` |
| T-003 | `CONN-CISO-ASSISTANT-API-R003` | Unit | Mocked HTTP session; username with and without `@`; a configured token. | Login hits the headless route, sends the right identity key, returns `meta.access_token`; a configured token makes no request. | `tests/test_auth.py::test_headless_login_returns_access_token` `tests/test_auth.py::test_configured_token_skips_login` |

## Negative and boundary cases

A blank `OPENBAO_TOKEN_REF` behaves as unset.

## Quality and release proof

Run `pytest tests/test_credential_refs.py`. Run `pipelines-hook spec-standard`.
| T-004 | `CONN-CISO-ASSISTANT-API-R004` | `tests/test_fleet_name.py::test_connector_name_is_the_fleet_name` | Every connector name in the package is `ciso-assistant-mcp`. |
