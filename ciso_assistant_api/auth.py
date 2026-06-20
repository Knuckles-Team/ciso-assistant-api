"""CISO Assistant Authentication Module.

Authentication priority:

1. **OIDC Delegation** — If ``ENABLE_DELEGATION`` is active, exchanges the
   IdP-issued user token for a downstream CISO Assistant token via RFC 8693 Token
   Exchange using the shared ``delegated_auth`` helper.
2. **Fixed Credentials** — Falls back to a pre-minted Knox token
   (``CISO_ASSISTANT_TOKEN``) or a username/password pair
   (``CISO_ASSISTANT_USERNAME`` / ``CISO_ASSISTANT_PASSWORD``) exchanged for a token
   at ``POST /api/iam/login/``.

See ``docs/guides/oauth_sso.md`` in agent-utilities for full details.
"""

import threading

from agent_utilities.base_utilities import get_logger
from agent_utilities.core.config import setting
from agent_utilities.core.exceptions import AuthError, UnauthorizedError

local = threading.local()
from ciso_assistant_api.api_client import Api

logger = get_logger(__name__)


def get_client(
    instance: str | None = None,
    token: str | None = None,
    username: str | None = None,
    password: str | None = None,
    verify: bool | None = None,
    config: dict | None = None,
) -> Api:
    """Factory function to create the CISO Assistant :class:`Api` client.

    Supports OIDC delegation, a fixed Knox token, and the username/password login
    flow. Uses the shared ``delegated_auth`` helper from agent-utilities.
    """
    if instance is None:
        instance = setting("CISO_ASSISTANT_URL", None)
    if token is None:
        token = setting("CISO_ASSISTANT_TOKEN", None)
    if username is None:
        username = setting("CISO_ASSISTANT_USERNAME", None)
    if password is None:
        password = setting("CISO_ASSISTANT_PASSWORD", None)
    if verify is None:
        verify = setting("CISO_ASSISTANT_SSL_VERIFY", True)

    from agent_utilities.mcp.delegated_auth import (
        get_delegated_token,
        get_user_identity,
        is_delegation_enabled,
    )

    # --- Path 1: OIDC Delegation (RFC 8693 Token Exchange) ---
    if is_delegation_enabled(config):
        try:
            delegated_token = get_delegated_token(
                config=config,
                audience=(config or {}).get("audience", instance or "ciso-assistant"),
                scopes=(config or {}).get("delegated_scopes", "api"),
                verify=verify,
            )
            identity = get_user_identity()
            logger.info(
                "Using OIDC delegated token for CISO Assistant API",
                extra={"user_email": identity.get("email"), "instance": instance},
            )
            return Api(url=instance, token=delegated_token, verify=verify)
        except Exception as e:
            logger.error(
                "OIDC delegation failed for CISO Assistant",
                extra={"error_type": type(e).__name__, "error_message": str(e)},
            )
            raise RuntimeError(f"Token exchange failed: {str(e)}") from e

    # --- Path 2: Fixed Credentials (Knox token or username/password login) ---
    logger.info("Using fixed credentials for CISO Assistant API")
    try:
        return Api(
            url=instance,
            token=token,
            username=username,
            password=password,
            verify=verify,
        )
    except (AuthError, UnauthorizedError) as e:
        raise RuntimeError(
            "AUTHENTICATION ERROR: The CISO Assistant credentials provided are not "
            "valid. Check CISO_ASSISTANT_URL and CISO_ASSISTANT_TOKEN (or "
            "CISO_ASSISTANT_USERNAME / CISO_ASSISTANT_PASSWORD). "
            f"Error details: {str(e)}"
        ) from e
