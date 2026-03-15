#!/usr/bin/env python3
"""Generate 250 example cultural heritage object records as Turtle RDF.

Reads reference data from data/example-collection/reference-data.yaml
and generates both Turtle RDF and JSON-LD output files.

Each record uses CIDOC-CRM event-based patterns with realistic museum data:
production events, materials, dimensions, actors, places, and time-spans.
"""

import json
import os
import random
import sys

import yaml

random.seed(42)

BASE = "https://metadatahub.eu/data/example-collection"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, "..", "data", "example-collection", "reference-data.yaml")
OUT_DIR = os.path.join(SCRIPT_DIR, "..", "hugo", "static", "data")

# ══════════════════════════════════════════════════════════════
# Load reference data from YAML
# ══════════════════════════════════════════════════════════════

if not os.path.exists(DATA_FILE):
    print(f"ERROR: Data file not found: {DATA_FILE}", file=sys.stderr)
    sys.exit(1)

with open(DATA_FILE, encoding="utf-8") as f:
    ref = yaml.safe_load(f)

OBJECT_TYPES = [(d["name"], d["crm_class"], d["aat_uri"]) for d in ref["object_types"]]
MATERIALS = [(d["name"], d["aat_uri"]) for d in ref["materials"]]
ARTISTS = [(d["name"], d["born"], d["died"], d["place"]) for d in ref["artists"]]
ANONYMOUS_MAKERS = ref["anonymous_makers"]
PLACES = [(d["name"], d["country"], d["geonames_uri"]) for d in ref["places"]]
COLLECTIONS = ref["collections"]
PERIODS = [(d["name"], d["start"], d["end"]) for d in ref["periods"]]
SUBJECTS = [(d["name"], d["aat_uri"]) for d in ref["subjects"]]
TITLES_ADJ = ref["title_adjectives"]
TITLES_NOUN = ref["title_nouns"]

print(f"Loaded reference data: {len(OBJECT_TYPES)} object types, {len(ARTISTS)} artists, {len(PLACES)} places")

# ══════════════════════════════════════════════════════════════
# Generate records
# ══════════════════════════════════════════════════════════════


def make_title(i, obj_type):
    adj = TITLES_ADJ[i % len(TITLES_ADJ)]
    noun = TITLES_NOUN[(i * 7) % len(TITLES_NOUN)]
    if obj_type in ("Coin", "Medal", "Brooch", "Ring", "Sword", "Axe head", "Stone tool"):
        return f"{adj} {obj_type} #{i+1}"
    if obj_type in ("Ceramic vessel", "Glass vessel"):
        return f"{adj} {obj_type.split()[0]} {noun} #{i+1}"
    if obj_type == "Runestone fragment":
        return f"Runestone Fragment {adj} #{i+1}"
    if obj_type == "Manuscript page":
        return f"Manuscript Leaf: {adj} {noun} #{i+1}"
    return f"{adj} {noun}"


def make_year(period):
    start, end = period[1], period[2]
    # Handle BC dates
    if "BC" in start:
        s = -int(start.replace(" BC", ""))
    else:
        s = int(start)
    if "BC" in end:
        e = -int(end.replace(" BC", ""))
    else:
        e = int(end)
    return random.randint(s, e)


def escape_turtle(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


lines = []
lines.append("# Example Cultural Heritage Collection — 250 Objects")
lines.append("# Generated for metadatahub.eu as sample linked data")
lines.append("#")
lines.append(f"# Total records: 250")
lines.append("")
lines.append("@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .")
lines.append("@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .")
lines.append("@prefix crm: <http://www.cidoc-crm.org/cidoc-crm/> .")
lines.append("@prefix dcterms: <http://purl.org/dc/terms/> .")
lines.append("@prefix skos: <http://www.w3.org/2004/02/skos/core#> .")
lines.append("@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .")
lines.append("@prefix aat: <http://vocab.getty.edu/aat/> .")
lines.append("@prefix gn: <http://sws.geonames.org/> .")
lines.append(f"@prefix ex: <{BASE}/> .")
lines.append("")

# Generate JSON-LD array too
jsonld_items = []

for i in range(250):
    obj_type, crm_class, aat_uri = OBJECT_TYPES[i % len(OBJECT_TYPES)]
    material_name, material_uri = MATERIALS[i % len(MATERIALS)]
    period = PERIODS[i % len(PERIODS)]
    place = PLACES[i % len(PLACES)]
    collection = COLLECTIONS[i % len(COLLECTIONS)]
    subject = SUBJECTS[i % len(SUBJECTS)]
    year = make_year(period)

    title = make_title(i, obj_type)

    # Decide if named artist or anonymous
    if i < 60 or (i % 5 == 0):
        artist = ARTISTS[i % len(ARTISTS)]
        actor_label = artist[0]
        actor_id = actor_label.lower().replace(" ", "-").replace("ø", "o").replace("ö", "o")
    else:
        anon = ANONYMOUS_MAKERS[i % len(ANONYMOUS_MAKERS)]
        actor_label = anon
        actor_id = f"anon-{i}"

    obj_id = f"obj-{i+1:04d}"

    # Dimensions
    if obj_type in ("Painting", "Drawing", "Print", "Photograph", "Icon", "Tapestry", "Manuscript page"):
        h = random.randint(15, 250)
        w = random.randint(10, 200)
        dim_str = f"{h} x {w} cm"
    elif obj_type in ("Sculpture", "Ceramic vessel", "Glass vessel", "Furniture piece"):
        h = random.randint(5, 180)
        w = random.randint(5, 80)
        d = random.randint(5, 80)
        dim_str = f"{h} x {w} x {d} cm"
    elif obj_type in ("Coin", "Medal", "Brooch", "Ring"):
        diam = random.randint(1, 8)
        dim_str = f"diameter {diam}.{random.randint(0,9)} cm"
    else:
        l = random.randint(10, 120)
        dim_str = f"length {l} cm"

    accession = f"{collection[:3].upper()}-{year}-{i+1:04d}"

    if year < 0:
        year_str = f"{abs(year)} BC"
        date_literal = f"{abs(year)} BCE"
    else:
        year_str = str(year)
        date_literal = str(year)

    lines.append(f"# --- Object {i+1}/250: {title} ---")
    lines.append(f"ex:{obj_id} a crm:{crm_class} ;")
    lines.append(f'    rdfs:label "{escape_turtle(title)}"@en ;')
    lines.append(f'    dcterms:identifier "{accession}" ;')
    lines.append(f'    crm:P2_has_type <{aat_uri}> ;')
    lines.append(f'    crm:P45_consists_of <{material_uri}> ;')
    lines.append(f'    crm:P43_has_dimension [')
    lines.append(f'        a crm:E54_Dimension ;')
    lines.append(f'        rdfs:label "{dim_str}"')
    lines.append(f'    ] ;')
    lines.append(f'    crm:P50_has_current_keeper [')
    lines.append(f'        a crm:E40_Legal_Body ;')
    lines.append(f'        rdfs:label "{collection}"')
    lines.append(f'    ] ;')
    lines.append(f'    crm:P129_is_about <{subject[1]}> ;')
    lines.append(f'    crm:P108i_was_produced_by ex:{obj_id}-production .')
    lines.append("")
    lines.append(f"ex:{obj_id}-production a crm:E12_Production ;")
    lines.append(f'    rdfs:label "Production of {escape_turtle(title)}"@en ;')
    lines.append(f'    crm:P14_carried_out_by ex:actor-{actor_id} ;')
    lines.append(f'    crm:P7_took_place_at <{place[2]}> ;')
    lines.append(f'    crm:P4_has_time-span [')
    lines.append(f'        a crm:E52_Time-Span ;')
    lines.append(f'        rdfs:label "{date_literal}" ;')
    lines.append(f'        crm:P82a_begin_of_the_begin "{year_str}"')
    lines.append(f'    ] .')
    lines.append("")
    lines.append(f'ex:actor-{actor_id} a crm:E39_Actor ;')
    lines.append(f'    rdfs:label "{escape_turtle(actor_label)}"@en .')
    lines.append("")

    # JSON-LD item
    jsonld_items.append({
        "@id": f"{BASE}/{obj_id}",
        "@type": f"crm:{crm_class}",
        "rdfs:label": {"@value": title, "@language": "en"},
        "dcterms:identifier": accession,
        "crm:P2_has_type": {"@id": aat_uri},
        "crm:P45_consists_of": {"@id": material_uri},
        "crm:P43_has_dimension": {"rdfs:label": dim_str},
        "crm:P50_has_current_keeper": {"rdfs:label": collection},
        "crm:P129_is_about": {"@id": subject[1]},
        "production": {
            "@type": "crm:E12_Production",
            "actor": actor_label,
            "place": f"{place[0]}, {place[1]}",
            "date": date_literal,
        }
    })

# Write Turtle
with open(os.path.join(OUT_DIR, "example-collection.ttl"), "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

# Write JSON-LD
jsonld_doc = {
    "@context": {
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "crm": "http://www.cidoc-crm.org/cidoc-crm/",
        "dcterms": "http://purl.org/dc/terms/",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "aat": "http://vocab.getty.edu/aat/",
    },
    "@id": BASE,
    "@type": "void:Dataset",
    "dcterms:title": "Example Cultural Heritage Collection",
    "dcterms:description": "250 sample cultural heritage object records for metadatahub.eu",
    "@graph": jsonld_items,
}

with open(os.path.join(OUT_DIR, "example-collection.jsonld"), "w", encoding="utf-8") as f:
    json.dump(jsonld_doc, f, indent=2, ensure_ascii=False)

print(f"Generated 250 objects")
print(f"  Turtle: hugo/static/data/example-collection.ttl")
print(f"  JSON-LD: hugo/static/data/example-collection.jsonld")
