---
title: "Nordic Thesaurus Mappings"
description: "SKOS mapping assertions between Nordic museum classification systems (K-samsök, DigitaltMuseum, Finna, Danish museums) and the Getty Art & Architecture Thesaurus (AAT), enabling cross-system interoperability for cultural heritage data."
date: 2025-01-15
type: dataset
publisher: "Port 30 KB"
license: "https://creativecommons.org/publicdomain/zero/1.0/"
theme: "http://publications.europa.eu/resource/authority/data-theme/EDUC"
spatial: "http://sws.geonames.org/2661886/"
accrualPeriodicity: "http://publications.europa.eu/resource/authority/frequency/ANNUAL"
standards:
  - SKOS
  - VoID
  - DCAT-AP
tags:
  - thesaurus
  - mappings
  - interoperability
  - K-samsök
  - DigitaltMuseum
  - Finna
  - AAT
  - Nordic
  - linked-data
distributions:
  - id: "turtle"
    title: "RDF Turtle (mapping assertions)"
    accessURL: "https://metadatahub.eu/data/nordic-thesaurus-mappings.ttl"
    downloadURL: "https://metadatahub.eu/data/nordic-thesaurus-mappings.ttl"
    mediaType: "text/turtle"
  - id: "jsonld"
    title: "JSON-LD (mapping assertions)"
    accessURL: "https://metadatahub.eu/data/nordic-thesaurus-mappings.jsonld"
    downloadURL: "https://metadatahub.eu/data/nordic-thesaurus-mappings.jsonld"
    mediaType: "application/ld+json"
---

## Overview

This dataset provides **formal SKOS mapping assertions** between the major Nordic museum classification systems and the Getty Art & Architecture Thesaurus (AAT). These mappings enable automatic alignment of object types, materials, and subject terms across national museum aggregators, facilitating cross-border search, federated access, and Europeana integration.

## Systems Mapped

| System | Country | Description |
|--------|---------|-------------|
| **K-samsök** | Sweden | Swedish Cultural Heritage aggregator (Riksantikvarieämbetet) |
| **DigitaltMuseum** | Norway/Sweden | Joint Norwegian-Swedish museum collections platform |
| **Finna/YSO** | Finland | Finnish Cultural Heritage aggregator using YSO vocabulary |
| **Danish museums** | Denmark | Danish National Museum classification terms |
| **Getty AAT** | International | Art & Architecture Thesaurus, the international standard |

## Statistics

| Mapping Direction | Count | Match Types |
|-------------------|-------|-------------|
| K-samsök → AAT | 25 | exactMatch, closeMatch, broadMatch |
| DigitaltMuseum → AAT | 20 | exactMatch, closeMatch |
| Finna/YSO → AAT | 18 | exactMatch, closeMatch |
| Danish museums → AAT | 19 | exactMatch, closeMatch, broadMatch |
| K-samsök ↔ DigitaltMuseum | 10 | exactMatch |
| K-samsök ↔ Finna | 5 | exactMatch |
| DigitaltMuseum ↔ Finna | 5 | exactMatch |

## Data Model

Each mapping assertion is a SKOS concept with a mapping relation to the target concept:

```
map:ksamsok-malning-aat a skos:Concept ;
    rdfs:label "Painting (K-samsök → AAT)"@en ;
    skos:definition "Direct equivalence for easel paintings."@en ;
    dcterms:source <https://kulturarvsdata.se/raa/ksamsok#type/Målning> ;
    skos:exactMatch <http://vocab.getty.edu/aat/300033618> ;
    dcterms:conformsTo "high" .
```

### Match Types

| SKOS Property | Meaning | Usage |
|---------------|---------|-------|
| `skos:exactMatch` | Identical meaning | Most object types (painting, sculpture, etc.) |
| `skos:closeMatch` | Similar, interchangeable in most contexts | Material-based classifications vs. object types |
| `skos:broadMatch` | Source is narrower than target | Period-specific types (e.g., "Viking find" → "archaeological objects") |
| `skos:narrowMatch` | Source is broader than target | General categories mapping to specific AAT terms |
| `skos:relatedMatch` | Related but not hierarchical | Conceptually linked but different facets |

## SPARQL Examples

Query these mappings via the [SPARQL endpoint](/sparql):

```sparql
# Find all exactMatch mappings to AAT
SELECT ?mapping ?label ?aatUri
WHERE {
  ?mapping a skos:Concept ;
           rdfs:label ?label ;
           skos:exactMatch ?aatUri .
  FILTER(STRSTARTS(STR(?aatUri), "http://vocab.getty.edu/aat/"))
  FILTER(LANG(?label) = "en")
}

# Find mappings between K-samsök and DigitaltMuseum
SELECT ?mapping ?label ?target
WHERE {
  ?mapping a skos:Concept ;
           rdfs:label ?label ;
           rdfs:comment ?comment ;
           skos:exactMatch ?target .
  FILTER(CONTAINS(?comment, "ksamsok"))
  FILTER(STRSTARTS(STR(?target), "https://digitaltmuseum.org/"))
  FILTER(LANG(?label) = "en")
}

# Count mappings by match type
SELECT ?matchType (COUNT(?m) AS ?count)
WHERE {
  ?m a skos:Concept .
  { ?m skos:exactMatch ?t . BIND("exactMatch" AS ?matchType) }
  UNION
  { ?m skos:closeMatch ?t . BIND("closeMatch" AS ?matchType) }
  UNION
  { ?m skos:broadMatch ?t . BIND("broadMatch" AS ?matchType) }
}
GROUP BY ?matchType
ORDER BY DESC(?count)
```

## Download

- [Turtle (text/turtle)](/data/nordic-thesaurus-mappings.ttl) — All mapping assertions with full SKOS structure
- [JSON-LD (application/ld+json)](/data/nordic-thesaurus-mappings.jsonld) — Same data as JSON-LD graph
