---
title: "Geologic Time Scale"
description: "250 linked data entries covering Earth's 4.6 billion year history — from the Hadean eon through geologic eras, periods, and epochs to archaeological ages (Stone Age, Bronze Age, Iron Age, Viking Age, Medieval) with a Scandinavian focus."
date: 2024-12-01
type: dataset
publisher: "Port 30 KB"
license: "https://creativecommons.org/licenses/by-sa/4.0/"
theme: "http://publications.europa.eu/resource/authority/data-theme/TECH"
standards:
  - GeoSciML
  - SKOS
  - ICS Chronostratigraphic Chart
tags:
  - geologic-time
  - stratigraphy
  - archaeology
  - Scandinavia
  - SKOS
  - linked-data
distributions:
  - id: "turtle"
    title: "RDF Turtle (250 entries)"
    accessURL: "https://metadatahub.eu/data/geologic-timescale.ttl"
    downloadURL: "https://metadatahub.eu/data/geologic-timescale.ttl"
    mediaType: "text/turtle"
  - id: "jsonld"
    title: "JSON-LD (250 entries)"
    accessURL: "https://metadatahub.eu/data/geologic-timescale.jsonld"
    downloadURL: "https://metadatahub.eu/data/geologic-timescale.jsonld"
    mediaType: "application/ld+json"
---

## Overview

This dataset models the **complete geologic time scale** as a SKOS concept scheme with 250 entries, using the [GeoSciML Geologic Timescale ontology](http://resource.geosciml.org/ontology/timescale/gts) and [W3C Time Ontology](http://www.w3.org/2006/time). It spans from the formation of Earth (4,600 Ma) through all geologic divisions down to individual ages/stages, then bridges into **archaeological and cultural periods** with a Scandinavian focus — from the Stone Age through the Viking Age and Medieval period to the Early Modern era.

## Sources

This dataset is compiled from the following sources:

- [Wikipedia: Geologic time scale](https://en.wikipedia.org/wiki/Geologic_time_scale) — primary source for hierarchical structure and dates
- [ICS International Chronostratigraphic Chart v2024/12](https://stratigraphy.org/ICSchart/ChronostratChart2024-12.pdf) — authoritative dates for all formally defined boundaries
- [Wikipedia: Holocene](https://en.wikipedia.org/wiki/Holocene) — Greenlandian, Northgrippian, Meghalayan ages
- [Wikipedia: Pleistocene](https://en.wikipedia.org/wiki/Pleistocene) — Gelasian, Calabrian, Chibanian, Late Pleistocene stages
- [Wikipedia: Three-age system](https://en.wikipedia.org/wiki/Three-age_system) — Stone Age, Bronze Age, Iron Age framework
- [Wikipedia: Scandinavian prehistory](https://en.wikipedia.org/wiki/Scandinavian_prehistory) — Nordic archaeological periods and cultures
- [Wikipedia: Viking Age](https://en.wikipedia.org/wiki/Viking_Age) — Viking Age dates and subdivisions

License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) (matching Wikipedia source license).

## Statistics

| Category | Count |
|----------|-------|
| **Total entries** | 250 |
| **Eons** | 4 (Hadean, Archean, Proterozoic, Phanerozoic) |
| **Eras** | 13 (incl. Hadean informal divisions) |
| **Periods** | 22 + 2 sub-periods (Mississippian, Pennsylvanian) |
| **Epochs** | 38 |
| **Ages/Stages** | ~80 (all Mesozoic + Cenozoic stages, Paleozoic key stages) |
| **Cultural ages** | ~50 (Stone Age through Early Modern, Scandinavian focus) |
| **Climate/extinction events** | ~15 (Big Five extinctions, Snowball Earth, PETM, etc.) |

## Hierarchy

The dataset follows the ICS hierarchy: **Eon > Era > Period > Epoch > Age**, with SKOS `broader`/`narrower` relationships linking each level. Cultural/archaeological ages are appended as a parallel hierarchy within the Holocene, bridging geologic and human timescales.

```
Phanerozoic (Eon, 538.8 Ma–Present)
├── Paleozoic (Era, 538.8–251.9 Ma)
│   ├── Cambrian (Period, 538.8–485.4 Ma)
│   │   ├── Terreneuvian (Epoch) → Fortunian, Stage 2
│   │   ├── Series 2 (Epoch) → Stage 3, Stage 4
│   │   ├── Miaolingian (Epoch) → Wuliuan, Drumian, Guzhangian
│   │   └── Furongian (Epoch) → Paibian, Jiangshanian, Stage 10
│   ├── ...
│   └── Permian (Period, 298.9–251.9 Ma)
│       ├── Cisuralian → Asselian, Sakmarian, Artinskian, Kungurian
│       ├── Guadalupian → Roadian, Wordian, Capitanian
│       └── Lopingian → Wuchiapingian, Changhsingian
├── Mesozoic (Era, 251.9–66 Ma)
│   ├── Triassic → Induan ... Rhaetian (7 stages)
│   ├── Jurassic → Hettangian ... Tithonian (11 stages)
│   └── Cretaceous → Berriasian ... Maastrichtian (12 stages)
└── Cenozoic (Era, 66 Ma–Present)
    ├── Paleogene → Danian ... Chattian
    ├── Neogene → Aquitanian ... Piacenzian
    └── Quaternary
        ├── Pleistocene → Gelasian, Calabrian, Chibanian, Late Pleistocene
        └── Holocene → Greenlandian, Northgrippian, Meghalayan
            ├── Stone Age (3.3 Ma–3300 BCE)
            │   ├── Paleolithic → Lower, Middle, Upper
            │   ├── Mesolithic → Maglemosian, Kongemose, Ertebølle
            │   └── Neolithic → Funnelbeaker, Pitted Ware, Battle Axe
            ├── Bronze Age → Early, Middle, Late, Nordic Bronze Age
            ├── Iron Age → Pre-Roman Iron Age
            ├── Roman Iron Age (1–400 CE)
            ├── Migration Period (375–550 CE)
            ├── Vendel Period (550–790 CE)
            ├── Viking Age (790–1100 CE)
            ├── Medieval Period (1050–1520 CE)
            └── Early Modern Period (1520–1789 CE)
```

## Data Model

Each entry uses GeoSciML's geochronologic class hierarchy with SKOS for labels and definitions:

```turtle
ts:jurassic a gts:GeochronologicPeriod ;
    rdfs:label "Jurassic"@en ;
    skos:inScheme <https://metadatahub.eu/data/geologic-timescale> ;
    skos:definition "Dinosaurs dominate; first birds (Archaeopteryx);
                     Pangaea breaks apart."@en ;
    gts:rank "Period" ;
    skos:broader ts:mesozoic ;
    time:hasBeginning [ time:inXSDgYear "201.4"^^xsd:decimal ;
                        rdfs:label "201.4 Ma" ] ;
    time:hasEnd [ time:inXSDgYear "143.1"^^xsd:decimal ;
                  rdfs:label "143.1 Ma" ] ;
    dcterms:source <https://en.wikipedia.org/wiki/Geologic_time_scale> .
```

## Key Geologic Periods

| Period | Dates | Highlights |
|--------|-------|------------|
| **Cambrian** | 538.8–485.4 Ma | Cambrian Explosion; most animal phyla appear |
| **Ordovician** | 485.4–443.8 Ma | Great Biodiversification; ends in mass extinction |
| **Silurian** | 443.8–419.2 Ma | First vascular land plants; jawed fish |
| **Devonian** | 419.2–358.9 Ma | Age of Fishes; first forests, insects, amphibians |
| **Carboniferous** | 358.9–298.9 Ma | Coal swamp forests; first reptiles; giant insects |
| **Permian** | 298.9–251.9 Ma | Pangaea; ends with the Great Dying (~96% species) |
| **Triassic** | 251.9–201.4 Ma | First dinosaurs, mammals, pterosaurs |
| **Jurassic** | 201.4–143.1 Ma | Dinosaurs dominate; Archaeopteryx; Pangaea rifts |
| **Cretaceous** | 143.1–66 Ma | Flowering plants; T. rex; K-Pg asteroid impact |
| **Paleogene** | 66–23 Ma | Mammals diversify; primates; warmest Cenozoic |
| **Neogene** | 23–2.58 Ma | Grasslands; great apes; Mediterranean crisis |
| **Quaternary** | 2.58 Ma–Present | Ice ages; Homo sapiens; civilization |

## Archaeological Ages (Scandinavian Focus)

| Period | Dates | Key Features |
|--------|-------|-------------|
| **Paleolithic** | 3.3 Ma–10,000 BCE | Stone tools; cave art; hunter-gatherers |
| **Mesolithic** | 10,000–4,000 BCE | Post-glacial; Maglemosian, Ertebølle cultures |
| **Neolithic** | 4,000–2,000 BCE | Funnelbeaker culture; megalithic tombs; farming |
| **Nordic Bronze Age** | 1,750–500 BCE | Burial mounds; rock carvings; sun chariot |
| **Pre-Roman Iron Age** | 500–1 BCE | Bog ore smelting; Hjortspring boat |
| **Roman Iron Age** | 1–400 CE | Runes develop; Roman trade goods |
| **Migration Period** | 375–550 CE | Gold bracteates; Völkerwanderung |
| **Vendel Period** | 550–790 CE | Boat burials; animal-style art |
| **Viking Age** | 790–1100 CE | Norse expansion; Birka, Hedeby; sagas |
| **Medieval** | 1050–1520 CE | Hanseatic trade; Kalmar Union; Black Death |
| **Early Modern** | 1520–1789 CE | Reformation; Swedish Empire; Linnaeus |

## SPARQL Examples

Query this dataset via the [SPARQL endpoint](/sparql):

```sparql
# List all geologic periods with dates
SELECT ?period ?label ?start ?end
WHERE {
  ?period gts:rank "Period" ;
          rdfs:label ?label ;
          time:hasBeginning [ rdfs:label ?start ] ;
          time:hasEnd [ rdfs:label ?end ] .
}
ORDER BY DESC(?start)

# Find all epochs within the Mesozoic
SELECT ?epoch ?label
WHERE {
  ?epoch gts:rank "Epoch" ;
         rdfs:label ?label ;
         skos:broader+ ts:mesozoic .
}

# All Viking Age and Medieval sub-periods
SELECT ?age ?label ?start ?end
WHERE {
  VALUES ?parent { ts:viking-age ts:medieval-period }
  ?age skos:broader ?parent ;
       rdfs:label ?label ;
       time:hasBeginning [ rdfs:label ?start ] ;
       time:hasEnd [ rdfs:label ?end ] .
}

# Mass extinction events
SELECT ?event ?label ?desc
WHERE {
  ?event rdfs:label ?label ;
         skos:definition ?desc .
  FILTER(CONTAINS(LCASE(STR(?label)), "extinction"))
}
```

## Download

- [Turtle (text/turtle)](/data/geologic-timescale.ttl) — 2,790 lines, all 250 entries with full hierarchy
- [JSON-LD (application/ld+json)](/data/geologic-timescale.jsonld) — Same data as JSON-LD graph
