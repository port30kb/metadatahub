---
title: "Nordic Techniques Vocabulary"
description: "170 linked data entries forming a SKOS vocabulary of techniques used in Nordic museum cataloguing — from Viking Age pattern welding and nålbinding to Sámi duodji, rosemaling, and modern printmaking."
date: 2025-03-15
type: dataset
publisher: "Port 30 KB"
license: "https://creativecommons.org/licenses/by-sa/4.0/"
theme: "http://publications.europa.eu/resource/authority/data-theme/TECH"
standards:
  - SKOS
  - Getty AAT
  - DCAT-AP
tags:
  - techniques
  - vocabulary
  - museum-cataloguing
  - Nordic
  - Scandinavia
  - Sámi
  - crafts
  - SKOS
  - linked-data
  - Getty-AAT
distributions:
  - id: "turtle"
    title: "RDF Turtle"
    accessURL: "https://metadatahub.eu/data/nordic-techniques.ttl"
    downloadURL: "https://metadatahub.eu/data/nordic-techniques.ttl"
    mediaType: "text/turtle"
  - id: "jsonld"
    title: "JSON-LD"
    accessURL: "https://metadatahub.eu/data/nordic-techniques.jsonld"
    downloadURL: "https://metadatahub.eu/data/nordic-techniques.jsonld"
    mediaType: "application/ld+json"
---

## Overview

This dataset provides a **SKOS concept scheme** of techniques used in Nordic museum cataloguing. It covers ~170 techniques organised into a hierarchy of categories, each with multilingual labels (English, Swedish, Danish, Norwegian Bokmål, Finnish, and Northern Sámi where applicable) and mappings to the [Getty Art & Architecture Thesaurus (AAT)](http://www.getty.edu/research/tools/vocabularies/aat/) where URIs exist.

The vocabulary is designed for use in collection management systems, digital catalogues, and linked data applications across Nordic cultural heritage institutions.

## Sources

- [Getty Art & Architecture Thesaurus (AAT)](http://www.getty.edu/research/tools/vocabularies/aat/) — authoritative technique URIs and definitions
- [Wikipedia: Viking Age crafts](https://en.wikipedia.org/wiki/Viking_art) — Norse metalworking, woodcarving, and textile techniques
- [Wikipedia: Duodji](https://en.wikipedia.org/wiki/Duodji) — Sámi traditional handicraft
- [Wikipedia: Rosemaling](https://en.wikipedia.org/wiki/Rosemaling) — Norwegian decorative painting
- [Wikipedia: Nålbinding](https://en.wikipedia.org/wiki/N%C3%A5lbinding) — Viking needle-binding textile technique
- Nordic museum cataloguing traditions (Nordiska museet, Nationalmuseet, etc.)

License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## Statistics

| Category | Count |
|----------|-------|
| **Total entries** | ~170 |
| **Metalworking** | ~28 (forging, pattern welding, casting, filigree, granulation, gilding, niello, damascening, enameling, etc.) |
| **Textile techniques** | ~20 (weaving, tablet weaving, nålbinding, rya knotting, felting, embroidery, knitting, etc.) |
| **Woodworking** | ~18 (carving, stave construction, clinker building, coopering, log building, marquetry, etc.) |
| **Ceramics** | ~14 (throwing, hand building, coiling, glazing, salt glazing, tin glazing, raku, sgraffito, etc.) |
| **Stone and lapidary** | ~13 (stone carving, rune carving, flint knapping, petroglyph carving, soapstone carving, etc.) |
| **Painting and surface** | ~14 (oil painting, tempera, fresco, rosemaling, kurbits painting, polychromy, etc.) |
| **Printmaking** | ~10 (woodcut, etching, lithography, aquatint, mezzotint, screen printing, linocut, etc.) |
| **Glass** | ~10 (glassblowing, lampworking, stained glass, glass bead making, fusing, etc.) |
| **Leather and fibre** | ~10 (tanning, bookbinding, basket weaving, rope making, parchment making, etc.) |
| **Sámi/Nordic-specific** | ~16 (duodji, tin-thread embroidery, root weaving, reindeer antler carving, bog iron smelting, etc.) |
| **Entries with AAT URIs** | ~100+ |
| **Languages** | 5–6 per entry (en, sv, da, nb, fi; se for Sámi entries) |

## Hierarchy

The vocabulary follows a two-level hierarchy using `skos:broader`:

```
Metalworking
├── Forging
│   ├── Pattern welding
│   └── Wrought ironwork
├── Casting
│   ├── Lost-wax casting
│   └── Sand casting
├── Filigree, Granulation, Gilding (→ Fire gilding)
├── Niello, Damascening, Enameling (→ Cloisonné, Champlevé)
├── Soldering, Riveting, Wire drawing, Sheet metalwork
└── Raising, Patination, Metal spinning, Stamping

Textile techniques
├── Weaving → Tapestry weaving, Tablet weaving
├── Nålbinding, Rya knotting, Spinning, Felting
├── Embroidery, Appliqué, Knitting, Braiding, Quilting
└── Lace making → Bobbin lace

Woodworking
├── Wood carving → Chip carving, Relief carving
├── Stave construction, Joinery, Marquetry
├── Boat building → Clinker building
├── Log building, Coopering, Bark working → Birch bark plaiting
└── Bentwood, Wood bending, Wood inlay

Ceramics
├── Throwing, Hand building (→ Coiling, Slab building)
├── Glazing → Salt glazing, Tin glazing
├── Firing → Stoneware firing, Raku
└── Slip decoration, Sgraffito, Kiln building

Stone and lapidary
├── Stone carving → Rune carving, Soapstone carving, Petroglyph carving
├── Flint knapping, Stone grinding, Gem cutting
└── Mosaic work, Stone masonry, Stone dressing, Stone setting

Painting and surface decoration
├── Oil painting, Tempera, Fresco, Watercolour, Encaustic
├── Rosemaling, Kurbits painting, Dala painting
├── Icon painting, Polychromy, Limewashing
└── Lacquering, Stenciling

Printmaking
├── Woodcut, Linocut
├── Engraving, Etching, Drypoint, Aquatint, Mezzotint
├── Lithography
└── Screen printing

Glass techniques
├── Glassblowing, Glass moulding, Glass casting
├── Lampworking, Glass bead making
├── Glass cutting, Glass engraving
└── Stained glass, Glass fusing

Leather and fibre
├── Tanning → Bark tanning
├── Leather tooling, Leather sewing, Saddlery
├── Bookbinding, Parchment making
└── Basket weaving, Rope making

Sámi and Nordic-specific
├── Duodji (Sámi handicraft)
│   ├── Tin thread embroidery, Root weaving
│   ├── Reindeer antler carving, Birch bark craft
│   ├── Sámi knife making, Sámi belt weaving
├── Bone carving, Horn working, Amber working
├── Ivory carving, Viking ship building
└── Tar production, Charcoal making, Bog iron smelting
```

## Data model

Each technique is modelled as a `skos:Concept` within a `skos:ConceptScheme`. Example in Turtle:

```turtle
@prefix skos:    <http://www.w3.org/2004/02/skos/core#> .
@prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix nt:      <https://metadatahub.eu/data/nordic-techniques/> .

nt:pattern-welding a skos:Concept ;
    rdfs:label "Pattern welding"@en ;
    rdfs:label "Mönstersvetsning"@sv ;
    rdfs:label "Mønstersvejsning"@da ;
    rdfs:label "Mønstersveising"@nb ;
    rdfs:label "Kuviohitsaus"@fi ;
    skos:prefLabel "Pattern welding"@en ;
    skos:prefLabel "Mönstersvetsning"@sv ;
    skos:inScheme <https://metadatahub.eu/data/nordic-techniques> ;
    skos:definition "Viking Age sword-making technique combining iron and steel rods to create patterned blades."@en ;
    skos:broader nt:forging ;
    skos:exactMatch <http://vocab.getty.edu/aat/300264568> .
```

## SPARQL examples

**List all metalworking techniques with their Swedish labels:**

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX nt:   <https://metadatahub.eu/data/nordic-techniques/>

SELECT ?technique ?label_en ?label_sv WHERE {
  ?technique skos:broader+ nt:metalworking ;
             rdfs:label ?label_en ;
             rdfs:label ?label_sv .
  FILTER(lang(?label_en) = "en")
  FILTER(lang(?label_sv) = "sv")
}
ORDER BY ?label_en
```

**Find all techniques with Getty AAT mappings:**

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?technique ?label ?aat_uri WHERE {
  ?technique a skos:Concept ;
             skos:inScheme <https://metadatahub.eu/data/nordic-techniques> ;
             rdfs:label ?label ;
             skos:exactMatch ?aat_uri .
  FILTER(lang(?label) = "en")
  FILTER(STRSTARTS(STR(?aat_uri), "http://vocab.getty.edu/aat/"))
}
ORDER BY ?label
```

**Retrieve the full hierarchy for a category:**

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX nt:   <https://metadatahub.eu/data/nordic-techniques/>

SELECT ?parent_label ?child_label WHERE {
  ?child skos:broader ?parent ;
         rdfs:label ?child_label .
  ?parent rdfs:label ?parent_label .
  FILTER(lang(?child_label) = "en")
  FILTER(lang(?parent_label) = "en")
}
ORDER BY ?parent_label ?child_label
```

**Find all Sámi (duodji) techniques with Northern Sámi labels:**

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX nt:   <https://metadatahub.eu/data/nordic-techniques/>

SELECT ?technique ?label_en ?label_se WHERE {
  ?technique skos:broader+ nt:duodji ;
             rdfs:label ?label_en ;
             rdfs:label ?label_se .
  FILTER(lang(?label_en) = "en")
  FILTER(lang(?label_se) = "se")
}
ORDER BY ?label_en
```
