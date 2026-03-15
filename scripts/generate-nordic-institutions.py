#!/usr/bin/env python3
"""Generate the Nordic Museum Institutions Authority as Linked Data (Turtle + JSON-LD).

Reads data from YAML file in data/nordic-institutions/ and generates:
  - hugo/static/data/nordic-institutions.ttl  (Turtle RDF)
  - hugo/static/data/nordic-institutions.jsonld  (JSON-LD)

Covers ~115 museum institutions across five Nordic countries:
- Sweden (~35 institutions)
- Norway (~25 institutions)
- Finland (~25 institutions)
- Denmark (~20 institutions)
- Iceland (~10 institutions)

Each entry has multilingual labels:
  - "en" (English) — primary language
  - Local language (sv, nb, nn, fi, da, is, se)

RDF modelling uses:
  - CIDOC-CRM E40_Legal_Body — cultural heritage institution class
  - org:Organization — W3C organization ontology
  - schema:Museum — Schema.org museum type

Data file: data/nordic-institutions/institutions.yaml
Schema:    data/nordic-institutions/_schema.yaml

Sources:
  https://en.wikipedia.org/wiki/List_of_museums_in_Sweden
  https://en.wikipedia.org/wiki/List_of_museums_in_Norway
  https://en.wikipedia.org/wiki/List_of_museums_in_Finland
  https://en.wikipedia.org/wiki/List_of_museums_in_Denmark
  https://en.wikipedia.org/wiki/List_of_museums_in_Iceland
"""

import json
import os
import sys

import yaml

BASE = "https://metadatahub.eu/data/nordic-institutions"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "data", "nordic-institutions")
OUT_DIR = os.path.join(SCRIPT_DIR, "..", "hugo", "static", "data")

VALID_TYPES = {
    "art-museum",
    "history-museum",
    "open-air-museum",
    "university-museum",
    "archaeology-museum",
    "design-museum",
    "maritime-museum",
    "natural-history-museum",
    "folk-museum",
    "specialized-museum",
}

VALID_COUNTRIES = {"SE", "NO", "FI", "DK", "IS"}

REQUIRED_FIELDS = {"id", "name", "type", "country", "city", "description"}

COUNTRY_NAMES = {
    "SE": "Sweden",
    "NO": "Norway",
    "FI": "Finland",
    "DK": "Denmark",
    "IS": "Iceland",
}

TYPE_LABELS = {
    "art-museum": "Art Museum",
    "history-museum": "History Museum",
    "open-air-museum": "Open-Air Museum",
    "university-museum": "University Museum",
    "archaeology-museum": "Archaeology Museum",
    "design-museum": "Design Museum",
    "maritime-museum": "Maritime Museum",
    "natural-history-museum": "Natural History Museum",
    "folk-museum": "Folk Museum",
    "specialized-museum": "Specialized Museum",
}

# ══════════════════════════════════════════════════════════════
# Load YAML data file
# ══════════════════════════════════════════════════════════════

DATA = []
filepath = os.path.join(DATA_DIR, "institutions.yaml")

if not os.path.exists(filepath):
    print(f"ERROR: Data file not found: {filepath}", file=sys.stderr)
    sys.exit(1)

with open(filepath, encoding="utf-8") as f:
    entries = yaml.safe_load(f)

if not entries:
    print(f"ERROR: No entries found in {filepath}", file=sys.stderr)
    sys.exit(1)

DATA = entries
print(f"Loaded {len(DATA)} entries from institutions.yaml")

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

    # Check type
    if d.get("type") not in VALID_TYPES:
        errors.append(f"{entry_id} has invalid type '{d.get('type')}'")

    # Check country
    if d.get("country") not in VALID_COUNTRIES:
        errors.append(f"{entry_id} has invalid country '{d.get('country')}'")

    # Check name
    name = d.get("name", {})
    if "en" not in name:
        errors.append(f"{entry_id} missing English name ('en')")

    # Ensure all name values are strings
    for lang, val in name.items():
        if not isinstance(val, str):
            d["name"][lang] = str(val)

if errors:
    print(f"\n{len(errors)} validation error(s):", file=sys.stderr)
    for e in errors:
        print(f"  - {e}", file=sys.stderr)
    sys.exit(1)

total = len(DATA)

# Count by country and type
by_country = {}
by_type = {}
for d in DATA:
    c = d["country"]
    t = d["type"]
    by_country[c] = by_country.get(c, 0) + 1
    by_type[t] = by_type.get(t, 0) + 1

print(f"Total institutions: {total}")
for c in sorted(by_country, key=lambda x: -by_country[x]):
    print(f"  {COUNTRY_NAMES.get(c, c)}: {by_country[c]}")

# ══════════════════════════════════════════════════════════════
# Generate Turtle
# ══════════════════════════════════════════════════════════════


def escape(s):
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")


lines = []
lines.append("# ═══════════════════════════════════════════════════════════════")
lines.append("# Nordic Museum Institutions Authority — Linked Data for metadatahub.eu")
lines.append(f"# {total} museum institutions across Sweden, Norway, Finland,")
lines.append("# Denmark, and Iceland.")
lines.append("#")
lines.append("# Sources:")
lines.append("#   https://en.wikipedia.org/wiki/List_of_museums_in_Sweden")
lines.append("#   https://en.wikipedia.org/wiki/List_of_museums_in_Norway")
lines.append("#   https://en.wikipedia.org/wiki/List_of_museums_in_Finland")
lines.append("#   https://en.wikipedia.org/wiki/List_of_museums_in_Denmark")
lines.append("#   https://en.wikipedia.org/wiki/List_of_museums_in_Iceland")
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
lines.append("@prefix foaf:    <http://xmlns.com/foaf/0.1/> .")
lines.append("@prefix org:     <http://www.w3.org/ns/org#> .")
lines.append("@prefix schema:  <https://schema.org/> .")
lines.append("@prefix crm:     <http://www.cidoc-crm.org/cidoc-crm/> .")
lines.append("@prefix wd:      <http://www.wikidata.org/entity/> .")
lines.append("@prefix gn:      <http://sws.geonames.org/> .")
lines.append(f"@prefix ni:      <{BASE}/> .")
lines.append("")

# Dataset metadata
lines.append(f"<{BASE}> a skos:ConceptScheme ;")
lines.append(f'    dcterms:title "Nordic Museum Institutions Authority"@en ;')
lines.append(
    f'    dcterms:description "{total} museum institutions across Sweden, Norway, Finland, Denmark, and Iceland — an authority file for Nordic cultural heritage organisations."@en ;'
)
lines.append(
    f"    dcterms:source <https://en.wikipedia.org/wiki/List_of_museums_in_Sweden> ;"
)
lines.append(
    f"    dcterms:source <https://en.wikipedia.org/wiki/List_of_museums_in_Norway> ;"
)
lines.append(
    f"    dcterms:source <https://en.wikipedia.org/wiki/List_of_museums_in_Finland> ;"
)
lines.append(
    f"    dcterms:source <https://en.wikipedia.org/wiki/List_of_museums_in_Denmark> ;"
)
lines.append(
    f"    dcterms:source <https://en.wikipedia.org/wiki/List_of_museums_in_Iceland> ;"
)
lines.append(f'    dcterms:creator "Port 30 KB" ;')
lines.append(
    f"    dcterms:license <https://creativecommons.org/licenses/by-sa/4.0/> ;"
)
lines.append(f'    dcterms:modified "2025-01-15"^^xsd:date .')
lines.append("")

for idx, d in enumerate(DATA, 1):
    en_name = d["name"].get("en", list(d["name"].values())[0])
    lines.append(f"# ── {idx}/{total}: {en_name} ({d['country']}) ──")

    # Type triple: CIDOC-CRM E40_Legal_Body, org:Organization, schema:Museum
    lines.append(
        f"ni:{d['id']} a crm:E40_Legal_Body , org:Organization , schema:Museum ;"
    )

    # Multilingual labels — English first, then others alphabetically
    name_items = sorted(d["name"].items(), key=lambda x: (x[0] != "en", x[0]))
    for lang, name in name_items:
        lines.append(f'    rdfs:label "{escape(name)}"@{lang} ;')

    # skos:prefLabel for English
    lines.append(f'    skos:prefLabel "{escape(en_name)}"@en ;')

    lines.append(f"    skos:inScheme <{BASE}> ;")
    lines.append(f'    skos:definition "{escape(d["description"])}"@en ;')

    # Museum type
    lines.append(
        f'    schema:additionalType "{d["type"]}" ;'
    )

    # Country
    lines.append(f'    schema:addressCountry "{d["country"]}" ;')

    # City
    lines.append(f'    schema:addressLocality "{escape(d["city"])}" ;')

    # Optional: GeoNames
    if d.get("geonames_uri"):
        lines.append(f"    schema:location <{d['geonames_uri']}> ;")

    # Optional: Wikidata
    if d.get("wikidata_uri"):
        lines.append(f"    owl:sameAs <{d['wikidata_uri']}> ;")

    # Optional: ISIL
    if d.get("isil"):
        lines.append(f'    dcterms:identifier "{d["isil"]}" ;')

    # Optional: website
    if d.get("website"):
        lines.append(f"    foaf:homepage <{d['website']}> ;")

    # Optional: established
    if d.get("established"):
        lines.append(
            f'    schema:foundingDate "{d["established"]}"^^xsd:gYear ;'
        )

    # Source
    lines.append(
        f"    dcterms:source <https://en.wikipedia.org/wiki/List_of_museums_in_{COUNTRY_NAMES[d['country']]}> ."
    )
    lines.append("")

os.makedirs(OUT_DIR, exist_ok=True)

with open(os.path.join(OUT_DIR, "nordic-institutions.ttl"), "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

# ══════════════════════════════════════════════════════════════
# Generate JSON-LD
# ══════════════════════════════════════════════════════════════

jsonld_items = []
for d in DATA:
    en_name = d["name"].get("en", list(d["name"].values())[0])

    # Build multilingual label array
    label_list = [
        {"@value": name, "@language": lang}
        for lang, name in sorted(
            d["name"].items(), key=lambda x: (x[0] != "en", x[0])
        )
    ]

    item = {
        "@id": f"{BASE}/{d['id']}",
        "@type": [
            "crm:E40_Legal_Body",
            "org:Organization",
            "schema:Museum",
        ],
        "rdfs:label": label_list if len(label_list) > 1 else label_list[0],
        "skos:prefLabel": {"@value": en_name, "@language": "en"},
        "skos:definition": {"@value": d["description"], "@language": "en"},
        "schema:additionalType": d["type"],
        "schema:addressCountry": d["country"],
        "schema:addressLocality": d["city"],
    }

    if d.get("geonames_uri"):
        item["schema:location"] = {"@id": d["geonames_uri"]}

    if d.get("wikidata_uri"):
        item["owl:sameAs"] = {"@id": d["wikidata_uri"]}

    if d.get("isil"):
        item["dcterms:identifier"] = d["isil"]

    if d.get("website"):
        item["foaf:homepage"] = {"@id": d["website"]}

    if d.get("established"):
        item["schema:foundingDate"] = {
            "@value": d["established"],
            "@type": "xsd:gYear",
        }

    item["dcterms:source"] = (
        f"https://en.wikipedia.org/wiki/List_of_museums_in_{COUNTRY_NAMES[d['country']]}"
    )

    jsonld_items.append(item)

jsonld_doc = {
    "@context": {
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "owl": "http://www.w3.org/2002/07/owl#",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "dcterms": "http://purl.org/dc/terms/",
        "foaf": "http://xmlns.com/foaf/0.1/",
        "org": "http://www.w3.org/ns/org#",
        "schema": "https://schema.org/",
        "crm": "http://www.cidoc-crm.org/cidoc-crm/",
    },
    "@id": BASE,
    "@type": "skos:ConceptScheme",
    "dcterms:title": "Nordic Museum Institutions Authority",
    "dcterms:description": f"{total} museum institutions across Sweden, Norway, Finland, Denmark, and Iceland — an authority file for Nordic cultural heritage organisations.",
    "dcterms:source": [
        "https://en.wikipedia.org/wiki/List_of_museums_in_Sweden",
        "https://en.wikipedia.org/wiki/List_of_museums_in_Norway",
        "https://en.wikipedia.org/wiki/List_of_museums_in_Finland",
        "https://en.wikipedia.org/wiki/List_of_museums_in_Denmark",
        "https://en.wikipedia.org/wiki/List_of_museums_in_Iceland",
    ],
    "dcterms:license": "https://creativecommons.org/licenses/by-sa/4.0/",
    "@graph": jsonld_items,
}

with open(
    os.path.join(OUT_DIR, "nordic-institutions.jsonld"), "w", encoding="utf-8"
) as f:
    json.dump(jsonld_doc, f, indent=2, ensure_ascii=False)

print(f"  Turtle: hugo/static/data/nordic-institutions.ttl ({len(lines)} lines)")
print(f"  JSON-LD: hugo/static/data/nordic-institutions.jsonld ({len(jsonld_items)} items)")
