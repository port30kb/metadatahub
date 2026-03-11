---
title: "Example Cultural Heritage Collection"
description: "250 sample cultural heritage object records spanning paintings, sculptures, ceramics, coins, textiles, and archaeological artifacts from Nordic museums, described using CIDOC-CRM event-based patterns."
date: 2024-09-15
type: dataset
publisher: "Port 30 KB"
license: "https://creativecommons.org/publicdomain/zero/1.0/"
theme: "http://publications.europa.eu/resource/authority/data-theme/EDUC"
spatial: "http://sws.geonames.org/2661886/"
accrualPeriodicity: "http://publications.europa.eu/resource/authority/frequency/ANNUAL"
standards:
  - CIDOC-CRM
  - DCAT-AP
tags:
  - example
  - CIDOC-CRM
  - museum-objects
  - Nordic
  - linked-data
distributions:
  - id: "turtle"
    title: "RDF Turtle (250 objects)"
    accessURL: "https://metadatahub.eu/data/example-collection.ttl"
    downloadURL: "https://metadatahub.eu/data/example-collection.ttl"
    mediaType: "text/turtle"
  - id: "jsonld"
    title: "JSON-LD (250 objects)"
    accessURL: "https://metadatahub.eu/data/example-collection.jsonld"
    downloadURL: "https://metadatahub.eu/data/example-collection.jsonld"
    mediaType: "application/ld+json"
---

## Overview

This dataset contains **250 sample cultural heritage object records** modeled using [CIDOC-CRM](/vocab/cidoc-crm/) event-based patterns. The records represent realistic museum objects from Nordic collections, spanning from the Stone Age to Early Modern period.

## Statistics

| Category | Count |
|----------|-------|
| **Total objects** | 250 |
| **Object types** | 20 (paintings, sculptures, ceramics, coins, textiles, weapons, manuscripts, etc.) |
| **Named artists** | 20 (Nordic artists including Anders Zorn, Helene Schjerfbeck, Edvard Munch, etc.) |
| **Locations** | 15 (Stockholm, Helsinki, Copenhagen, Oslo, Visby, Birka, etc.) |
| **Collections** | 10 (Nationalmuseum, Nordiska museet, Historiska museet, etc.) |
| **Time periods** | 15 (Stone Age through Early Modern) |
| **Materials** | 20 (oil on canvas, bronze, marble, ceramic, silk, parchment, etc.) |

## Data Model

Each object record follows the CIDOC-CRM event pattern:

```
ex:obj-0001 a crm:E22_Human-Made_Object ;
    rdfs:label "Northern Landscape"@en ;
    dcterms:identifier "NAT-1887-0001" ;
    crm:P2_has_type aat:300033618 ;          # AAT: paintings
    crm:P45_consists_of aat:300015050 ;      # AAT: oil on canvas
    crm:P43_has_dimension [ ... ] ;          # dimensions
    crm:P50_has_current_keeper [ ... ] ;     # holding institution
    crm:P129_is_about aat:300015636 ;        # subject: landscape
    crm:P108i_was_produced_by ex:obj-0001-production .

ex:obj-0001-production a crm:E12_Production ;
    crm:P14_carried_out_by ex:actor-anders-zorn ;
    crm:P7_took_place_at gn:2673730 ;       # Stockholm
    crm:P4_has_time-span [ ... ] .           # date
```

## Object Types

| Type | AAT Concept | Examples |
|------|-------------|---------|
| Painting | [aat:300033618](http://vocab.getty.edu/aat/300033618) | Oil on canvas, oil on panel, tempera, watercolor |
| Sculpture | [aat:300047090](http://vocab.getty.edu/aat/300047090) | Marble, bronze, wood, limestone |
| Drawing | [aat:300033973](http://vocab.getty.edu/aat/300033973) | Pencil, charcoal, ink studies |
| Print | [aat:300041273](http://vocab.getty.edu/aat/300041273) | Etchings, lithographs, woodcuts |
| Photograph | [aat:300046300](http://vocab.getty.edu/aat/300046300) | Historical photography |
| Ceramic vessel | [aat:300024841](http://vocab.getty.edu/aat/300024841) | Stoneware, earthenware |
| Textile | [aat:300014063](http://vocab.getty.edu/aat/300014063) | Silk, wool, linen |
| Coin | [aat:300037222](http://vocab.getty.edu/aat/300037222) | Viking Age and medieval coinage |
| Medal | [aat:300046025](http://vocab.getty.edu/aat/300046025) | Commemorative medals |
| Brooch | [aat:300045991](http://vocab.getty.edu/aat/300045991) | Viking and medieval brooches |
| Ring | [aat:300046012](http://vocab.getty.edu/aat/300046012) | Gold and silver rings |
| Sword | [aat:300037048](http://vocab.getty.edu/aat/300037048) | Viking Age swords |
| Axe head | [aat:300024664](http://vocab.getty.edu/aat/300024664) | Bronze and iron axe heads |
| Runestone fragment | [aat:300006958](http://vocab.getty.edu/aat/300006958) | Inscribed stone fragments |
| Manuscript page | [aat:300028569](http://vocab.getty.edu/aat/300028569) | Medieval manuscript leaves |
| Icon | [aat:300263063](http://vocab.getty.edu/aat/300263063) | Religious icon paintings |
| Tapestry | [aat:300205002](http://vocab.getty.edu/aat/300205002) | Woven tapestries |
| Furniture | [aat:300037680](http://vocab.getty.edu/aat/300037680) | Historical furniture |
| Glass vessel | [aat:300010898](http://vocab.getty.edu/aat/300010898) | Blown and molded glass |
| Stone tool | [aat:300024823](http://vocab.getty.edu/aat/300024823) | Neolithic and Bronze Age tools |

## Featured Artists

The collection includes works by 20 named Nordic artists:

- **Swedish**: Anders Zorn, Carl Larsson, Bruno Liljefors, Ernst Josephson, Hanna Pauli, Eva Bonnier, Prince Eugen
- **Finnish**: Helene Schjerfbeck, Akseli Gallen-Kallela, Fanny Churberg, Albert Edelfelt, Hugo Simberg, Eero Järnefelt
- **Norwegian**: Edvard Munch, Christian Krohg, Harriet Backer
- **Danish**: Vilhelm Hammershøi, P.S. Krøyer, Anna Ancher, Michael Ancher

Anonymous makers include Viking Age smiths, medieval workshop artisans, and Sámi craftspeople.

## SPARQL Examples

Query these objects via the [SPARQL endpoint](/sparql):

```sparql
# Count objects by type
SELECT ?type (COUNT(?obj) AS ?count)
WHERE {
  ?obj a crm:E22_Human-Made_Object ;
       crm:P2_has_type ?type .
}
GROUP BY ?type
ORDER BY DESC(?count)

# Find all paintings by Anders Zorn
SELECT ?obj ?title
WHERE {
  ?obj a crm:E22_Human-Made_Object ;
       rdfs:label ?title ;
       crm:P108i_was_produced_by ?prod .
  ?prod crm:P14_carried_out_by ?actor .
  ?actor rdfs:label "Anders Zorn"@en .
}

# Objects from the Viking Age
SELECT ?obj ?title ?place
WHERE {
  ?obj crm:P108i_was_produced_by ?prod .
  ?obj rdfs:label ?title .
  ?prod crm:P4_has_time-span ?ts .
  ?ts crm:P82a_begin_of_the_begin ?date .
  ?prod crm:P7_took_place_at ?place .
  FILTER(?date >= "793" && ?date <= "1066")
}
```

## Download

- [Turtle (text/turtle)](/data/example-collection.ttl) — 7,500+ lines, all 250 objects with full CIDOC-CRM event structure
- [JSON-LD (application/ld+json)](/data/example-collection.jsonld) — Same data as JSON-LD graph
