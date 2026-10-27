---
name: ciso-assistant-api-development
skill_type: skill
description: >-
  Develop and verify ciso-assistant-api as a connector-owned package while
  preserving its generated CISO Assistant client, action-routed MCP tools,
  SDK authentication boundary, packaged content, and spec-delivery contract.
---

# CISO Assistant API Development

Use this skill for changes to the `ciso-assistant-api` connector. The package
owns CISO Assistant API calls, mappings, MCP tools, and connector content; it
does not own the connector SDK, Arbora admission, the shared Pages renderer, or
Pipelines hooks.

## Repository map and runtime boundary

- `ciso_assistant_api/specs/*.json` are the vendored OpenAPI sources. The
  generator emits the domain clients, operation manifest, and generated MCP
  modules; change the generator or source spec before regenerating those files.
- `ciso_assistant_api/api_client.py` composes the generated API domains, while
  `api/api_client_base.py`, `auth.py`, and `mcp/mcp_custom_api.py` contain the
  hand-authored client, authentication, and custom surface. Preserve the SDK
  `Connector` registration in `__init__.py`.
- `mcp_server.py` registers the action-routed generated tool domains, typed
  verbose operations, opt-in KG ingestion, and prompts. Keep the
  `MCP_TOOL_MODE` and `KG_INGESTTOOL` boundaries intact when changing tools.
- `ciso_assistant_api/ontology/`, `prompts/`, and `skills/` are packaged
  connector content. The package-data table includes these trees; inspect a
  built wheel when changing them.
- `auth.py` resolves `CISO_ASSISTANT_URL`, referenced credentials, delegation,
  and the named CISO Assistant TLS profile. Keep secret values out of source,
  tests, logs, and durable connector configuration.

## Rapid delivery: the 5-minute contract

1. Read the owning `specs/` row and this repository's `AGENTS.md` before
   editing.
2. Inspect the active generated client or MCP registration path and its
   focused tests before changing API behavior, auth, ontology content, or
   packaged skills.
3. Prefer the smallest connector-owned change. Preserve generated-file
   provenance, action names, parameter schemas, SDK `Connector` wiring, CISO
   Assistant authentication, and package-data declarations.
4. Run focused tests through the narrow test-slot wrapper, then run the
   repository pre-commit and pre-push gates without bypasses.
5. For public packaged content, update the patch version and `uv.lock`
   together; inspect the built wheel for the new skill.
6. Treat Pages as a separate proof: after the exact main SHA has a successful
   Pages run, check `/spec-delivery/`, its `index.html`, and `snapshot.json`
   over HTTPS and record the revision from the snapshot.

## Focused development commands

From the repository root:

```bash
uv sync --locked

/var/tmp/arbora-delivery/scale/run-narrow-test-slot.sh \
  uv run --locked --extra test pytest -q \
    tests/test_publication_workflow.py \
    tests/test_default_content_surfaces.py \
    tests/test_mcp_server.py

uvx pre-commit run --all-files
uvx pre-commit run --all-files --hook-stage pre-push
```

These checks cover the publication contract, packaged content, and MCP server
surface. Keep tests credential-free and do not replace them with a live CISO
Assistant call.

## Pages and package publication

`.github/workflows/pages.yml` is the one Pages caller. It invokes the shared
Pipelines `pages_pipeline.yml@main` workflow with the dashboard enabled and
keeps the docs, specs, dashboard configuration, and workflow path filters.
After a merge, verify the exact main SHA in the successful Pages run and probe:

```bash
curl -fsSI https://knuckles-team.github.io/ciso-assistant-api/
curl -fsSI https://knuckles-team.github.io/ciso-assistant-api/spec-delivery/
curl -fsSI https://knuckles-team.github.io/ciso-assistant-api/spec-delivery/index.html
curl -fsS https://knuckles-team.github.io/ciso-assistant-api/spec-delivery/snapshot.json
```

Keep package and container publication on their shared Pipelines workflows.
Inspect generated output and the built wheel before making a public release
claim; a local build does not prove Pages or registry publication.

## Change discipline

- Keep CISO Assistant API calls, request models, ontology mappings, and MCP
  schemas under this repository's `CONN-CISO-ASSISTANT-API-*` boundary. The
  connector SDK and shared Pipelines behavior belong to their owner repositories.
- Do not hand-edit generated API clients, operation manifests, or generated MCP
  modules. Use `scripts/generate_from_openapi.py` and inspect the resulting diff.
- Use `CISO_ASSISTANT_TOKEN_REF` or the username/password reference settings
  only through the runtime credential boundary. Preserve TLS verification and
  the named profile path.
- Keep KG ingestion opt-in and preserve its privacy, tenant, provenance, and
  attachment policy. Do not claim graph persistence from a local mock.
- For mutations, inspect current state first and require operator approval
  where the existing connector procedure calls for it.
