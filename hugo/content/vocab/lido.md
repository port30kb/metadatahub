---
title: "LIDO — Lightweight Information Describing Objects"
description: "The LIDO XML schema for describing museum and cultural heritage objects, designed for contributing content to cultural heritage repositories."
date: 2024-03-15
type: vocab
rdf_type: "skos:ConceptScheme"
version: "1.1"
creator: "ICOM-CIDOC LIDO Working Group"
license: "https://creativecommons.org/licenses/by/4.0/"
seeAlso: "http://www.lido-schema.org/"
standards:
  - LIDO
tags:
  - schema
  - museum
  - harvesting
  - metadata
classes:
  - id: "ObjectWorkType"
    label: "Object/Work Type"
    comment: "The specific type of the object/work being described."
  - id: "Classification"
    label: "Classification"
    comment: "Concepts used to categorize an object/work."
  - id: "Event"
    label: "Event"
    comment: "An event in the life of the object (production, acquisition, etc.)."
  - id: "Actor"
    label: "Actor"
    comment: "A person or organization involved in an event related to the object."
---

## Overview

**LIDO** (Lightweight Information Describing Objects) is an XML harvesting schema intended for delivering metadata from cultural heritage repositories. It is designed to support the full range of descriptive information about museum objects and is compatible with the CIDOC-CRM ontology.

## Structure

LIDO organizes object metadata into several major information groups:

1. **Object Classification** — What kind of object it is
2. **Object Identification** — Title, inscriptions, measurements
3. **Events** — Production, finding, acquisition, and other lifecycle events
4. **Relations** — Links to related objects, people, places, and concepts
5. **Administrative Metadata** — Record and resource information

## Mapping to CIDOC-CRM

LIDO's event-centric structure maps directly to CIDOC-CRM's event model:

- LIDO `eventType` → CIDOC-CRM `E5_Event` subclasses
- LIDO `eventActor` → CIDOC-CRM `E39_Actor` via `P14_carried_out_by`
- LIDO `eventDate` → CIDOC-CRM `E52_Time-Span` via `P4_has_time-span`
- LIDO `eventPlace` → CIDOC-CRM `E53_Place` via `P7_took_place_at`

## References

- [LIDO Schema v1.1](http://www.lido-schema.org/schema/v1.1/lido-v1.1.xsd)
- [LIDO Technical Documentation](http://www.lido-schema.org/documents/information.html)
