"""Ciso Assistant ontology contribution (CONCEPT:AU-KG.ontology.federation-provider-leg).

Data-only subpackage: it carries ``ciso.ttl`` (the ``owl:Ontology``
``https://knuckles-team.github.io/ontology/connector/ciso`` module) which the scion-sdk hub federates in via
the ``scion_sdk.ontology_providers`` entry-point. It holds no business logic
and no heavy imports so the hub can resolve it cheaply.
"""
