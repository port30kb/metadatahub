---
title: "CIDOC Conceptual Reference Model (CIDOC-CRM)"
description: "The CIDOC-CRM ontology for cultural heritage documentation, providing a formal structure for describing concepts and relationships used in cultural heritage information."
date: 2024-06-01
type: vocab
rdf_type: "owl:Ontology"
version: "7.1.3"
creator: "CIDOC-CRM Special Interest Group"
license: "https://creativecommons.org/licenses/by/4.0/"
seeAlso: "https://www.cidoc-crm.org/"
standards:
  - CIDOC-CRM
tags:
  - ontology
  - cultural-heritage
  - museum
  - documentation
classes:
  - id: "E1_CRM_Entity"
    label: "CRM Entity"
    comment: "The top-level class in the CIDOC-CRM hierarchy, comprising all things in the universe of discourse."
  - id: "E18_Physical_Thing"
    label: "Physical Thing"
    comment: "All persistent physical items with a relatively stable form, human-made or natural."
    subClassOf: "https://metadatahub.eu/vocab/cidoc-crm/E1_CRM_Entity"
  - id: "E22_Human-Made_Object"
    label: "Human-Made Object"
    comment: "Physical objects purposely created by human activity."
    subClassOf: "https://metadatahub.eu/vocab/cidoc-crm/E18_Physical_Thing"
  - id: "E39_Actor"
    label: "Actor"
    comment: "People, either combinely or individually, who have the potential to perform intentional actions."
    subClassOf: "https://metadatahub.eu/vocab/cidoc-crm/E1_CRM_Entity"
  - id: "E52_Time-Span"
    label: "Time-Span"
    comment: "Abstract temporal extents with a beginning, an end, and a duration."
    subClassOf: "https://metadatahub.eu/vocab/cidoc-crm/E1_CRM_Entity"
  - id: "E53_Place"
    label: "Place"
    comment: "Extents in space, in particular on the surface of the earth."
    subClassOf: "https://metadatahub.eu/vocab/cidoc-crm/E1_CRM_Entity"
properties:
  - id: "P1_is_identified_by"
    label: "is identified by"
    comment: "Describes the naming or identification of any real-world item."
    domain: "https://metadatahub.eu/vocab/cidoc-crm/E1_CRM_Entity"
    range: "http://www.w3.org/2000/01/rdf-schema#Literal"
  - id: "P2_has_type"
    label: "has type"
    comment: "Allows sub-typing of CRM entities."
    domain: "https://metadatahub.eu/vocab/cidoc-crm/E1_CRM_Entity"
    range: "http://www.w3.org/2004/02/skos/core#Concept"
---

## Overview

The **CIDOC Conceptual Reference Model** (CIDOC-CRM) is the ISO standard (ISO 21127) for the interchange of cultural heritage information. It provides definitions and a formal structure for describing the implicit and explicit concepts and relationships used in cultural heritage documentation.

## Key Classes

| Class | Label | Description |
|-------|-------|-------------|
| E1 | CRM Entity | Top-level class for all entities |
| E18 | Physical Thing | Persistent physical items |
| E22 | Human-Made Object | Objects created by human activity |
| E39 | Actor | People or groups capable of intentional action |
| E52 | Time-Span | Abstract temporal extents |
| E53 | Place | Spatial extents |

## Usage in the Helix Ecosystem

CIDOC-CRM serves as the core ontology for mapping museum object metadata within the Helix ecosystem. LIDO records are mapped to CIDOC-CRM event-based patterns, enabling cross-collection querying via the SPARQL endpoint.

## References

- [CIDOC-CRM Official Site](https://www.cidoc-crm.org/)
- [ISO 21127:2023](https://www.iso.org/standard/57832.html)
- [CIDOC-CRM in RDFS](https://cidoc-crm.org/rdfs/7.1.3/CIDOC_CRM_v7.1.3.rdfs)
