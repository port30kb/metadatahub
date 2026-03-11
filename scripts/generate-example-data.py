#!/usr/bin/env python3
"""Generate 250 example cultural heritage object records as Turtle RDF.

Each record uses CIDOC-CRM event-based patterns with realistic museum data:
production events, materials, dimensions, actors, places, and time-spans.
"""

import random
import json

random.seed(42)

BASE = "https://metadatahub.eu/data/example-collection"

OBJECT_TYPES = [
    ("Painting", "E22_Human-Made_Object", "http://vocab.getty.edu/aat/300033618"),
    ("Sculpture", "E22_Human-Made_Object", "http://vocab.getty.edu/aat/300047090"),
    ("Drawing", "E22_Human-Made_Object", "http://vocab.getty.edu/aat/300033973"),
    ("Print", "E22_Human-Made_Object", "http://vocab.getty.edu/aat/300041273"),
    ("Photograph", "E22_Human-Made_Object", "http://vocab.getty.edu/aat/300046300"),
    ("Ceramic vessel", "E22_Human-Made_Object", "http://vocab.getty.edu/aat/300024841"),
    ("Textile", "E22_Human-Made_Object", "http://vocab.getty.edu/aat/300014063"),
    ("Coin", "E22_Human-Made_Object", "http://vocab.getty.edu/aat/300037222"),
    ("Medal", "E22_Human-Made_Object", "http://vocab.getty.edu/aat/300046025"),
    ("Brooch", "E22_Human-Made_Object", "http://vocab.getty.edu/aat/300045991"),
    ("Ring", "E22_Human-Made_Object", "http://vocab.getty.edu/aat/300046012"),
    ("Sword", "E22_Human-Made_Object", "http://vocab.getty.edu/aat/300037048"),
    ("Axe head", "E22_Human-Made_Object", "http://vocab.getty.edu/aat/300024664"),
    ("Runestone fragment", "E22_Human-Made_Object", "http://vocab.getty.edu/aat/300006958"),
    ("Manuscript page", "E22_Human-Made_Object", "http://vocab.getty.edu/aat/300028569"),
    ("Icon", "E22_Human-Made_Object", "http://vocab.getty.edu/aat/300263063"),
    ("Tapestry", "E22_Human-Made_Object", "http://vocab.getty.edu/aat/300205002"),
    ("Furniture piece", "E22_Human-Made_Object", "http://vocab.getty.edu/aat/300037680"),
    ("Glass vessel", "E22_Human-Made_Object", "http://vocab.getty.edu/aat/300010898"),
    ("Stone tool", "E22_Human-Made_Object", "http://vocab.getty.edu/aat/300024823"),
]

MATERIALS = [
    ("oil on canvas", "http://vocab.getty.edu/aat/300015050"),
    ("oil on panel", "http://vocab.getty.edu/aat/300015062"),
    ("tempera on panel", "http://vocab.getty.edu/aat/300015064"),
    ("watercolor on paper", "http://vocab.getty.edu/aat/300015045"),
    ("marble", "http://vocab.getty.edu/aat/300011443"),
    ("bronze", "http://vocab.getty.edu/aat/300010957"),
    ("iron", "http://vocab.getty.edu/aat/300011002"),
    ("silver", "http://vocab.getty.edu/aat/300011029"),
    ("gold", "http://vocab.getty.edu/aat/300011021"),
    ("ceramic", "http://vocab.getty.edu/aat/300010669"),
    ("wood", "http://vocab.getty.edu/aat/300011914"),
    ("limestone", "http://vocab.getty.edu/aat/300011286"),
    ("granite", "http://vocab.getty.edu/aat/300011183"),
    ("silk", "http://vocab.getty.edu/aat/300243428"),
    ("wool", "http://vocab.getty.edu/aat/300243430"),
    ("linen", "http://vocab.getty.edu/aat/300243425"),
    ("parchment", "http://vocab.getty.edu/aat/300014109"),
    ("glass", "http://vocab.getty.edu/aat/300010797"),
    ("copper alloy", "http://vocab.getty.edu/aat/300010942"),
    ("stoneware", "http://vocab.getty.edu/aat/300010829"),
]

ARTISTS = [
    ("Anders Zorn", "1860", "1920", "Mora"),
    ("Carl Larsson", "1853", "1919", "Stockholm"),
    ("Bruno Liljefors", "1860", "1939", "Uppsala"),
    ("Ernst Josephson", "1851", "1906", "Stockholm"),
    ("Hanna Pauli", "1864", "1940", "Stockholm"),
    ("Eva Bonnier", "1857", "1909", "Stockholm"),
    ("Prince Eugen", "1865", "1947", "Stockholm"),
    ("Helene Schjerfbeck", "1862", "1946", "Helsinki"),
    ("Akseli Gallen-Kallela", "1865", "1931", "Pori"),
    ("Edvard Munch", "1863", "1944", "Kristiania"),
    ("Vilhelm Hammershøi", "1864", "1916", "Copenhagen"),
    ("P.S. Krøyer", "1851", "1909", "Skagen"),
    ("Anna Ancher", "1859", "1935", "Skagen"),
    ("Michael Ancher", "1849", "1927", "Skagen"),
    ("Christian Krohg", "1852", "1925", "Kristiania"),
    ("Harriet Backer", "1845", "1932", "Kristiania"),
    ("Fanny Churberg", "1845", "1892", "Helsinki"),
    ("Albert Edelfelt", "1854", "1905", "Helsinki"),
    ("Hugo Simberg", "1873", "1917", "Hamina"),
    ("Eero Järnefelt", "1863", "1937", "Helsinki"),
]

ANONYMOUS_MAKERS = [
    "Unknown Swedish craftsman",
    "Unknown Nordic smith",
    "Unknown Viking Age artisan",
    "Unknown medieval workshop",
    "Unknown Sámi artisan",
    "Unknown Baltic craftsman",
    "Unknown Gotlandic metalworker",
    "Unknown Finnish weaver",
    "Unknown Danish potter",
    "Unknown Norwegian woodcarver",
]

PLACES = [
    ("Stockholm", "Sweden", "http://sws.geonames.org/2673730/"),
    ("Gothenburg", "Sweden", "http://sws.geonames.org/2711537/"),
    ("Malmö", "Sweden", "http://sws.geonames.org/2692969/"),
    ("Uppsala", "Sweden", "http://sws.geonames.org/2666199/"),
    ("Visby", "Sweden", "http://sws.geonames.org/2662689/"),
    ("Lund", "Sweden", "http://sws.geonames.org/2693678/"),
    ("Birka", "Sweden", "http://sws.geonames.org/2720543/"),
    ("Sigtuna", "Sweden", "http://sws.geonames.org/2678005/"),
    ("Helsinki", "Finland", "http://sws.geonames.org/658225/"),
    ("Turku", "Finland", "http://sws.geonames.org/633679/"),
    ("Copenhagen", "Denmark", "http://sws.geonames.org/2618425/"),
    ("Oslo", "Norway", "http://sws.geonames.org/3143244/"),
    ("Bergen", "Norway", "http://sws.geonames.org/3161732/"),
    ("Trondheim", "Norway", "http://sws.geonames.org/3133880/"),
    ("Reykjavik", "Iceland", "http://sws.geonames.org/3413829/"),
]

COLLECTIONS = [
    "Nationalmuseum",
    "Nordiska museet",
    "Historiska museet",
    "Moderna Museet",
    "Göteborgs konstmuseum",
    "Malmö Museer",
    "Uppsala universitetsmuseum",
    "Gotlands Museum",
    "Ateneum Art Museum",
    "National Museum of Denmark",
]

PERIODS = [
    ("Viking Age", "793", "1066"),
    ("Medieval", "1066", "1500"),
    ("Renaissance", "1400", "1600"),
    ("Baroque", "1600", "1750"),
    ("Rococo", "1730", "1780"),
    ("Neoclassical", "1760", "1830"),
    ("Romantic", "1800", "1870"),
    ("Realist", "1848", "1900"),
    ("Impressionist", "1860", "1910"),
    ("Art Nouveau", "1890", "1910"),
    ("National Romantic", "1880", "1920"),
    ("Early Modern", "1900", "1940"),
    ("Iron Age", "500 BC", "793"),
    ("Bronze Age", "1700 BC", "500 BC"),
    ("Stone Age", "8000 BC", "1700 BC"),
]

SUBJECTS = [
    ("landscape", "http://vocab.getty.edu/aat/300015636"),
    ("portrait", "http://vocab.getty.edu/aat/300015637"),
    ("still life", "http://vocab.getty.edu/aat/300015638"),
    ("mythology", "http://vocab.getty.edu/aat/300055985"),
    ("religious scene", "http://vocab.getty.edu/aat/300073708"),
    ("genre scene", "http://vocab.getty.edu/aat/300139140"),
    ("marine scene", "http://vocab.getty.edu/aat/300015639"),
    ("animal study", "http://vocab.getty.edu/aat/300249799"),
    ("botanical illustration", "http://vocab.getty.edu/aat/300015578"),
    ("architectural view", "http://vocab.getty.edu/aat/300015636"),
    ("battle scene", "http://vocab.getty.edu/aat/300386274"),
    ("allegory", "http://vocab.getty.edu/aat/300055866"),
    ("folk life", "http://vocab.getty.edu/aat/300139140"),
    ("winter scene", "http://vocab.getty.edu/aat/300015636"),
    ("self-portrait", "http://vocab.getty.edu/aat/300124534"),
]

TITLES_ADJ = [
    "Northern", "Summer", "Winter", "Autumn", "Spring",
    "Evening", "Morning", "Midnight", "Golden", "Silver",
    "Ancient", "Lost", "Hidden", "Sacred", "Royal",
    "Coastal", "Mountain", "Forest", "Lake", "River",
    "Ceremonial", "Decorated", "Ornamental", "Miniature", "Grand",
]

TITLES_NOUN = [
    "Landscape", "Harbor", "Interior", "Garden", "Shore",
    "Village", "Meadow", "Fjord", "Archipelago", "Bridge",
    "Chapel", "Farmstead", "Market", "Festival", "Procession",
    "Portrait", "Study", "Composition", "Scene", "View",
    "Vessel", "Ornament", "Pendant", "Figurine", "Relief",
]


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
with open("/home/user/metadatahub/hugo/static/data/example-collection.ttl", "w") as f:
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

with open("/home/user/metadatahub/hugo/static/data/example-collection.jsonld", "w") as f:
    json.dump(jsonld_doc, f, indent=2, ensure_ascii=False)

print(f"Generated 250 objects")
print(f"  Turtle: hugo/static/data/example-collection.ttl")
print(f"  JSON-LD: hugo/static/data/example-collection.jsonld")
