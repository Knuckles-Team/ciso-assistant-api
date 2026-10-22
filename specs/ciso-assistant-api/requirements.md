# CONN-CISO-ASSISTANT-API — Requirements

Governing spec: [spec.md](spec.md).

Each row is one requirement. A row names the file it touches and the test that proves it.

| ID | Requirement | Acceptance |
|---|---|---|
| `CONN-CISO-ASSISTANT-API-R001` | **SDK floor.** `pyproject.toml` must require `agent-connector-sdk[mcp]>=0.3.10`, the first release where `default_credential_resolver()` serves `env://` when `OPENBAO_TOKEN_REF` is unset. | `tests/test_credential_refs.py::test_sdk_floor_is_declared` must pass. |
| `CONN-CISO-ASSISTANT-API-R002` | **Wiring.** `get_client` in `ciso_assistant_api/auth.py` must resolve `CISO_ASSISTANT_USERNAME_REF` and `CISO_ASSISTANT_PASSWORD_REF` through `resolve_secret_reference` with `OPENBAO_ADDR` set and no `OPENBAO_TOKEN_REF`. | `tests/test_credential_refs.py::test_env_refs_resolve_with_openbao_addr_and_no_token_ref` must build a client through `get_client`. |
