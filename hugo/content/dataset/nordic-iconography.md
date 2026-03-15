---
title: "Nordic Iconography and Subject Classification"
description: "SKOS vocabulary of Nordic-specific subject terms for museum cataloguing, covering Norse mythology, Kalevala, Sámi motifs, Christian-Nordic iconography, folk art, seasonal traditions, and nature/landscape subjects."
date: 2025-01-15
type: dataset
publisher: "Port 30 KB"
license: "https://creativecommons.org/publicdomain/zero/1.0/"
theme: "http://publications.europa.eu/resource/authority/data-theme/EDUC"
spatial: "http://sws.geonames.org/2661886/"
accrualPeriodicity: "http://publications.europa.eu/resource/authority/frequency/ANNUAL"
standards:
  - SKOS
  - DCAT-AP
tags:
  - iconography
  - subjects
  - Norse-mythology
  - Kalevala
  - Sámi
  - folk-art
  - Nordic
  - linked-data
distributions:
  - id: "turtle"
    title: "RDF Turtle (subject terms)"
    accessURL: "https://metadatahub.eu/data/nordic-iconography.ttl"
    downloadURL: "https://metadatahub.eu/data/nordic-iconography.ttl"
    mediaType: "text/turtle"
  - id: "jsonld"
    title: "JSON-LD (subject terms)"
    accessURL: "https://metadatahub.eu/data/nordic-iconography.jsonld"
    downloadURL: "https://metadatahub.eu/data/nordic-iconography.jsonld"
    mediaType: "application/ld+json"
---

## Overview

This vocabulary provides **Nordic-specific subject and iconographic terms** for museum cataloguing, filling gaps in international systems like Getty AAT and Iconclass. The terms are organized hierarchically using SKOS and cover subjects from Norse mythology to contemporary Nordic cultural traditions.

## Subject Categories

| Category | Count | Examples |
|----------|-------|---------|
| **Norse mythology** | ~40 | Odin, Thor, Freya, Yggdrasil, Ragnarök, Valhalla |
| **Kalevala / Finnish mythology** | ~25 | Väinämöinen, Ilmarinen, Sampo, Kantele |
| **Sámi subjects** | ~20 | Noaidi, drum motifs, reindeer, Stállu |
| **Christian-Nordic** | ~25 | Stave church iconography, Nordic saints, Birgitta visions |
| **Folk art motifs** | ~25 | Kurbits, rosemaling, Dala horse, Viking art styles |
| **Seasonal/cultural** | ~20 | Midsummer, Lucia, Jul, Valborg |
| **Nature/landscape** | ~25 | Midnight sun, aurora borealis, fjord, birch forest |

## Data Model

Each subject is a SKOS concept with multilingual labels and optional links to AAT and Iconclass:

```
icon:odin a skos:Concept ;
    rdfs:label "Odin"@en , "Oden"@sv , "Óðinn"@is , "Óðinn"@non ;
    skos:prefLabel "Odin"@en ;
    skos:inScheme <https://metadatahub.eu/data/nordic-iconography> ;
    skos:definition "Chief god of Norse mythology..."@en ;
    skos:broader icon:norse-gods ;
    skos:closeMatch <http://vocab.getty.edu/aat/300379889> ;
    skos:notation "91D" .
```

## SPARQL Examples

```sparql
# All Norse mythology subjects
SELECT ?subject ?label
WHERE {
  ?subject skos:broader* <https://metadatahub.eu/data/nordic-iconography/norse-mythology> ;
           rdfs:label ?label .
  FILTER(LANG(?label) = "en")
}

# Subjects with Iconclass codes
SELECT ?subject ?label ?code
WHERE {
  ?subject a skos:Concept ;
           rdfs:label ?label ;
           skos:notation ?code .
  FILTER(LANG(?label) = "en")
}

# Search for subjects in Swedish
SELECT ?subject ?svLabel ?enLabel
WHERE {
  ?subject a skos:Concept ;
           rdfs:label ?svLabel ;
           rdfs:label ?enLabel .
  FILTER(LANG(?svLabel) = "sv")
  FILTER(LANG(?enLabel) = "en")
}
```

## Download

- [Turtle (text/turtle)](/data/nordic-iconography.ttl) — All subject terms with SKOS hierarchy
- [JSON-LD (application/ld+json)](/data/nordic-iconography.jsonld) — Same data as JSON-LD graph
