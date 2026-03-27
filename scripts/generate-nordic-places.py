#!/usr/bin/env python3
"""Generate the Nordic Place Name Authority as Linked Data (Turtle + JSON-LD).

Reads data from YAML files in data/nordic-places/ and generates:
  - hugo/static/data/nordic-places.ttl  (Turtle RDF)
  - hugo/static/data/nordic-places.jsonld  (JSON-LD)

Multi-language place name authority covering:
- 5 Nordic countries (Sweden, Norway, Finland, Denmark, Iceland)
- Swedish landskap (25 historical provinces)
- Norwegian historical regions
- Finnish historical provinces
- Danish regions and islands
- Icelandic regions
- Sápmi (Sámi homeland) regions
- Major cities with coordinates
- Important archaeological sites
- Historical name variants

Each entry has multilingual labels:
  - "en" (English) — always included
  - Local language (sv, nb, nn, fi, da, is, se, fo, kl)

Data files: data/nordic-places/*.yaml
Schema:     data/nordic-places/_schema.yaml

Sources:
  https://en.wikipedia.org/wiki/Nordic_countries
  https://www.geonames.org/
  https://www.wikidata.org/
"""

import glob
import json
import os
import sys

import yaml

BASE = "https://metadatahub.eu/data/nordic-places"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "data", "nordic-places")
OUT_DIR = os.path.join(SCRIPT_DIR, "..", "hugo", "static", "data")

VALID_TYPES = {
    "country", "region", "landskap", "municipality", "city",
    "town", "village", "island", "archaeological-site", "parish",
}
REQUIRED_FIELDS = {"id", "type", "labels", "description"}

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

    # Check type
    if d.get("type") not in VALID_TYPES:
        errors.append(f"{src}: {entry_id} has invalid type '{d.get('type')}'")

    # Check labels
    labels = d.get("labels", {})
    if "en" not in labels:
        errors.append(f"{src}: {entry_id} missing English label ('en')")

    # Ensure all label values are strings
    for lang, name in labels.items():
        if not isinstance(name, str):
            d["labels"][lang] = str(name)

# Check broader references (second pass)
for d in DATA:
    if d.get("broader") and d["broader"] not in ids:
        errors.append(f"{d.get('_source_file', '?')}: {d['id']} has unknown broader '{d['broader']}'")

if errors:
    print(f"\n{len(errors)} validation error(s):", file=sys.stderr)
    for e in errors:
        print(f"  - {e}", file=sys.stderr)
    sys.exit(1)

total = len(DATA)
print(f"Total data points: {total}")

# Count by type and country
type_counts = {}
for d in DATA:
    t = d["type"]
    type_counts[t] = type_counts.get(t, 0) + 1

for t, c in sorted(type_counts.items()):
    print(f"  {t}: {c}")

# ══════════════════════════════════════════════════════════════
# Generate Turtle
# ══════════════════════════════════════════════════════════════

TYPE_TO_CLASS = {
    "country": "schema:Country",
    "region": "schema:AdministrativeArea",
    "landskap": "schema:AdministrativeArea",
    "municipality": "schema:AdministrativeArea",
    "city": "schema:City",
    "town": "schema:City",
    "village": "schema:Place",
    "island": "schema:Place",
    "archaeological-site": "schema:LandmarksOrHistoricalBuildings",
    "parish": "schema:AdministrativeArea",
}


def escape(s):
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")


lines = []
lines.append("# ═══════════════════════════════════════════════════════════════")
lines.append("# Nordic Place Name Authority — Linked Data for metadatahub.eu")
lines.append(f"# {total} entries: countries, regions, cities, towns, islands,")
lines.append("# archaeological sites, and Sámi place names across")
lines.append("# Sweden, Norway, Finland, Denmark, and Iceland.")
lines.append("#")
lines.append("# Sources:")
lines.append("#   https://www.geonames.org/")
lines.append("#   https://www.wikidata.org/")
lines.append("#   https://en.wikipedia.org/wiki/Nordic_countries")
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
lines.append("@prefix schema:  <https://schema.org/> .")
lines.append("@prefix geo:     <http://www.w3.org/2003/01/geo/wgs84_pos#> .")
lines.append(f"@prefix np:      <{BASE}/> .")
lines.append("")

# Dataset metadata
lines.append(f"<{BASE}> a skos:ConceptScheme ;")
lines.append(f'    dcterms:title "Nordic Place Name Authority"@en ;')
lines.append(f'    dcterms:description "{total} entries covering place names across Sweden, Norway, Finland, Denmark, Iceland, and Sápmi — countries, regions, cities, archaeological sites, and historical name variants."@en ;')
lines.append(f'    dcterms:source <https://www.geonames.org/> ;')
lines.append(f'    dcterms:source <https://www.wikidata.org/> ;')
lines.append(f'    dcterms:source <https://en.wikipedia.org/wiki/Nordic_countries> ;')
lines.append(f'    dcterms:creator "Port 30 KB" ;')
lines.append(f'    dcterms:license <https://creativecommons.org/licenses/by-sa/4.0/> ;')
lines.append(f'    dcterms:modified "2025-01-15"^^xsd:date .')
lines.append("")

for idx, d in enumerate(DATA, 1):
    cls = TYPE_TO_CLASS.get(d["type"], "schema:Place")
    en_label = d["labels"].get("en", list(d["labels"].values())[0])
    lines.append(f"# ── {idx}/{total}: {en_label} ({d['type']}) ──")
    lines.append(f"np:{d['id']} a skos:Concept, {cls} ;")

    # Multilingual labels — English first, then others alphabetically
    label_items = sorted(d["labels"].items(), key=lambda x: (x[0] != "en", x[0]))
    for lang, name in label_items:
        lines.append(f'    rdfs:label "{escape(name)}"@{lang} ;')

    # skos:prefLabel — all languages
    for lang, name in label_items:
        lines.append(f'    skos:prefLabel "{escape(name)}"@{lang} ;')

    # skos:altLabel — alternative labels
    if d.get("alt_labels"):
        for lang, names in sorted(d["alt_labels"].items()):
            for name in names:
                lines.append(f'    skos:altLabel "{escape(name)}"@{lang} ;')

    # skos:hiddenLabel — historical labels
    if d.get("historical_labels"):
        for lang, names in sorted(d["historical_labels"].items()):
            for name in names:
                lines.append(f'    skos:hiddenLabel "{escape(name)}"@{lang} ;')

    lines.append(f'    skos:inScheme <{BASE}> ;')
    lines.append(f'    skos:definition "{escape(d["description"])}"@en ;')
    lines.append(f'    dcterms:type "{d["type"]}" ;')

    if d["broader"]:
        lines.append(f'    skos:broader np:{d["broader"]} ;')

    # Timeline
    if d.get("timeline_start") is not None:
        lines.append(f'    <{BASE}/ontology/timelineStart> "{d["timeline_start"]}"^^xsd:long ;')
    if d.get("timeline_end") is not None:
        lines.append(f'    <{BASE}/ontology/timelineEnd> "{d["timeline_end"]}"^^xsd:long ;')

    # Coordinates
    if d.get("lat") is not None and d.get("lon") is not None:
        lines.append(f'    geo:lat "{d["lat"]}"^^xsd:decimal ;')
        lines.append(f'    geo:long "{d["lon"]}"^^xsd:decimal ;')

    # External links
    same_as = []
    if d.get("geonames_uri"):
        same_as.append(d["geonames_uri"])
    if d.get("wikidata_uri"):
        same_as.append(d["wikidata_uri"])

    if same_as:
        for i, uri in enumerate(same_as):
            sep = " ;" if i < len(same_as) - 1 else " ."
            lines.append(f'    owl:sameAs <{uri}>{sep}')
    else:
        # Close the last property with a period
        if lines[-1].endswith(" ;"):
            lines[-1] = lines[-1][:-2] + " ."

    lines.append("")

# Fix any trailing semicolons that should be periods
for i in range(len(lines)):
    # If the next non-empty line starts with "# ──" or "np:" or is empty,
    # ensure the previous property line ends with "."
    pass

os.makedirs(OUT_DIR, exist_ok=True)

with open(os.path.join(OUT_DIR, "nordic-places.ttl"), "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

# ══════════════════════════════════════════════════════════════
# Generate JSON-LD
# ══════════════════════════════════════════════════════════════

jsonld_items = []
for d in DATA:
    cls = TYPE_TO_CLASS.get(d["type"], "schema:Place")
    en_label = d["labels"].get("en", list(d["labels"].values())[0])

    # Build multilingual label array
    label_items = sorted(d["labels"].items(), key=lambda x: (x[0] != "en", x[0]))
    label_list = [{"@value": name, "@language": lang} for lang, name in label_items]

    # Build prefLabel array
    pref_label_list = [{"@value": name, "@language": lang} for lang, name in label_items]

    item = {
        "@id": f"{BASE}/{d['id']}",
        "@type": ["skos:Concept", cls],
        "rdfs:label": label_list if len(label_list) > 1 else label_list[0],
        "skos:prefLabel": pref_label_list if len(pref_label_list) > 1 else pref_label_list[0],
        "skos:definition": {"@value": d["description"], "@language": "en"},
        "dcterms:type": d["type"],
        "skos:inScheme": {"@id": BASE},
    }

    if d["broader"]:
        item["skos:broader"] = {"@id": f"{BASE}/{d['broader']}"}

    # Timeline
    if d.get("timeline_start") is not None:
        item["mhub:timelineStart"] = d["timeline_start"]
    if d.get("timeline_end") is not None:
        item["mhub:timelineEnd"] = d["timeline_end"]

    # Alt labels
    if d.get("alt_labels"):
        alt_list = []
        for lang, names in sorted(d["alt_labels"].items()):
            for name in names:
                alt_list.append({"@value": name, "@language": lang})
        if alt_list:
            item["skos:altLabel"] = alt_list if len(alt_list) > 1 else alt_list[0]

    # Historical labels
    if d.get("historical_labels"):
        hist_list = []
        for lang, names in sorted(d["historical_labels"].items()):
            for name in names:
                hist_list.append({"@value": name, "@language": lang})
        if hist_list:
            item["skos:hiddenLabel"] = hist_list if len(hist_list) > 1 else hist_list[0]

    # Coordinates
    if d.get("lat") is not None and d.get("lon") is not None:
        item["geo:lat"] = d["lat"]
        item["geo:long"] = d["lon"]

    # External links
    same_as = []
    if d.get("geonames_uri"):
        same_as.append({"@id": d["geonames_uri"]})
    if d.get("wikidata_uri"):
        same_as.append({"@id": d["wikidata_uri"]})
    if same_as:
        item["owl:sameAs"] = same_as if len(same_as) > 1 else same_as[0]

    jsonld_items.append(item)

jsonld_doc = {
    "@context": {
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "owl": "http://www.w3.org/2002/07/owl#",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "dcterms": "http://purl.org/dc/terms/",
        "schema": "https://schema.org/",
        "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#",
        "mhub": f"{BASE}/ontology/",
    },
    "@id": BASE,
    "@type": "skos:ConceptScheme",
    "dcterms:title": "Nordic Place Name Authority",
    "dcterms:description": f"{total} entries covering place names across Sweden, Norway, Finland, Denmark, Iceland, and Sápmi.",
    "dcterms:source": [
        "https://www.geonames.org/",
        "https://www.wikidata.org/",
        "https://en.wikipedia.org/wiki/Nordic_countries",
    ],
    "dcterms:license": "https://creativecommons.org/licenses/by-sa/4.0/",
    "@graph": jsonld_items,
}

with open(os.path.join(OUT_DIR, "nordic-places.jsonld"), "w", encoding="utf-8") as f:
    json.dump(jsonld_doc, f, indent=2, ensure_ascii=False)

print(f"  Turtle: hugo/static/data/nordic-places.ttl ({len(lines)} lines)")
print(f"  JSON-LD: hugo/static/data/nordic-places.jsonld ({len(jsonld_items)} items)")
