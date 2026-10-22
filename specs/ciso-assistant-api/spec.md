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
The SDK owns the resolver rule (`SDK-CONNECTOR-CONTROL-R035`); this connector owns only its floor on that release.

## Requirements

See [requirements.md](requirements.md), [plan.md](plan.md), and [test-spec.md](test-spec.md).
