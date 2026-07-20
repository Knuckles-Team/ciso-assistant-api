# Configuration, trust, and privacy

`ciso-assistant-api` resolves deployment values through the shared
`AgentConfig` boundary. Endpoints, secret references, TLS profiles, and
observability destinations belong in the operator-owned XDG configuration or
launch environment, never in this repository, MCP arguments, skill content, or
generated reports.

## Endpoint and authentication

Set `CISO_ASSISTANT_URL` to the target instance. Remote endpoints must use HTTPS;
HTTP is accepted only for a loopback development service. Embedded credentials,
URL fragments, and cross-origin pagination links are rejected.

Choose one authentication path:

- `CISO_ASSISTANT_TOKEN_REF` resolves a pre-minted Knox token.
- `CISO_ASSISTANT_USERNAME_REF` and `CISO_ASSISTANT_PASSWORD_REF` resolve a
  credential pair exchanged at the native login endpoint.
- An OIDC-delegated deployment uses the shared RFC 8693 settings and request
  identity boundary.

References must use an enabled `env://`, `vault://`, or `secret://` provider.
Store only the reference in AgentConfig. Do not place resolved credentials in a
configuration file, command line, MCP payload, log, trace, or report.

## TLS profiles

Certificate and hostname verification are mandatory. Select a named profile
with `CISO_ASSISTANT_TLS_PROFILE`, backed by the AgentConfig TLS catalog, or set
`CISO_ASSISTANT_TLS_PROFILE_REF` to one runtime secret containing a TLS profile.
The shared resolver supports platform trust, complete-chain CA bundles, mTLS,
and proxy policy without adding machine-specific paths or certificate material
to this package.

For a private certificate authority, provide the issuing intermediate and root
through the runtime TLS profile. Do not add or use a verification-disable switch
to compensate for an incomplete server chain.

## MCP and tool policy

`MCP_TOOL_MODE=condensed` is the current delegated surface. Domain switches such
as `COMPLIANCETOOL`, `INCIDENTSTOOL`, and `RISK_MANAGEMENTTOOL` can reduce the
surface further. Enable only the domains required by deployment policy. The
arbitrary-request tool should remain disabled unless policy explicitly permits
its broader endpoint access.

Use `stdio` for a local MCP child process. A network transport must bind to an
explicit interface and use the deployment's authentication, authorization,
rate limiting, and reverse-proxy controls.

## Knowledge graph and privacy

KG ingestion is an explicit operation. Preserve source provenance, tenant, ACL,
classification, retention, and checkpoint metadata. Store personal identity
only as an approved opaque reference. Do not persist raw credentials, local
paths, private hostnames, attachment content, prompts, or tool payloads in graph
properties or observability systems unless an approved data contract defines
access and retention.

The packaged skill and source presets remain human-authored inputs. Release tooling
derives and commits the exact local schema fingerprints, signed manifest, SHACL shapes,
neutral mapping and fixtures, migration ledger, and offline source attestation. None of
those artifacts contains deployment values or claims external-live certification.

## Readiness checks

Before enabling the provider:

1. Validate AgentConfig and confirm every required secret reference resolves
   without printing its value.
2. Verify the complete certificate chain and hostname with verification enabled.
3. Start the condensed MCP surface and run one least-privilege read action.
4. If KG ingestion is enabled, ingest a bounded sample and verify provenance and
   access-policy fields.
5. Confirm telemetry is metadata-only and contains no endpoint, identity,
   credential, local-path, or record-content fields.
