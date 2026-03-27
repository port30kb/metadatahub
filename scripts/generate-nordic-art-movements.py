#!/usr/bin/env python3
"""Generate the Nordic Art and Design Movements Thesaurus as Linked Data (Turtle + JSON-LD).

Reads data from YAML file in data/nordic-art-movements/ and generates:
  - hugo/static/data/nordic-art-movements.ttl   (Turtle RDF)
  - hugo/static/data/nordic-art-movements.jsonld (JSON-LD)

~95 entries covering Nordic art, architecture, and design movements
from the Renaissance through contemporary movements, organized as a
SKOS vocabulary with multilingual labels (en, sv, da, nb, fi).

Each entry has:
  - Multilingual labels (en + sv minimum, typically 5 languages)
  - Temporal extents (start/end years)
  - SKOS broader/narrower hierarchy
  - Optional Getty AAT mappings via skos:closeMatch

Data file:  data/nordic-art-movements/movements.yaml
Schema:     data/nordic-art-movements/_schema.yaml

Sources:
  https://en.wikipedia.org/wiki/Scandinavian_design
  https://en.wikipedia.org/wiki/Nordic_art
  https://en.wikipedia.org/wiki/Danish_Golden_Age
  https://en.wikipedia.org/wiki/National_Romanticism
  https://en.wikipedia.org/wiki/Skagen_Painters
  https://en.wikipedia.org/wiki/Functionalism_(architecture)
"""

import json
import os
import sys

import yaml

BASE = "https://metadatahub.eu/data/nordic-art-movements"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "data", "nordic-art-movements")
OUT_DIR = os.path.join(SCRIPT_DIR, "..", "hugo", "static", "data")

REQUIRED_FIELDS = {"id", "start", "end", "labels", "description"}

# ══════════════════════════════════════════════════════════════
# Load YAML data
# ══════════════════════════════════════════════════════════════

data_file = os.path.join(DATA_DIR, "movements.yaml")

if not os.path.exists(data_file):
    print(f"ERROR: Data file not found: {data_file}", file=sys.stderr)
    sys.exit(1)

with open(data_file, encoding="utf-8") as f:
    DATA = yaml.safe_load(f)

if not DATA:
    print("ERROR: No entries found in movements.yaml", file=sys.stderr)
    sys.exit(1)

print(f"Loaded {len(DATA)} entries from movements.yaml")

# ══════════════════════════════════════════════════════════════
# Validate
# ══════════════════════════════════════════════════════════════

errors = []
ids = set()

for i, d in enumerate(DATA):
    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in d:
            errors.append(f"entry #{i+1} missing required field '{field}'")

    entry_id = d.get("id", f"(entry #{i+1})")

    # Check for duplicate IDs
    if d.get("id") in ids:
        errors.append(f"duplicate id '{d['id']}'")
    ids.add(d.get("id"))

    # Check labels
    labels = d.get("labels", {})
    if "en" not in labels:
        errors.append(f"{entry_id} missing English label ('en')")
    if "sv" not in labels:
        errors.append(f"{entry_id} missing Swedish label ('sv')")

    # Ensure all label values are strings
    for lang, name in labels.items():
        if not isinstance(name, str):
            d["labels"][lang] = str(name)

    # Ensure start/end are strings
    if "start" in d and not isinstance(d["start"], str):
        d["start"] = str(d["start"])
    if "end" in d and not isinstance(d["end"], str):
        d["end"] = str(d["end"])

# Check broader references (second pass)
for d in DATA:
    if d.get("broader") and d["broader"] not in ids:
        errors.append(f"{d['id']} has unknown broader '{d['broader']}'")

if errors:
    print(f"\n{len(errors)} validation error(s):", file=sys.stderr)
    for e in errors:
        print(f"  - {e}", file=sys.stderr)
    sys.exit(1)

total = len(DATA)
print(f"Total entries: {total}")

# ══════════════════════════════════════════════════════════════
# Generate Turtle
# ══════════════════════════════════════════════════════════════

def escape(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')

lines = []
lines.append("# ═══════════════════════════════════════════════════════════════")
lines.append("# Nordic Art and Design Movements Thesaurus")
lines.append("# Linked Data for metadatahub.eu")
lines.append(f"# {total} entries: art, architecture, and design movements")
lines.append("# from the Nordic countries (Denmark, Finland, Iceland, Norway, Sweden).")
lines.append("#")
lines.append("# Sources:")
lines.append("#   https://en.wikipedia.org/wiki/Scandinavian_design")
lines.append("#   https://en.wikipedia.org/wiki/Nordic_art")
lines.append("#   https://en.wikipedia.org/wiki/Danish_Golden_Age")
lines.append("#   https://en.wikipedia.org/wiki/National_Romanticism")
lines.append("#   https://en.wikipedia.org/wiki/Skagen_Painters")
lines.append("#   https://en.wikipedia.org/wiki/Functionalism_(architecture)")
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
lines.append(f"@prefix nam:     <{BASE}/> .")
lines.append("")

# Dataset metadata
lines.append(f"<{BASE}> a skos:ConceptScheme ;")
lines.append(f'    dcterms:title "Nordic Art and Design Movements Thesaurus"@en ;')
lines.append(f'    dcterms:title "Tesaurus för nordisk konst och design"@sv ;')
lines.append(f'    dcterms:description "{total} entries covering Nordic art, architecture, and design movements from the Renaissance to contemporary, with multilingual labels in five Nordic languages."@en ;')
lines.append(f'    dcterms:source <https://en.wikipedia.org/wiki/Scandinavian_design> ;')
lines.append(f'    dcterms:source <https://en.wikipedia.org/wiki/Nordic_art> ;')
lines.append(f'    dcterms:source <https://en.wikipedia.org/wiki/Danish_Golden_Age> ;')
lines.append(f'    dcterms:source <https://en.wikipedia.org/wiki/National_Romanticism> ;')
lines.append(f'    dcterms:source <https://en.wikipedia.org/wiki/Skagen_Painters> ;')
lines.append(f'    dcterms:source <https://en.wikipedia.org/wiki/Functionalism_(architecture)> ;')
lines.append(f'    dcterms:creator "Port 30 KB" ;')
lines.append(f'    dcterms:license <https://creativecommons.org/licenses/by-sa/4.0/> ;')
lines.append(f'    dcterms:modified "2025-03-15"^^xsd:date .')
lines.append("")

for idx, d in enumerate(DATA, 1):
    en_label = d["labels"].get("en", list(d["labels"].values())[0])
    lines.append(f"# ── {idx}/{total}: {en_label} ──")
    lines.append(f"nam:{d['id']} a skos:Concept ;")

    # Multilingual labels — English first, then others alphabetically
    label_items = sorted(d["labels"].items(), key=lambda x: (x[0] != "en", x[0]))
    for lang, name in label_items:
        lines.append(f'    rdfs:label "{escape(name)}"@{lang} ;')

    # skos:prefLabel for each language
    for lang, name in label_items:
        lines.append(f'    skos:prefLabel "{escape(name)}"@{lang} ;')

    lines.append(f'    skos:inScheme <{BASE}> ;')
    lines.append(f'    skos:definition "{escape(d["description"])}"@en ;')

    if d.get("broader"):
        lines.append(f'    skos:broader nam:{d["broader"]} ;')

    # AAT close match
    if d.get("aat_uri"):
        lines.append(f'    skos:closeMatch <{d["aat_uri"]}> ;')

    # Temporal extent using W3C Time Ontology
    start = d["start"]
    end = d["end"]
    lines.append(f'    time:hasBeginning [ time:inXSDgYear "{start}"^^xsd:gYear ] ;')
    lines.append(f'    time:hasEnd [ time:inXSDgYear "{end}"^^xsd:gYear ] ;')

    # Timeline integers
    if d.get("timeline_start") is not None:
        lines.append(f'    <{BASE}/ontology/timelineStart> "{d["timeline_start"]}"^^xsd:long ;')
    if d.get("timeline_end") is not None:
        lines.append(f'    <{BASE}/ontology/timelineEnd> "{d["timeline_end"]}"^^xsd:long ;')

    lines.append(f'    dcterms:source <https://en.wikipedia.org/wiki/Nordic_art> .')
    lines.append("")

os.makedirs(OUT_DIR, exist_ok=True)

ttl_path = os.path.join(OUT_DIR, "nordic-art-movements.ttl")
with open(ttl_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

# ══════════════════════════════════════════════════════════════
# Generate JSON-LD
# ══════════════════════════════════════════════════════════════

jsonld_items = []
for d in DATA:
    en_label = d["labels"].get("en", list(d["labels"].values())[0])

    # Build multilingual label array
    label_items = sorted(d["labels"].items(), key=lambda x: (x[0] != "en", x[0]))
    label_list = [{"@value": name, "@language": lang} for lang, name in label_items]

    item = {
        "@id": f"{BASE}/{d['id']}",
        "@type": "skos:Concept",
        "rdfs:label": label_list if len(label_list) > 1 else label_list[0],
        "skos:prefLabel": label_list if len(label_list) > 1 else label_list[0],
        "skos:definition": {"@value": d["description"], "@language": "en"},
        "skos:inScheme": {"@id": BASE},
    }

    if d.get("broader"):
        item["skos:broader"] = {"@id": f"{BASE}/{d['broader']}"}

    if d.get("aat_uri"):
        item["skos:closeMatch"] = {"@id": d["aat_uri"]}

    item["time:hasBeginning"] = {"time:inXSDgYear": d["start"]}
    item["time:hasEnd"] = {"time:inXSDgYear": d["end"]}

    if d.get("timeline_start") is not None:
        item["mhub:timelineStart"] = d["timeline_start"]
    if d.get("timeline_end") is not None:
        item["mhub:timelineEnd"] = d["timeline_end"]

    item["dcterms:source"] = "https://en.wikipedia.org/wiki/Nordic_art"
    jsonld_items.append(item)

jsonld_doc = {
    "@context": {
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "owl": "http://www.w3.org/2002/07/owl#",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "dcterms": "http://purl.org/dc/terms/",
        "time": "http://www.w3.org/2006/time#",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "mhub": f"{BASE}/ontology/",
    },
    "@id": BASE,
    "@type": "skos:ConceptScheme",
    "dcterms:title": [
        {"@value": "Nordic Art and Design Movements Thesaurus", "@language": "en"},
        {"@value": "Tesaurus för nordisk konst och design", "@language": "sv"},
    ],
    "dcterms:description": f"{total} entries covering Nordic art, architecture, and design movements from the Renaissance to contemporary, with multilingual labels in five Nordic languages.",
    "dcterms:source": [
        "https://en.wikipedia.org/wiki/Scandinavian_design",
        "https://en.wikipedia.org/wiki/Nordic_art",
        "https://en.wikipedia.org/wiki/Danish_Golden_Age",
        "https://en.wikipedia.org/wiki/National_Romanticism",
        "https://en.wikipedia.org/wiki/Skagen_Painters",
        "https://en.wikipedia.org/wiki/Functionalism_(architecture)",
    ],
    "dcterms:license": "https://creativecommons.org/licenses/by-sa/4.0/",
    "dcterms:modified": "2025-03-15",
    "@graph": jsonld_items,
}

jsonld_path = os.path.join(OUT_DIR, "nordic-art-movements.jsonld")
with open(jsonld_path, "w", encoding="utf-8") as f:
    json.dump(jsonld_doc, f, indent=2, ensure_ascii=False)

print(f"  Turtle:  hugo/static/data/nordic-art-movements.ttl ({len(lines)} lines)")
print(f"  JSON-LD: hugo/static/data/nordic-art-movements.jsonld ({len(jsonld_items)} items)")
