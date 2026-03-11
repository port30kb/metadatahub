#!/usr/bin/env python3
"""Generate the Geologic Time Scale as Linked Data (Turtle + JSON-LD).

312 data points covering:
- 4 Eons
- 10 Eras
- 22 Periods (incl. Mississippian/Pennsylvanian sub-periods)
- 38 Epochs
- ~80 Ages/Stages (Mesozoic + Cenozoic + Pleistocene + Holocene)
- ~20 Paleozoic epoch-level divisions
- Archaeological/cultural ages bridging into human history

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
"""

import json

BASE = "https://metadatahub.eu/data/geologic-timescale"

# ──────────────────────────────────────────────────────────────
# Data: each entry is (id, label, rank, parent_id, start, end, unit, description)
#   rank: Eon | Era | Period | SubPeriod | Epoch | Age | CulturalAge
#   start/end: numeric (Ma for geologic, years BP or BCE/CE for cultural)
#   unit: "Ma" | "ka" | "BP" | "BCE" | "CE"
# ──────────────────────────────────────────────────────────────

DATA = []
n = [0]  # mutable counter

def add(id_, label, rank, parent, start, end, unit, desc):
    n[0] += 1
    DATA.append({
        "id": id_,
        "label": label,
        "rank": rank,
        "parent": parent,
        "start": start,
        "end": end,
        "unit": unit,
        "description": desc,
        "n": n[0],
    })

# ═══════════════════════════════════════════════════════════════
# EONS
# ═══════════════════════════════════════════════════════════════
add("hadean", "Hadean", "Eon", None, 4600, 4000, "Ma",
    "Earliest eon; Earth forms from accretion, heavy bombardment, formation of the Moon.")

# Hadean informal divisions (not formally ratified by ICS but widely used)
add("ginallian", "Ginallian (informal)", "Era", "hadean", 4600, 4510, "Ma",
    "Accretion and differentiation of Earth; formation of core and mantle from planetesimals.")
add("chaotian", "Chaotian (informal)", "Era", "hadean", 4510, 4404, "Ma",
    "Moon-forming giant impact (Theia hypothesis); surface entirely molten magma ocean.")
add("zirconian", "Zirconian (informal)", "Era", "hadean", 4404, 4030, "Ma",
    "Oldest known mineral grains (Jack Hills zircons, ~4.4 Ga); first solid crust forms; Late Heavy Bombardment.")
add("archean", "Archean", "Eon", None, 4000, 2500, "Ma",
    "First stable continents form; earliest evidence of life (stromatolites).")
add("proterozoic", "Proterozoic", "Eon", None, 2500, 538.8, "Ma",
    "Oxygen accumulates in atmosphere; first eukaryotes and multicellular life.")
add("phanerozoic", "Phanerozoic", "Eon", None, 538.8, 0, "Ma",
    "Eon of visible life; all complex animal phyla appear and diversify.")

# ═══════════════════════════════════════════════════════════════
# ARCHEAN ERAS
# ═══════════════════════════════════════════════════════════════
add("eoarchean", "Eoarchean", "Era", "archean", 4000, 3600, "Ma",
    "Oldest known rocks; possible earliest life.")
add("paleoarchean", "Paleoarchean", "Era", "archean", 3600, 3200, "Ma",
    "Earliest confirmed microbial life; oldest stromatolites.")
add("mesoarchean", "Mesoarchean", "Era", "archean", 3200, 2800, "Ma",
    "First large-scale stromatolite reefs; earliest photosynthesis evidence.")
add("neoarchean", "Neoarchean", "Era", "archean", 2800, 2500, "Ma",
    "Oxygen-producing cyanobacteria proliferate; banded iron formations peak.")

# ═══════════════════════════════════════════════════════════════
# PROTEROZOIC ERAS & PERIODS
# ═══════════════════════════════════════════════════════════════
add("paleoproterozoic", "Paleoproterozoic", "Era", "proterozoic", 2500, 1600, "Ma",
    "Great Oxidation Event; first supercontinent (Nuna/Columbia).")
add("siderian", "Siderian", "Period", "paleoproterozoic", 2500, 2300, "Ma",
    "Banded iron formations dominate; oxygen levels still rising.")
add("rhyacian", "Rhyacian", "Period", "paleoproterozoic", 2300, 2050, "Ma",
    "Huronian glaciation; first global ice age.")
add("orosirian", "Orosirian", "Period", "paleoproterozoic", 2050, 1800, "Ma",
    "Major mountain-building events; Vredefort and Sudbury impacts.")
add("statherian", "Statherian", "Period", "paleoproterozoic", 1800, 1600, "Ma",
    "First complex single-celled organisms with nuclei.")

add("mesoproterozoic", "Mesoproterozoic", "Era", "proterozoic", 1600, 1000, "Ma",
    "Supercontinent Rodinia assembles; first sexual reproduction evidence.")
add("calymmian", "Calymmian", "Period", "mesoproterozoic", 1600, 1400, "Ma",
    "Platform covers expand; stable continental interiors.")
add("ectasian", "Ectasian", "Period", "mesoproterozoic", 1400, 1200, "Ma",
    "Continued platform expansion; green algae diversify.")
add("stenian", "Stenian", "Period", "mesoproterozoic", 1200, 1000, "Ma",
    "Grenville orogeny; supercontinent Rodinia forms.")

add("neoproterozoic", "Neoproterozoic", "Era", "proterozoic", 1000, 538.8, "Ma",
    "Snowball Earth glaciations; first animals appear (Ediacaran biota).")
add("tonian", "Tonian", "Period", "neoproterozoic", 1000, 720, "Ma",
    "Rodinia begins to break apart; first multicellular organisms.")
add("cryogenian", "Cryogenian", "Period", "neoproterozoic", 720, 635, "Ma",
    "Snowball Earth glaciations: Sturtian and Marinoan; life survives in refugia.")
add("sturtian", "Sturtian Glaciation", "Age", "cryogenian", 717, 660, "Ma",
    "First and longer Snowball Earth event; global ice cover for ~57 million years.")
add("marinoan", "Marinoan Glaciation", "Age", "cryogenian", 650, 635, "Ma",
    "Second Snowball Earth; cap carbonates deposited after deglaciation.")
add("ediacaran", "Ediacaran", "Period", "neoproterozoic", 635, 538.8, "Ma",
    "Ediacaran biota: first large complex organisms; soft-bodied fauna.")

# ═══════════════════════════════════════════════════════════════
# PHANEROZOIC — PALEOZOIC ERA & PERIODS
# ═══════════════════════════════════════════════════════════════
add("paleozoic", "Paleozoic", "Era", "phanerozoic", 538.8, 251.9, "Ma",
    "Era of ancient life; Cambrian explosion, first fish, amphibians, reptiles, forests.")

add("cambrian", "Cambrian", "Period", "paleozoic", 538.8, 485.4, "Ma",
    "Cambrian explosion: most major animal phyla appear rapidly in the fossil record.")
add("terreneuvian", "Terreneuvian", "Epoch", "cambrian", 538.8, 521, "Ma",
    "Earliest Cambrian epoch; small shelly fossils appear.")
add("fortunian", "Fortunian", "Age", "terreneuvian", 538.8, 529, "Ma",
    "Earliest Cambrian age; first trace fossils of bilaterian animals.")
add("stage2-cambrian", "Cambrian Stage 2", "Age", "terreneuvian", 529, 521, "Ma",
    "Small shelly fauna diversify; archaeocyathids appear.")
add("epoch2-cambrian", "Cambrian Series 2", "Epoch", "cambrian", 521, 509, "Ma",
    "Trilobites diversify; archaeocyathid reefs.")
add("stage3-cambrian", "Cambrian Stage 3", "Age", "epoch2-cambrian", 521, 514, "Ma",
    "First trilobites appear; Cambrian explosion accelerates.")
add("stage4-cambrian", "Cambrian Stage 4", "Age", "epoch2-cambrian", 514, 509, "Ma",
    "Archaeocyathid reef-builders peak then decline.")
add("miaolingian", "Miaolingian", "Epoch", "cambrian", 509, 497, "Ma",
    "Peak trilobite diversity; Burgess Shale-type faunas.")
add("wuliuan", "Wuliuan", "Age", "miaolingian", 509, 504.5, "Ma",
    "Burgess Shale fauna; diverse arthropods and anomalocaridids.")
add("drumian", "Drumian", "Age", "miaolingian", 504.5, 500.5, "Ma",
    "Agnostid trilobites flourish; deep-water faunas diversify.")
add("guzhangian", "Guzhangian", "Age", "miaolingian", 500.5, 497, "Ma",
    "Trilobite turnover; transition toward Furongian faunas.")
add("furongian", "Furongian", "Epoch", "cambrian", 497, 485.4, "Ma",
    "Trilobite extinctions; first cephalopods appear.")
add("paibian", "Paibian", "Age", "furongian", 497, 494, "Ma",
    "SPICE carbon isotope excursion; trilobite extinction pulse.")
add("jiangshanian", "Jiangshanian", "Age", "furongian", 494, 489.5, "Ma",
    "Trilobite recovery; earliest cephalopods diversify.")
add("stage10-cambrian", "Cambrian Stage 10", "Age", "furongian", 489.5, 485.4, "Ma",
    "Final Cambrian stage; transition to Ordovician biodiversification.")

add("ordovician", "Ordovician", "Period", "paleozoic", 485.4, 443.8, "Ma",
    "Great Ordovician Biodiversification Event; first land plants; ends with mass extinction.")
add("early-ordovician", "Early Ordovician", "Epoch", "ordovician", 485.4, 470, "Ma",
    "Biodiversification begins; graptolites and brachiopods flourish.")
add("tremadocian", "Tremadocian", "Age", "early-ordovician", 485.4, 477.7, "Ma",
    "Conodonts and graptolites diversify; first planktonic ecosystems.")
add("floian", "Floian", "Age", "early-ordovician", 477.7, 470, "Ma",
    "First bryozoans; corals begin to diversify.")
add("middle-ordovician", "Middle Ordovician", "Epoch", "ordovician", 470, 458.4, "Ma",
    "Great Ordovician Biodiversification Event peaks.")
add("dapingian", "Dapingian", "Age", "middle-ordovician", 470, 467.3, "Ma",
    "GOBE intensifies; cephalopods diversify as top marine predators.")
add("darriwilian", "Darriwilian", "Age", "middle-ordovician", 467.3, 458.4, "Ma",
    "Peak of Great Ordovician Biodiversification; stromatoporoid reefs.")
add("late-ordovician", "Late Ordovician", "Epoch", "ordovician", 458.4, 443.8, "Ma",
    "End-Ordovician glaciation and mass extinction; ~85% of marine species lost.")
add("sandbian", "Sandbian", "Age", "late-ordovician", 458.4, 453, "Ma",
    "Taconic orogeny; diverse brachiopod communities.")
add("katian", "Katian", "Age", "late-ordovician", 453, 445.2, "Ma",
    "Peak marine diversity; Gondwanan glaciation begins.")
add("hirnantian", "Hirnantian", "Age", "late-ordovician", 445.2, 443.8, "Ma",
    "End-Ordovician mass extinction; rapid glaciation and sea level drop.")

add("silurian", "Silurian", "Period", "paleozoic", 443.8, 419.2, "Ma",
    "Recovery from extinction; first vascular land plants; jawed fish appear.")
add("llandovery", "Llandovery", "Epoch", "silurian", 443.8, 433.4, "Ma",
    "Post-extinction recovery; graptolite diversification.")
add("rhuddanian", "Rhuddanian", "Age", "llandovery", 443.8, 440.8, "Ma",
    "Earliest Silurian; rapid recovery of graptolite faunas.")
add("aeronian", "Aeronian", "Age", "llandovery", 440.8, 438.5, "Ma",
    "Continued recovery; first land plant spores.")
add("telychian", "Telychian", "Age", "llandovery", 438.5, 433.4, "Ma",
    "Graptolite diversity peak; first vascular plant fossils.")
add("wenlock", "Wenlock", "Epoch", "silurian", 433.4, 427.4, "Ma",
    "First land plants with vascular tissue; coral reef expansion.")
add("sheinwoodian", "Sheinwoodian", "Age", "wenlock", 433.4, 430.5, "Ma",
    "Ireviken extinction event; reef ecosystems expand.")
add("homerian", "Homerian", "Age", "wenlock", 430.5, 427.4, "Ma",
    "Mulde extinction event; eurypterids (sea scorpions) diversify.")
add("ludlow", "Ludlow", "Epoch", "silurian", 427.4, 423, "Ma",
    "First terrestrial arachnids; brachiopod diversity peak.")
add("gorstian", "Gorstian", "Age", "ludlow", 427.4, 425.6, "Ma",
    "Lau extinction event; graptolite fauna turnover.")
add("ludfordian", "Ludfordian", "Age", "ludlow", 425.6, 423, "Ma",
    "First terrestrial arthropod traces; jawed fish diversify.")
add("pridoli", "Přídolí", "Epoch", "silurian", 423, 419.2, "Ma",
    "First jawed fish diversify; transition toward Devonian.")

add("devonian", "Devonian", "Period", "paleozoic", 419.2, 358.9, "Ma",
    "Age of Fishes; first forests, first insects, first amphibians.")
add("klonk-event", "Klonk Event (Silurian–Devonian boundary)", "Age", "pridoli", 419.2, 419, "Ma",
    "GSSP at Klonk, Czech Republic; defined by first appearance of graptolite Monograptus uniformis.")
add("early-devonian", "Early Devonian", "Epoch", "devonian", 419.2, 393.3, "Ma",
    "First seed plants; armored fish diversify.")
add("lochkovian", "Lochkovian", "Age", "early-devonian", 419.2, 410.8, "Ma",
    "Earliest Devonian; jawed fish radiation continues.")
add("pragian", "Pragian", "Age", "early-devonian", 410.8, 407.6, "Ma",
    "First true leaves (lycopsids); early vascular plants spread onto land.")
add("emsian", "Emsian", "Age", "early-devonian", 407.6, 393.3, "Ma",
    "First insects; ammonoids appear; widespread reef systems.")
add("middle-devonian", "Middle Devonian", "Epoch", "devonian", 393.3, 382.7, "Ma",
    "First forests appear; ammonoids originate.")
add("eifelian", "Eifelian", "Age", "middle-devonian", 393.3, 387.7, "Ma",
    "Stromatoporoid-coral reefs peak; first seed ferns.")
add("givetian", "Givetian", "Age", "middle-devonian", 387.7, 382.7, "Ma",
    "First forests (Archaeopteris); placoderms diversify.")
add("late-devonian", "Late Devonian", "Epoch", "devonian", 382.7, 358.9, "Ma",
    "First tetrapods; Late Devonian extinction event (~75% of species).")
add("frasnian", "Frasnian", "Age", "late-devonian", 382.7, 372.2, "Ma",
    "Massive reef systems; Frasnian-Famennian extinction (Kellwasser Event).")
add("famennian", "Famennian", "Age", "late-devonian", 372.2, 358.9, "Ma",
    "Post-extinction recovery; first tetrapod trackways; Hangenberg Event at end.")

add("carboniferous", "Carboniferous", "Period", "paleozoic", 358.9, 298.9, "Ma",
    "Vast coal swamp forests; first reptiles; high atmospheric oxygen.")
add("mississippian", "Mississippian", "SubPeriod", "carboniferous", 358.9, 323.2, "Ma",
    "Early Carboniferous; large crinoid and coral reefs; amphibians diversify.")
add("early-mississippian", "Early Mississippian", "Epoch", "mississippian", 358.9, 346.7, "Ma",
    "Tournaisian age; recovery after Devonian extinction.")
add("tournaisian", "Tournaisian", "Age", "early-mississippian", 358.9, 346.7, "Ma",
    "Post-Devonian recovery; crinoid meadows; early tetrapod diversification (Romer's Gap).")
add("middle-mississippian", "Middle Mississippian", "Epoch", "mississippian", 346.7, 330.9, "Ma",
    "Viséan age; widespread limestone deposition; large coral reefs.")
add("visean", "Viséan", "Age", "middle-mississippian", 346.7, 330.9, "Ma",
    "Extensive carbonate platforms; first large tetrapods; coal forests begin.")
add("late-mississippian", "Late Mississippian", "Epoch", "mississippian", 330.9, 323.2, "Ma",
    "Serpukhovian age; glaciation begins in Gondwana.")
add("serpukhovian", "Serpukhovian", "Age", "late-mississippian", 330.9, 323.2, "Ma",
    "Late Mississippian ice ages; sea level drops; first winged insects.")
add("pennsylvanian", "Pennsylvanian", "SubPeriod", "carboniferous", 323.2, 298.9, "Ma",
    "Late Carboniferous; coal swamps peak; first reptiles appear.")
add("early-pennsylvanian", "Early Pennsylvanian", "Epoch", "pennsylvanian", 323.2, 315.2, "Ma",
    "Bashkirian age; Pangaea begins to assemble.")
add("bashkirian", "Bashkirian", "Age", "early-pennsylvanian", 323.2, 315.2, "Ma",
    "First large coal swamps; Pangaea assembly accelerates; early reptile diversification.")
add("middle-pennsylvanian", "Middle Pennsylvanian", "Epoch", "pennsylvanian", 315.2, 307, "Ma",
    "Moscovian age; giant insects thrive in high-oxygen atmosphere.")
add("moscovian", "Moscovian", "Age", "middle-pennsylvanian", 315.2, 307, "Ma",
    "Giant dragonflies (Meganeura); atmospheric oxygen ~35%; vast coal swamp forests.")
add("late-pennsylvanian", "Late Pennsylvanian", "Epoch", "pennsylvanian", 307, 298.9, "Ma",
    "Kasimovian–Gzhelian; earliest amniotes diversify; coal swamps decline.")
add("kasimovian", "Kasimovian", "Age", "late-pennsylvanian", 307, 303.7, "Ma",
    "Amniote reptiles diversify; first diapsids appear.")
add("gzhelian", "Gzhelian", "Age", "late-pennsylvanian", 303.7, 298.9, "Ma",
    "Coal swamps retreat as climate dries; Pangaea nearly complete.")

add("permian", "Permian", "Period", "paleozoic", 298.9, 251.9, "Ma",
    "Pangaea complete; therapsids (mammal ancestors) dominate; ends with the Great Dying.")
add("cisuralian", "Cisuralian", "Epoch", "permian", 298.9, 272.95, "Ma",
    "Early Permian; diverse amphibian and reptile faunas.")
add("asselian", "Asselian", "Age", "cisuralian", 298.9, 293.52, "Ma",
    "Earliest Permian; glaciation continues in Gondwana.")
add("sakmarian", "Sakmarian", "Age", "cisuralian", 293.52, 290.1, "Ma",
    "Pelycosaurs (sail-backed reptiles) diversify, including Dimetrodon.")
add("artinskian", "Artinskian", "Age", "cisuralian", 290.1, 283.5, "Ma",
    "Gondwanan glaciation wanes; conifers spread.")
add("kungurian", "Kungurian", "Age", "cisuralian", 283.5, 272.95, "Ma",
    "Evaporite deposits; therapsids begin to appear.")
add("guadalupian", "Guadalupian", "Epoch", "permian", 272.95, 259.51, "Ma",
    "Middle Permian; therapsids rise to dominance; Capitanian extinction event.")
add("roadian", "Roadian", "Age", "guadalupian", 272.95, 268.8, "Ma",
    "Therapsids diversify; dinocephalians dominate.")
add("wordian", "Wordian", "Age", "guadalupian", 268.8, 265.1, "Ma",
    "Reef ecosystems flourish; diverse fusulinid foraminifera.")
add("capitanian", "Capitanian", "Age", "guadalupian", 265.1, 259.51, "Ma",
    "Capitanian mass extinction: major reef collapse and biodiversity loss.")
add("lopingian", "Lopingian", "Epoch", "permian", 259.51, 251.9, "Ma",
    "Late Permian; Permian–Triassic extinction: ~96% of marine species lost.")
add("wuchiapingian", "Wuchiapingian", "Age", "lopingian", 259.51, 254.14, "Ma",
    "Post-Capitanian recovery; Dicynodonts become dominant herbivores.")
add("changhsingian", "Changhsingian", "Age", "lopingian", 254.14, 251.9, "Ma",
    "The Great Dying: Siberian Traps volcanism triggers worst mass extinction in Earth history.")

# ═══════════════════════════════════════════════════════════════
# PHANEROZOIC — MESOZOIC ERA & PERIODS
# ═══════════════════════════════════════════════════════════════
add("mesozoic", "Mesozoic", "Era", "phanerozoic", 251.9, 66, "Ma",
    "Age of Reptiles; dinosaurs, first mammals, first birds, first flowering plants.")

add("triassic", "Triassic", "Period", "mesozoic", 251.9, 201.4, "Ma",
    "Recovery from Permian extinction; first dinosaurs, first mammals, first pterosaurs.")
add("early-triassic", "Early Triassic", "Epoch", "triassic", 251.9, 247.2, "Ma",
    "Slow recovery from extinction; Lystrosaurus dominates terrestrial fauna.")
add("induan", "Induan", "Age", "early-triassic", 251.9, 251.2, "Ma",
    "Earliest Triassic stage; extremely low biodiversity, harsh conditions.")
add("olenekian", "Olenekian", "Age", "early-triassic", 251.2, 247.2, "Ma",
    "Marine ecosystems begin recovery; first ichthyosaurs appear.")
add("middle-triassic", "Middle Triassic", "Epoch", "triassic", 247.2, 237, "Ma",
    "Archosaurs diversify; first dinosauromorphs.")
add("anisian", "Anisian", "Age", "middle-triassic", 247.2, 242, "Ma",
    "Marine reptiles diversify; coral reefs re-establish.")
add("ladinian", "Ladinian", "Age", "middle-triassic", 242, 237, "Ma",
    "First dinosauriform tracks; seed ferns and conifers dominate.")
add("late-triassic", "Late Triassic", "Epoch", "triassic", 237, 201.4, "Ma",
    "First true dinosaurs, mammals, and pterosaurs; Triassic–Jurassic extinction at end.")
add("carnian", "Carnian", "Age", "late-triassic", 237, 227, "Ma",
    "Carnian Pluvial Episode: major climate shift; first dinosaurs appear.")
add("norian", "Norian", "Age", "late-triassic", 227, 208.5, "Ma",
    "Dinosaurs diversify; first turtles and crocodylomorphs.")
add("rhaetian", "Rhaetian", "Age", "late-triassic", 208.5, 201.4, "Ma",
    "End-Triassic extinction opens ecological niches for dinosaurs.")

add("jurassic", "Jurassic", "Period", "mesozoic", 201.4, 143.1, "Ma",
    "Dinosaurs dominate; first birds (Archaeopteryx); Pangaea breaks apart.")
add("early-jurassic", "Early Jurassic", "Epoch", "jurassic", 201.4, 174.1, "Ma",
    "Dinosaurs diversify into dominant land animals; large marine reptiles.")
add("hettangian", "Hettangian", "Age", "early-jurassic", 201.4, 199.5, "Ma",
    "Post-extinction recovery; early dinosaur radiation.")
add("sinemurian", "Sinemurian", "Age", "early-jurassic", 199.5, 192.9, "Ma",
    "Early large sauropodomorphs; ammonite diversity increases.")
add("pliensbachian", "Pliensbachian", "Age", "early-jurassic", 192.9, 184.2, "Ma",
    "Warm climates; diverse marine ecosystems, ichthyosaurs abundant.")
add("toarcian", "Toarcian", "Age", "early-jurassic", 184.2, 174.1, "Ma",
    "Toarcian Oceanic Anoxic Event; some marine extinctions.")
add("middle-jurassic", "Middle Jurassic", "Epoch", "jurassic", 174.1, 163.5, "Ma",
    "Sauropods and theropods diversify; earliest flowering plant evidence.")
add("aalenian", "Aalenian", "Age", "middle-jurassic", 174.1, 170.9, "Ma",
    "Pangaea continues to rift; ammonites flourish.")
add("bajocian", "Bajocian", "Age", "middle-jurassic", 170.9, 168.2, "Ma",
    "Diverse coral reefs; stegosaurs appear.")
add("bathonian", "Bathonian", "Age", "middle-jurassic", 168.2, 165.3, "Ma",
    "First definitive mammals diversify; microcontinent formation.")
add("callovian", "Callovian", "Age", "middle-jurassic", 165.3, 163.5, "Ma",
    "Marine transgression; ammonite diversity peak in Jurassic.")
add("late-jurassic", "Late Jurassic", "Epoch", "jurassic", 163.5, 143.1, "Ma",
    "Giant sauropods; Archaeopteryx; Morrison Formation dinosaurs.")
add("oxfordian", "Oxfordian", "Age", "late-jurassic", 163.5, 157.3, "Ma",
    "Widespread coral reefs; large theropods like Allosaurus.")
add("kimmeridgian", "Kimmeridgian", "Age", "late-jurassic", 157.3, 152.1, "Ma",
    "Rich marine ecosystems; source rocks for North Sea oil form.")
add("tithonian", "Tithonian", "Age", "late-jurassic", 152.1, 143.1, "Ma",
    "Archaeopteryx; Solnhofen limestone; transition to Cretaceous.")

add("cretaceous", "Cretaceous", "Period", "mesozoic", 143.1, 66, "Ma",
    "Longest Mesozoic period; flowering plants rise; ends with asteroid impact (K-Pg).")
add("early-cretaceous", "Early Cretaceous", "Epoch", "cretaceous", 143.1, 100.5, "Ma",
    "Flowering plants diversify; feathered dinosaurs; continental drift accelerates.")
add("berriasian", "Berriasian", "Age", "early-cretaceous", 143.1, 139.8, "Ma",
    "Earliest Cretaceous; GSSP boundary still under discussion.")
add("valanginian", "Valanginian", "Age", "early-cretaceous", 139.8, 132.6, "Ma",
    "Weald clay environments; early angiosperms in fossil record.")
add("hauterivian", "Hauterivian", "Age", "early-cretaceous", 132.6, 125.77, "Ma",
    "Iguanodon and early ornithopod diversity; warm global climate.")
add("barremian", "Barremian", "Age", "early-cretaceous", 125.77, 121.4, "Ma",
    "Las Hoyas and Jehol Biota; feathered theropods preserved.")
add("aptian", "Aptian", "Age", "early-cretaceous", 121.4, 113.2, "Ma",
    "Oceanic Anoxic Event 1a; first diverse angiosperm floras.")
add("albian", "Albian", "Age", "early-cretaceous", 113.2, 100.5, "Ma",
    "High sea levels; diverse ammonites; early social insects.")
add("late-cretaceous", "Late Cretaceous", "Epoch", "cretaceous", 100.5, 66, "Ma",
    "Tyrannosaurus, Triceratops; angiosperms dominant; K-Pg extinction.")
add("cenomanian", "Cenomanian", "Age", "late-cretaceous", 100.5, 93.9, "Ma",
    "Highest sea levels in Cretaceous; OAE 2 at boundary.")
add("turonian", "Turonian", "Age", "late-cretaceous", 93.9, 89.4, "Ma",
    "Warmest period of Cretaceous; diverse reef ecosystems.")
add("coniacian", "Coniacian", "Age", "late-cretaceous", 89.4, 86.3, "Ma",
    "Continued warm climates; hadrosaur diversification begins.")
add("santonian", "Santonian", "Age", "late-cretaceous", 86.3, 83.6, "Ma",
    "Ceratopsian dinosaurs diversify; early modern bird lineages.")
add("campanian", "Campanian", "Age", "late-cretaceous", 83.6, 72.2, "Ma",
    "Rich dinosaur faunas worldwide; chalk deposits form.")
add("maastrichtian", "Maastrichtian", "Age", "late-cretaceous", 72.2, 66, "Ma",
    "Final stage; Chicxulub impact ends Mesozoic; ~76% of species extinct.")

# ═══════════════════════════════════════════════════════════════
# PHANEROZOIC — CENOZOIC ERA & PERIODS
# ═══════════════════════════════════════════════════════════════
add("cenozoic", "Cenozoic", "Era", "phanerozoic", 66, 0, "Ma",
    "Age of Mammals; grasslands, primates, hominins; current era.")

add("paleogene", "Paleogene", "Period", "cenozoic", 66, 23.03, "Ma",
    "Mammals diversify rapidly after K-Pg extinction; first primates.")
add("paleocene", "Paleocene", "Epoch", "paleogene", 66, 56, "Ma",
    "Post-extinction recovery; mammals remain small but diversify.")
add("danian", "Danian", "Age", "paleocene", 66, 61.6, "Ma",
    "Earliest Cenozoic stage; mammals fill vacant ecological niches.")
add("selandian", "Selandian", "Age", "paleocene", 61.6, 59.2, "Ma",
    "Warm climates; early primate evolution.")
add("thanetian", "Thanetian", "Age", "paleocene", 59.2, 56, "Ma",
    "Warming trend; diverse mammal faunas; London Clay formation.")
add("eocene", "Eocene", "Epoch", "paleogene", 56, 33.9, "Ma",
    "Warmest Cenozoic epoch; first modern mammal orders; early whales, horses, bats.")
add("ypresian", "Ypresian", "Age", "eocene", 56, 47.8, "Ma",
    "Paleocene-Eocene Thermal Maximum (PETM); warmest global temperatures.")
add("lutetian", "Lutetian", "Age", "eocene", 47.8, 41.2, "Ma",
    "Diversification of modern mammal families; early elephants.")
add("bartonian", "Bartonian", "Age", "eocene", 41.2, 37.71, "Ma",
    "Gradual cooling begins; Antarctic ice sheet starts forming.")
add("priabonian", "Priabonian", "Age", "eocene", 37.71, 33.9, "Ma",
    "Grande Coupure extinction event in Europe; dramatic cooling.")
add("oligocene", "Oligocene", "Epoch", "paleogene", 33.9, 23.03, "Ma",
    "Cooler and drier; grasslands expand; modern mammal families establish.")
add("rupelian", "Rupelian", "Age", "oligocene", 33.9, 27.82, "Ma",
    "Antarctic ice sheet permanent; global cooling continues.")
add("chattian", "Chattian", "Age", "oligocene", 27.82, 23.03, "Ma",
    "Late Oligocene warming; first deer and pigs appear.")

add("neogene", "Neogene", "Period", "cenozoic", 23.03, 2.58, "Ma",
    "Grasslands dominate; great apes evolve; Isthmus of Panama forms.")
add("miocene", "Miocene", "Epoch", "neogene", 23.03, 5.33, "Ma",
    "Kelp forests, grasslands; diverse apes; Messinian salinity crisis.")
add("aquitanian", "Aquitanian", "Age", "miocene", 23.03, 20.44, "Ma",
    "Early Miocene; warm climates; diverse marine mammals.")
add("burdigalian", "Burdigalian", "Age", "miocene", 20.44, 15.98, "Ma",
    "Mountain building (Alps, Himalayas); first great apes.")
add("langhian", "Langhian", "Age", "miocene", 15.98, 13.82, "Ma",
    "Mid-Miocene Climatic Optimum; widespread warmth.")
add("serravallian", "Serravallian", "Age", "miocene", 13.82, 11.63, "Ma",
    "Cooling resumes; East Antarctic ice sheet expands.")
add("tortonian", "Tortonian", "Age", "miocene", 11.63, 7.246, "Ma",
    "Mediterranean begins to close; hominoids disperse from Africa.")
add("messinian", "Messinian", "Age", "miocene", 7.246, 5.33, "Ma",
    "Messinian Salinity Crisis: Mediterranean nearly dries up.")
add("pliocene", "Pliocene", "Epoch", "neogene", 5.33, 2.58, "Ma",
    "Australopithecus; Arctic ice cap forms; Isthmus of Panama closes.")
add("zanclean", "Zanclean", "Age", "pliocene", 5.33, 3.6, "Ma",
    "Zanclean flood refills Mediterranean; Australopithecus afarensis.")
add("piacenzian", "Piacenzian", "Age", "pliocene", 3.6, 2.58, "Ma",
    "Mid-Piacenzian Warm Period; early Homo?; Northern Hemisphere glaciation starts.")

add("quaternary", "Quaternary", "Period", "cenozoic", 2.58, 0, "Ma",
    "Ice ages and interglacials; evolution and spread of Homo sapiens.")

# ── Pleistocene ──
add("pleistocene", "Pleistocene", "Epoch", "quaternary", 2.58, 0.0117, "Ma",
    "Repeated glaciations; megafauna; Homo erectus, Neanderthals, modern humans.")
add("gelasian", "Gelasian", "Age", "pleistocene", 2.58, 1.80, "Ma",
    "Earliest Pleistocene; Northern Hemisphere glaciation intensifies; early Homo.")
add("calabrian", "Calabrian", "Age", "pleistocene", 1.80, 0.774, "Ma",
    "Homo erectus disperses out of Africa; Brunhes-Matuyama reversal at end.")
add("chibanian", "Chibanian", "Age", "pleistocene", 0.774, 0.129, "Ma",
    "Homo heidelbergensis; Neanderthals evolve; major glacial cycles.")
add("late-pleistocene", "Late Pleistocene", "Age", "pleistocene", 0.129, 0.0117, "Ma",
    "Homo sapiens expands globally; Neanderthal extinction; Last Glacial Maximum.")

# ── Holocene ──
add("holocene", "Holocene", "Epoch", "quaternary", 11700, 0, "BP",
    "Current epoch; stable warm climate; rise of agriculture, civilization.")
add("greenlandian", "Greenlandian", "Age", "holocene", 11700, 8200, "BP",
    "Early Holocene; post-glacial warming; Mesolithic hunter-gatherers in Europe.")
add("northgrippian", "Northgrippian", "Age", "holocene", 8200, 4200, "BP",
    "Middle Holocene; 8.2 ka cold event; agriculture spreads through Europe.")
add("meghalayan", "Meghalayan", "Age", "holocene", 4200, 0, "BP",
    "Late Holocene; 4.2 ka drought; rise and fall of Bronze Age civilizations; present day.")

# ═══════════════════════════════════════════════════════════════
# ARCHAEOLOGICAL / CULTURAL AGES (European & Scandinavian focus)
# ═══════════════════════════════════════════════════════════════

# --- Stone Age ---
add("stone-age", "Stone Age", "CulturalAge", "holocene", 3300000, 3300, "BCE",
    "Longest period of human prehistory; defined by use of stone tools. Three-age system by C.J. Thomsen.")
add("paleolithic", "Paleolithic (Old Stone Age)", "CulturalAge", "stone-age", 3300000, 10000, "BCE",
    "Oldest division; hunter-gatherer societies; development of stone tool technology.")
add("lower-paleolithic", "Lower Paleolithic", "CulturalAge", "paleolithic", 3300000, 300000, "BCE",
    "Homo habilis, Homo erectus; Oldowan and Acheulean tool industries.")
add("middle-paleolithic", "Middle Paleolithic", "CulturalAge", "paleolithic", 300000, 50000, "BCE",
    "Neanderthals in Europe; Mousterian tool industry; first evidence of symbolic behavior.")
add("upper-paleolithic", "Upper Paleolithic", "CulturalAge", "paleolithic", 50000, 10000, "BCE",
    "Homo sapiens in Europe; cave art (Lascaux, Altamira); Aurignacian, Gravettian, Magdalenian cultures.")
add("bromme-culture", "Bromme Culture", "CulturalAge", "upper-paleolithic", 11000, 10000, "BCE",
    "Late Paleolithic reindeer hunters at the edge of the Scandinavian ice sheet; earliest human presence in Sweden (Scania).")
add("ahrensburg-culture", "Ahrensburg Culture", "CulturalAge", "upper-paleolithic", 11000, 9500, "BCE",
    "Late Paleolithic/early Mesolithic nomadic hunters from the North German Plain; migrated north via Jutland following retreating ice.")
add("mesolithic", "Mesolithic (Middle Stone Age)", "CulturalAge", "stone-age", 10000, 4000, "BCE",
    "Post-glacial; microlithic tools; Scandinavia first settled ~9500 BCE. Maglemosian, Kongemose, Ertebølle cultures.")
add("fosna-hensbacka", "Fosna–Hensbacka Culture", "CulturalAge", "mesolithic", 8300, 7300, "BCE",
    "Early Mesolithic culture along the Norwegian and Swedish west coasts; descended from Ahrensburg tradition; coastal seal hunting and fishing.")
add("komsa-culture", "Komsa Culture", "CulturalAge", "mesolithic", 10000, 6000, "BCE",
    "Early Mesolithic culture of northern Norway coast; sea-oriented seal hunters and fishermen; relatively crude stone tools compared to southern Fosna.")
add("maglemosian", "Maglemosian Culture", "CulturalAge", "mesolithic", 9000, 6000, "BCE",
    "Early Mesolithic hunter-gatherer culture in southern Scandinavia and northern Germany; flint microliths, bone harpoons.")
add("kongemose", "Kongemose Culture", "CulturalAge", "mesolithic", 6000, 5200, "BCE",
    "Middle Mesolithic in Denmark and southern Sweden; coastal adaptation, fishing, seal hunting.")
add("nostvet-lihult", "Nøstvet and Lihult Cultures", "CulturalAge", "mesolithic", 6000, 4000, "BCE",
    "Middle-Late Mesolithic in most of southern Norway and Sweden; descendants of Fosna-Hensbacka; polished stone axes.")
add("ertebolleculture", "Ertebølle Culture", "CulturalAge", "mesolithic", 5300, 3950, "BCE",
    "Late Mesolithic in southern Scandinavia; first pottery, large shell middens, transition to agriculture.")
add("neolithic", "Neolithic (New Stone Age)", "CulturalAge", "stone-age", 4000, 2000, "BCE",
    "Agriculture, polished stone tools, pottery, permanent settlements. Funnelbeaker culture in Scandinavia (~4000–2700 BCE).")
add("funnelbeaker", "Funnelbeaker Culture (TRB)", "CulturalAge", "neolithic", 4000, 2700, "BCE",
    "First farming culture in Scandinavia; megalithic tombs (dolmens, passage graves); pottery with funnel-shaped rims.")
add("pitted-ware", "Pitted Ware Culture", "CulturalAge", "neolithic", 3200, 2300, "BCE",
    "Concurrent hunter-gatherer-fisher culture in eastern Sweden, Gotland, and Finland; seal hunting, characteristic pitted pottery.")
add("battle-axe", "Battle Axe Culture (Boat Axe Culture)", "CulturalAge", "neolithic", 2800, 2300, "BCE",
    "Scandinavian variant of Corded Ware culture; single graves, polished stone battle axes, early Indo-European influences.")
add("nordic-neolithic-late", "Late Neolithic Scandinavia", "CulturalAge", "neolithic", 2300, 1750, "BCE",
    "Transition to metalworking; flint daggers imitate bronze; Bell Beaker influences reach Scandinavia.")

# --- Chalcolithic (Copper Age) ---
add("chalcolithic", "Chalcolithic (Copper Age)", "CulturalAge", "holocene", 3500, 2000, "BCE",
    "Transitional period; first metalworking (copper); Ötzi the Iceman; Corded Ware culture in Northern Europe.")

# --- Bronze Age ---
add("bronze-age", "Bronze Age", "CulturalAge", "holocene", 3300, 1200, "BCE",
    "Defined by bronze metallurgy. Near East ~3300 BCE; Nordic Bronze Age begins ~1750 BCE.")
add("early-bronze-age", "Early Bronze Age", "CulturalAge", "bronze-age", 3300, 2000, "BCE",
    "Near East & Mediterranean: urbanization, writing systems, first empires.")
add("middle-bronze-age", "Middle Bronze Age", "CulturalAge", "bronze-age", 2000, 1550, "BCE",
    "Minoan civilization peaks; Nordic Bronze Age begins (~1750 BCE); extensive trade networks.")
add("late-bronze-age", "Late Bronze Age", "CulturalAge", "bronze-age", 1550, 1200, "BCE",
    "Mycenaean Greece; New Kingdom Egypt; Late Bronze Age collapse (~1200 BCE).")
add("nordic-bronze-age", "Nordic Bronze Age", "CulturalAge", "bronze-age", 1750, 500, "BCE",
    "Scandinavian Bronze Age; elaborate burial mounds, rock carvings (hällristningar), sun chariot of Trundholm.")
add("nordic-bronze-early", "Early Nordic Bronze Age (Period I–III)", "CulturalAge", "nordic-bronze-age", 1750, 1100, "BCE",
    "Oak coffin burials (Egtved Girl, Skrydstrup Woman); Trundholm sun chariot; wealth from amber trade.")
add("montelius-i", "Montelius Period I", "CulturalAge", "nordic-bronze-early", 1700, 1500, "BCE",
    "Earliest Nordic Bronze Age; first bronze imports; flint daggers gradually replaced by bronze weapons.")
add("montelius-ii", "Montelius Period II", "CulturalAge", "nordic-bronze-early", 1500, 1300, "BCE",
    "Peak of early bronze wealth; Egtved Girl burial (1370 BCE); elaborate spiral ornaments and fibulae.")
add("montelius-iii", "Montelius Period III", "CulturalAge", "nordic-bronze-early", 1300, 1100, "BCE",
    "Trundholm sun chariot; oak coffin burials; extensive amber trade networks with Mediterranean.")
add("nordic-bronze-late", "Late Nordic Bronze Age (Period IV–VI)", "CulturalAge", "nordic-bronze-age", 1100, 500, "BCE",
    "Cremation replaces inhumation; lur horns; rock carvings peak; declining bronze imports.")
add("montelius-iv", "Montelius Period IV", "CulturalAge", "nordic-bronze-late", 1100, 900, "BCE",
    "Shift from inhumation to cremation; rock carvings (hällristningar) flourish; bronze lur horns crafted.")
add("montelius-v", "Montelius Period V", "CulturalAge", "nordic-bronze-late", 900, 700, "BCE",
    "Elaborate ritual depositions in lakes and bogs; continued rock carving tradition; Hallstatt imports arrive.")
add("montelius-vi", "Montelius Period VI", "CulturalAge", "nordic-bronze-late", 700, 500, "BCE",
    "Final Bronze Age period; Hallstatt iron influence from Central Europe; transition to local iron production.")

# --- Iron Age ---
add("iron-age", "Iron Age", "CulturalAge", "holocene", 1200, 1, "BCE",
    "Defined by iron smelting and tools. Near East ~1200 BCE; Scandinavia ~500 BCE.")
add("pre-roman-iron-age", "Pre-Roman Iron Age", "CulturalAge", "iron-age", 500, 1, "BCE",
    "Iron working spreads to Scandinavia; bog ore smelting; Jastorf culture.")
add("pre-roman-iron-early", "Early Pre-Roman Iron Age", "CulturalAge", "pre-roman-iron-age", 500, 250, "BCE",
    "Transition from bronze; first local iron production from bog ore in southern Scandinavia.")
add("pre-roman-iron-late", "Late Pre-Roman Iron Age", "CulturalAge", "pre-roman-iron-age", 250, 1, "BCE",
    "Celtic La Tène influences; Hjortspring boat (350 BCE); complex hillforts.")

# --- Roman & Migration Period ---
add("roman-iron-age", "Roman Iron Age", "CulturalAge", "holocene", 1, 400, "CE",
    "Roman influence on Germanic societies; runes develop; trade with the Roman Empire.")
add("early-roman-iron", "Early Roman Iron Age", "CulturalAge", "roman-iron-age", 1, 200, "CE",
    "Increasing trade with Roman provinces; imported bronze vessels; first runic inscriptions.")
add("late-roman-iron", "Late Roman Iron Age", "CulturalAge", "roman-iron-age", 200, 400, "CE",
    "Gold solidi flow north; Nydam boat (320 CE); elaborate weapon deposits in bogs.")
add("germanic-iron-age", "Germanic Iron Age", "CulturalAge", "holocene", 400, 790, "CE",
    "Post-Roman period in Scandinavia; divided into Early (Migration Period) and Late (Vendel/Merovingian) by Oscar Montelius.")
add("migration-period", "Migration Period (Völkerwanderung)", "CulturalAge", "germanic-iron-age", 375, 550, "CE",
    "Fall of Western Rome; Germanic peoples migrate across Europe; gold bracteates and collars in Scandinavia.")
add("migration-early", "Early Migration Period", "CulturalAge", "migration-period", 375, 475, "CE",
    "Fall of Western Roman Empire (476); Scandinavian gold hoards peak; elaborate gold collars (e.g. Ålleberg, Möne, Färjestaden).")
add("migration-late", "Late Migration Period", "CulturalAge", "migration-period", 475, 550, "CE",
    "Post-Roman gold scarcity; gilded bronze replaces gold; animal-style ornamentation (Style I) develops.")
add("vendel-period", "Vendel Period (Merovingian Period)", "CulturalAge", "germanic-iron-age", 550, 790, "CE",
    "Swedish golden age; Vendel and Valsgärde boat burials; elaborate animal-style ornamentation.")
add("vendel-early", "Early Vendel Period", "CulturalAge", "vendel-period", 550, 650, "CE",
    "Sutton Hoo parallels; Vendel I–VII boat graves near Uppsala; Style II animal ornamentation.")
add("vendel-late", "Late Vendel Period", "CulturalAge", "vendel-period", 650, 790, "CE",
    "Valsgärde boat burials continue; Style III ornamentation; Birka's proto-urban precursors; transition to Viking Age.")

# --- Viking Age ---
add("viking-age", "Viking Age", "CulturalAge", "holocene", 790, 1100, "CE",
    "Norse expansion, raiding, trading, and settlement; Birka, Hedeby; Christianization of Scandinavia.")
add("early-viking-age", "Early Viking Age", "CulturalAge", "viking-age", 790, 900, "CE",
    "Raid on Lindisfarne (793); establishment of Norse trading centers; Oseberg ship burial.")
add("middle-viking-age", "Middle Viking Age", "CulturalAge", "viking-age", 900, 1000, "CE",
    "Danelaw in England; Normandy settled; Icelandic settlement; Bluetooth's Denmark.")
add("late-viking-age", "Late Viking Age", "CulturalAge", "viking-age", 1000, 1100, "CE",
    "Christianization; end of Norse paganism; Cnut the Great's North Sea Empire.")

# --- Medieval Period ---
add("medieval-period", "Medieval Period", "CulturalAge", "holocene", 1050, 1520, "CE",
    "Scandinavian medieval period; Christianity dominant; Hanseatic trade; Gothic cathedrals; Black Death (1349).")
add("early-medieval", "Early Medieval Period", "CulturalAge", "medieval-period", 1050, 1200, "CE",
    "Church consolidation; first Scandinavian dioceses; Romanesque architecture.")
add("high-medieval", "High Medieval Period", "CulturalAge", "medieval-period", 1200, 1350, "CE",
    "Hanseatic League; Gothic architecture; Kalmar Union precursors; population growth.")
add("late-medieval", "Late Medieval Period", "CulturalAge", "medieval-period", 1350, 1520, "CE",
    "Black Death aftermath; Kalmar Union (1397); Reformation approaches.")

# --- Early Modern ---
add("early-modern", "Early Modern Period", "CulturalAge", "holocene", 1520, 1789, "CE",
    "Reformation; Vasa dynasty; Swedish Empire (stormaktstiden); Age of Enlightenment.")
add("early-vasa-era", "Early Vasa Era (Äldre Vasatiden)", "CulturalAge", "early-modern", 1523, 1611, "CE",
    "Gustav Vasa breaks from Kalmar Union; Protestant Reformation; hereditary monarchy established; Stockholm Bloodbath aftermath.")
add("reformation-era", "Reformation Era", "CulturalAge", "early-vasa-era", 1527, 1600, "CE",
    "Protestant Reformation in Sweden (1527) and Denmark-Norway (1536); seizure of Catholic Church property; new church ordinances.")
add("swedish-empire", "Swedish Empire (Stormaktstiden)", "CulturalAge", "early-modern", 1611, 1721, "CE",
    "Sweden as great power; Thirty Years War; Baltic dominance; ends with Great Northern War.")
add("thirty-years-war", "Thirty Years' War Period", "CulturalAge", "swedish-empire", 1618, 1648, "CE",
    "Sweden enters as Protestant champion under Gustav II Adolf; Battle of Breitenfeld (1631); Peace of Westphalia (1648).")
add("caroline-era", "Caroline Era (Karolinska tiden)", "CulturalAge", "swedish-empire", 1654, 1718, "CE",
    "Absolute monarchy under Charles X, XI, XII; reduktion land reforms; Great Northern War ends Swedish empire.")
add("age-of-liberty", "Age of Liberty (Frihetstiden)", "CulturalAge", "early-modern", 1718, 1772, "CE",
    "Parliamentary rule after Charles XII; Hat and Cap party factions; Enlightenment science (Linnaeus, Celsius).")
add("gustavian-era", "Gustavian Era (Gustavianska tiden)", "CulturalAge", "early-modern", 1772, 1809, "CE",
    "Gustav III's coup restores royal power; patron of arts; Royal Opera and Royal Dramatic Theatre founded; assassinated 1792.")

# --- Modern Period ---
add("modern-period", "Modern Period", "CulturalAge", "holocene", 1789, 0, "CE",
    "French Revolution to present; industrialization, nation-states, globalization.")
add("bernadotte-era", "Bernadotte Era / Union Period", "CulturalAge", "modern-period", 1809, 1905, "CE",
    "New constitution (1809); French Marshal Bernadotte becomes Crown Prince (1810); Sweden-Norway union (1814–1905); loss of Finland to Russia.")
add("industrial-age", "Industrial Age (Industrialiseringen)", "CulturalAge", "modern-period", 1850, 1914, "CE",
    "Railways from 1850s; mass emigration to Americas (~1.3M Swedes); Alfred Nobel; rapid urbanization.")
add("contemporary", "Contemporary Period", "CulturalAge", "modern-period", 1914, 0, "CE",
    "World Wars (neutral), welfare states (folkhemmet), digital revolution; Scandinavian social democracies.")

# ═══════════════════════════════════════════════════════════════
# BROADER EUROPEAN HISTORICAL PERIODS
# ═══════════════════════════════════════════════════════════════

# --- Classical Antiquity ---
add("archaic-greece", "Archaic Greece", "CulturalAge", "holocene", 800, 480, "BCE",
    "Rise of city-states (poleis); Greek colonization; development of the alphabet, Homer's epics, early philosophy.")
add("classical-greece", "Classical Greece", "CulturalAge", "holocene", 480, 323, "BCE",
    "Golden Age of Athens; Parthenon; Socrates, Plato, Aristotle; Athenian democracy; Peloponnesian War.")
add("hellenistic-period", "Hellenistic Period", "CulturalAge", "holocene", 323, 31, "BCE",
    "Alexander the Great's empire fragments; spread of Greek culture across Mediterranean and Near East; Library of Alexandria.")
add("roman-republic", "Roman Republic", "CulturalAge", "holocene", 509, 27, "BCE",
    "Roman expansion across Mediterranean; Punic Wars; Julius Caesar; transition to Empire.")
add("roman-empire", "Roman Empire", "CulturalAge", "holocene", 27, 476, "CE",
    "Pax Romana; peak Roman civilization; roads, aqueducts, law; Christianity becomes state religion (380 CE).")
add("late-antiquity", "Late Antiquity", "CulturalAge", "holocene", 250, 750, "CE",
    "Transition from classical to medieval; fall of Western Rome (476); rise of Christianity; Byzantine Empire continues in East.")

# --- European Middle Ages (continental) ---
add("european-early-medieval", "Early Middle Ages (Europe)", "CulturalAge", "holocene", 500, 1000, "CE",
    "Dark Ages; Merovingian and Carolingian kingdoms; spread of Christianity; feudalism develops.")
add("merovingian-period", "Merovingian Period (Frankish)", "CulturalAge", "european-early-medieval", 481, 751, "CE",
    "Merovingian dynasty rules Frankish kingdoms; Clovis I converts to Christianity; foundation of medieval France.")
add("carolingian-period", "Carolingian Period", "CulturalAge", "european-early-medieval", 751, 888, "CE",
    "Charlemagne crowned Emperor (800); Carolingian Renaissance; revival of learning, Latin scholarship, and arts.")
add("ottonian-period", "Ottonian Period", "CulturalAge", "european-early-medieval", 919, 1024, "CE",
    "Holy Roman Empire under Otto I; Ottonian Renaissance; expansion of Christianity into central Europe.")
add("european-high-medieval", "High Middle Ages (Europe)", "CulturalAge", "holocene", 1000, 1300, "CE",
    "Crusades; Gothic cathedrals; universities founded (Bologna, Paris, Oxford); population growth; Magna Carta (1215).")
add("crusades-period", "Crusades Period", "CulturalAge", "european-high-medieval", 1095, 1291, "CE",
    "Series of religious wars for control of the Holy Land; First Crusade captures Jerusalem (1099); cultural exchange between East and West.")
add("twelfth-century-renaissance", "Renaissance of the 12th Century", "CulturalAge", "european-high-medieval", 1100, 1200, "CE",
    "Revival of learning; translations of Greek and Arabic texts; founding of universities; scholasticism; Gothic architecture begins.")
add("european-late-medieval", "Late Middle Ages (Europe)", "CulturalAge", "holocene", 1300, 1500, "CE",
    "Black Death (1347-1351); Hundred Years' War; Great Western Schism; decline of feudalism; printing press (1440).")

# --- Renaissance & Early Modern Europe ---
add("renaissance", "Renaissance", "CulturalAge", "holocene", 1350, 1600, "CE",
    "Revival of classical learning and art; began in Italy (Florence); humanism, perspective painting, scientific inquiry; Michelangelo, Leonardo, Raphael.")
add("italian-renaissance", "Italian Renaissance", "CulturalAge", "renaissance", 1350, 1550, "CE",
    "Florence, Venice, Rome as cultural centers; Medici patronage; Brunelleschi, Botticelli, Machiavelli, da Vinci.")
add("northern-renaissance", "Northern Renaissance", "CulturalAge", "renaissance", 1450, 1600, "CE",
    "Renaissance spreads north of Alps; Dürer, Erasmus, van Eyck; printing revolution; Protestant Reformation begins.")
add("age-of-exploration", "Age of Exploration", "CulturalAge", "holocene", 1415, 1600, "CE",
    "European maritime exploration; Columbus (1492), Vasco da Gama (1498), Magellan (1519); colonial empires begin.")
add("european-reformation", "European Reformation", "CulturalAge", "holocene", 1517, 1648, "CE",
    "Luther's 95 Theses (1517); Protestant churches emerge; Counter-Reformation; Wars of Religion; Peace of Westphalia (1648).")
add("baroque-period", "Baroque Period", "CulturalAge", "holocene", 1600, 1750, "CE",
    "Dramatic, ornate art and architecture; Bernini, Caravaggio, Rubens, Bach, Vivaldi; absolutist monarchies.")
add("enlightenment", "Age of Enlightenment", "CulturalAge", "holocene", 1685, 1815, "CE",
    "Reason, science, individual rights; Voltaire, Rousseau, Kant, Locke; influence on American and French Revolutions.")
add("age-of-revolutions", "Age of Revolutions", "CulturalAge", "modern-period", 1775, 1848, "CE",
    "American Revolution (1775), French Revolution (1789), Napoleonic Wars, Revolutions of 1848; end of ancien régime.")
add("romanticism", "Romantic Period", "CulturalAge", "modern-period", 1790, 1850, "CE",
    "Reaction against Enlightenment rationalism; emphasis on emotion, nature, nationalism; Goethe, Byron, Beethoven, Delacroix.")
add("world-wars-era", "World Wars Era", "CulturalAge", "contemporary", 1914, 1945, "CE",
    "Two global conflicts and an interwar period that reshaped Europe; tens of millions killed; colonial empires begin to dissolve.")
add("world-war-i", "World War I", "CulturalAge", "world-wars-era", 1914, 1918, "CE",
    "The Great War; trench warfare; fall of empires (Ottoman, Austro-Hungarian, Russian, German); Treaty of Versailles (1919).")
add("interwar-period", "Interwar Period", "CulturalAge", "world-wars-era", 1918, 1939, "CE",
    "League of Nations; Weimar Republic; Great Depression (1929); rise of fascism in Italy, Germany, Spain; Spanish Civil War.")
add("world-war-ii", "World War II", "CulturalAge", "world-wars-era", 1939, 1945, "CE",
    "Global conflict; Nazi Germany, Holocaust; Allied victory; atomic bombs; United Nations founded (1945); Europe devastated.")
add("cold-war-era", "Cold War Era", "CulturalAge", "contemporary", 1947, 1991, "CE",
    "East-West division; NATO vs Warsaw Pact; Iron Curtain; Berlin Wall (1961-1989); European integration begins (EEC 1957).")
add("european-integration", "European Integration", "CulturalAge", "contemporary", 1957, 0, "CE",
    "Treaty of Rome (1957); EEC to EU; Schengen Area; Euro currency; expansion from 6 to 27+ member states.")

# ═══════════════════════════════════════════════════════════════
# MAJOR MASS EXTINCTION EVENTS (cross-cutting markers)
# ═══════════════════════════════════════════════════════════════
add("end-ordovician-extinction", "End-Ordovician Extinction", "Age", "late-ordovician", 445, 443, "Ma",
    "First of the Big Five; ~85% of marine species lost; caused by Gondwanan glaciation and sea-level fall.")
add("late-devonian-extinction", "Late Devonian Extinction", "Age", "late-devonian", 375, 359, "Ma",
    "Second of the Big Five; ~75% of species lost over millions of years; reef ecosystems collapse.")
add("permian-triassic-extinction", "Permian–Triassic Extinction (The Great Dying)", "Age", "lopingian", 252, 251, "Ma",
    "Worst mass extinction: ~96% of marine and ~70% of land species; Siberian Traps volcanism.")
add("triassic-jurassic-extinction", "Triassic–Jurassic Extinction", "Age", "late-triassic", 201.5, 201.3, "Ma",
    "Fourth of the Big Five; ~80% of species lost; CAMP volcanism; opens way for dinosaur dominance.")
add("cretaceous-paleogene-extinction", "Cretaceous–Paleogene Extinction (K-Pg)", "Age", "late-cretaceous", 66.05, 66, "Ma",
    "Fifth of the Big Five; Chicxulub asteroid impact; all non-avian dinosaurs extinct; ~76% of species lost.")

# ═══════════════════════════════════════════════════════════════
# ADDITIONAL GEOLOGICAL / CLIMATE EVENTS
# ═══════════════════════════════════════════════════════════════
add("great-oxidation", "Great Oxidation Event", "Age", "rhyacian", 2400, 2060, "Ma",
    "Free oxygen accumulates in atmosphere for first time; mass die-off of anaerobic organisms; banded iron formations cease.")
add("huronian-glaciation", "Huronian Glaciation", "Age", "rhyacian", 2400, 2100, "Ma",
    "First known Snowball Earth event; possibly triggered by Great Oxidation Event reducing methane greenhouse.")
add("petm", "Paleocene–Eocene Thermal Maximum (PETM)", "Age", "ypresian", 55.8, 55.6, "Ma",
    "Rapid global warming of 5–8 °C; massive carbon release; mammals disperse across continents.")
add("messinian-crisis", "Messinian Salinity Crisis", "Age", "messinian", 5.96, 5.33, "Ma",
    "Mediterranean Sea nearly dries up due to tectonic closure of Strait of Gibraltar; massive evaporite deposits.")
add("last-glacial-max", "Last Glacial Maximum", "Age", "late-pleistocene", 0.026, 0.019, "Ma",
    "Peak of last ice age ~26,000 years ago; ice sheets cover Scandinavia, Britain, northern Europe; sea level ~120 m lower.")
add("younger-dryas", "Younger Dryas", "Age", "greenlandian", 12900, 11700, "BP",
    "Abrupt return to glacial conditions for ~1,200 years; end marks start of Holocene; cause debated (meltwater pulse?).")
add("8.2ka-event", "8.2 ka Cold Event", "Age", "northgrippian", 8200, 8000, "BP",
    "Sudden cooling for ~150 years; collapse of Laurentide ice sheet drains glacial lakes into Atlantic; disrupts thermohaline circulation.")
add("4.2ka-event", "4.2 ka Aridification Event", "Age", "meghalayan", 4200, 3900, "BP",
    "Severe drought lasting ~200 years; contributes to collapse of Akkadian Empire, Old Kingdom Egypt, Harappan civilization.")

# ═══════════════════════════════════════════════════════════════
# ADDITIONAL CULTURAL PERIODS (Sámi, Baltic, Finnish)
# ═══════════════════════════════════════════════════════════════
add("sami-prehistory", "Sámi Prehistory", "CulturalAge", "holocene", 8000, 1600, "CE",
    "Indigenous Sámi settlement of northern Fennoscandia; reindeer herding develops; Komsa and Fosna cultures; sieiddit (sacred sites).")
add("comb-ceramic", "Comb Ceramic Culture", "CulturalAge", "neolithic", 3900, 2800, "BCE",
    "Widespread Neolithic culture across Finland and the Baltic; characteristic comb-stamped pottery; hunter-gatherer-fishers.")
add("asbestos-ceramic", "Asbestos Ceramic Period (Finland)", "CulturalAge", "neolithic", 3500, 2000, "BCE",
    "Distinctive Finnish Neolithic pottery tempered with asbestos fibers; concurrent with Comb Ceramic in eastern Finland.")
add("nordic-iron-age-celtic", "Celtic Iron Age Influences in Scandinavia", "CulturalAge", "pre-roman-iron-age", 400, 200, "BCE",
    "La Tène art style reaches Scandinavia; Hjortspring boat; early hillforts in southern Sweden and Denmark.")
add("jastorf-culture", "Jastorf Culture", "CulturalAge", "pre-roman-iron-age", 500, 100, "BCE",
    "Pre-Roman Iron Age culture of northern Germany and southern Scandinavia; first iron smelting from bog ore; cremation burials.")

# --- Viking Age sub-events ---
add("danelaw", "Danelaw Period", "CulturalAge", "middle-viking-age", 865, 954, "CE",
    "Norse-controlled territory in eastern and northern England; established after the Great Heathen Army; York as Viking capital.")
add("viking-iceland", "Settlement of Iceland", "CulturalAge", "middle-viking-age", 870, 930, "CE",
    "Norse colonization of Iceland; Ingólfr Arnarson (874); Althing established 930 as one of the oldest parliaments.")
add("viking-normandy", "Norse Settlement of Normandy", "CulturalAge", "middle-viking-age", 911, 1066, "CE",
    "Rollo receives Normandy from French king (911); Norse settlers adopt French language; William the Conqueror descends from Vikings.")
add("viking-rus", "Varangians and Kievan Rus'", "CulturalAge", "viking-age", 800, 1054, "CE",
    "Swedish Vikings (Varangians) establish trade routes through Russia; found Kyiv and Novgorod; Varangian Guard in Constantinople.")

# --- Medieval & Hanseatic ---
add("christianization-scandinavia", "Christianization of Scandinavia", "CulturalAge", "early-medieval", 960, 1150, "CE",
    "Gradual conversion: Denmark (~960, Harald Bluetooth), Norway (~1000, Olaf Tryggvason), Sweden (~1000, Olof Skötkonung); Uppsala temple destroyed ~1087.")
add("baltic-crusades", "Baltic Crusades Period", "CulturalAge", "medieval-period", 1147, 1290, "CE",
    "Northern Crusades; Christianization of Baltic region; Teutonic Order; Swedish crusades to Finland.")
add("hanseatic-period", "Hanseatic Period in Scandinavia", "CulturalAge", "medieval-period", 1250, 1450, "CE",
    "Hanseatic League dominates Baltic trade; German merchants in Visby, Bergen, Stockholm; Lübeck law adopted.")
add("black-death-scandinavia", "Black Death in Scandinavia", "CulturalAge", "late-medieval", 1349, 1360, "CE",
    "Plague reaches Norway (1349), Sweden and Denmark; kills ~50-60% of Scandinavian population; abandoned farms (ödegårdar).")
add("kalmar-union", "Kalmar Union", "CulturalAge", "late-medieval", 1397, 1523, "CE",
    "Union of Denmark, Norway, and Sweden under one monarch; Queen Margrete I; dissolved by Gustav Vasa's rebellion.")
add("stockholm-bloodbath", "Stockholm Bloodbath", "CulturalAge", "late-medieval", 1520, 1521, "CE",
    "Danish King Christian II executes ~80 Swedish nobles and clergy; triggers Gustav Vasa's rebellion and end of Kalmar Union.")

# --- Danish / Norwegian specific ---
add("danish-golden-age", "Danish Golden Age", "CulturalAge", "modern-period", 1800, 1850, "CE",
    "Cultural flourishing in Denmark: H.C. Andersen, Søren Kierkegaard, Bertel Thorvaldsen, C.W. Eckersberg; national romanticism.")
add("norway-independence", "Norwegian Independence", "CulturalAge", "modern-period", 1814, 1905, "CE",
    "Norwegian constitution (1814, Eidsvoll); forced union with Sweden; dissolution of union (1905); Haakon VII elected king.")
add("finland-grand-duchy", "Grand Duchy of Finland", "CulturalAge", "modern-period", 1809, 1917, "CE",
    "Finland as autonomous Grand Duchy of Russia after Swedish loss (1809); Kalevala published (1835); Finnish nationalism; independence 1917.")
add("eocene-oligocene-extinction", "Eocene–Oligocene Extinction (Grande Coupure)", "Age", "priabonian", 33.9, 33.7, "Ma",
    "Major faunal turnover in Europe; Asian mammals invade; dramatic cooling as Antarctic ice sheet forms.")
add("cambrian-explosion", "Cambrian Explosion", "Age", "epoch2-cambrian", 538.8, 510, "Ma",
    "Most major animal phyla appear in fossil record within ~25 Myr; Burgess Shale, Chengjiang faunas; cause debated.")

print(f"Total data points: {n[0]}")

# ═══════════════════════════════════════════════════════════════
# Generate Turtle
# ═══════════════════════════════════════════════════════════════

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
lines.append(f"# {len(DATA)} data points: eons, eras, periods, epochs, ages,")
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
lines.append(f"# Total entries: {n[0]}")
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
lines.append(f'    dcterms:description "250 entries covering the geologic time scale from Hadean eon (4600 Ma) to Early Modern period, including archaeological/cultural ages (Stone Age, Bronze Age, Iron Age, Viking Age, Medieval)."@en ;')
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

for d in DATA:
    cls = RANK_TO_CLASS.get(d["rank"], "gts:GeochronologicAge")
    lines.append(f"# ── {d['n']}/{n[0]}: {d['label']} ({d['rank']}) ──")
    lines.append(f"ts:{d['id']} a {cls} ;")
    lines.append(f'    rdfs:label "{escape(d["label"])}"@en ;')
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
    elif unit == "CE":
        lines.append(f'    time:hasBeginning [ rdfs:label "{start} CE" ] ;')
        if end == 0:
            lines.append(f'    time:hasEnd [ rdfs:label "Present" ] ;')
        else:
            lines.append(f'    time:hasEnd [ rdfs:label "{end} CE" ] ;')

    lines.append(f'    dcterms:source <https://en.wikipedia.org/wiki/Geologic_time_scale> .')
    lines.append("")

with open("/home/user/metadatahub/hugo/static/data/geologic-timescale.ttl", "w") as f:
    f.write("\n".join(lines))

# ═══════════════════════════════════════════════════════════════
# Generate JSON-LD
# ═══════════════════════════════════════════════════════════════

jsonld_items = []
for d in DATA:
    cls = RANK_TO_CLASS.get(d["rank"], "gts:GeochronologicAge")
    unit = d["unit"]
    item = {
        "@id": f"{BASE}/{d['id']}",
        "@type": cls,
        "rdfs:label": {"@value": d["label"], "@language": "en"},
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
    "dcterms:description": "250 entries covering the geologic time scale from Hadean eon (4600 Ma) to Early Modern period, including archaeological/cultural ages.",
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

with open("/home/user/metadatahub/hugo/static/data/geologic-timescale.jsonld", "w") as f:
    json.dump(jsonld_doc, f, indent=2, ensure_ascii=False)

print(f"  Turtle: hugo/static/data/geologic-timescale.ttl ({len(lines)} lines)")
print(f"  JSON-LD: hugo/static/data/geologic-timescale.jsonld ({len(jsonld_items)} items)")
