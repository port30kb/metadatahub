---
title: "Nordic Art and Design Movements Thesaurus"
description: "~95 linked data entries covering Nordic art, architecture, and design movements from the Renaissance to contemporary — a SKOS vocabulary with multilingual labels in five Nordic languages and Getty AAT mappings."
date: 2025-03-15
type: dataset
publisher: "Port 30 KB"
license: "https://creativecommons.org/licenses/by-sa/4.0/"
theme: "http://publications.europa.eu/resource/authority/data-theme/EDUC"
standards:
  - SKOS
  - W3C Time Ontology
  - Getty AAT
tags:
  - art-history
  - design
  - Scandinavia
  - Nordic
  - Denmark
  - Finland
  - Iceland
  - Norway
  - Sweden
  - SKOS
  - linked-data
  - thesaurus
distributions:
  - id: "turtle"
    title: "RDF Turtle (~95 entries)"
    accessURL: "https://metadatahub.eu/data/nordic-art-movements.ttl"
    downloadURL: "https://metadatahub.eu/data/nordic-art-movements.ttl"
    mediaType: "text/turtle"
  - id: "jsonld"
    title: "JSON-LD (~95 entries)"
    accessURL: "https://metadatahub.eu/data/nordic-art-movements.jsonld"
    downloadURL: "https://metadatahub.eu/data/nordic-art-movements.jsonld"
    mediaType: "application/ld+json"
---

## Overview

This dataset models **Nordic art and design movements** as a [SKOS](https://www.w3.org/2004/02/skos/core) concept scheme with ~95 entries, using the [W3C Time Ontology](http://www.w3.org/2006/time) for temporal extents and [Getty AAT](http://vocab.getty.edu/aat/) mappings via `skos:closeMatch`. It covers movements from the Nordic Renaissance (c. 1500) through contemporary movements such as New Nordic Design and Scandinavian Minimalism.

The thesaurus spans the five Nordic countries (Denmark, Finland, Iceland, Norway, Sweden) and organizes movements into a `skos:broader`/`skos:narrower` hierarchy — for example, Nordic National Romanticism encompasses Swedish National Romanticism, Finnish Karelian National Romanticism, and Norwegian Dragestil as narrower concepts.

Each entry includes multilingual labels in at least English and Swedish, with most entries also providing Danish, Norwegian Bokmal, and Finnish translations.

## Sources

This dataset is compiled from the following sources:

- [Wikipedia: Scandinavian design](https://en.wikipedia.org/wiki/Scandinavian_design) — post-war design movement, Danish Modern, Finnish Design
- [Wikipedia: Nordic art](https://en.wikipedia.org/wiki/Nordic_art) — overview of art traditions across the Nordic countries
- [Wikipedia: Danish Golden Age](https://en.wikipedia.org/wiki/Danish_Golden_Age) — early 19th-century Danish painting and culture
- [Wikipedia: National Romanticism](https://en.wikipedia.org/wiki/National_Romanticism) — pan-Nordic architectural and artistic movement
- [Wikipedia: Skagen Painters](https://en.wikipedia.org/wiki/Skagen_Painters) — Danish-Scandinavian artists' colony
- [Wikipedia: Functionalism (architecture)](https://en.wikipedia.org/wiki/Functionalism_(architecture)) — Nordic Functionalism (funkis)
- [Getty Art & Architecture Thesaurus](http://vocab.getty.edu/aat/) — authoritative URIs for style/movement concepts

License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) (matching Wikipedia source license).

## Statistics

| Category | Count |
|----------|-------|
| **Total entries** | ~95 |
| **Pre-modern Nordic** | ~10 (Renaissance, Baroque, Rococo, Gustavian, Neoclassicism) |
| **Golden Ages** | ~10 (Danish Golden Age, Romantic Nationalism, Finnish Awakening) |
| **Late 19th Century** | ~20 (Skagen, Naturalism, Realism, National Romanticism, Impressionism) |
| **Fin-de-siecle / Early Modern** | ~15 (Jugend, Symbolism, Expressionism, Nordic Classicism, Swedish Grace) |
| **Modernism** | ~15 (Functionalism, CoBrA, Concrete Art, Constructivism, Informalism) |
| **Post-war / Design** | ~15 (Scandinavian Design, Danish Modern, Finnish Design, Brutalism) |
| **Contemporary** | ~10 (Nordic Noir, New Nordic, Minimalism, Sustainable Design) |
| **Languages** | 5 primary (en, sv, da, nb, fi) + is for Icelandic entries |
| **AAT mappings** | ~20 entries with `skos:closeMatch` to Getty AAT |
| **Hierarchical links** | ~30 `skos:broader` relationships |

## Hierarchy

The dataset uses SKOS `broader`/`narrower` relationships to organize movements:

```
Nordic Art and Design Movements (ConceptScheme)
├── Pre-modern
│   ├── Nordic Renaissance (1500–1650)
│   ├── Nordic Baroque (1600–1750)
│   │   ├── Danish-Norwegian Baroque
│   │   └── Swedish Baroque
│   ├── Nordic Rococo (1730–1790)
│   ├── Nordic Neoclassicism (1760–1850)
│   │   └── Danish Neoclassicism
│   ├── Gustavian Neoclassicism (1772–1809)
│   └── Swedish Classicism (1780–1850)
├── Golden Ages
│   ├── Danish Golden Age (1800–1850)
│   ├── Nordic Romanticism (1800–1870)
│   │   ├── Norwegian Romantic Nationalism
│   │   ├── Swedish Romantic Landscape Painting
│   │   ├── Finnish Romantic Painting
│   │   ├── Icelandic Romanticism
│   │   └── Scandinavian Musical Romanticism
│   └── Finnish National Awakening (1835–1880)
├── Late 19th Century
│   ├── Nordic Realism (1870–1900)
│   │   ├── Skagen Painters (1870–1910)
│   │   ├── Opponenterna (1885–1895)
│   │   └── Varberg School (1893–1910)
│   ├── Nordic Naturalism (1880–1900)
│   ├── Nordic Impressionism (1880–1910)
│   └── Nordic National Romanticism (1880–1920)
│       ├── Swedish National Romanticism
│       ├── Finnish Karelian National Romanticism
│       └── Norwegian Dragon Style (Dragestil)
├── Fin-de-siècle / Early Modern
│   ├── Nordic Art Nouveau / Jugend (1890–1915)
│   │   ├── Swedish Jugend
│   │   ├── Finnish Jugend
│   │   └── Ålesund Jugend
│   ├── Nordic Symbolism (1890–1910)
│   ├── Nordic Expressionism (1905–1940)
│   ├── Swedish Grace (1920–1935)
│   └── Nordic Classicism (1910–1935)
│       ├── Danish Neoclassical Revival
│       └── Finnish Classicism
├── Modernism
│   ├── Nordic Functionalism (1927–1950)
│   │   ├── Swedish Functionalism
│   │   ├── Danish Functionalism
│   │   └── Finnish Modernism (Aalto)
│   ├── Norwegian Modernism (1930–1960)
│   ├── CoBrA — Nordic Participants (1948–1951)
│   ├── Nordic Concrete Art (1945–1970)
│   └── Nordic Constructivism (1950–1970)
├── Post-war / Design
│   ├── Scandinavian Design (1945–1975)
│   │   ├── Danish Modern
│   │   ├── Swedish Modern
│   │   ├── Finnish Design (Marimekko, Arabia, Iittala)
│   │   ├── Scandinavian Mid-Century Modern
│   │   └── Nordic Textile Design
│   ├── Nordic Industrial Design (1960–1990)
│   ├── Nordic Brutalism (1955–1975)
│   └── Nordic Pop Art (1962–1975)
└── Contemporary
    ├── Nordic Neo-Expressionism (1980–2000)
    ├── Nordic Noir Aesthetic (1990–present)
    ├── Scandinavian Minimalism (1990–present)
    ├── Nordic Contemporary Art (1990–present)
    ├── New Nordic Design (2000–present)
    ├── Nordic Sustainable Design (2010–present)
    └── Nordic Parametric Architecture (2005–present)
```

## Data Model

Each movement is a `skos:Concept` within a `skos:ConceptScheme`, with:

| Property | Usage |
|----------|-------|
| `rdfs:label` | Multilingual name (en, sv, da, nb, fi) |
| `skos:prefLabel` | Preferred label per language |
| `skos:definition` | English description |
| `skos:broader` | Parent movement |
| `skos:inScheme` | Link to ConceptScheme |
| `skos:closeMatch` | Getty AAT URI (where available) |
| `time:hasBeginning` | Start year (`xsd:gYear`) |
| `time:hasEnd` | End year (`xsd:gYear`) |
| `dcterms:source` | Wikipedia source |

## SPARQL Examples

### All movements with English labels and dates

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX time: <http://www.w3.org/2006/time#>

SELECT ?concept ?label ?start ?end
WHERE {
  ?concept a skos:Concept ;
           rdfs:label ?label ;
           time:hasBeginning [ time:inXSDgYear ?start ] ;
           time:hasEnd [ time:inXSDgYear ?end ] .
  FILTER(lang(?label) = "en")
}
ORDER BY ?start
```

### Movements with Getty AAT mappings

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?concept ?label ?aat
WHERE {
  ?concept a skos:Concept ;
           rdfs:label ?label ;
           skos:closeMatch ?aat .
  FILTER(lang(?label) = "en")
  FILTER(STRSTARTS(STR(?aat), "http://vocab.getty.edu/aat/"))
}
ORDER BY ?label
```

### Sub-movements of National Romanticism

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX nam:  <https://metadatahub.eu/data/nordic-art-movements/>

SELECT ?child ?label
WHERE {
  ?child skos:broader nam:national-romanticism ;
         rdfs:label ?label .
  FILTER(lang(?label) = "en")
}
```

### Finnish labels for all movements

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?concept ?fi_label ?en_label
WHERE {
  ?concept a skos:Concept ;
           rdfs:label ?fi_label ;
           rdfs:label ?en_label .
  FILTER(lang(?fi_label) = "fi")
  FILTER(lang(?en_label) = "en")
}
ORDER BY ?en_label
```

### Movements active in a given year (e.g. 1900)

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>

SELECT ?concept ?label ?start ?end
WHERE {
  ?concept a skos:Concept ;
           rdfs:label ?label ;
           time:hasBeginning [ time:inXSDgYear ?start ] ;
           time:hasEnd [ time:inXSDgYear ?end ] .
  FILTER(lang(?label) = "en")
  FILTER(?start <= "1900"^^xsd:gYear && ?end >= "1900"^^xsd:gYear)
}
ORDER BY ?start
```
