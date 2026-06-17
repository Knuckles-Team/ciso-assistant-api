#!/usr/bin/python
"""Base HTTP client for the CISO Assistant API.

Handles the cross-cutting concerns shared by every generated domain client:

* **Authentication** — CISO Assistant (intuitem) uses Django-REST-Knox **token**
  auth. Provide a pre-minted token (``CISO_ASSISTANT_TOKEN``) or a
  username/password pair (``CISO_ASSISTANT_USERNAME`` / ``CISO_ASSISTANT_PASSWORD``)
  which is exchanged for a token at ``POST /api/iam/login/``. The token is sent as
  ``Authorization: Token <token>`` on every request.
* **Single host** — all operations target one backend host (``CISO_ASSISTANT_URL``,
  e.g. ``https://ciso.arpa``). The generated methods carry the relative path
  (``/api/...``); this base prefixes the configured host.
* **Pagination** — DRF list endpoints (``page`` / ``limit`` + ``offset``) return
  ``{"count", "next", "previous", "results"}``; this base transparently follows the
  ``next`` links and concatenates ``results``.
* **Rate limiting / transient errors** — honours ``429`` ``Retry-After`` and retries
  ``429``/``502``/``503``/``504`` with bounded exponential backoff.
"""

import logging
import threading
import time
from typing import Any, TypeVar

import requests
import urllib3
from agent_utilities.base_utilities import get_logger
from agent_utilities.core.exceptions import (
    AuthError,
    MissingParameterError,
    ParameterError,
    UnauthorizedError,
)
from pydantic import ValidationError

from ciso_assistant_api.ciso_assistant_models import Response

logger = get_logger(__name__)

T = TypeVar("T")


class CisoAssistantApiBase:
    def __init__(
        self,
        url: str | None = None,
        token: str | None = None,
        username: str | None = None,
        password: str | None = None,
        proxies: dict | None = None,
        verify: bool = True,
        max_retries: int = 3,
        max_pages: int = 50,
        debug: bool = False,
    ):
        logger.setLevel(logging.DEBUG if debug else logging.ERROR)

        self.verify = verify
        self.proxies = proxies
        self.debug = debug
        self.max_retries = max_retries
        self.max_pages = max_pages
        self._session = requests.Session()
        self._token_lock = threading.Lock()
        self._token = token
        self._username = username
        self._password = password

        host = (url or "http://localhost:8000").strip().rstrip("/")
        if not host.startswith(("http://", "https://")):
            host = f"https://{host}"
        self.url = host
        self.hostname = host.split("://", 1)[-1]

        if self.verify is False:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        if not self._token and not (self._username and self._password):
            raise MissingParameterError(
                "Provide CISO_ASSISTANT_TOKEN, or CISO_ASSISTANT_USERNAME and "
                "CISO_ASSISTANT_PASSWORD for the Knox login flow."
            )

    # ------------------------------------------------------------------ auth
    def _ensure_token(self) -> str:
        """Return a valid Knox token, logging in with credentials if needed."""
        if self._token:
            return self._token
        with self._token_lock:
            if self._token:
                return self._token
            login_url = f"{self.url}/api/iam/login/"
            try:
                resp = self._session.post(
                    url=login_url,
                    json={"username": self._username, "password": self._password},
                    headers={"Accept": "application/json"},
                    verify=self.verify,
                    proxies=self.proxies,
                    timeout=30,
                )
            except requests.RequestException as e:
                raise AuthError(f"CISO Assistant login request failed: {e}") from e
            if resp.status_code in (401, 403):
                raise UnauthorizedError(
                    f"CISO Assistant credentials rejected ({resp.status_code})."
                )
            if not resp.ok:
                raise AuthError(
                    f"CISO Assistant login returned {resp.status_code}: {resp.text}"
                )
            payload = resp.json()
            self._token = payload.get("token") or payload.get("key")
            if not self._token:
                raise AuthError("CISO Assistant login response contained no token.")
            return self._token

    def _auth_headers(self, content_type: str | None = "application/json") -> dict:
        headers = {
            "Authorization": f"Token {self._ensure_token()}",
            "Accept": "application/json",
        }
        if content_type:
            headers["Content-Type"] = content_type
        return headers

    # --------------------------------------------------------------- url build
    def _resolve_url(self, url_template: str, path_kwargs: dict) -> str:
        """Resolve a relative spec path into an absolute URL.

        Interpolates ``{param}`` path parameters by name, then prefixes the
        configured backend host.
        """
        path = url_template
        for key, value in (path_kwargs or {}).items():
            path = path.replace("{" + key + "}", str(value))
        if "{" in path:
            missing = (
                path[path.index("{") + 1 : path.index("}")] if "}" in path else "?"
            )
            raise MissingParameterError(f"Missing required path parameter: {missing}")
        if path.startswith(("http://", "https://")):
            return path
        return f"{self.url}/{path.lstrip('/')}"

    # ----------------------------------------------------------------- request
    def _request(
        self,
        method: str,
        url: str,
        params: dict | None = None,
        json: Any | None = None,
        data: Any | None = None,
        headers: dict | None = None,
    ) -> requests.Response:
        """Perform an HTTP request with rate-limit / transient-error retries."""
        request_headers = headers or self._auth_headers()
        attempt = 0
        while True:
            response = self._session.request(
                method=method.upper(),
                url=url,
                params=params or None,
                json=json,
                data=data,
                headers=request_headers,
                verify=self.verify,
                proxies=self.proxies,
                timeout=60,
            )
            if response.status_code == 429 and attempt < self.max_retries:
                delay = self._retry_delay(response, attempt)
                logger.debug("Rate limited (429); sleeping %.1fs", delay)
                time.sleep(delay)
                attempt += 1
                continue
            if response.status_code in (502, 503, 504) and attempt < self.max_retries:
                time.sleep(self._retry_delay(response, attempt))
                attempt += 1
                continue
            if response.status_code in (401, 403):
                raise (AuthError if response.status_code == 401 else UnauthorizedError)(
                    f"CISO Assistant request to {url} failed ({response.status_code})."
                )
            return response

    @staticmethod
    def _retry_delay(response: requests.Response, attempt: int) -> float:
        retry_after = response.headers.get("Retry-After")
        if retry_after:
            try:
                return min(float(retry_after), 60.0)
            except ValueError:
                pass
        return min(2.0**attempt, 30.0)

    @staticmethod
    def _decode(response: requests.Response) -> Any:
        if not response.content:
            return None
        if "application/json" in response.headers.get("Content-Type", ""):
            try:
                return response.json()
            except ValueError:
                return response.text
        return response.text

    # -------------------------------------------------------------- pagination
    def _fetch_all_pages(
        self, method: str, url: str, params: dict, max_pages: int
    ) -> tuple[requests.Response, list]:
        """Follow DRF ``next`` links, concatenating ``results`` across pages."""
        params = dict(params or {})
        first = self._request(method, url, params=params)
        body = self._decode(first)
        all_data = list(self._extract_items(body))
        cap = max_pages if max_pages and max_pages > 0 else self.max_pages

        next_url = body.get("next") if isinstance(body, dict) else None
        fetched = 1
        while next_url and fetched < cap:
            # ``next`` is an absolute URL already carrying the page cursor.
            resp = self._request(method, next_url)
            body = self._decode(resp)
            all_data.extend(self._extract_items(body))
            next_url = body.get("next") if isinstance(body, dict) else None
            fetched += 1
        return first, all_data

    @staticmethod
    def _extract_items(body: Any) -> list:
        if isinstance(body, list):
            return body
        if isinstance(body, dict):
            for key in ("results", "content", "data", "items", "records"):
                if isinstance(body.get(key), list):
                    return body[key]
        return []

    # ----------------------------------------------------------- generated call
    def _call(
        self,
        http: str,
        url_template: str,
        path_params: list[str],
        query_params: list[str],
        has_body: bool,
        paginate: str,
        kwargs: dict,
    ) -> Response:
        """Dispatch a single generated operation. Used by every domain method."""
        try:
            kwargs = {k: v for k, v in (kwargs or {}).items() if v is not None}
            path_kwargs = {k: kwargs.pop(k) for k in path_params if k in kwargs}
            url = self._resolve_url(url_template, path_kwargs)

            params = {k: kwargs.pop(k) for k in query_params if k in kwargs}
            body = None
            if has_body:
                body = kwargs.pop("body", None)
                if body is None and kwargs:
                    body = kwargs
                    kwargs = {}
            params.update(kwargs)

            if http.upper() == "GET" and paginate == "page":
                max_pages = int(params.pop("max_pages", 0) or 0)
                response, data = self._fetch_all_pages(http, url, params, max_pages)
                return Response(response=response, data=data)

            params.pop("max_pages", None)
            response = self._request(http, url, params=params, json=body)
            return Response(response=response, data=self._decode(response))
        except (AuthError, UnauthorizedError, MissingParameterError):
            raise
        except ValidationError as e:
            raise ParameterError(f"Invalid parameters: {e.errors()}") from e
        except requests.RequestException as e:
            logger.error("CISO Assistant request error: %s", e)
            raise

    # --------------------------------------------------------------- escape hatch
    def api_request(
        self,
        method: str,
        endpoint: str,
        params: dict | None = None,
        json: Any | None = None,
        data: Any | None = None,
    ) -> Response:
        """Make an arbitrary CISO Assistant REST request against the backend host.

        ``endpoint`` is a path (e.g. ``/api/assets/``) appended to the configured
        base URL. Use this for operations not covered by a typed method.
        """
        if method.upper() not in ("GET", "POST", "PUT", "DELETE", "PATCH"):
            raise ValueError(f"Unsupported HTTP method: {method.upper()}")
        url = f"{self.url}/{endpoint.lstrip('/')}"
        response = self._request(method, url, params=params, json=json, data=data)
        return Response(response=response, data=self._decode(response))
