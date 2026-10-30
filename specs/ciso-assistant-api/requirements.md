# CONN-CISO-ASSISTANT-API — Requirements

Governing spec: [spec.md](spec.md).

Each row is one requirement. A row names the file it touches and the test that proves it.

| ID | Requirement | Acceptance |
|---|---|---|
| `CONN-CISO-ASSISTANT-API-R001` | **SDK floor.** `pyproject.toml` must require `scion-sdk[mcp]>=0.5.6,<1.0.0`, the compatible renamed SDK release preserving the credential behavior introduced in scion-sdk 0.3.10, where `default_credential_resolver()` serves `env://` when `OPENBAO_TOKEN_REF` is unset. | `tests/test_credential_refs.py::test_sdk_floor_is_declared` must pass. |
| `CONN-CISO-ASSISTANT-API-R002` | **Wiring.** `get_client` in `ciso_assistant_api/auth.py` must resolve `CISO_ASSISTANT_USERNAME_REF` and `CISO_ASSISTANT_PASSWORD_REF` through `resolve_secret_reference` with `OPENBAO_ADDR` set and no `OPENBAO_TOKEN_REF`. | `tests/test_credential_refs.py::test_env_refs_resolve_with_openbao_addr_and_no_token_ref` must build a client through `get_client`. |
| `CONN-CISO-ASSISTANT-API-R003` | **Headless login.** `_ensure_token` in `ciso_assistant_api/api/api_client_base.py` must use a configured token without logging in; otherwise it must `POST /api/_allauth/app/v1/auth/login` with JSON `email` (or `username` when the identity has no `@`) and `password`, and use `meta.access_token` from the response as the API token. It must not call `/api/iam/login/`. | `tests/test_auth.py::test_headless_login_returns_access_token` and `tests/test_auth.py::test_configured_token_skips_login` must pass. |
| `CONN-CISO-ASSISTANT-API-R004` | **Fleet name.** `pyproject.toml` declares `ciso-assistant-mcp` as the single `scion_sdk.connector` entry point. The content pack, the manifest `connector`, the fingerprints and the ingest binding all carry `ciso-assistant-mcp`. Proving test: `tests/test_fleet_name.py::test_connector_name_is_the_fleet_name`. | Every connector name in the package is `ciso-assistant-mcp`. |
