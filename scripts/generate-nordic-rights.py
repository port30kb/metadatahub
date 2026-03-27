#!/usr/bin/env python3
"""Generate the Nordic Rights and Licenses Vocabulary as Linked Data (Turtle + JSON-LD).

Reads data from YAML file in data/nordic-rights/ and generates:
  - hugo/static/data/nordic-rights.ttl   (Turtle RDF)
  - hugo/static/data/nordic-rights.jsonld (JSON-LD)

Covers ~53 entries across five categories:
- Creative Commons Licenses (CC0, CC-BY, CC-BY-SA, etc.)
- RightsStatements.org standardized statements
- Nordic copyright law concepts (Swedish, Finnish, Norwegian, Danish, Icelandic)
- Europeana rights framework tiers and policies
- Common museum scenario guidance

Each entry has multilingual labels:
  - "en" (English) — primary language
  - "sv" (Swedish) — always included
  - Additional Nordic languages: fi, da, nb, is, se

Data file: data/nordic-rights/rights-vocabulary.yaml
Schema:    data/nordic-rights/_schema.yaml

Sources:
  https://creativecommons.org/licenses/
  https://rightsstatements.org/
  https://pro.europeana.eu/page/available-rights-statements
  https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-1960729-om-upphovsratt-till-litterara-och_sfs-1960-729/
  https://www.finlex.fi/fi/laki/ajantasa/1961/19610404
  https://lovdata.no/dokument/NL/lov/2018-06-15-40
"""

import json
import os
import sys

import yaml

BASE = "https://metadatahub.eu/data/nordic-rights"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "data", "nordic-rights")
OUT_DIR = os.path.join(SCRIPT_DIR, "..", "hugo", "static", "data")

VALID_CATEGORIES = {
    "creative-commons",
    "rights-statement",
    "nordic-copyright-law",
    "europeana-framework",
    "museum-scenario",
}
VALID_TIERS = {"tier-1", "tier-2", "tier-3", "tier-4"}
REQUIRED_FIELDS = {"id", "labels", "category", "description"}

# ══════════════════════════════════════════════════════════════
# Load YAML data file
# ══════════════════════════════════════════════════════════════

data_file = os.path.join(DATA_DIR, "rights-vocabulary.yaml")
if not os.path.isfile(data_file):
    print(f"ERROR: Data file not found: {data_file}", file=sys.stderr)
    sys.exit(1)

with open(data_file, encoding="utf-8") as f:
    DATA = yaml.safe_load(f)

if not DATA:
    print(f"ERROR: No entries found in {data_file}", file=sys.stderr)
    sys.exit(1)

print(f"Loaded {len(DATA)} entries from rights-vocabulary.yaml")

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

    # Check category
    if d.get("category") not in VALID_CATEGORIES:
        errors.append(f"{entry_id} has invalid category '{d.get('category')}'")

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

    # Check europeana_tier if present
    tier = d.get("europeana_tier")
    if tier is not None and tier not in VALID_TIERS:
        errors.append(f"{entry_id} has invalid europeana_tier '{tier}'")

    # Set defaults for optional fields
    d.setdefault("broader", None)
    d.setdefault("canonical_uri", None)
    d.setdefault("europeana_tier", None)
    d.setdefault("usage_guidance", None)

# Check broader references (second pass)
for d in DATA:
    if d.get("broader") and d["broader"] not in ids:
        errors.append(f"{d['id']} has unknown broader concept '{d['broader']}'")

if errors:
    print(f"\n{len(errors)} validation error(s):", file=sys.stderr)
    for e in errors:
        print(f"  - {e}", file=sys.stderr)
    sys.exit(1)

total = len(DATA)
print(f"Total entries: {total}")

# Count by category
cat_counts = {}
for d in DATA:
    cat = d["category"]
    cat_counts[cat] = cat_counts.get(cat, 0) + 1
for cat, count in sorted(cat_counts.items()):
    print(f"  {cat}: {count}")

# ══════════════════════════════════════════════════════════════
# Generate Turtle
# ══════════════════════════════════════════════════════════════

CATEGORY_TO_CLASS = {
    "creative-commons": "mhub:License",
    "rights-statement": "mhub:RightsStatement",
    "nordic-copyright-law": "mhub:CopyrightConcept",
    "europeana-framework": "mhub:RightsFramework",
    "museum-scenario": "mhub:UsageScenario",
}


def escape(s):
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")


lines = []
lines.append("# ═══════════════════════════════════════════════════════════════")
lines.append("# Nordic Rights and Licenses Vocabulary — Linked Data for metadatahub.eu")
lines.append(f"# {total} entries: Creative Commons licenses, RightsStatements.org,")
lines.append("# Nordic copyright law concepts, Europeana rights framework,")
lines.append("# and common museum scenario guidance.")
lines.append("#")
lines.append("# Sources:")
lines.append("#   https://creativecommons.org/licenses/")
lines.append("#   https://rightsstatements.org/")
lines.append("#   https://pro.europeana.eu/page/available-rights-statements")
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
lines.append("@prefix cc:      <http://creativecommons.org/ns#> .")
lines.append("@prefix odrl:    <http://www.w3.org/ns/odrl/2/> .")
lines.append(f"@prefix mhub:    <{BASE}/ontology/> .")
lines.append(f"@prefix nr:      <{BASE}/> .")
lines.append("")

# Dataset metadata
lines.append(f"<{BASE}> a skos:ConceptScheme ;")
lines.append(f'    dcterms:title "Nordic Rights and Licenses Vocabulary"@en ;')
lines.append(f'    dcterms:title "Nordiskt rattighets- och licensvokabular"@sv ;')
lines.append(
    f'    dcterms:description "{total} entries covering rights statements, licenses, and copyright concepts for Nordic cultural heritage institutions."@en ;'
)
lines.append(f"    dcterms:source <https://creativecommons.org/licenses/> ;")
lines.append(f"    dcterms:source <https://rightsstatements.org/> ;")
lines.append(
    f"    dcterms:source <https://pro.europeana.eu/page/available-rights-statements> ;")
lines.append(f'    dcterms:creator "Port 30 KB" ;')
lines.append(
    f"    dcterms:license <https://creativecommons.org/licenses/by-sa/4.0/> ;")
lines.append(f'    dcterms:modified "2025-01-15"^^xsd:date .')
lines.append("")

# Custom property definition
lines.append("# Custom property for Europeana tier classification")
lines.append("mhub:europeanaTier a owl:DatatypeProperty ;")
lines.append('    rdfs:label "Europeana licensing tier"@en ;')
lines.append('    rdfs:comment "Classifies a rights statement by Europeana openness tier (tier-1 most restrictive to tier-4 most open)."@en ;')
lines.append("    rdfs:domain skos:Concept ;")
lines.append("    rdfs:range xsd:string .")
lines.append("")

for idx, d in enumerate(DATA, 1):
    cls = CATEGORY_TO_CLASS.get(d["category"], "skos:Concept")
    en_label = d["labels"].get("en", list(d["labels"].values())[0])
    lines.append(f"# ── {idx}/{total}: {en_label} ──")
    lines.append(f"nr:{d['id']} a {cls}, skos:Concept ;")

    # Multilingual labels — English first, then others alphabetically
    label_items = sorted(
        d["labels"].items(), key=lambda x: (x[0] != "en", x[0])
    )
    for lang, name in label_items:
        lines.append(f'    rdfs:label "{escape(name)}"@{lang} ;')

    # skos:prefLabel for English
    lines.append(f'    skos:prefLabel "{escape(en_label)}"@en ;')

    # Swedish prefLabel
    sv_label = d["labels"].get("sv")
    if sv_label and sv_label != en_label:
        lines.append(f'    skos:prefLabel "{escape(sv_label)}"@sv ;')

    lines.append(f"    skos:inScheme <{BASE}> ;")
    lines.append(f'    skos:definition "{escape(d["description"])}"@en ;')
    lines.append(f'    mhub:category "{d["category"]}" ;')

    if d["broader"]:
        lines.append(f"    skos:broader nr:{d['broader']} ;")

    if d["canonical_uri"]:
        lines.append(f"    skos:exactMatch <{d['canonical_uri']}> ;")

    if d["europeana_tier"]:
        lines.append(f'    mhub:europeanaTier "{d["europeana_tier"]}" ;')

    if d["usage_guidance"]:
        lines.append(
            f'    skos:scopeNote "{escape(d["usage_guidance"])}"@en ;'
        )

    if d.get("timeline_start") is not None:
        lines.append(f'    <{BASE}/ontology/timelineStart> "{d["timeline_start"]}"^^xsd:long ;')
    if d.get("timeline_end") is not None:
        lines.append(f'    <{BASE}/ontology/timelineEnd> "{d["timeline_end"]}"^^xsd:long ;')

    # Close with source
    lines.append(
        f"    dcterms:source <https://creativecommons.org/licenses/> ."
    )
    lines.append("")

os.makedirs(OUT_DIR, exist_ok=True)

ttl_path = os.path.join(OUT_DIR, "nordic-rights.ttl")
with open(ttl_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

# ══════════════════════════════════════════════════════════════
# Generate JSON-LD
# ══════════════════════════════════════════════════════════════

jsonld_items = []
for d in DATA:
    cls = CATEGORY_TO_CLASS.get(d["category"], "skos:Concept")
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
        "@type": [cls, "skos:Concept"],
        "rdfs:label": label_list if len(label_list) > 1 else label_list[0],
        "skos:prefLabel": {"@value": en_label, "@language": "en"},
        "skos:definition": {"@value": d["description"], "@language": "en"},
        "mhub:category": d["category"],
    }

    if d["broader"]:
        item["skos:broader"] = {"@id": f"{BASE}/{d['broader']}"}

    if d["canonical_uri"]:
        item["skos:exactMatch"] = {"@id": d["canonical_uri"]}

    if d["europeana_tier"]:
        item["mhub:europeanaTier"] = d["europeana_tier"]

    if d["usage_guidance"]:
        item["skos:scopeNote"] = {
            "@value": d["usage_guidance"],
            "@language": "en",
        }

    if d.get("timeline_start") is not None:
        item["mhub:timelineStart"] = d["timeline_start"]
    if d.get("timeline_end") is not None:
        item["mhub:timelineEnd"] = d["timeline_end"]

    jsonld_items.append(item)

jsonld_doc = {
    "@context": {
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "owl": "http://www.w3.org/2002/07/owl#",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "dcterms": "http://purl.org/dc/terms/",
        "cc": "http://creativecommons.org/ns#",
        "odrl": "http://www.w3.org/ns/odrl/2/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "mhub": f"{BASE}/ontology/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
    },
    "@id": BASE,
    "@type": "skos:ConceptScheme",
    "dcterms:title": [
        {"@value": "Nordic Rights and Licenses Vocabulary", "@language": "en"},
        {
            "@value": "Nordiskt rattighets- och licensvokabular",
            "@language": "sv",
        },
    ],
    "dcterms:description": f"{total} entries covering rights statements, licenses, and copyright concepts for Nordic cultural heritage institutions.",
    "dcterms:source": [
        "https://creativecommons.org/licenses/",
        "https://rightsstatements.org/",
        "https://pro.europeana.eu/page/available-rights-statements",
    ],
    "dcterms:license": "https://creativecommons.org/licenses/by-sa/4.0/",
    "dcterms:creator": "Port 30 KB",
    "dcterms:modified": "2025-01-15",
    "@graph": jsonld_items,
}

jsonld_path = os.path.join(OUT_DIR, "nordic-rights.jsonld")
with open(jsonld_path, "w", encoding="utf-8") as f:
    json.dump(jsonld_doc, f, indent=2, ensure_ascii=False)

print(f"  Turtle:  hugo/static/data/nordic-rights.ttl ({len(lines)} lines)")
print(f"  JSON-LD: hugo/static/data/nordic-rights.jsonld ({len(jsonld_items)} items)")
