# CONN-CISO-ASSISTANT-API — Test specification

Governing spec: [spec.md](spec.md).

| Test ID | Requirement | Level | Setup and input | Expected observation | Evidence |
|---|---|---|---|---|---|
| T-001 | `CONN-CISO-ASSISTANT-API-R001` | Unit | Read `pyproject.toml`. | Every SDK requirement has a floor of 0.3.10 or higher. | `tests/test_credential_refs.py::test_sdk_floor_is_declared` |
| T-002 | `CONN-CISO-ASSISTANT-API-R002` | Integration | `OPENBAO_ADDR` set, `OPENBAO_TOKEN_REF` unset, `env://` username and password references. | `get_client` returns an `Api` client. | `tests/test_credential_refs.py::test_env_refs_resolve_with_openbao_addr_and_no_token_ref` |

## Negative and boundary cases

A blank `OPENBAO_TOKEN_REF` behaves as unset.

## Quality and release proof

Run `pytest tests/test_credential_refs.py`. Run `pipelines-hook spec-standard`.
