#!/usr/bin/env python3
"""Generate Nordic Thesaurus Mappings as Linked Data (Turtle + JSON-LD).

Reads mapping data from YAML files in data/nordic-thesaurus-mappings/ and generates:
  - hugo/static/data/nordic-thesaurus-mappings.ttl  (Turtle RDF)
  - hugo/static/data/nordic-thesaurus-mappings.jsonld  (JSON-LD)

Maps object type and subject classifications between Nordic museum systems:
  - K-samsök (Swedish Cultural Heritage)
  - DigitaltMuseum (Norway/Sweden)
  - Finna/YSO (Finland)
  - Danish National Museum classification
  - Getty Art & Architecture Thesaurus (AAT)

Data files: data/nordic-thesaurus-mappings/*.yaml
Schema:     data/nordic-thesaurus-mappings/_schema.yaml
"""

import glob
import json
import os
import sys

import yaml

BASE = "https://metadatahub.eu/data/nordic-thesaurus-mappings"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "data", "nordic-thesaurus-mappings")
OUT_DIR = os.path.join(SCRIPT_DIR, "..", "hugo", "static", "data")

VALID_MATCH_TYPES = {"exactMatch", "closeMatch", "broadMatch", "narrowMatch", "relatedMatch"}
VALID_SYSTEMS = {"ksamsok", "digitaltmuseum", "finna", "dkmuseum", "aat"}
REQUIRED_FIELDS = {"id", "source_system", "source_label", "target_system", "target_uri", "target_label", "match_type", "labels", "description"}

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
        entry["_source_file"] = fname
        DATA.append(entry)

print(f"Loaded {len(DATA)} mapping entries from {len(yaml_files)} files")

# ══════════════════════════════════════════════════════════════
# Validate
# ══════════════════════════════════════════════════════════════

errors = []
ids = set()

for i, d in enumerate(DATA):
    src = d.get("_source_file", "?")

    for field in REQUIRED_FIELDS:
        if field not in d:
            errors.append(f"{src}: entry #{i+1} missing required field '{field}'")

    entry_id = d.get("id", f"(entry #{i+1})")

    if d.get("id") in ids:
        errors.append(f"{src}: duplicate id '{d['id']}'")
    ids.add(d.get("id"))

    if d.get("match_type") not in VALID_MATCH_TYPES:
        errors.append(f"{src}: {entry_id} has invalid match_type '{d.get('match_type')}'")

    if d.get("source_system") not in VALID_SYSTEMS:
        errors.append(f"{src}: {entry_id} has invalid source_system '{d.get('source_system')}'")

    if d.get("target_system") not in VALID_SYSTEMS:
        errors.append(f"{src}: {entry_id} has invalid target_system '{d.get('target_system')}'")

    labels = d.get("labels", {})
    if "en" not in labels:
        errors.append(f"{src}: {entry_id} missing English label ('en')")
    if "sv" not in labels:
        errors.append(f"{src}: {entry_id} missing Swedish label ('sv')")

if errors:
    print(f"\n{len(errors)} validation error(s):", file=sys.stderr)
    for e in errors:
        print(f"  - {e}", file=sys.stderr)
    sys.exit(1)

total = len(DATA)

# Count by type
system_pairs = {}
for d in DATA:
    pair = f"{d['source_system']} → {d['target_system']}"
    system_pairs[pair] = system_pairs.get(pair, 0) + 1

print(f"Total mapping assertions: {total}")
for pair, count in sorted(system_pairs.items()):
    print(f"  {pair}: {count}")

# ══════════════════════════════════════════════════════════════
# Generate Turtle
# ══════════════════════════════════════════════════════════════

SYSTEM_LABELS = {
    "ksamsok": "K-samsök (Swedish Cultural Heritage)",
    "digitaltmuseum": "DigitaltMuseum (Norway/Sweden)",
    "finna": "Finna/YSO (Finland)",
    "dkmuseum": "Danish National Museum",
    "aat": "Getty Art & Architecture Thesaurus",
}

def escape(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')

lines = []
lines.append("# ═══════════════════════════════════════════════════════════════")
lines.append("# Nordic Thesaurus Mappings — Linked Data for metadatahub.eu")
lines.append(f"# {total} SKOS mapping assertions between Nordic museum systems")
lines.append("# and international standards (Getty AAT).")
lines.append("#")
lines.append("# Systems:")
for sys_id, label in SYSTEM_LABELS.items():
    lines.append(f"#   {sys_id}: {label}")
lines.append("#")
lines.append(f"# Total assertions: {total}")
lines.append("# ═══════════════════════════════════════════════════════════════")
lines.append("")
lines.append("@prefix rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .")
lines.append("@prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> .")
lines.append("@prefix owl:     <http://www.w3.org/2002/07/owl#> .")
lines.append("@prefix xsd:     <http://www.w3.org/2001/XMLSchema#> .")
lines.append("@prefix skos:    <http://www.w3.org/2004/02/skos/core#> .")
lines.append("@prefix dcterms: <http://purl.org/dc/terms/> .")
lines.append("@prefix void:    <http://rdfs.org/ns/void#> .")
lines.append(f"@prefix map:     <{BASE}/> .")
lines.append("")

# Dataset metadata as void:Linkset
lines.append(f"<{BASE}> a void:Linkset , skos:ConceptScheme ;")
lines.append(f'    dcterms:title "Nordic Thesaurus Mappings"@en ;')
lines.append(f'    dcterms:description "{total} SKOS mapping assertions between Nordic museum classification systems (K-samsök, DigitaltMuseum, Finna, Danish museums) and Getty AAT."@en ;')
lines.append(f'    dcterms:creator "Port 30 KB" ;')
lines.append(f'    dcterms:license <https://creativecommons.org/publicdomain/zero/1.0/> ;')
lines.append(f'    dcterms:modified "2025-01-15"^^xsd:date ;')
lines.append(f'    void:triples "{total}"^^xsd:integer .')
lines.append("")

for idx, d in enumerate(DATA, 1):
    en_label = d["labels"].get("en", d["id"])
    lines.append(f"# ── {idx}/{total}: {en_label} ──")
    lines.append(f"map:{d['id']} a skos:Concept ;")

    # Labels
    label_items = sorted(d["labels"].items(), key=lambda x: (x[0] != "en", x[0]))
    for lang, name in label_items:
        lines.append(f'    rdfs:label "{escape(name)}"@{lang} ;')

    lines.append(f'    skos:prefLabel "{escape(en_label)}"@en ;')
    lines.append(f'    skos:inScheme <{BASE}> ;')
    lines.append(f'    skos:definition "{escape(d["description"])}"@en ;')

    # Source concept
    source_uri = d.get("source_uri")
    if source_uri:
        lines.append(f'    dcterms:source <{source_uri}> ;')
    lines.append(f'    rdfs:comment "Source: {escape(d["source_label"])} ({d["source_system"]})"@en ;')

    # The actual SKOS mapping assertion
    match_type = d["match_type"]
    target_uri = d["target_uri"]
    lines.append(f'    skos:{match_type} <{target_uri}> ;')

    # Confidence
    confidence = d.get("confidence", "medium")
    lines.append(f'    dcterms:conformsTo "{confidence}" ;')

    # Note
    note = d.get("note")
    if note:
        lines.append(f'    skos:note "{escape(note)}"@en ;')

    if d.get("timeline_start") is not None:
        lines.append(f'    <{BASE}/ontology/timelineStart> "{d["timeline_start"]}"^^xsd:long ;')
    if d.get("timeline_end") is not None:
        lines.append(f'    <{BASE}/ontology/timelineEnd> "{d["timeline_end"]}"^^xsd:long ;')

    lines.append(f'    dcterms:creator "Port 30 KB" .')
    lines.append("")

os.makedirs(OUT_DIR, exist_ok=True)
with open(os.path.join(OUT_DIR, "nordic-thesaurus-mappings.ttl"), "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

# ══════════════════════════════════════════════════════════════
# Generate JSON-LD
# ══════════════════════════════════════════════════════════════

jsonld_items = []
for d in DATA:
    en_label = d["labels"].get("en", d["id"])
    label_list = [{"@value": name, "@language": lang}
                  for lang, name in sorted(d["labels"].items(), key=lambda x: (x[0] != "en", x[0]))]

    item = {
        "@id": f"{BASE}/{d['id']}",
        "@type": "skos:Concept",
        "rdfs:label": label_list if len(label_list) > 1 else label_list[0],
        "skos:prefLabel": {"@value": en_label, "@language": "en"},
        "skos:definition": {"@value": d["description"], "@language": "en"},
        f"skos:{d['match_type']}": {"@id": d["target_uri"]},
        "source_system": d["source_system"],
        "source_label": d["source_label"],
        "target_system": d["target_system"],
        "target_label": d["target_label"],
        "match_type": d["match_type"],
        "confidence": d.get("confidence", "medium"),
    }

    if d.get("source_uri"):
        item["dcterms:source"] = {"@id": d["source_uri"]}

    if d.get("note"):
        item["skos:note"] = {"@value": d["note"], "@language": "en"}

    if d.get("timeline_start") is not None:
        item["mhub:timelineStart"] = d["timeline_start"]
    if d.get("timeline_end") is not None:
        item["mhub:timelineEnd"] = d["timeline_end"]

    jsonld_items.append(item)

jsonld_doc = {
    "@context": {
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "dcterms": "http://purl.org/dc/terms/",
        "void": "http://rdfs.org/ns/void#",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "mhub": f"{BASE}/ontology/",
    },
    "@id": BASE,
    "@type": ["void:Linkset", "skos:ConceptScheme"],
    "dcterms:title": "Nordic Thesaurus Mappings",
    "dcterms:description": f"{total} SKOS mapping assertions between Nordic museum classification systems (K-samsök, DigitaltMuseum, Finna, Danish museums) and Getty AAT.",
    "dcterms:license": "https://creativecommons.org/publicdomain/zero/1.0/",
    "@graph": jsonld_items,
}

with open(os.path.join(OUT_DIR, "nordic-thesaurus-mappings.jsonld"), "w", encoding="utf-8") as f:
    json.dump(jsonld_doc, f, indent=2, ensure_ascii=False)

print(f"  Turtle: hugo/static/data/nordic-thesaurus-mappings.ttl ({len(lines)} lines)")
print(f"  JSON-LD: hugo/static/data/nordic-thesaurus-mappings.jsonld ({len(jsonld_items)} items)")
