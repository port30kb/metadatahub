---
title: "Geologic Time Scale"
description: "361 linked data entries covering Earth's 4.6 billion year history — from the Hadean eon through geologic eras, periods, and epochs to archaeological ages (Stone Age, Bronze Age, Iron Age, Viking Age, Medieval) with Scandinavian, European, and South American coverage."
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
  - South-America
  - SKOS
  - linked-data
distributions:
  - id: "turtle"
    title: "RDF Turtle (361 entries)"
    accessURL: "https://metadatahub.eu/data/geologic-timescale.ttl"
    downloadURL: "https://metadatahub.eu/data/geologic-timescale.ttl"
    mediaType: "text/turtle"
  - id: "jsonld"
    title: "JSON-LD (361 entries)"
    accessURL: "https://metadatahub.eu/data/geologic-timescale.jsonld"
    downloadURL: "https://metadatahub.eu/data/geologic-timescale.jsonld"
    mediaType: "application/ld+json"
---

## Overview

This dataset models the **complete geologic time scale** as a SKOS concept scheme with 361 entries, using the [GeoSciML Geologic Timescale ontology](http://resource.geosciml.org/ontology/timescale/gts) and [W3C Time Ontology](http://www.w3.org/2006/time). It spans from the formation of Earth (4,600 Ma) through all geologic divisions down to individual ages/stages, then bridges into **archaeological and cultural periods** — Scandinavian (Stone Age through Viking Age to Modern), European (Classical Greece through EU), and South American (Norte Chico through Inca Empire to 21st century).

## Sources

This dataset is compiled from the following sources:

- [Wikipedia: Geologic time scale](https://en.wikipedia.org/wiki/Geologic_time_scale) — primary source for hierarchical structure and dates
- [ICS International Chronostratigraphic Chart v2024/12](https://stratigraphy.org/ICSchart/ChronostratChart2024-12.pdf) — authoritative dates for all formally defined boundaries
- [Wikipedia: Holocene](https://en.wikipedia.org/wiki/Holocene) — Greenlandian, Northgrippian, Meghalayan ages
- [Wikipedia: Pleistocene](https://en.wikipedia.org/wiki/Pleistocene) — Gelasian, Calabrian, Chibanian, Late Pleistocene stages
- [Wikipedia: Three-age system](https://en.wikipedia.org/wiki/Three-age_system) — Stone Age, Bronze Age, Iron Age framework
- [Wikipedia: Scandinavian prehistory](https://en.wikipedia.org/wiki/Scandinavian_prehistory) — Nordic archaeological periods and cultures
- [Wikipedia: Viking Age](https://en.wikipedia.org/wiki/Viking_Age) — Viking Age dates and subdivisions
- [Wikipedia: History of Europe](https://en.wikipedia.org/wiki/History_of_Europe) — European historical periods framework
- [Wikipedia: Nordic Bronze Age](https://en.wikipedia.org/wiki/Nordic_Bronze_Age) — Montelius periods I–VI
- [Wikipedia: Iron Age Scandinavia](https://en.wikipedia.org/wiki/Iron_Age_Scandinavia) — Germanic Iron Age subdivisions
- [Wikipedia: History of Sweden](https://en.wikipedia.org/wiki/History_of_Sweden) — Swedish historical periods (Vasa, Stormaktstiden, Frihetstiden, Gustavian)
- [Wikipedia: Pre-Columbian era](https://en.wikipedia.org/wiki/Pre-Columbian_era) — Andean and South American civilizations
- [Wikipedia: Inca Empire](https://en.wikipedia.org/wiki/Inca_Empire) — Tawantinsuyu, expansion, and Spanish conquest
- [Wikipedia: History of South America](https://en.wikipedia.org/wiki/History_of_South_America) — Colonial, independence, and modern periods

License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) (matching Wikipedia source license).

## Statistics

| Category | Count |
|----------|-------|
| **Total entries** | 361 |
| **Eons** | 4 (Hadean, Archean, Proterozoic, Phanerozoic) |
| **Eras** | 13 (incl. Hadean informal divisions) |
| **Periods** | 22 + 2 sub-periods (Mississippian, Pennsylvanian) |
| **Epochs** | 38 |
| **Ages/Stages** | ~80 (all Mesozoic + Cenozoic stages, Paleozoic key stages) |
| **Cultural ages (Nordic)** | ~80 (Stone Age cultures, Bronze Age (Montelius I–VI), Iron Age, Viking Age, Medieval through Modern) |
| **Cultural ages (European)** | ~25 (Classical Greece, Roman Empire, Carolingian, Crusades, Renaissance, Baroque, Enlightenment, etc.) |
| **South American periods** | ~49 (Norte Chico, Chavín, Moche, Inca Empire, colonial viceroyalties, independence wars, modern) |
| **Climate/extinction events** | ~15 (Big Five extinctions, Snowball Earth, PETM, etc.) |
| **Nordic-specific** | ~40 (Bromme, Fosna-Hensbacka, Komsa, Ertebølle, Vendel, Kalmar Union, Stormaktstiden, etc.) |

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
            │
            ├── Stone Age (3.3 Ma–3300 BCE)
            │   ├── Paleolithic → Lower, Middle, Upper
            │   │   └── Bromme Culture, Ahrensburg Culture
            │   ├── Mesolithic → Fosna-Hensbacka, Komsa, Maglemosian,
            │   │                Kongemose, Nøstvet-Lihult, Ertebølle
            │   └── Neolithic → Funnelbeaker, Pitted Ware, Battle Axe,
            │                   Comb Ceramic, Late Neolithic
            ├── Bronze Age → Early, Middle, Late
            │   └── Nordic Bronze Age → Montelius I–VI
            ├── Iron Age → Pre-Roman (+ Jastorf Culture)
            │
            │ ── SCANDINAVIAN TRACK ──
            ├── Roman Iron Age (1–400 CE) → Early, Late
            ├── Germanic Iron Age (400–790 CE)
            │   ├── Migration Period → Early, Late
            │   └── Vendel Period → Early, Late
            ├── Viking Age (790–1100 CE)
            │   ├── Early, Middle (Danelaw, Iceland, Normandy), Late
            │   └── Varangians and Kievan Rus'
            ├── Medieval (1050–1520 CE) → Christianization,
            │   Hanseatic, Black Death, Kalmar Union, Stockholm Bloodbath
            ├── Early Modern (1520–1789 CE) → Vasa Era, Reformation,
            │   Stormaktstiden, Frihetstiden, Gustavian Era
            └── Modern → Bernadotte, Industrial, Contemporary
            │
            │ ── EUROPEAN TRACK ──
            ├── Archaic Greece (800–480 BCE)
            ├── Classical Greece (480–323 BCE)
            ├── Hellenistic (323–31 BCE)
            ├── Roman Republic & Empire (509 BCE–476 CE)
            ├── Late Antiquity (250–750 CE)
            ├── Merovingian → Carolingian → Ottonian
            ├── High Middle Ages → Crusades, 12th-C Renaissance
            ├── Late Middle Ages (1300–1500)
            ├── Renaissance → Italian, Northern
            ├── Reformation, Baroque, Enlightenment
            └── Revolutions, Romanticism, World Wars, Cold War, EU
            │
            │ ── SOUTH AMERICAN TRACK ──
            ├── Pre-Columbian South America
            │   ├── Norte Chico/Caral (3000–1800 BCE)
            │   ├── Valdivia (3500–1800 BCE), Chavín (900–200 BCE)
            │   ├── Paracas, Nazca, Moche, Tiwanaku, Wari
            │   ├── Chimú (900–1470), Muisca, San Agustín
            │   ├── Mapuche, Guaraní
            │   └── Inca Empire (1438–1533) → Expansion, Huayna Cápac, Civil War
            ├── Colonial South America (1492–1825)
            │   ├── Spanish Conquest → Viceroyalties (Peru, New Granada, Río de la Plata)
            │   ├── Portuguese Brazil → Sugar, Gold Rush
            │   ├── Jesuit Missions, Potosí Silver
            │   └── Túpac Amaru II Rebellion
            ├── Wars of Independence (1808–1833)
            │   ├── Argentina, Chile, Peru, Bolivia, Uruguay, Paraguay
            │   ├── Gran Colombia (Bolívar), Brazilian Independence
            │   └── Empire of Brazil (1822–1889)
            ├── 19th Century → War of Triple Alliance, War of Pacific, Rubber Boom
            └── 20th–21st Century → Peronism, Vargas, Dirty Wars, Pink Tide
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

## European Historical Periods

| Period | Dates | Key Features |
|--------|-------|-------------|
| **Archaic Greece** | 800–480 BCE | Rise of city-states; colonization; Homer, early philosophy |
| **Classical Greece** | 480–323 BCE | Golden Age of Athens; Parthenon; Socrates, Plato, Aristotle |
| **Hellenistic Period** | 323–31 BCE | Alexander's legacy; spread of Greek culture; Library of Alexandria |
| **Roman Republic** | 509–27 BCE | Mediterranean expansion; Punic Wars; Julius Caesar |
| **Roman Empire** | 27 BCE–476 CE | Pax Romana; roads, law; Christianity becomes state religion |
| **Late Antiquity** | 250–750 CE | Fall of Western Rome; rise of Christianity; Byzantine East |
| **Merovingian Period** | 481–751 CE | Frankish kingdoms; Clovis I converts to Christianity |
| **Carolingian Period** | 751–888 CE | Charlemagne; Carolingian Renaissance; revival of learning |
| **Ottonian Period** | 919–1024 CE | Holy Roman Empire; Ottonian Renaissance |
| **Crusades** | 1095–1291 CE | Religious wars for Holy Land; cultural exchange East-West |
| **12th-Century Renaissance** | 1100–1200 CE | Universities founded; translation movement; Gothic architecture |
| **Late Middle Ages** | 1300–1500 CE | Black Death; Hundred Years' War; printing press (1440) |
| **Renaissance** | 1350–1600 CE | Revival of classical learning; Italian then Northern Renaissance |
| **Age of Exploration** | 1415–1600 CE | Columbus, Vasco da Gama, Magellan; colonial empires |
| **European Reformation** | 1517–1648 CE | Luther; Protestant churches; Wars of Religion; Westphalia |
| **Baroque Period** | 1600–1750 CE | Dramatic art; absolutist monarchies; Bach, Bernini |
| **Enlightenment** | 1685–1815 CE | Reason and science; Voltaire, Kant; influences revolutions |
| **Age of Revolutions** | 1775–1848 CE | American and French Revolutions; Napoleonic Wars; 1848 |
| **Romantic Period** | 1790–1850 CE | Emotion, nature, nationalism; Goethe, Beethoven |
| **World War I** | 1914–1918 CE | The Great War; trench warfare; fall of empires |
| **Interwar Period** | 1918–1939 CE | Great Depression; rise of fascism |
| **World War II** | 1939–1945 CE | Global conflict; Holocaust; Allied victory; UN founded |
| **Cold War** | 1947–1991 CE | East-West division; NATO vs Warsaw Pact; Berlin Wall |
| **European Integration** | 1957–present | EEC to EU; Schengen; Euro; 27+ member states |

## South American Historical Periods

| Period | Dates | Key Features |
|--------|-------|-------------|
| **Norte Chico (Caral)** | 3000–1800 BCE | Oldest American civilization; monumental architecture; no pottery |
| **Valdivia Culture** | 3500–1800 BCE | Ecuador coast; oldest American pottery; Venus figurines |
| **Chavín Culture** | 900–200 BCE | Andean Peru; Chavín de Huántar; jaguar iconography |
| **Paracas Culture** | 800–100 BCE | Extraordinary textiles; cranial trepanation |
| **Nazca Culture** | 100 BCE–800 CE | Nazca Lines geoglyphs; polychrome pottery |
| **Moche Civilization** | 100–700 CE | Sipán royal tombs; portrait vessels; irrigation |
| **Tiwanaku Empire** | 300–1000 CE | Lake Titicaca; Gateway of the Sun; raised fields |
| **Wari Empire** | 600–1000 CE | Road network predating Inca; terraced agriculture |
| **Chimú Empire** | 900–1470 CE | Chan Chan (largest adobe city); conquered by Inca |
| **Muisca Confederation** | 600–1541 CE | Colombian highlands; El Dorado legend; gold and tumbaga |
| **Inca Empire** | 1438–1533 CE | Largest pre-Columbian empire; Machu Picchu; Qhapaq Ñan |
| **Colonial Period** | 1492–1825 CE | Spanish viceroyalties; Portuguese Brazil; Potosí silver |
| **Wars of Independence** | 1808–1833 CE | Bolívar, San Martín; liberation of South America |
| **Empire of Brazil** | 1822–1889 CE | Pedro I and II; coffee economy; abolition 1888 |
| **War of Triple Alliance** | 1864–1870 CE | Paraguay loses ~60-70% of population |
| **War of the Pacific** | 1879–1884 CE | Chile vs. Bolivia and Peru; Atacama nitrates |
| **Rubber Boom** | 1879–1912 CE | Amazon; Manaus; Teatro Amazonas |
| **Dirty Wars** | 1968–1990 CE | Military dictatorships; Operation Condor; desaparecidos |
| **Pink Tide** | 1998–2015 CE | Left-wing wave; Chávez, Lula, Morales, Kirchner |

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

- [Turtle (text/turtle)](/data/geologic-timescale.ttl) — 4,000+ lines, all 361 entries with full hierarchy
- [JSON-LD (application/ld+json)](/data/geologic-timescale.jsonld) — Same data as JSON-LD graph
