# CONN-CISO-ASSISTANT-API — Implementation tasks

Governing spec: [spec.md](spec.md). Design: [plan.md](plan.md). Rows: [requirements.md](requirements.md).

- [x] `CONN-CISO-ASSISTANT-API-R001`: Raise the SDK floor to 0.3.10 in `pyproject.toml`.
- [x] `CONN-CISO-ASSISTANT-API-R002`: Prove `get_client` resolves `env://` references without `OPENBAO_TOKEN_REF`.
- [x] `CONN-CISO-ASSISTANT-API-R003`: Log in through the headless allauth route and use `meta.access_token`.
- [x] **CONN-CISO-ASSISTANT-API-R004:** File the pack, manifest and ingest binding under the fleet name `ciso-assistant-mcp`.
- [x] `CONN-CISO-ASSISTANT-API-R005`: Move the base onto the SDK governed client and delete the retry loop and the `requests` pin.
- [x] `CONN-CISO-ASSISTANT-API-R006`: Keep the error contract and hold an `httpx.Response` in the `Response` model.
