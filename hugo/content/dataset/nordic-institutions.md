---
title: "Nordic Museum Institutions Authority"
description: "116 museum institutions across Sweden, Norway, Finland, Denmark, and Iceland — a linked data authority file for Nordic cultural heritage organisations with multilingual names, ISIL codes, Wikidata links, and GeoNames locations."
date: 2025-01-15
type: dataset
publisher: "Port 30 KB"
license: "https://creativecommons.org/licenses/by-sa/4.0/"
theme: "http://publications.europa.eu/resource/authority/data-theme/EDUC"
standards:
  - CIDOC-CRM
  - Schema.org
  - W3C Organization Ontology
  - SKOS
tags:
  - museums
  - institutions
  - Nordic
  - Sweden
  - Norway
  - Finland
  - Denmark
  - Iceland
  - Sami
  - cultural-heritage
  - authority-file
  - linked-data
  - ISIL
  - Wikidata
distributions:
  - id: "turtle"
    title: "RDF Turtle (116 entries)"
    accessURL: "https://metadatahub.eu/data/nordic-institutions.ttl"
    downloadURL: "https://metadatahub.eu/data/nordic-institutions.ttl"
    mediaType: "text/turtle"
  - id: "jsonld"
    title: "JSON-LD (116 entries)"
    accessURL: "https://metadatahub.eu/data/nordic-institutions.jsonld"
    downloadURL: "https://metadatahub.eu/data/nordic-institutions.jsonld"
    mediaType: "application/ld+json"
---

## Overview

This dataset is an **authority file of Nordic museum institutions** modelled as a SKOS concept scheme with 116 entries. Each institution is typed as a [CIDOC-CRM E40_Legal_Body](http://www.cidoc-crm.org/cidoc-crm/E40_Legal_Body), a [W3C org:Organization](http://www.w3.org/ns/org#Organization), and a [Schema.org Museum](https://schema.org/Museum). Entries include multilingual labels (English plus local language), geographic location via GeoNames URIs, identity links via Wikidata URIs, ISIL identifiers where available, founding dates, and museum type classifications.

The dataset covers five Nordic countries — **Sweden**, **Norway**, **Finland**, **Denmark**, and **Iceland** — spanning art museums, history museums, open-air museums, university museums, archaeology museums, design museums, maritime museums, natural history museums, folk/Sami museums, and specialized museums.

## Sources

This dataset is compiled from the following sources:

- [Wikipedia: List of museums in Sweden](https://en.wikipedia.org/wiki/List_of_museums_in_Sweden)
- [Wikipedia: List of museums in Norway](https://en.wikipedia.org/wiki/List_of_museums_in_Norway)
- [Wikipedia: List of museums in Finland](https://en.wikipedia.org/wiki/List_of_museums_in_Finland)
- [Wikipedia: List of museums in Denmark](https://en.wikipedia.org/wiki/List_of_museums_in_Denmark)
- [Wikipedia: List of museums in Iceland](https://en.wikipedia.org/wiki/List_of_museums_in_Iceland)
- [ISIL Registry](https://sigel.staatsbibliothek-berlin.de/en/suche)
- [Wikidata](https://www.wikidata.org/)
- [GeoNames](https://www.geonames.org/)

License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) (matching Wikipedia source license).

## Statistics

### By Country

| Country | Count | Notable Institutions |
|---------|-------|---------------------|
| **Sweden** | 38 | Nationalmuseum, Nordiska museet, Vasamuseet, Skansen, Moderna Museet, Historiska museet |
| **Norway** | 24 | Nasjonalmuseet, Munchmuseet, Vikingskipshuset, Norsk Folkemuseum, Maihaugen, KODE Bergen |
| **Finland** | 24 | Ateneum, Kiasma, Kansallismuseo, Design Museum, Siida, Amos Rex |
| **Denmark** | 20 | Nationalmuseet, SMK, Louisiana, Ny Carlsberg Glyptotek, ARoS, Vikingeskibsmuseet |
| **Iceland** | 10 | Þjóðminjasafn Íslands, Listasafn Reykjavíkur, Listasafn Íslands, Skógasafn |
| **Total** | **116** | |

### By Museum Type

| Type | Count | Examples |
|------|-------|---------|
| **Art Museum** | 37 | Nationalmuseum, Nasjonalmuseet, Ateneum, SMK, Louisiana |
| **History Museum** | 29 | Nordiska museet, Nationalmuseet (DK), Kansallismuseo, Þjóðminjasafn |
| **Open-Air Museum** | 9 | Skansen, Norsk Folkemuseum, Maihaugen, Seurasaari, Den Gamle By |
| **University Museum** | 6 | Gustavianum, Bergen Museum, Tromsø Museum, Lunds UHSM |
| **Archaeology Museum** | 6 | Vikingskipshuset, Moesgaard, Aboa Vetus Ars Nova, Medelhavsmuseet |
| **Maritime Museum** | 6 | Vasamuseet, Vikingeskibsmuseet, Frammuseet, M/S Maritime Museum |
| **Design Museum** | 4 | Röhsska museet, ArkDes, Design Museum Helsinki, Designmuseum Danmark |
| **Natural History Museum** | 3 | Naturhistoriska riksmuseet, Luomus, Húsavík Whale Museum |
| **Folk Museum** | 4 | Ájtte, RiddoDuottarMuseat, Siida, Skógar Museum |
| **Specialized Museum** | 5 | Tekniska museet, Kon-Tiki Museet, Arktikum |

### Linked Data Coverage

| Identifier | Count | Notes |
|------------|-------|-------|
| **Wikidata URI** | 109 | Links to Wikidata Q-items |
| **GeoNames URI** | 105 | Links to GeoNames city entries |
| **ISIL code** | 17 | International Standard Identifier for Libraries (ISO 15511) |
| **Website** | 116 | Official institution homepage |
| **Founding date** | 109 | Year established |

## RDF Model

Each institution is represented as a triple-typed resource:

```turtle
ni:nationalmuseum-se a crm:E40_Legal_Body , org:Organization , schema:Museum ;
    rdfs:label "Nationalmuseum"@en , "Nationalmuseum"@sv ;
    skos:prefLabel "Nationalmuseum"@en ;
    skos:inScheme <https://metadatahub.eu/data/nordic-institutions> ;
    skos:definition "Sweden's museum of art and design..."@en ;
    schema:additionalType "art-museum" ;
    schema:addressCountry "SE" ;
    schema:addressLocality "Stockholm" ;
    schema:location <http://sws.geonames.org/2673730/> ;
    owl:sameAs <http://www.wikidata.org/entity/Q842858> ;
    dcterms:identifier "SE-Nm" ;
    foaf:homepage <https://www.nationalmuseum.se/> ;
    schema:foundingDate "1792"^^xsd:gYear .
```

### Prefixes

| Prefix | Namespace | Purpose |
|--------|-----------|---------|
| `crm:` | `http://www.cidoc-crm.org/cidoc-crm/` | CIDOC-CRM cultural heritage ontology |
| `org:` | `http://www.w3.org/ns/org#` | W3C Organization Ontology |
| `schema:` | `https://schema.org/` | Schema.org vocabulary |
| `skos:` | `http://www.w3.org/2004/02/skos/core#` | SKOS concept scheme |
| `foaf:` | `http://xmlns.com/foaf/0.1/` | FOAF vocabulary |
| `dcterms:` | `http://purl.org/dc/terms/` | Dublin Core Terms |
| `owl:` | `http://www.w3.org/2002/07/owl#` | OWL (for sameAs links) |
| `ni:` | `https://metadatahub.eu/data/nordic-institutions/` | This dataset |

## SPARQL Examples

### List all Swedish museums

```sparql
PREFIX schema: <https://schema.org/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?museum ?name ?city ?type WHERE {
  ?museum schema:addressCountry "SE" ;
          rdfs:label ?name ;
          schema:addressLocality ?city ;
          schema:additionalType ?type .
  FILTER(lang(?name) = "en")
}
ORDER BY ?name
```

### Find all open-air museums

```sparql
PREFIX schema: <https://schema.org/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?museum ?name ?country ?city WHERE {
  ?museum schema:additionalType "open-air-museum" ;
          rdfs:label ?name ;
          schema:addressCountry ?country ;
          schema:addressLocality ?city .
  FILTER(lang(?name) = "en")
}
ORDER BY ?country ?name
```

### Museums with Wikidata links

```sparql
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX schema: <https://schema.org/>

SELECT ?museum ?name ?wikidata WHERE {
  ?museum owl:sameAs ?wikidata ;
          rdfs:label ?name ;
          schema:addressCountry ?country .
  FILTER(lang(?name) = "en")
  FILTER(STRSTARTS(STR(?wikidata), "http://www.wikidata.org/"))
}
ORDER BY ?country ?name
```

### Sami museums across the Nordic countries

```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX schema: <https://schema.org/>

SELECT ?museum ?name ?country ?description WHERE {
  ?museum skos:definition ?description ;
          rdfs:label ?name ;
          schema:addressCountry ?country .
  FILTER(lang(?name) = "en")
  FILTER(CONTAINS(LCASE(?description), "sami"))
}
ORDER BY ?country
```

### Count museums by country

```sparql
PREFIX schema: <https://schema.org/>

SELECT ?country (COUNT(?museum) AS ?count) WHERE {
  ?museum schema:addressCountry ?country .
}
GROUP BY ?country
ORDER BY DESC(?count)
```

### Museums founded before 1900

```sparql
PREFIX schema: <https://schema.org/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?museum ?name ?year ?country WHERE {
  ?museum schema:foundingDate ?year ;
          rdfs:label ?name ;
          schema:addressCountry ?country .
  FILTER(lang(?name) = "en")
  FILTER(xsd:integer(?year) < 1900)
}
ORDER BY ?year
```

### Museums in a specific city with full details

```sparql
PREFIX schema: <https://schema.org/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?museum ?name ?type ?year ?website ?description WHERE {
  ?museum schema:addressLocality "Stockholm" ;
          rdfs:label ?name ;
          schema:additionalType ?type ;
          skos:definition ?description .
  OPTIONAL { ?museum schema:foundingDate ?year }
  OPTIONAL { ?museum foaf:homepage ?website }
  FILTER(lang(?name) = "en")
}
ORDER BY ?type ?name
```

## Data Generation

The Turtle and JSON-LD files are generated from YAML source data:

```bash
python3 scripts/generate-nordic-institutions.py
```

Source data: `data/nordic-institutions/institutions.yaml`
Schema: `data/nordic-institutions/_schema.yaml`
