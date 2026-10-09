"""CISO Assistant Authentication Module.

Authentication priority:

1. **OIDC Delegation** — If ``ENABLE_DELEGATION`` is active, exchanges the
   IdP-issued user token for a downstream CISO Assistant token via RFC 8693 Token
   Exchange using the shared ``delegated_auth`` helper.
2. **Referenced Credentials** — Resolves a pre-minted Knox token or a
   username/password pair from the configured runtime secret backend. Secret
   values are never part of durable provider configuration.

See ``docs/guides/oauth_sso.md`` in agent-utilities for full details.
"""

import logging
import threading

from agent_connector_sdk.config import setting
from agent_connector_sdk.credentials.references import SecretReferenceError
from agent_connector_sdk.credentials.resolution import resolve_secret_reference
from agent_connector_sdk.credentials.resolver import CredentialUnavailableError
from agent_connector_sdk.exceptions import AuthError, UnauthorizedError
from agent_connector_sdk.tls.profile import ResolvedTLSProfile
from agent_connector_sdk.tls.resolve import resolve_tls_profile

local = threading.local()
from ciso_assistant_api.api_client import Api

logger = logging.getLogger(__name__)


def get_client(
    instance: str | None = None,
    token: str | None = None,
    username: str | None = None,
    password: str | None = None,
    tls_profile: ResolvedTLSProfile | None = None,
    config: dict | None = None,
) -> Api:
    """Factory function to create the CISO Assistant :class:`Api` client.

    Supports OIDC delegation, a referenced Knox token, and the
    username/password login flow. Explicit credential arguments are accepted as
    process-memory values for library callers; deployment configuration accepts
    secret references only.
    """
    if instance is None:
        instance = setting("CISO_ASSISTANT_URL", None)
    if token is None:
        token = _resolve_optional_secret(setting("CISO_ASSISTANT_TOKEN_REF"))
    if username is None:
        username = _resolve_optional_secret(setting("CISO_ASSISTANT_USERNAME_REF"))
    if password is None:
        password = _resolve_optional_secret(setting("CISO_ASSISTANT_PASSWORD_REF"))
    if tls_profile is None:
        tls_profile = resolve_tls_profile(
            "CISO_ASSISTANT",
            profile_name=setting("CISO_ASSISTANT_TLS_PROFILE"),
            profile_ref=setting("CISO_ASSISTANT_TLS_PROFILE_REF"),
        )

    from agent_utilities.mcp.delegated_auth import (
        get_delegated_token,
        is_delegation_enabled,
    )

    # --- Path 1: OIDC Delegation (RFC 8693 Token Exchange) ---
    if is_delegation_enabled(config):
        try:
            delegated_token = get_delegated_token(
                config=config,
                audience=(config or {}).get("audience", instance or "ciso-assistant"),
                scopes=(config or {}).get("delegated_scopes", "api"),
            )
            logger.info("Using OIDC delegated authentication for CISO Assistant")
            return Api(url=instance, token=delegated_token, tls_profile=tls_profile)
        except Exception as exc:
            logger.error(
                "OIDC delegation failed for CISO Assistant (exception_type=%s)",
                type(exc).__name__,
            )
            raise RuntimeError("CISO Assistant token exchange failed") from None

    # --- Path 2: Referenced credentials (Knox token or native login) ---
    logger.info("Using referenced authentication for CISO Assistant API")
    try:
        return Api(
            url=instance,
            token=token,
            username=username,
            password=password,
            tls_profile=tls_profile,
        )
    except (AuthError, UnauthorizedError):
        raise RuntimeError(
            "CISO Assistant authentication failed; verify the configured endpoint "
            "and runtime secret references"
        ) from None


def _resolve_optional_secret(reference: str | None) -> str | None:
    if not reference:
        return None
    try:
        return resolve_secret_reference(reference)
    except (SecretReferenceError, CredentialUnavailableError):
        raise RuntimeError("CISO Assistant runtime secret is unavailable") from None
