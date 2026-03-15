#!/usr/bin/env python3
"""Generate the Geologic Time Scale as Linked Data (Turtle + JSON-LD).

Reads data from YAML files in data/geologic-timescale/ and generates:
  - hugo/static/data/geologic-timescale.ttl  (Turtle RDF)
  - hugo/static/data/geologic-timescale.jsonld  (JSON-LD)

Multi-language data covering:
- 4 Eons
- 10 Eras
- 22 Periods (incl. Mississippian/Pennsylvanian sub-periods)
- 38 Epochs
- ~140 Ages/Stages (all ICS formal stages + geologic events)
- ~630 Archaeological/cultural ages bridging into human history

Each entry has multilingual labels:
  - "en" (English) — primary language
  - Local/etymological language (e.g. "grc" for Ancient Greek, "zh" for Chinese)
  - "sv" (Swedish) — always included

Data files: data/geologic-timescale/*.yaml
Schema:     data/geologic-timescale/_schema.yaml

Source: Wikipedia, "Geologic time scale"
  https://en.wikipedia.org/wiki/Geologic_time_scale
Additional sources:
  https://en.wikipedia.org/wiki/Holocene
  https://en.wikipedia.org/wiki/Pleistocene
  https://en.wikipedia.org/wiki/Three-age_system
  https://en.wikipedia.org/wiki/Scandinavian_prehistory
  https://en.wikipedia.org/wiki/Viking_Age
ICS International Chronostratigraphic Chart v2024/12
  https://stratigraphy.org/ICSchart/ChronostratChart2024-12.pdf

All dates follow the ICS 2024/12 chart where available.
Ma = million years ago; ka = thousand years ago; BP = before present.

Language codes follow ISO 639:
  en=English, sv=Swedish, grc=Ancient Greek, el=Modern Greek,
  cy=Welsh, fr=French, de=German, zh=Chinese, ru=Russian,
  la=Latin, ar=Arabic, es=Spanish, it=Italian, pt=Portuguese,
  nl=Dutch, ja=Japanese, ko=Korean, hi=Hindi, ur=Urdu,
  nb=Norwegian Bokmål, nn=Norwegian Nynorsk, da=Danish,
  fi=Finnish, is=Icelandic, se=Northern Sámi, pl=Polish,
  cs=Czech, hu=Hungarian, tr=Turkish, ka=Georgian, hy=Armenian,
  he=Hebrew, fa=Persian, sa=Sanskrit, nah=Nahuatl, qu=Quechua,
  mi=Māori, haw=Hawaiian, sm=Samoan, to=Tongan
"""

import glob
import json
import os
import sys

import yaml

BASE = "https://metadatahub.eu/data/geologic-timescale"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "data", "geologic-timescale")
OUT_DIR = os.path.join(SCRIPT_DIR, "..", "hugo", "static", "data")

VALID_RANKS = {"Eon", "Era", "Period", "SubPeriod", "Epoch", "Age", "CulturalAge"}
VALID_UNITS = {"Ma", "ka", "BP", "BCE", "CE", "BCE-CE"}
REQUIRED_FIELDS = {"id", "rank", "start", "end", "unit", "labels", "description"}

# ══════════════════════════════════════════════════════════════
# Load YAML data files
# ══════════════════════════════════════════════════════════════

DATA = []
yaml_files = sorted(glob.glob(os.path.join(DATA_DIR, "[0-9]*.yaml")))

if not yaml_files:
    print(f"ERROR: No data files found in {DATA_DIR}", file=sys.stderr)
    sys.exit(1)

for filepath in yaml_files:
    fname = os.path.basename(filepath)
    with open(filepath, encoding="utf-8") as f:
        entries = yaml.safe_load(f)
    if not entries:
        continue
    for entry in entries:
        entry.setdefault("parent", None)
        entry["_source_file"] = fname
        DATA.append(entry)

print(f"Loaded {len(DATA)} entries from {len(yaml_files)} files")

# ══════════════════════════════════════════════════════════════
# Validate
# ══════════════════════════════════════════════════════════════

errors = []
ids = set()

for i, d in enumerate(DATA):
    src = d.get("_source_file", "?")

    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in d:
            errors.append(f"{src}: entry #{i+1} missing required field '{field}'")

    entry_id = d.get("id", f"(entry #{i+1})")

    # Check for duplicate IDs
    if d.get("id") in ids:
        errors.append(f"{src}: duplicate id '{d['id']}'")
    ids.add(d.get("id"))

    # Check rank
    if d.get("rank") not in VALID_RANKS:
        errors.append(f"{src}: {entry_id} has invalid rank '{d.get('rank')}'")

    # Check unit
    if d.get("unit") not in VALID_UNITS:
        errors.append(f"{src}: {entry_id} has invalid unit '{d.get('unit')}'")

    # Check labels
    labels = d.get("labels", {})
    if "en" not in labels:
        errors.append(f"{src}: {entry_id} missing English label ('en')")
    if "sv" not in labels:
        errors.append(f"{src}: {entry_id} missing Swedish label ('sv')")

    # Ensure all label values are strings
    for lang, name in labels.items():
        if not isinstance(name, str):
            d["labels"][lang] = str(name)

# Check parent references (second pass)
for d in DATA:
    if d.get("parent") and d["parent"] not in ids:
        errors.append(f"{d.get('_source_file', '?')}: {d['id']} has unknown parent '{d['parent']}'")

if errors:
    print(f"\n{len(errors)} validation error(s):", file=sys.stderr)
    for e in errors:
        print(f"  - {e}", file=sys.stderr)
    sys.exit(1)

total = len(DATA)
print(f"Total data points: {total}")

# ══════════════════════════════════════════════════════════════
# Generate Turtle
# ══════════════════════════════════════════════════════════════

RANK_TO_CLASS = {
    "Eon": "gts:GeochronologicEon",
    "Era": "gts:GeochronologicEra",
    "Period": "gts:GeochronologicPeriod",
    "SubPeriod": "gts:GeochronologicPeriod",
    "Epoch": "gts:GeochronologicEpoch",
    "Age": "gts:GeochronologicAge",
    "CulturalAge": "gts:GeochronologicAge",
}

def escape(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')

lines = []
lines.append("# ═══════════════════════════════════════════════════════════════")
lines.append("# Geologic Time Scale — Linked Data for metadatahub.eu")
lines.append(f"# {total} data points: eons, eras, periods, epochs, ages,")
lines.append("# and archaeological/cultural periods bridging to human history.")
lines.append("#")
lines.append("# Source: Wikipedia, 'Geologic time scale'")
lines.append("#   https://en.wikipedia.org/wiki/Geologic_time_scale")
lines.append("# Additional sources:")
lines.append("#   https://en.wikipedia.org/wiki/Holocene")
lines.append("#   https://en.wikipedia.org/wiki/Pleistocene")
lines.append("#   https://en.wikipedia.org/wiki/Three-age_system")
lines.append("#   https://en.wikipedia.org/wiki/Scandinavian_prehistory")
lines.append("#   https://en.wikipedia.org/wiki/Viking_Age")
lines.append("# ICS International Chronostratigraphic Chart v2024/12")
lines.append("#   https://stratigraphy.org/ICSchart/ChronostratChart2024-12.pdf")
lines.append("#")
lines.append(f"# Total entries: {total}")
lines.append("# ═══════════════════════════════════════════════════════════════")
lines.append("")
lines.append("@prefix rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .")
lines.append("@prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> .")
lines.append("@prefix owl:     <http://www.w3.org/2002/07/owl#> .")
lines.append("@prefix xsd:     <http://www.w3.org/2001/XMLSchema#> .")
lines.append("@prefix skos:    <http://www.w3.org/2004/02/skos/core#> .")
lines.append("@prefix dcterms: <http://purl.org/dc/terms/> .")
lines.append("@prefix time:    <http://www.w3.org/2006/time#> .")
lines.append("@prefix gts:     <http://resource.geosciml.org/ontology/timescale/gts#> .")
lines.append("@prefix isc:     <http://resource.geosciml.org/classifier/ics/ischart/> .")
lines.append(f"@prefix ts:      <{BASE}/> .")
lines.append("")

# Dataset metadata
lines.append(f"<{BASE}> a skos:ConceptScheme ;")
lines.append(f'    dcterms:title "Geologic Time Scale"@en ;')
lines.append(f'    dcterms:description "{total} entries covering the geologic time scale from Hadean eon (4600 Ma) to present, including Scandinavian, European, and South American cultural/historical periods."@en ;')
lines.append(f'    dcterms:source <https://en.wikipedia.org/wiki/Geologic_time_scale> ;')
lines.append(f'    dcterms:source <https://stratigraphy.org/ICSchart/ChronostratChart2024-12.pdf> ;')
lines.append(f'    dcterms:source <https://en.wikipedia.org/wiki/Holocene> ;')
lines.append(f'    dcterms:source <https://en.wikipedia.org/wiki/Pleistocene> ;')
lines.append(f'    dcterms:source <https://en.wikipedia.org/wiki/Three-age_system> ;')
lines.append(f'    dcterms:source <https://en.wikipedia.org/wiki/Scandinavian_prehistory> ;')
lines.append(f'    dcterms:source <https://en.wikipedia.org/wiki/Viking_Age> ;')
lines.append(f'    dcterms:source <https://en.wikipedia.org/wiki/History_of_Europe> ;')
lines.append(f'    dcterms:source <https://en.wikipedia.org/wiki/Nordic_Bronze_Age> ;')
lines.append(f'    dcterms:source <https://en.wikipedia.org/wiki/Iron_Age_Scandinavia> ;')
lines.append(f'    dcterms:source <https://en.wikipedia.org/wiki/History_of_Sweden> ;')
lines.append(f'    dcterms:creator "Port 30 KB" ;')
lines.append(f'    dcterms:license <https://creativecommons.org/licenses/by-sa/4.0/> ;')
lines.append(f'    dcterms:modified "2024-12-01"^^xsd:date .')
lines.append("")

for idx, d in enumerate(DATA, 1):
    cls = RANK_TO_CLASS.get(d["rank"], "gts:GeochronologicAge")
    en_label = d["labels"].get("en", list(d["labels"].values())[0])
    lines.append(f"# ── {idx}/{total}: {en_label} ({d['rank']}) ──")
    lines.append(f"ts:{d['id']} a {cls} ;")

    # Multilingual labels — English first, then others alphabetically
    label_items = sorted(d["labels"].items(), key=lambda x: (x[0] != "en", x[0]))
    for lang, name in label_items:
        lines.append(f'    rdfs:label "{escape(name)}"@{lang} ;')

    # skos:prefLabel for English
    lines.append(f'    skos:prefLabel "{escape(en_label)}"@en ;')

    lines.append(f'    skos:inScheme <{BASE}> ;')
    lines.append(f'    skos:definition "{escape(d["description"])}"@en ;')
    lines.append(f'    gts:rank "{d["rank"]}" ;')

    if d["parent"]:
        lines.append(f'    skos:broader ts:{d["parent"]} ;')

    # Temporal extent
    unit = d["unit"]
    start = d["start"]
    end = d["end"]

    if unit == "Ma":
        lines.append(f'    time:hasBeginning [ time:inXSDgYear "{start}"^^xsd:decimal ; rdfs:label "{start} Ma" ] ;')
        if end == 0:
            lines.append(f'    time:hasEnd [ rdfs:label "Present" ] ;')
        else:
            lines.append(f'    time:hasEnd [ time:inXSDgYear "{end}"^^xsd:decimal ; rdfs:label "{end} Ma" ] ;')
    elif unit == "BP":
        lines.append(f'    time:hasBeginning [ rdfs:label "{start} years BP" ] ;')
        if end == 0:
            lines.append(f'    time:hasEnd [ rdfs:label "Present" ] ;')
        else:
            lines.append(f'    time:hasEnd [ rdfs:label "{end} years BP" ] ;')
    elif unit == "BCE":
        lines.append(f'    time:hasBeginning [ rdfs:label "{start} BCE" ] ;')
        if end <= 0:
            lines.append(f'    time:hasEnd [ rdfs:label "Present" ] ;')
        else:
            lines.append(f'    time:hasEnd [ rdfs:label "{end} BCE" ] ;')
    elif unit == "BCE-CE":
        lines.append(f'    time:hasBeginning [ rdfs:label "{start} BCE" ] ;')
        if end == 0:
            lines.append(f'    time:hasEnd [ rdfs:label "Present" ] ;')
        else:
            lines.append(f'    time:hasEnd [ rdfs:label "{end} CE" ] ;')
    elif unit == "CE":
        lines.append(f'    time:hasBeginning [ rdfs:label "{start} CE" ] ;')
        if end == 0:
            lines.append(f'    time:hasEnd [ rdfs:label "Present" ] ;')
        else:
            lines.append(f'    time:hasEnd [ rdfs:label "{end} CE" ] ;')

    lines.append(f'    dcterms:source <https://en.wikipedia.org/wiki/Geologic_time_scale> .')
    lines.append("")

with open(os.path.join(OUT_DIR, "geologic-timescale.ttl"), "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

# ══════════════════════════════════════════════════════════════
# Generate JSON-LD
# ══════════════════════════════════════════════════════════════

jsonld_items = []
for d in DATA:
    cls = RANK_TO_CLASS.get(d["rank"], "gts:GeochronologicAge")
    unit = d["unit"]
    en_label = d["labels"].get("en", list(d["labels"].values())[0])
    # Build multilingual label array
    label_list = [{"@value": name, "@language": lang}
                  for lang, name in sorted(d["labels"].items(), key=lambda x: (x[0] != "en", x[0]))]
    item = {
        "@id": f"{BASE}/{d['id']}",
        "@type": cls,
        "rdfs:label": label_list if len(label_list) > 1 else label_list[0],
        "skos:prefLabel": {"@value": en_label, "@language": "en"},
        "skos:definition": {"@value": d["description"], "@language": "en"},
        "gts:rank": d["rank"],
    }
    if d["parent"]:
        item["skos:broader"] = {"@id": f"{BASE}/{d['parent']}"}

    if unit == "Ma":
        item["time:hasBeginning"] = f"{d['start']} Ma"
        item["time:hasEnd"] = "Present" if d["end"] == 0 else f"{d['end']} Ma"
    elif unit == "BP":
        item["time:hasBeginning"] = f"{d['start']} years BP"
        item["time:hasEnd"] = "Present" if d["end"] == 0 else f"{d['end']} years BP"
    elif unit == "BCE":
        item["time:hasBeginning"] = f"{d['start']} BCE"
        item["time:hasEnd"] = "Present" if d["end"] <= 0 else f"{d['end']} BCE"
    elif unit == "BCE-CE":
        item["time:hasBeginning"] = f"{d['start']} BCE"
        item["time:hasEnd"] = "Present" if d["end"] == 0 else f"{d['end']} CE"
    elif unit == "CE":
        item["time:hasBeginning"] = f"{d['start']} CE"
        item["time:hasEnd"] = "Present" if d["end"] == 0 else f"{d['end']} CE"

    item["dcterms:source"] = "https://en.wikipedia.org/wiki/Geologic_time_scale"
    jsonld_items.append(item)

jsonld_doc = {
    "@context": {
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "dcterms": "http://purl.org/dc/terms/",
        "time": "http://www.w3.org/2006/time#",
        "gts": "http://resource.geosciml.org/ontology/timescale/gts#",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
    },
    "@id": BASE,
    "@type": "skos:ConceptScheme",
    "dcterms:title": "Geologic Time Scale",
    "dcterms:description": f"{total} entries covering the geologic time scale from Hadean eon (4600 Ma) to present, including Scandinavian, European, and South American cultural/historical periods.",
    "dcterms:source": [
        "https://en.wikipedia.org/wiki/Geologic_time_scale",
        "https://stratigraphy.org/ICSchart/ChronostratChart2024-12.pdf",
        "https://en.wikipedia.org/wiki/Holocene",
        "https://en.wikipedia.org/wiki/Pleistocene",
        "https://en.wikipedia.org/wiki/Three-age_system",
        "https://en.wikipedia.org/wiki/Scandinavian_prehistory",
        "https://en.wikipedia.org/wiki/Viking_Age",
    ],
    "dcterms:license": "https://creativecommons.org/licenses/by-sa/4.0/",
    "@graph": jsonld_items,
}

with open(os.path.join(OUT_DIR, "geologic-timescale.jsonld"), "w", encoding="utf-8") as f:
    json.dump(jsonld_doc, f, indent=2, ensure_ascii=False)

print(f"  Turtle: hugo/static/data/geologic-timescale.ttl ({len(lines)} lines)")
print(f"  JSON-LD: hugo/static/data/geologic-timescale.jsonld ({len(jsonld_items)} items)")
