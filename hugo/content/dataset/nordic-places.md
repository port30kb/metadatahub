---
title: "Nordic Place Name Authority"
description: "206 linked data entries covering place names across Sweden, Norway, Finland, Denmark, Iceland, and Sápmi — countries, regions, historical provinces, cities, archaeological sites, and historical name variants with multilingual labels, coordinates, and links to GeoNames and Wikidata."
date: 2025-01-15
type: dataset
publisher: "Port 30 KB"
license: "https://creativecommons.org/licenses/by-sa/4.0/"
theme: "http://publications.europa.eu/resource/authority/data-theme/REGI"
standards:
  - SKOS
  - WGS84
  - GeoNames
  - Wikidata
tags:
  - Nordic
  - Scandinavia
  - Sweden
  - Norway
  - Finland
  - Denmark
  - Iceland
  - Sápmi
  - place-names
  - geography
  - archaeology
  - SKOS
  - linked-data
distributions:
  - id: "turtle"
    title: "RDF Turtle (206 entries)"
    accessURL: "https://metadatahub.eu/data/nordic-places.ttl"
    downloadURL: "https://metadatahub.eu/data/nordic-places.ttl"
    mediaType: "text/turtle"
  - id: "jsonld"
    title: "JSON-LD (206 entries)"
    accessURL: "https://metadatahub.eu/data/nordic-places.jsonld"
    downloadURL: "https://metadatahub.eu/data/nordic-places.jsonld"
    mediaType: "application/ld+json"
---

## Overview

This dataset models a **Nordic Place Name Authority** as a SKOS concept scheme with 206 entries, using [SKOS](http://www.w3.org/2004/02/skos/core) for hierarchical relationships and multilingual labels, [WGS84](http://www.w3.org/2003/01/geo/wgs84_pos) for geographic coordinates, and [OWL sameAs](http://www.w3.org/2002/07/owl) links to [GeoNames](https://www.geonames.org/) and [Wikidata](https://www.wikidata.org/). It covers the five Nordic countries plus the Sámi cultural region (Sápmi), with place names in English and local languages including Swedish, Norwegian (Bokmål and Nynorsk), Finnish, Danish, Icelandic, Northern Sámi, Faroese, and Kalaallisut (Greenlandic).

The dataset includes historical name variants (e.g., Kristiania/Christiania for Oslo, Åbo for Turku, Helsingfors for Helsinki, Nidaros for Trondheim, Godthåb for Nuuk) as `skos:hiddenLabel` properties, enabling search across historical and modern nomenclature.

## Sources

- [GeoNames](https://www.geonames.org/) — geographic coordinates and identifiers
- [Wikidata](https://www.wikidata.org/) — structured data identifiers (Q-numbers)
- [Wikipedia: Nordic countries](https://en.wikipedia.org/wiki/Nordic_countries) — general reference

## Statistics

| Country / Region | Entries | Types |
|---|---|---|
| **Sweden** | ~60 | 1 country, 24 landskap, 3 regions, 22 cities/towns, 2 islands |
| **Norway** | ~42 | 1 country, 12 regions, 15 cities/towns, 3 islands, 2 villages |
| **Finland** | ~32 | 1 country, 12 regions, 18 cities/towns |
| **Denmark** | ~30 | 1 country, 8 regions/islands, 16 cities/towns |
| **Iceland** | ~20 | 1 country, 6 regions, 8 cities/towns, 2 archaeological sites |
| **Sápmi** | ~20 | 8 regions, 12 towns/villages |
| **Archaeological sites** | ~32 | Birka, Hedeby, Jelling, Gamla Uppsala, etc. |

### Place Types

| Type | Count | Description |
|---|---|---|
| `country` | 5 | National entities |
| `region` | 44 | Modern and historical regions |
| `landskap` | 24 | Swedish historical provinces |
| `city` | 67 | Major cities |
| `town` | 22 | Smaller towns |
| `village` | 3 | Small settlements |
| `island` | 9 | Islands and archipelagos |
| `archaeological-site` | 32 | Archaeological and historical sites |

## Data Model

Each place is modelled as both a `skos:Concept` and a Schema.org type (`schema:City`, `schema:Country`, `schema:AdministrativeArea`, or `schema:Place`). The concept scheme uses:

- **`skos:prefLabel`** — preferred name in each language
- **`skos:altLabel`** — alternative current names
- **`skos:hiddenLabel`** — historical/former names (for search indexing)
- **`skos:broader`** — hierarchical parent (e.g., Stockholm → Uppland → Sweden)
- **`skos:definition`** — English description
- **`geo:lat` / `geo:long`** — WGS84 coordinates
- **`owl:sameAs`** — links to GeoNames and Wikidata URIs

### Base URI

```
https://metadatahub.eu/data/nordic-places
```

Individual place URIs follow the pattern:

```
https://metadatahub.eu/data/nordic-places/{id}
```

For example:
- `https://metadatahub.eu/data/nordic-places/stockholm`
- `https://metadatahub.eu/data/nordic-places/birka`
- `https://metadatahub.eu/data/nordic-places/sapmi`

## SPARQL Examples

### All Swedish landskap

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX np: <https://metadatahub.eu/data/nordic-places/>

SELECT ?place ?name ?description
WHERE {
  ?place skos:inScheme <https://metadatahub.eu/data/nordic-places> ;
         dcterms:type "landskap" ;
         skos:prefLabel ?name ;
         skos:definition ?description .
  FILTER(lang(?name) = "en")
}
ORDER BY ?name
```

### Cities with coordinates, linked to Wikidata

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT ?place ?name ?lat ?lon ?wikidata
WHERE {
  ?place skos:inScheme <https://metadatahub.eu/data/nordic-places> ;
         dcterms:type "city" ;
         skos:prefLabel ?name ;
         geo:lat ?lat ;
         geo:long ?lon ;
         owl:sameAs ?wikidata .
  FILTER(lang(?name) = "en")
  FILTER(STRSTARTS(STR(?wikidata), "http://www.wikidata.org/"))
}
ORDER BY ?name
```

### Places with historical name variants

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?place ?currentName ?historicalName
WHERE {
  ?place skos:inScheme <https://metadatahub.eu/data/nordic-places> ;
         skos:prefLabel ?currentName ;
         skos:hiddenLabel ?historicalName .
  FILTER(lang(?currentName) = "en")
}
ORDER BY ?currentName
```

### Sámi place names with their Nordic-language equivalents

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?place ?samiName ?englishName
WHERE {
  ?place skos:inScheme <https://metadatahub.eu/data/nordic-places> ;
         skos:prefLabel ?samiName ;
         skos:prefLabel ?englishName .
  FILTER(lang(?samiName) = "se")
  FILTER(lang(?englishName) = "en")
}
ORDER BY ?samiName
```

### All archaeological sites with coordinates

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>

SELECT ?site ?name ?lat ?lon ?description
WHERE {
  ?site skos:inScheme <https://metadatahub.eu/data/nordic-places> ;
        dcterms:type "archaeological-site" ;
        skos:prefLabel ?name ;
        skos:definition ?description .
  FILTER(lang(?name) = "en")
  OPTIONAL { ?site geo:lat ?lat ; geo:long ?lon }
}
ORDER BY ?name
```

### Hierarchical browsing — all places within a region

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?place ?name ?type
WHERE {
  ?place skos:broader+ <https://metadatahub.eu/data/nordic-places/uppland> ;
         skos:prefLabel ?name ;
         dcterms:type ?type .
  FILTER(lang(?name) = "en")
}
ORDER BY ?type ?name
```

## Download

- **Turtle**: [nordic-places.ttl](/data/nordic-places.ttl) (text/turtle)
- **JSON-LD**: [nordic-places.jsonld](/data/nordic-places.jsonld) (application/ld+json)

## Regeneration

To regenerate after editing the YAML source data:

```bash
python3 scripts/generate-nordic-places.py
```
