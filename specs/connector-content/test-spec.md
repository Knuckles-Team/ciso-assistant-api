# CONN-CISO-ASSISTANT-API-CONNECTOR-CONTENT — Test specification

Governing spec: [spec.md](spec.md).

| Test ID | Requirement | Proving test | Expected observation |
|---|---|---|---|
| T-001 | `CONN-CISO-ASSISTANT-API-CONNECTOR-CONTENT-R001` | `tests/test_default_content_surfaces.py` | The listings include the packaged skills, ontology and prompts. |

## Rows awaiting bound tests
- `CONN-CISO-ASSISTANT-API-CONNECTOR-CONTENT-R002`: planned proof `tests/test_access_contracts.py::test_competency_contracts_certified`. Expected: The ontology certification passes and each recording validates against its contract's key and column names.. Refusal: A recording with a column missing from the ontology or a contract without ac:pagination fails..
