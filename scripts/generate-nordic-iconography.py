#!/usr/bin/env python3
"""Generate the Nordic Iconography and Subject Classification as Linked Data.

Reads data from YAML files in data/nordic-iconography/ and generates:
  - hugo/static/data/nordic-iconography.ttl  (Turtle RDF)
  - hugo/static/data/nordic-iconography.jsonld  (JSON-LD)

Covers ~180 entries across 7 thematic files:
  01 - Norse mythology (gods, beings, places, events)
  02 - Kalevala / Finnish mythology
  03 - Sámi cultural and mythological subjects
  04 - Christian iconography in Nordic context
  05 - Nordic folk art motifs and traditions
  06 - Seasonal and cultural subjects
  07 - Nature and landscape subjects

Each entry has multilingual labels:
  - "en" (English) — required
  - "sv" (Swedish) — required
  - Additional Nordic languages: da, nb, fi, is, non, se

External vocabulary mappings:
  - aat_uri  → skos:closeMatch (Getty Art & Architecture Thesaurus)
  - iconclass → skos:relatedMatch (Iconclass)

Data files: data/nordic-iconography/*.yaml
Schema:     data/nordic-iconography/_schema.yaml

Sources:
  https://en.wikipedia.org/wiki/Norse_mythology
  https://en.wikipedia.org/wiki/Kalevala
  https://en.wikipedia.org/wiki/S%C3%A1mi_mythology
  https://www.iconclass.org/
  https://www.getty.edu/research/tools/vocabularies/aat/
"""

import glob
import json
import os
import sys
from collections import Counter

import yaml

BASE = "https://metadatahub.eu/data/nordic-iconography"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "data", "nordic-iconography")
OUT_DIR = os.path.join(SCRIPT_DIR, "..", "hugo", "static", "data")

REQUIRED_FIELDS = {"id", "labels", "description"}

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
        entry.setdefault("broader", None)
        entry.setdefault("aat_uri", None)
        entry.setdefault("iconclass", None)
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

# Check broader references (second pass)
for d in DATA:
    if d.get("broader") and d["broader"] not in ids:
        errors.append(
            f"{d.get('_source_file', '?')}: {d['id']} has unknown broader '{d['broader']}'"
        )

if errors:
    print(f"\n{len(errors)} validation error(s):", file=sys.stderr)
    for e in errors:
        print(f"  - {e}", file=sys.stderr)
    sys.exit(1)

total = len(DATA)
print(f"Validated {total} entries — no errors")

# Count by source file for statistics
file_counts = Counter(d["_source_file"] for d in DATA)
for fname, count in sorted(file_counts.items()):
    print(f"  {fname}: {count} entries")

# ══════════════════════════════════════════════════════════════
# Generate Turtle
# ══════════════════════════════════════════════════════════════


def escape(s):
    """Escape a string for Turtle literal."""
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")


lines = []
lines.append("# ═══════════════════════════════════════════════════════════════")
lines.append("# Nordic Iconography and Subject Classification — Linked Data")
lines.append(f"# {total} entries covering Norse mythology, Kalevala, Sámi culture,")
lines.append("# Christian Nordic iconography, folk art, seasonal traditions,")
lines.append("# and Nordic nature/landscape subjects.")
lines.append("#")
lines.append("# Generated for metadatahub.eu")
lines.append("#")
lines.append("# Sources:")
lines.append("#   https://en.wikipedia.org/wiki/Norse_mythology")
lines.append("#   https://en.wikipedia.org/wiki/Kalevala")
lines.append("#   https://en.wikipedia.org/wiki/S%C3%A1mi_mythology")
lines.append("#   https://www.iconclass.org/")
lines.append("#   https://www.getty.edu/research/tools/vocabularies/aat/")
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
lines.append("@prefix aat:     <http://vocab.getty.edu/aat/> .")
lines.append("@prefix ic:      <http://iconclass.org/> .")
lines.append(f"@prefix ni:      <{BASE}/> .")
lines.append("")

# Dataset metadata
lines.append(f"<{BASE}> a skos:ConceptScheme ;")
lines.append(f'    dcterms:title "Nordic Iconography and Subject Classification"@en ;')
lines.append(
    f'    dcterms:title "Nordisk ikonografi och ämnesklassifikation"@sv ;'
)
lines.append(
    f'    dcterms:description "{total} entries covering Nordic iconographic subjects '
    f"from Norse mythology, Finnish Kalevala, Sámi culture, Christian Nordic art, "
    f'folk art traditions, seasonal celebrations, and landscape subjects."@en ;'
)
lines.append(
    f"    dcterms:source <https://en.wikipedia.org/wiki/Norse_mythology> ;"
)
lines.append(f"    dcterms:source <https://en.wikipedia.org/wiki/Kalevala> ;")
lines.append(
    f"    dcterms:source <https://en.wikipedia.org/wiki/S%C3%A1mi_mythology> ;"
)
lines.append(f"    dcterms:source <https://www.iconclass.org/> ;")
lines.append(
    f"    dcterms:source <https://www.getty.edu/research/tools/vocabularies/aat/> ;"
)
lines.append(f'    dcterms:creator "Port 30 KB" ;')
lines.append(
    f"    dcterms:license <https://creativecommons.org/licenses/by-sa/4.0/> ;"
)
lines.append(f'    dcterms:modified "2025-01-15"^^xsd:date .')
lines.append("")

for idx, d in enumerate(DATA, 1):
    en_label = d["labels"].get("en", list(d["labels"].values())[0])
    lines.append(f"# ── {idx}/{total}: {en_label} ──")
    lines.append(f"ni:{d['id']} a skos:Concept ;")

    # Multilingual labels — English first, then others alphabetically
    label_items = sorted(
        d["labels"].items(), key=lambda x: (x[0] != "en", x[0])
    )
    for lang, name in label_items:
        lines.append(f'    rdfs:label "{escape(name)}"@{lang} ;')

    # skos:prefLabel for all languages
    for lang, name in label_items:
        lines.append(f'    skos:prefLabel "{escape(name)}"@{lang} ;')

    lines.append(f"    skos:inScheme <{BASE}> ;")
    lines.append(f'    skos:definition "{escape(d["description"])}"@en ;')

    # Broader concept
    if d["broader"]:
        lines.append(f"    skos:broader ni:{d['broader']} ;")

    # External mappings
    if d["aat_uri"]:
        lines.append(f"    skos:closeMatch <{d['aat_uri']}> ;")

    if d["iconclass"]:
        lines.append(
            f'    skos:relatedMatch <http://iconclass.org/{d["iconclass"]}> ;'
        )

    # Close the entry — replace last ; with .
    if lines[-1].endswith(" ;"):
        lines[-1] = lines[-1][:-2] + " ."
    lines.append("")

os.makedirs(OUT_DIR, exist_ok=True)
ttl_path = os.path.join(OUT_DIR, "nordic-iconography.ttl")
with open(ttl_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

# ══════════════════════════════════════════════════════════════
# Generate JSON-LD
# ══════════════════════════════════════════════════════════════

jsonld_items = []
for d in DATA:
    en_label = d["labels"].get("en", list(d["labels"].values())[0])
    label_items = sorted(
        d["labels"].items(), key=lambda x: (x[0] != "en", x[0])
    )
    label_list = [
        {"@value": name, "@language": lang} for lang, name in label_items
    ]

    item = {
        "@id": f"{BASE}/{d['id']}",
        "@type": "skos:Concept",
        "rdfs:label": label_list if len(label_list) > 1 else label_list[0],
        "skos:prefLabel": label_list if len(label_list) > 1 else label_list[0],
        "skos:definition": {"@value": d["description"], "@language": "en"},
    }

    if d["broader"]:
        item["skos:broader"] = {"@id": f"{BASE}/{d['broader']}"}

    if d["aat_uri"]:
        item["skos:closeMatch"] = {"@id": d["aat_uri"]}

    if d["iconclass"]:
        item["skos:relatedMatch"] = {
            "@id": f"http://iconclass.org/{d['iconclass']}"
        }

    jsonld_items.append(item)

jsonld_doc = {
    "@context": {
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "dcterms": "http://purl.org/dc/terms/",
        "aat": "http://vocab.getty.edu/aat/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
    },
    "@id": BASE,
    "@type": "skos:ConceptScheme",
    "dcterms:title": [
        {
            "@value": "Nordic Iconography and Subject Classification",
            "@language": "en",
        },
        {
            "@value": "Nordisk ikonografi och ämnesklassifikation",
            "@language": "sv",
        },
    ],
    "dcterms:description": (
        f"{total} entries covering Nordic iconographic subjects "
        f"from Norse mythology, Finnish Kalevala, Sámi culture, Christian Nordic art, "
        f"folk art traditions, seasonal celebrations, and landscape subjects."
    ),
    "dcterms:source": [
        "https://en.wikipedia.org/wiki/Norse_mythology",
        "https://en.wikipedia.org/wiki/Kalevala",
        "https://en.wikipedia.org/wiki/S%C3%A1mi_mythology",
        "https://www.iconclass.org/",
        "https://www.getty.edu/research/tools/vocabularies/aat/",
    ],
    "dcterms:license": "https://creativecommons.org/licenses/by-sa/4.0/",
    "@graph": jsonld_items,
}

jsonld_path = os.path.join(OUT_DIR, "nordic-iconography.jsonld")
with open(jsonld_path, "w", encoding="utf-8") as f:
    json.dump(jsonld_doc, f, indent=2, ensure_ascii=False)

print(f"\nOutput files:")
print(f"  Turtle:  hugo/static/data/nordic-iconography.ttl ({len(lines)} lines)")
print(
    f"  JSON-LD: hugo/static/data/nordic-iconography.jsonld ({len(jsonld_items)} items)"
)
