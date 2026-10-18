# Concepts

This package is registered in the agent-packages ecosystem Knowledge Graph under
the `CISO` concept prefix. The markers below let the ontology trace this connector
and its bidirectional integration with the KG hub.

| Concept ID | Title | Where |
| --- | --- | --- |
| `CISO-002` | CISO Assistant GRC → Knowledge Graph extractor (`domain="ciso_assistant"`) | `agent-connector-sdk` `AU-KG.enrichment.ciso-assistant-extraction` |
| `CISO-003` | Knowledge Graph → CISO Assistant writeback sink (`CISO_ASSISTANT_ENABLE_WRITE`) | `agent-connector-sdk` `AU-KG.enrichment.ciso-2` |

## Ecosystem bridge

CISO Assistant is modeled as a Governance/Risk/Compliance source system whose
entities (`Policy`, `Control`, `Risk`, `Goal`, `Principle`) map to the canonical
ontology classes shared with **egeria** (open metadata) and **camunda** (business
process). Reconciliation across systems is by GUID via `ALIGNED_WITH` equivalence
edges, so a CISO control aligned to an egeria policy or a camunda process is
resolved into one logical concept by the OWL reasoner.

See `agent-connector-sdk` `docs/architecture/ciso_assistant_kg_integration.md` for the
full bidirectional data-flow.
