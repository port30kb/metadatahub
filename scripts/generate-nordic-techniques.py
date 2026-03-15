#!/usr/bin/env python3
"""Generate the Nordic Techniques Vocabulary as Linked Data (Turtle + JSON-LD).

Reads data from data/nordic-techniques/techniques.yaml and generates:
  - hugo/static/data/nordic-techniques.ttl   (Turtle RDF)
  - hugo/static/data/nordic-techniques.jsonld (JSON-LD)

A SKOS-style hierarchical vocabulary of ~170 technique entries used in
Nordic museum cataloguing, covering:
- Metalworking (forging, casting, filigree, niello, enameling, ...)
- Textile techniques (weaving, nalbinding, rya-knotting, ...)
- Woodworking (carving, stave construction, clinker building, ...)
- Ceramics (throwing, glazing, firing, ...)
- Stone and lapidary (rune carving, flint knapping, ...)
- Painting and surface decoration (rosemaling, kurbits, ...)
- Printmaking (woodcut, etching, lithography, ...)
- Glass (glassblowing, stained glass, bead making, ...)
- Leather and fibre (tanning, bookbinding, basket weaving, ...)
- Sami/Nordic-specific (duodji, tin-thread embroidery, ...)

Each entry has multilingual labels (en, sv, da, nb, fi minimum)
and optional Getty AAT URI mappings.

Data file:  data/nordic-techniques/techniques.yaml
Schema:     data/nordic-techniques/_schema.yaml

Sources:
  Getty Art & Architecture Thesaurus (AAT)
    http://www.getty.edu/research/tools/vocabularies/aat/
  Wikipedia (various technique articles)
  Nordic museum cataloguing traditions
"""

import json
import os
import sys

import yaml

BASE = "https://metadatahub.eu/data/nordic-techniques"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "data", "nordic-techniques")
OUT_DIR = os.path.join(SCRIPT_DIR, "..", "hugo", "static", "data")

REQUIRED_FIELDS = {"id", "labels", "description"}

# ══════════════════════════════════════════════════════════════
# Load YAML data file
# ══════════════════════════════════════════════════════════════

data_file = os.path.join(DATA_DIR, "techniques.yaml")

if not os.path.exists(data_file):
    print(f"ERROR: Data file not found: {data_file}", file=sys.stderr)
    sys.exit(1)

with open(data_file, encoding="utf-8") as f:
    DATA = yaml.safe_load(f)

if not DATA:
    print("ERROR: No entries found in techniques.yaml", file=sys.stderr)
    sys.exit(1)

print(f"Loaded {len(DATA)} entries from techniques.yaml")

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

# Check broader references (second pass)
for d in DATA:
    if d.get("broader") and d["broader"] not in ids:
        errors.append(f"{d['id']} has unknown broader reference '{d['broader']}'")

if errors:
    print(f"\n{len(errors)} validation error(s):", file=sys.stderr)
    for e in errors:
        print(f"  - {e}", file=sys.stderr)
    sys.exit(1)

total = len(DATA)
print(f"Validated {total} entries (0 errors)")

# Count categories
top_level = [d for d in DATA if not d.get("broader")]
with_aat = [d for d in DATA if d.get("aat_uri")]
print(f"  Top-level categories: {len(top_level)}")
print(f"  Entries with AAT URIs: {len(with_aat)}")

# ══════════════════════════════════════════════════════════════
# Generate Turtle
# ══════════════════════════════════════════════════════════════


def escape(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


lines = []
lines.append("# ═══════════════════════════════════════════════════════════════")
lines.append("# Nordic Techniques Vocabulary — Linked Data for metadatahub.eu")
lines.append(f"# {total} entries: techniques used in Nordic museum cataloguing.")
lines.append("#")
lines.append("# Categories: metalworking, textiles, woodworking, ceramics,")
lines.append("# stone/lapidary, painting, printmaking, glass, leather/fibre,")
lines.append("# and Sami/Nordic-specific crafts.")
lines.append("#")
lines.append("# Sources:")
lines.append("#   Getty Art & Architecture Thesaurus (AAT)")
lines.append("#     http://www.getty.edu/research/tools/vocabularies/aat/")
lines.append("#   Wikipedia (various technique articles)")
lines.append("#   Nordic museum cataloguing traditions")
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
lines.append(f"@prefix nt:      <{BASE}/> .")
lines.append("")

# Dataset metadata
lines.append(f"<{BASE}> a skos:ConceptScheme ;")
lines.append(f'    dcterms:title "Nordic Techniques Vocabulary"@en ;')
lines.append(
    f'    dcterms:title "Nordisk teknikvokabulär"@sv ;'
)
lines.append(
    f'    dcterms:description "{total} entries covering techniques used in Nordic museum cataloguing — metalworking, textiles, woodworking, ceramics, stone, painting, printmaking, glass, leather, and Sami/Nordic-specific crafts."@en ;'
)
lines.append(
    f"    dcterms:source <http://www.getty.edu/research/tools/vocabularies/aat/> ;"
)
lines.append(f'    dcterms:creator "Port 30 KB" ;')
lines.append(
    f"    dcterms:license <https://creativecommons.org/licenses/by-sa/4.0/> ;"
)
lines.append(f'    dcterms:modified "2025-03-15"^^xsd:date .')
lines.append("")

for idx, d in enumerate(DATA, 1):
    en_label = d["labels"].get("en", list(d["labels"].values())[0])
    lines.append(f"# ── {idx}/{total}: {en_label} ──")
    lines.append(f"nt:{d['id']} a skos:Concept ;")

    # Multilingual labels — English first, then others alphabetically
    label_items = sorted(
        d["labels"].items(), key=lambda x: (x[0] != "en", x[0])
    )
    for lang, name in label_items:
        lines.append(f'    rdfs:label "{escape(name)}"@{lang} ;')
        lines.append(f'    skos:prefLabel "{escape(name)}"@{lang} ;')

    lines.append(f"    skos:inScheme <{BASE}> ;")
    lines.append(f'    skos:definition "{escape(d["description"])}"@en ;')

    if d.get("broader"):
        lines.append(f"    skos:broader nt:{d['broader']} ;")

    if d.get("aat_uri"):
        lines.append(f"    skos:exactMatch <{d['aat_uri']}> ;")

    lines.append(f"    dcterms:source <http://www.getty.edu/research/tools/vocabularies/aat/> .")
    lines.append("")

os.makedirs(OUT_DIR, exist_ok=True)
ttl_path = os.path.join(OUT_DIR, "nordic-techniques.ttl")
with open(ttl_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

# ══════════════════════════════════════════════════════════════
# Generate JSON-LD
# ══════════════════════════════════════════════════════════════

jsonld_items = []
for d in DATA:
    en_label = d["labels"].get("en", list(d["labels"].values())[0])

    # Build multilingual label array
    label_list = [
        {"@value": name, "@language": lang}
        for lang, name in sorted(
            d["labels"].items(), key=lambda x: (x[0] != "en", x[0])
        )
    ]

    item = {
        "@id": f"{BASE}/{d['id']}",
        "@type": "skos:Concept",
        "rdfs:label": label_list if len(label_list) > 1 else label_list[0],
        "skos:prefLabel": label_list if len(label_list) > 1 else label_list[0],
        "skos:definition": {"@value": d["description"], "@language": "en"},
    }

    if d.get("broader"):
        item["skos:broader"] = {"@id": f"{BASE}/{d['broader']}"}

    if d.get("aat_uri"):
        item["skos:exactMatch"] = {"@id": d["aat_uri"]}

    item["dcterms:source"] = (
        "http://www.getty.edu/research/tools/vocabularies/aat/"
    )
    jsonld_items.append(item)

jsonld_doc = {
    "@context": {
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "owl": "http://www.w3.org/2002/07/owl#",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "dcterms": "http://purl.org/dc/terms/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
    },
    "@id": BASE,
    "@type": "skos:ConceptScheme",
    "dcterms:title": [
        {"@value": "Nordic Techniques Vocabulary", "@language": "en"},
        {"@value": "Nordisk teknikvokabulär", "@language": "sv"},
    ],
    "dcterms:description": f"{total} entries covering techniques used in Nordic museum cataloguing — metalworking, textiles, woodworking, ceramics, stone, painting, printmaking, glass, leather, and Sami/Nordic-specific crafts.",
    "dcterms:source": [
        "http://www.getty.edu/research/tools/vocabularies/aat/",
    ],
    "dcterms:license": "https://creativecommons.org/licenses/by-sa/4.0/",
    "@graph": jsonld_items,
}

jsonld_path = os.path.join(OUT_DIR, "nordic-techniques.jsonld")
with open(jsonld_path, "w", encoding="utf-8") as f:
    json.dump(jsonld_doc, f, indent=2, ensure_ascii=False)

print(f"  Turtle:  hugo/static/data/nordic-techniques.ttl ({len(lines)} lines)")
print(f"  JSON-LD: hugo/static/data/nordic-techniques.jsonld ({len(jsonld_items)} items)")
