---
title: "Nordic Rights and Licenses Vocabulary"
description: "55 linked data entries covering rights statements, Creative Commons licenses, Nordic copyright law concepts, Europeana rights framework tiers, and practical museum scenario guidance — multilingual in English, Swedish, Finnish, Danish, and Norwegian."
date: 2025-01-15
type: dataset
publisher: "Port 30 KB"
license: "https://creativecommons.org/licenses/by-sa/4.0/"
theme: "http://publications.europa.eu/resource/authority/data-theme/GOVE"
standards:
  - SKOS
  - RightsStatements.org
  - Creative Commons
  - DCAT-AP
  - Europeana Data Model
tags:
  - rights
  - licenses
  - copyright
  - creative-commons
  - rights-statements
  - nordic
  - Europeana
  - museum
  - cultural-heritage
  - SKOS
  - linked-data
distributions:
  - id: "turtle"
    title: "RDF Turtle (55 entries)"
    accessURL: "https://metadatahub.eu/data/nordic-rights.ttl"
    downloadURL: "https://metadatahub.eu/data/nordic-rights.ttl"
    mediaType: "text/turtle"
  - id: "jsonld"
    title: "JSON-LD (55 entries)"
    accessURL: "https://metadatahub.eu/data/nordic-rights.jsonld"
    downloadURL: "https://metadatahub.eu/data/nordic-rights.jsonld"
    mediaType: "application/ld+json"
---

## Overview

This dataset models a **Nordic Rights and Licenses Vocabulary** as a SKOS concept scheme with 55 entries, designed for Nordic cultural heritage institutions working with digital collections. It covers the full spectrum of rights information needed when digitizing, cataloging, and publishing museum collections online.

The vocabulary spans five categories:

- **Creative Commons Licenses** (9 entries) — CC0 through CC-BY-NC-ND, with Europeana tier classification
- **RightsStatements.org Statements** (12 entries) — All standardized rights statements for cultural heritage
- **Nordic Copyright Law Concepts** (15 entries) — Swedish, Finnish, Norwegian, Danish, and Icelandic copyright acts plus key legal concepts (moral rights, database rights, extended collective licensing, freedom of panorama)
- **Europeana Rights Framework** (8 entries) — Tier system, Data Exchange Agreement, Public Domain Charter
- **Common Museum Scenarios** (9 entries) — Practical guidance for pre-1900 artworks, living artists, archaeological finds, Sámi heritage, and more

Each entry includes multilingual labels (English, Swedish, Finnish, Danish, Norwegian Bokmål), links to canonical URIs via `skos:exactMatch`, Europeana tier classification, and practical usage guidance as `skos:scopeNote`.

## Quick Reference: Museum Scenario to Rights Statement

| Scenario | Recommended Rights Statement | Europeana Tier |
|----------|------------------------------|----------------|
| Pre-1900 artwork, public domain original | [Public Domain Mark 1.0](https://creativecommons.org/publicdomain/mark/1.0/) | Tier 4 |
| Museum documentation photo of public domain 2D work | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) or PDM 1.0 | Tier 4 |
| Museum-created metadata and catalog records | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) | Tier 4 |
| Born-digital museum content | [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) | Tier 4 |
| Archaeological finds (state-owned, museum photo) | [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) | Tier 4 |
| Contemporary artwork by living artist | [InC](http://rightsstatements.org/vocab/InC/1.0/) (In Copyright) | Tier 1 |
| Educational use of copyrighted material | [InC-EDU](http://rightsstatements.org/vocab/InC-EDU/1.0/) | Tier 1 |
| Orphan work (diligent search completed) | [InC-OW-EU](http://rightsstatements.org/vocab/InC-OW-EU/1.0/) | Tier 1 |
| Rights holder unlocatable | [InC-RUU](http://rightsstatements.org/vocab/InC-RUU/1.0/) | Tier 1 |
| Sámi cultural heritage materials | Consider [TK Labels](https://localcontexts.org/labels/traditional-knowledge-labels/) + InC | Varies |

## Sources

- [Creative Commons Licenses](https://creativecommons.org/licenses/) — official license texts and legal code
- [RightsStatements.org](https://rightsstatements.org/) — standardized rights statements for cultural heritage
- [Europeana Available Rights Statements](https://pro.europeana.eu/page/available-rights-statements) — tier classification
- [Europeana Data Exchange Agreement](https://pro.europeana.eu/page/the-data-exchange-agreement) — metadata licensing
- [Europeana Public Domain Charter](https://pro.europeana.eu/page/the-europeana-public-domain-charter) — public domain principles
- [Swedish Copyright Act (SFS 1960:729)](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-1960729-om-upphovsratt-till-litterara-och_sfs-1960-729/)
- [Finnish Copyright Act (404/1961)](https://www.finlex.fi/fi/laki/ajantasa/1961/19610404)
- [Norwegian Copyright Act (LOV-2018-06-15-40)](https://lovdata.no/dokument/NL/lov/2018-06-15-40)
- [Local Contexts — Traditional Knowledge Labels](https://localcontexts.org/labels/traditional-knowledge-labels/)

## Data Model

Each concept is modeled as a `skos:Concept` within the concept scheme `<https://metadatahub.eu/data/nordic-rights>`. Additional RDF types are assigned by category:

| Category | RDF Type |
|----------|----------|
| Creative Commons licenses | `mhub:License` |
| RightsStatements.org | `mhub:RightsStatement` |
| Nordic copyright law | `mhub:CopyrightConcept` |
| Europeana framework | `mhub:RightsFramework` |
| Museum scenarios | `mhub:UsageScenario` |

Key properties:
- `skos:prefLabel` — multilingual preferred labels (en, sv, fi, da, nb)
- `skos:definition` — English description
- `skos:broader` — hierarchical relationship to parent concept
- `skos:exactMatch` — link to canonical URI (CC license URL, RightsStatements.org URI)
- `skos:scopeNote` — practical usage guidance for museum professionals
- `mhub:europeanaTier` — Europeana openness tier (tier-1 to tier-4)
- `mhub:category` — vocabulary category classification

## SPARQL Examples

### List all Creative Commons licenses with their Europeana tiers

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX mhub: <https://metadatahub.eu/data/nordic-rights/ontology/>
PREFIX nr:   <https://metadatahub.eu/data/nordic-rights/>

SELECT ?concept ?label ?tier ?canonicalUri
WHERE {
  ?concept skos:inScheme <https://metadatahub.eu/data/nordic-rights> ;
           mhub:category "creative-commons" ;
           skos:prefLabel ?label ;
           mhub:europeanaTier ?tier ;
           skos:exactMatch ?canonicalUri .
  FILTER (lang(?label) = "en")
}
ORDER BY ?tier ?label
```

### Find the recommended rights statement for a given museum scenario

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX mhub: <https://metadatahub.eu/data/nordic-rights/ontology/>

SELECT ?scenario ?label ?guidance
WHERE {
  ?scenario skos:inScheme <https://metadatahub.eu/data/nordic-rights> ;
            mhub:category "museum-scenario" ;
            skos:prefLabel ?label ;
            skos:scopeNote ?guidance .
  FILTER (lang(?label) = "en")
}
ORDER BY ?label
```

### Get all Tier 4 (most open) rights statements with Swedish labels

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX mhub: <https://metadatahub.eu/data/nordic-rights/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?concept ?svLabel ?enLabel ?canonicalUri
WHERE {
  ?concept skos:inScheme <https://metadatahub.eu/data/nordic-rights> ;
           mhub:europeanaTier "tier-4" ;
           rdfs:label ?svLabel ;
           skos:prefLabel ?enLabel .
  FILTER (lang(?svLabel) = "sv")
  FILTER (lang(?enLabel) = "en")
  OPTIONAL { ?concept skos:exactMatch ?canonicalUri }
}
ORDER BY ?enLabel
```

### Look up Nordic copyright law concepts and their source legislation

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX mhub: <https://metadatahub.eu/data/nordic-rights/ontology/>

SELECT ?concept ?label ?definition ?legislationUri
WHERE {
  ?concept skos:inScheme <https://metadatahub.eu/data/nordic-rights> ;
           mhub:category "nordic-copyright-law" ;
           skos:prefLabel ?label ;
           skos:definition ?definition .
  FILTER (lang(?label) = "en")
  OPTIONAL { ?concept skos:exactMatch ?legislationUri }
}
ORDER BY ?label
```

### Map a canonical license URI to its Nordic labels

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?lang ?label
WHERE {
  ?concept skos:exactMatch <https://creativecommons.org/licenses/by/4.0/> ;
           rdfs:label ?label .
  BIND (lang(?label) AS ?lang)
}
ORDER BY ?lang
```

## Regenerating

To regenerate the Turtle and JSON-LD output files after editing the source data:

```bash
python3 scripts/generate-nordic-rights.py
```

This reads from `data/nordic-rights/rights-vocabulary.yaml`, validates all entries, and writes to `hugo/static/data/nordic-rights.ttl` and `hugo/static/data/nordic-rights.jsonld`.
