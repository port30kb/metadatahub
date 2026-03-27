---
title: "Nordic Iconography and Subject Classification"
description: "180 SKOS concept entries covering Nordic-specific subject terms for museum cataloguing — Norse mythology, Finnish Kalevala, Sámi culture, Christian-Nordic iconography, folk art motifs, seasonal traditions, and nature/landscape subjects, with multilingual labels and mappings to Getty AAT and Iconclass."
date: 2025-01-15
type: dataset
publisher: "Port 30 KB"
license: "https://creativecommons.org/licenses/by-sa/4.0/"
theme: "http://publications.europa.eu/resource/authority/data-theme/EDUC"
spatial: "http://sws.geonames.org/2661886/"
accrualPeriodicity: "http://publications.europa.eu/resource/authority/frequency/ANNUAL"
standards:
  - SKOS
  - DCAT-AP
  - Getty AAT
  - Iconclass
tags:
  - iconography
  - subjects
  - Norse-mythology
  - Kalevala
  - Sámi
  - folk-art
  - Viking-Age
  - Nordic
  - SKOS
  - linked-data
distributions:
  - id: "turtle"
    title: "RDF Turtle (180 entries)"
    accessURL: "https://metadatahub.eu/data/nordic-iconography.ttl"
    downloadURL: "https://metadatahub.eu/data/nordic-iconography.ttl"
    mediaType: "text/turtle"
  - id: "jsonld"
    title: "JSON-LD (180 entries)"
    accessURL: "https://metadatahub.eu/data/nordic-iconography.jsonld"
    downloadURL: "https://metadatahub.eu/data/nordic-iconography.jsonld"
    mediaType: "application/ld+json"
---

## Overview

This dataset provides **180 Nordic-specific subject and iconographic terms** as a SKOS concept scheme for museum cataloguing and cultural heritage description. It fills gaps in international classification systems like the Getty Art & Architecture Thesaurus (AAT) and Iconclass by providing detailed entries for subjects unique to or strongly associated with the Nordic cultural sphere.

Each concept includes **multilingual labels** (English, Swedish, Finnish, Danish, Norwegian Bokmål, Icelandic, and Old Norse where relevant), **structured hierarchies**, and **mappings to external vocabularies** (Getty AAT via `skos:closeMatch`, Iconclass via `skos:relatedMatch`).

## Sources

- [Wikipedia: Norse mythology](https://en.wikipedia.org/wiki/Norse_mythology) — Poetic Edda and Prose Edda subjects
- [Wikipedia: Kalevala](https://en.wikipedia.org/wiki/Kalevala) — Finnish national epic characters and scenes
- [Wikipedia: Sámi mythology](https://en.wikipedia.org/wiki/S%C3%A1mi_mythology) — Sámi spiritual traditions
- [Getty AAT](https://www.getty.edu/research/tools/vocabularies/aat/) — Art & Architecture Thesaurus URIs
- [Iconclass](https://www.iconclass.org/) — Iconographic classification system codes

## Statistics by Category

| Category | Entries | Broader concepts | AAT mappings | Iconclass codes |
|----------|---------|-----------------|--------------|-----------------|
| **Norse mythology** | 43 | norse-gods, norse-beings, norse-places, norse-events | 13 | 36 |
| **Kalevala / Finnish** | 23 | kalevala-characters, kalevala-concepts, kalevala-scenes | 0 | 15 |
| **Sámi subjects** | 20 | sami-culture, sami-mythology | 1 | 0 |
| **Christian-Nordic** | 24 | nordic-church-art, nordic-saints | 5 | 16 |
| **Folk art motifs** | 25 | nordic-folk-motifs, nordic-folk-beings, viking-art-styles | 6 | 3 |
| **Seasonal/cultural** | 20 | nordic-seasons | 0 | 0 |
| **Nature/landscape** | 25 | nordic-nature, nordic-light, nordic-terrain | 6 | 0 |
| **Total** | **180** | | | |

## Language Coverage

| Language | Code | Coverage |
|----------|------|----------|
| English | `en` | 180 entries (100%) |
| Swedish | `sv` | 180 entries (100%) |
| Finnish | `fi` | 178 entries (99%) |
| Danish | `da` | 172 entries (96%) |
| Norwegian Bokmål | `nb` | 172 entries (96%) |
| Icelandic | `is` | 52 entries (29%) |
| Old Norse | `non` | 18 entries (10%) |
| Northern Sámi | `se` | 12 entries (7%) |

## Data Model

Each subject is a `skos:Concept` in a `skos:ConceptScheme` with multilingual labels and optional links to AAT and Iconclass:

```turtle
ni:odin a skos:Concept ;
    rdfs:label "Odin"@en , "Oden"@sv , "Odin"@da , "Odin"@nb ,
               "Odin"@fi , "Óðinn"@is , "Óðinn"@non ;
    skos:prefLabel "Odin"@en , "Oden"@sv ;
    skos:inScheme <https://metadatahub.eu/data/nordic-iconography> ;
    skos:definition "Chief god of Norse mythology, associated with wisdom,
        war, death, and poetry..."@en ;
    skos:broader ni:norse-gods ;
    skos:closeMatch <http://vocab.getty.edu/aat/300379889> ;
    skos:relatedMatch <http://iconclass.org/91D1> .
```

### Vocabulary Mappings

- **`skos:closeMatch`** → [Getty AAT](https://www.getty.edu/research/tools/vocabularies/aat/) — semantically close concepts in the Art & Architecture Thesaurus
- **`skos:relatedMatch`** → [Iconclass](https://www.iconclass.org/) — related iconographic classification codes

## SPARQL Examples

### Find all Norse gods with their labels

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ni: <https://metadatahub.eu/data/nordic-iconography/>

SELECT ?god ?enLabel ?svLabel
WHERE {
  ?god skos:broader ni:norse-gods ;
       rdfs:label ?enLabel ;
       rdfs:label ?svLabel .
  FILTER(LANG(?enLabel) = "en")
  FILTER(LANG(?svLabel) = "sv")
}
ORDER BY ?enLabel
```

### Find subjects with Getty AAT mappings

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?subject ?label ?aatUri
WHERE {
  ?subject a skos:Concept ;
           rdfs:label ?label ;
           skos:closeMatch ?aatUri .
  FILTER(LANG(?label) = "en")
  FILTER(STRSTARTS(STR(?aatUri), "http://vocab.getty.edu/aat/"))
}
ORDER BY ?label
```

### Browse the hierarchy — all concepts under Kalevala characters

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ni: <https://metadatahub.eu/data/nordic-iconography/>

SELECT ?concept ?label ?definition
WHERE {
  ?concept skos:broader ni:kalevala-characters ;
           rdfs:label ?label ;
           skos:definition ?definition .
  FILTER(LANG(?label) = "en")
}
ORDER BY ?label
```

### Search across languages — find Finnish labels for nature subjects

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ni: <https://metadatahub.eu/data/nordic-iconography/>

SELECT ?concept ?fiLabel ?enLabel
WHERE {
  ?concept skos:broader+ ni:nordic-nature ;
           rdfs:label ?fiLabel ;
           rdfs:label ?enLabel .
  FILTER(LANG(?fiLabel) = "fi")
  FILTER(LANG(?enLabel) = "en")
}
ORDER BY ?enLabel
```

### Find all subjects with Iconclass codes

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?subject ?label ?iconclass
WHERE {
  ?subject a skos:Concept ;
           rdfs:label ?label ;
           skos:relatedMatch ?iconclass .
  FILTER(LANG(?label) = "en")
  FILTER(STRSTARTS(STR(?iconclass), "http://iconclass.org/"))
}
ORDER BY ?iconclass
```

## Download

- [Turtle (text/turtle)](/data/nordic-iconography.ttl) — 180 subject terms as SKOS concept scheme
- [JSON-LD (application/ld+json)](/data/nordic-iconography.jsonld) — Same data as JSON-LD graph
