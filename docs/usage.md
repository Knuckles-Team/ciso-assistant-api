# Usage

Configure the endpoint, credential references, and TLS policy before invoking a
client or server. See [Configuration](configuration.md).

## Python client

```python
from ciso_assistant_api.auth import get_client

client = get_client()
try:
    response = client.api_incidents_list(status="open", limit=25)
    records = response.data
finally:
    client.close()
```

Every generated method returns a `Response` wrapper with decoded `.data`, the
underlying HTTP response, status, and headers. List operations follow bounded
DRF pagination automatically.

Library callers may pass a token directly to `get_client` as an in-memory value.
Durable deployments must use secret-reference settings instead.

## MCP server

Run the condensed surface locally:

```bash
ciso-assistant-mcp --transport stdio
```

Each domain router accepts an `action` and a JSON-encoded `params_json` string.
For example, invoke `ciso_assistant_incidents` with:

```json
{
  "action": "api_incidents_list",
  "params_json": "{\"status\":\"open\",\"limit\":25}"
}
```

Retrieve exact source objects before correlating them:

```json
{
  "action": "api_risk_scenarios_retrieve",
  "params_json": "{\"id\":\"<source_uuid>\"}"
}
```

The generated operation inventory in the README is authoritative for available
actions. Keep `MCP_TOOL_MODE=condensed` for delegated agents; enable verbose
per-operation tools only for an approved diagnostic need.

## Knowledge-graph ingestion

`ciso_ingest` materializes supported source records with provenance. Start with a
bounded sample and state the target graph before invoking it:

```json
{
  "kind": "risk_scenarios",
  "params_json": "{\"limit\":100}"
}
```

Supported kinds include risk scenarios, risk assessments, applied controls,
vulnerabilities, compliance assessments, incidents, and evidence metadata. The
MCP ingestion boundary never persists raw evidence attachment bytes.

## A2A agent

```bash
ciso-assistant-agent --provider <configured-provider> --model-id <configured-model>
```

The agent discovers the local MCP entrypoint from the packaged MCP config.
Configure model credentials through AgentConfig secret references, not command
arguments.
