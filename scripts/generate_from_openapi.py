#!/usr/bin/env python
"""Generate the CISO Assistant API client + MCP tools from the vendored OpenAPI spec.

This is an **author-time** developer tool, not a runtime dependency. It reads the
single drf-spectacular spec in ``ciso_assistant_api/specs/ciso_assistant.json`` and
emits fleet-conformant, committed code:

* ``ciso_assistant_api/api/api_client_<domain>.py`` — one method per OpenAPI
  operation, composed into ``ciso_assistant_api.api_client.Api`` via multiple
  inheritance.
* ``ciso_assistant_api/api/_operation_manifest.py`` — the machine-readable
  ``operationId -> method -> action`` map that the coverage test asserts against.
* ``ciso_assistant_api/mcp/mcp_<domain>.py`` — one consolidated, action-routed MCP
  tool per domain exposing every operation as an ``action``.
* ``ciso_assistant_api/mcp/__init__.py`` — ``TOOL_REGISTRY`` consumed by
  ``mcp_server.py``.
* ``ciso_assistant_api/api_client.py`` — the composite ``Api`` class.

CISO Assistant (intuitem) tags every operation ``api`` in its drf-spectacular
schema, so domains are derived from the **URL path** (the first segment after
``/api/``) and grouped into the published documentation categories via
``GROUP_MAP``. Any unmapped resource falls back to a snake_case of its segment, so
no operation is ever dropped.

Re-run after refreshing the spec:  ``python scripts/generate_from_openapi.py``
"""

from __future__ import annotations

import json
import keyword
import re
from pathlib import Path

PKG = Path(__file__).resolve().parent.parent / "ciso_assistant_api"
SPECS_DIR = PKG / "specs"
API_DIR = PKG / "api"
MCP_DIR = PKG / "mcp"

# Top-level URL resource (first path segment after ``/api/``) -> documentation
# domain. Mirrors the 18 categories published at https://ca-api-doc.pages.dev/ .
GROUP_MAP = {
    # Analytics & Metrology
    "metrology": "analytics_metrology",
    "analytics": "analytics_metrology",
    "agg_data": "analytics_metrology",
    "composer_data": "analytics_metrology",
    "get_metrics": "analytics_metrology",
    "get_counters": "analytics_metrology",
    "get_audits_metrics": "analytics_metrology",
    "get_combined_assessments_status": "analytics_metrology",
    "get_governance_calendar_data": "analytics_metrology",
    # Assets
    "assets": "assets",
    "asset-class": "assets",
    "asset-capabilities": "assets",
    # Authentication & Users
    "iam": "auth_users",
    "users": "auth_users",
    "user-groups": "auth_users",
    "role-assignments": "auth_users",
    "teams": "auth_users",
    "accounts": "auth_users",
    "user-preferences": "auth_users",
    "csrf": "auth_users",
    # Compliance
    "compliance-assessments": "compliance",
    "requirement-assessments": "compliance",
    "requirement-nodes": "compliance",
    "requirement-assignments": "compliance",
    "requirement-mapping-sets": "compliance",
    "applied-controls": "compliance",
    "reference-controls": "compliance",
    "policies": "compliance",
    "mapping-libraries": "compliance",
    # EBIOS-RM
    "ebios-rm": "ebios_rm",
    # Evidence & Attachments
    "evidences": "evidence",
    "evidence-revisions": "evidence",
    "document-revisions": "evidence",
    "document-attachments": "evidence",
    "attachment-metadata": "evidence",
    "batch-download-attachments": "evidence",
    "batch-upload-attachments": "evidence",
    "managed-documents": "evidence",
    # Frameworks & Libraries
    "frameworks": "frameworks_libraries",
    "stored-libraries": "frameworks_libraries",
    "loaded-libraries": "frameworks_libraries",
    "library-filtering-labels": "frameworks_libraries",
    "filtering-labels": "frameworks_libraries",
    "presets": "frameworks_libraries",
    "terminologies": "frameworks_libraries",
    # Governance
    "folders": "governance",
    "perimeters": "governance",
    "organisation-objectives": "governance",
    "organisation-issues": "governance",
    "journeys": "governance",
    "journey-steps": "governance",
    "validation-flows": "governance",
    "quick-start": "governance",
    "comments": "governance",
    # Incidents
    "incidents": "incidents",
    "timeline-entries": "incidents",
    # Integrations & Tooling
    "integrations": "integrations",
    "webhooks": "integrations",
    "data-wizard": "integrations",
    "dump-db": "integrations",
    "full-restore": "integrations",
    "load-backup": "integrations",
    "build": "integrations",
    "content-types": "integrations",
    "search": "integrations",
    "health": "integrations",
    "serdes": "integrations",
    # Privacy
    "privacy": "privacy",
    # Quantitative Risk (CRQ)
    "crq": "crq",
    # Resilience
    "resilience": "resilience",
    "pmbok": "resilience",
    # Risk Management
    "risk-assessments": "risk_management",
    "risk-scenarios": "risk_management",
    "risk-matrices": "risk_management",
    "risk-acceptances": "risk_management",
    "threats": "risk_management",
    "vulnerabilities": "risk_management",
    "cwes": "risk_management",
    # Security Exceptions & Findings
    "security-exceptions": "security_findings",
    "findings": "security_findings",
    "findings-assessments": "security_findings",
    "security-advisories": "security_findings",
    # Tasks & Timeline
    "task-templates": "tasks_timeline",
    "task-nodes": "tasks_timeline",
    "campaigns": "tasks_timeline",
    "answers": "tasks_timeline",
    "questions": "tasks_timeline",
    "question-choices": "tasks_timeline",
    # Third-Party Risk Management
    "entities": "third_party",
    "entity-assessments": "third_party",
    "representatives": "third_party",
    "contracts": "third_party",
    "solutions": "third_party",
    "actors": "third_party",
    # Chat
    "chat": "chat",
}

HTTP_METHODS = ("get", "post", "put", "delete", "patch")


def snake(name: str) -> str:
    """Convert an operationId / slug to a safe snake_case Python identifier."""
    name = re.sub(r"[^0-9a-zA-Z]+", "_", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    name = re.sub(r"_+", "_", name).strip("_").lower()
    if not name:
        name = "op"
    if name[0].isdigit():
        name = "op_" + name
    if keyword.iskeyword(name):
        name += "_"
    return name


def camel(domain: str) -> str:
    return "".join(part.capitalize() for part in domain.split("_"))


def domain_for(path: str) -> str:
    """Derive the documentation domain from a URL path's first resource segment."""
    parts = [p for p in path.split("/") if p and not p.startswith("{")]
    if len(parts) > 1 and parts[0] == "api":
        seg = parts[1]
    elif parts:
        seg = parts[0]
    else:
        seg = "root"
    return GROUP_MAP.get(seg, snake(seg))


def detect_pagination(http: str, query_params: list[str]) -> str:
    """DRF list endpoints expose ``page`` (PageNumber) or ``limit``/``offset``."""
    if http.upper() != "GET":
        return "none"
    qs = set(query_params)
    if "page" in qs or {"limit", "offset"} & qs:
        return "page"
    return "none"


def collect_operations() -> dict[str, list[dict]]:
    """Return ``{domain: [operation_meta, ...]}`` from the single vendored spec."""
    by_domain: dict[str, list[dict]] = {}
    global_methods: set[str] = set()
    actions_by_domain: dict[str, set[str]] = {}
    synthetic = 0

    spec_path = SPECS_DIR / "ciso_assistant.json"
    spec = json.loads(spec_path.read_text())

    for path, methods in (spec.get("paths") or {}).items():
        if not isinstance(methods, dict):
            continue
        shared = methods.get("parameters", [])
        domain = domain_for(path)
        for http, op in methods.items():
            if http not in HTTP_METHODS or not isinstance(op, dict):
                continue
            op_id = op.get("operationId")
            if not op_id:
                synthetic += 1
                op_id = snake(f"{http}_{path}")
            params = list(shared) + list(op.get("parameters") or [])
            path_params = [p["name"] for p in params if p.get("in") == "path"]
            for token in re.findall(r"\{([^}]+)\}", path):
                if token not in path_params:
                    path_params.append(token)
            query_params = [p["name"] for p in params if p.get("in") == "query"]
            has_body = "requestBody" in op

            method_name = snake(op_id)
            while method_name in global_methods:
                method_name += "_x"
            global_methods.add(method_name)

            seen = actions_by_domain.setdefault(domain, set())
            action = snake(op_id)
            while action in seen:
                action += "_x"
            seen.add(action)

            raw_summary = (op.get("summary") or op.get("description") or op_id).strip()
            summary = (
                re.sub(r"\s+", " ", raw_summary.splitlines()[0])[:160]
                if raw_summary
                else op_id
            )

            by_domain.setdefault(domain, []).append(
                {
                    "operation_id": op_id,
                    "method": method_name,
                    "action": action,
                    "domain": domain,
                    "http": http.upper(),
                    "url_template": path,
                    "path_params": path_params,
                    "query_params": query_params,
                    "has_body": has_body,
                    "paginate": detect_pagination(http, query_params),
                    "summary": summary,
                }
            )

    print(
        f"Collected {sum(len(v) for v in by_domain.values())} operations "
        f"across {len(by_domain)} domains ({synthetic} synthetic ids)."
    )
    return by_domain


# --------------------------------------------------------------------- emitters
AUTOGEN = (
    '"""Auto-generated by scripts/generate_from_openapi.py — do not edit by hand."""'
)


def emit_client_module(domain: str, ops: list[dict]) -> None:
    cls = f"CisoAssistant{camel(domain)}"
    lines = [
        "#!/usr/bin/python",
        AUTOGEN,
        "",
        "from ciso_assistant_api.api.api_client_base import CisoAssistantApiBase",
        "from ciso_assistant_api.ciso_assistant_models import Response",
        "",
        "",
        f"class {cls}(CisoAssistantApiBase):",
    ]
    for op in ops:
        doc = op["summary"].replace('"', "'")
        lines += [
            f"    def {op['method']}(self, **kwargs) -> Response:",
            f'        """{doc}"""',
            "        return self._call(",
            f"            http={op['http']!r},",
            f"            url_template={op['url_template']!r},",
            f"            path_params={op['path_params']!r},",
            f"            query_params={op['query_params']!r},",
            f"            has_body={op['has_body']!r},",
            f"            paginate={op['paginate']!r},",
            "            kwargs=kwargs,",
            "        )",
            "",
        ]
    (API_DIR / f"api_client_{domain}.py").write_text("\n".join(lines) + "\n")


def emit_mcp_module(domain: str, ops: list[dict]) -> None:
    tag = domain.replace("_", "-")
    actions = ", ".join(f"'{op['action']}'" for op in ops)
    lines = [
        AUTOGEN,
        "",
        "from typing import Any",
        "",
        "from fastmcp import Context, FastMCP",
        "from fastmcp.dependencies import Depends",
        "from pydantic import Field",
        "",
        "from ciso_assistant_api.auth import get_client",
        "",
        "",
        f"def register_{domain}_tools(mcp: FastMCP):",
        f'    @mcp.tool(tags={{"{tag}"}})',
        f"    async def ciso_assistant_{domain}(",
        "        action: str = Field(",
        f'            description="Action to perform. One of: {actions}"',
        "        ),",
        "        params_json: str = Field(",
        '            default="{}",',
        '            description="JSON string of parameters (path, query, and body fields) for the action.",',
        "        ),",
        "        client=Depends(get_client),",
        "        ctx: Context | None = Field(",
        '            default=None, description="MCP context for progress reporting"',
        "        ),",
        "    ) -> Any:",
        f'        """Manage CISO Assistant {domain.replace("_", " ")} operations."""',
        "        if ctx:",
        '            await ctx.info(f"Executing ciso_assistant_'
        + domain
        + ' action: {action}")',
        "        import json",
        "",
        "        try:",
        "            kwargs = json.loads(params_json) if params_json else {}",
        "        except Exception as e:",
        '            return {"error": f"Invalid params_json: {e}"}',
        "        if not isinstance(kwargs, dict):",
        '            return {"error": "params_json must decode to a JSON object"}',
        "        kwargs = {k: v for k, v in kwargs.items() if v is not None}",
        "",
    ]
    first = True
    for op in ops:
        kw = "if" if first else "elif"
        first = False
        lines.append(f'        {kw} action == "{op["action"]}":')
        lines.append(f"            return client.{op['method']}(**kwargs)")
    lines += [
        '        raise ValueError(f"Unknown action: {action}")',
        "",
    ]
    (MCP_DIR / f"mcp_{domain}.py").write_text("\n".join(lines) + "\n")


def emit_manifest(by_domain: dict[str, list[dict]]) -> None:
    operations = [
        {
            "operation_id": op["operation_id"],
            "domain": domain,
            "method": op["method"],
            "action": op["action"],
            "http": op["http"],
            "path": op["url_template"],
            "paginate": op["paginate"],
        }
        for domain in sorted(by_domain)
        for op in by_domain[domain]
    ]
    lines = [
        AUTOGEN,
        "",
        "# Each entry: {operation_id, domain, method, action, http, path, paginate}",
        f"OPERATIONS = {json.dumps(operations, indent=4)}",
        "",
        "DOMAINS = " + json.dumps(sorted(by_domain), indent=4),
        "",
        "# domain -> ordered list of MCP action names",
        "ACTIONS_BY_DOMAIN: dict[str, list[str]] = {}",
        "for _op in OPERATIONS:",
        "    ACTIONS_BY_DOMAIN.setdefault(_op['domain'], []).append(_op['action'])",
        "",
    ]
    (API_DIR / "_operation_manifest.py").write_text("\n".join(lines) + "\n")


def emit_api_client(by_domain: dict[str, list[dict]]) -> None:
    domains = sorted(by_domain)
    imports = [
        f"from ciso_assistant_api.api.api_client_{d} import CisoAssistant{camel(d)}"
        for d in domains
    ]
    bases = ",\n    ".join(f"CisoAssistant{camel(d)}" for d in domains)
    lines = [
        "#!/usr/bin/python",
        AUTOGEN,
        "",
        *imports,
        "",
        "",
        f"class Api(\n    {bases},\n):",
        '    """Composite CISO Assistant API client — every domain client, one class."""',
        "",
        "    __slots__ = ()",
        "",
    ]
    (PKG / "api_client.py").write_text("\n".join(lines) + "\n")


def emit_mcp_init(by_domain: dict[str, list[dict]]) -> None:
    domains = sorted(by_domain)
    # Emit imports isort-sorted (custom_api interleaves alphabetically) so the
    # generated file is ruff-clean and codegen stays idempotent.
    imports = sorted(
        [
            f"from ciso_assistant_api.mcp.mcp_{d} import register_{d}_tools"
            for d in domains
        ]
        + [
            "from ciso_assistant_api.mcp.mcp_custom_api import register_custom_api_tools"
        ]
    )
    registry = [
        f'    ("{d.replace("_", "-")}", "{d.upper()}TOOL", register_{d}_tools),'
        for d in domains
    ]
    lines = [
        AUTOGEN,
        "",
        *imports,
        "",
        "# (tag, toggle_env_var, register_fn) — consumed by mcp_server.get_mcp_instance().",
        "TOOL_REGISTRY = [",
        *registry,
        '    ("custom-api", "CUSTOM_APITOOL", register_custom_api_tools),',
        "]",
        "",
        "__all__ = [",
        *[f'    "register_{d}_tools",' for d in domains],
        '    "register_custom_api_tools",',
        '    "TOOL_REGISTRY",',
        "]",
        "",
    ]
    (MCP_DIR / "__init__.py").write_text("\n".join(lines) + "\n")


def main() -> None:
    API_DIR.mkdir(exist_ok=True)
    MCP_DIR.mkdir(exist_ok=True)
    (API_DIR / "__init__.py").write_text(
        '"""CISO Assistant API client package (generated modules live here)."""\n'
    )
    by_domain = collect_operations()
    for domain, ops in by_domain.items():
        emit_client_module(domain, ops)
        emit_mcp_module(domain, ops)
    emit_manifest(by_domain)
    emit_api_client(by_domain)
    emit_mcp_init(by_domain)
    tools = len(by_domain) + 1  # + custom_api
    print(f"Generated {len(by_domain)} client modules, {tools} MCP tools.")


if __name__ == "__main__":
    main()
