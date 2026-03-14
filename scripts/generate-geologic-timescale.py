#!/usr/bin/env python3
"""Generate the Geologic Time Scale as Linked Data (Turtle + JSON-LD).

852 data points covering:
- 4 Eons
- 10 Eras
- 22 Periods (incl. Mississippian/Pennsylvanian sub-periods)
- 38 Epochs
- ~90 Ages/Stages (Mesozoic + Cenozoic + Pleistocene + Holocene + geologic events)
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
add("hadean", "Hadean (Ἅιδης)", "Eon", None, 4567, 4031, "Ma",
    "Earliest eon; Earth forms from accretion, heavy bombardment, formation of the Moon.")

# Hadean informal divisions (proposed by Goldblatt et al. 2010; GTS 2012; not ratified by ICS)
add("chaotian", "Chaotian (informal / Χάος Cháos)", "Era", "hadean", 4567, 4404, "Ma",
    "Accretion and differentiation of Earth; Moon-forming giant impact (Theia hypothesis, ~4510 Ma); surface entirely molten magma ocean.")
add("zirconian", "Zirconian (informal / Zirkon, زرگون zargun)", "Era", "hadean", 4404, 4031, "Ma",
    "Oldest known mineral grains (Jack Hills zircons, ~4.4 Ga); first solid crust forms; Late Heavy Bombardment.")
add("late-heavy-bombardment", "Late Heavy Bombardment (LHB / Ἅιδης)", "Age", "hadean", 4100, 3800, "Ma",
    "Proposed period of intense asteroid and comet impacts on inner Solar System; evidence from lunar craters and Apollo samples; shaped early Earth crust; timing and intensity debated (Nice model).")

add("archean", "Archean (Ἀρχαῖος)", "Eon", None, 4031, 2500, "Ma",
    "First stable continents form; earliest evidence of life (stromatolites).")
add("proterozoic", "Proterozoic (Πρότερος ζωή)", "Eon", None, 2500, 538.8, "Ma",
    "Oxygen accumulates in atmosphere; first eukaryotes and multicellular life.")
add("phanerozoic", "Phanerozoic (Φανερός ζωή)", "Eon", None, 538.8, 0, "Ma",
    "Eon of visible life; all complex animal phyla appear and diversify.")

# ═══════════════════════════════════════════════════════════════
# ARCHEAN ERAS
# ═══════════════════════════════════════════════════════════════
add("eoarchean", "Eoarchean (Ἠώς ἀρχαῖος)", "Era", "archean", 4031, 3600, "Ma",
    "Oldest known rocks; possible earliest life.")
add("paleoarchean", "Paleoarchean (Παλαιός ἀρχαῖος)", "Era", "archean", 3600, 3200, "Ma",
    "Earliest confirmed microbial life; oldest stromatolites.")
add("mesoarchean", "Mesoarchean (Μέσος ἀρχαῖος)", "Era", "archean", 3200, 2800, "Ma",
    "First large-scale stromatolite reefs; earliest photosynthesis evidence.")
add("neoarchean", "Neoarchean (Νέος ἀρχαῖος)", "Era", "archean", 2800, 2500, "Ma",
    "Oxygen-producing cyanobacteria proliferate; banded iron formations peak.")

# ═══════════════════════════════════════════════════════════════
# PROTEROZOIC ERAS & PERIODS
# ═══════════════════════════════════════════════════════════════
add("paleoproterozoic", "Paleoproterozoic (Παλαιός πρότερος)", "Era", "proterozoic", 2500, 1600, "Ma",
    "Great Oxidation Event; first supercontinent (Nuna/Columbia).")
add("siderian", "Siderian (σίδηρος)", "Period", "paleoproterozoic", 2500, 2300, "Ma",
    "Banded iron formations dominate; oxygen levels still rising.")
add("rhyacian", "Rhyacian (ῥύαξ)", "Period", "paleoproterozoic", 2300, 2050, "Ma",
    "Huronian glaciation; first global ice age.")
add("orosirian", "Orosirian (ὀροσειρά)", "Period", "paleoproterozoic", 2050, 1800, "Ma",
    "Major mountain-building events; Vredefort and Sudbury impacts.")
add("statherian", "Statherian (σταθερός)", "Period", "paleoproterozoic", 1800, 1600, "Ma",
    "First complex single-celled organisms with nuclei.")

add("mesoproterozoic", "Mesoproterozoic (Μέσος πρότερος)", "Era", "proterozoic", 1600, 1000, "Ma",
    "Supercontinent Rodinia assembles; first sexual reproduction evidence.")
add("calymmian", "Calymmian (κάλυμμα)", "Period", "mesoproterozoic", 1600, 1400, "Ma",
    "Platform covers expand; stable continental interiors.")
add("ectasian", "Ectasian (ἔκτασις)", "Period", "mesoproterozoic", 1400, 1200, "Ma",
    "Continued platform expansion; green algae diversify.")
add("stenian", "Stenian (στενός)", "Period", "mesoproterozoic", 1200, 1000, "Ma",
    "Grenville orogeny; supercontinent Rodinia forms.")

add("neoproterozoic", "Neoproterozoic (Νέος πρότερος)", "Era", "proterozoic", 1000, 538.8, "Ma",
    "Snowball Earth glaciations; first animals appear (Ediacaran biota).")
add("tonian", "Tonian (τόνος)", "Period", "neoproterozoic", 1000, 720, "Ma",
    "Rodinia begins to break apart; first multicellular organisms.")
add("cryogenian", "Cryogenian (κρύος γένεσις)", "Period", "neoproterozoic", 720, 635, "Ma",
    "Snowball Earth glaciations: Sturtian and Marinoan; life survives in refugia.")
add("sturtian", "Sturtian Glaciation (Sturt River, South Australia)", "Age", "cryogenian", 717, 660, "Ma",
    "First and longer Snowball Earth event; global ice cover for ~57 million years.")
add("marinoan", "Marinoan Glaciation (Marino, South Australia)", "Age", "cryogenian", 639, 635, "Ma",
    "Second Snowball Earth; onset ~639 Ma per U-Pb geochronology; cap carbonates deposited after deglaciation.")
add("ediacaran", "Ediacaran (Idiyakra / Yata Takarra)", "Period", "neoproterozoic", 635, 538.8, "Ma",
    "Ediacaran biota: first large complex organisms; soft-bodied fauna. Named for Ediacara Creek, Flinders Ranges, South Australia, on traditional Adnyamathanha lands; Adnyamathanha name disputed: 'Idiyakra' (place near water, oldest recorded form) or 'Yata Takarra' (hard/stony ground); 2023 Nilpena Ediacara National Park formalizes Adnyamathanha custodianship.")
add("gaskiers", "Gaskiers Glaciation (Gaskiers, Terre-Neuve)", "Age", "ediacaran", 580.9, 579.6, "Ma",
    "Last major Neoproterozoic glaciation; short-lived (~1.3 Myr); followed by deep ocean oxygenation enabling rise of Ediacaran fauna.")

# ═══════════════════════════════════════════════════════════════
# PHANEROZOIC — PALEOZOIC ERA & PERIODS
# ═══════════════════════════════════════════════════════════════
add("paleozoic", "Paleozoic (Παλαιός ζωή)", "Era", "phanerozoic", 538.8, 251.9, "Ma",
    "Era of ancient life; Cambrian explosion, first fish, amphibians, reptiles, forests.")

add("cambrian", "Cambrian (Cymru)", "Period", "paleozoic", 538.8, 485.4, "Ma",
    "Cambrian explosion: most major animal phyla appear rapidly in the fossil record.")
add("terreneuvian", "Terreneuvian (Terre-Neuve)", "Epoch", "cambrian", 538.8, 521, "Ma",
    "Earliest Cambrian epoch; small shelly fossils appear.")
add("fortunian", "Fortunian (Fortune Head)", "Age", "terreneuvian", 538.8, 529, "Ma",
    "Earliest Cambrian age; first trace fossils of bilaterian animals.")
add("stage2-cambrian", "Cambrian Stage 2 (unnamed)", "Age", "terreneuvian", 529, 521, "Ma",
    "Small shelly fauna diversify; archaeocyathids appear.")
add("epoch2-cambrian", "Cambrian Series 2 (unnamed)", "Epoch", "cambrian", 521, 509, "Ma",
    "Trilobites diversify; archaeocyathid reefs.")
add("stage3-cambrian", "Cambrian Stage 3 (unnamed)", "Age", "epoch2-cambrian", 521, 514, "Ma",
    "First trilobites appear; Cambrian explosion accelerates.")
add("stage4-cambrian", "Cambrian Stage 4 (unnamed)", "Age", "epoch2-cambrian", 514, 509, "Ma",
    "Archaeocyathid reef-builders peak then decline.")
add("miaolingian", "Miaolingian (苗岭)", "Epoch", "cambrian", 509, 497, "Ma",
    "Peak trilobite diversity; Burgess Shale-type faunas.")
add("wuliuan", "Wuliuan (乌溜)", "Age", "miaolingian", 509, 504.5, "Ma",
    "Burgess Shale fauna; diverse arthropods and anomalocaridids.")
add("drumian", "Drumian (Drum Mountains)", "Age", "miaolingian", 504.5, 500.5, "Ma",
    "Agnostid trilobites flourish; deep-water faunas diversify.")
add("guzhangian", "Guzhangian (古丈)", "Age", "miaolingian", 500.5, 497, "Ma",
    "Trilobite turnover; transition toward Furongian faunas.")
add("furongian", "Furongian (芙蓉)", "Epoch", "cambrian", 497, 485.4, "Ma",
    "Trilobite extinctions; first cephalopods appear.")
add("paibian", "Paibian (排碧)", "Age", "furongian", 497, 494.2, "Ma",
    "SPICE carbon isotope excursion; trilobite extinction pulse.")
add("jiangshanian", "Jiangshanian (江山)", "Age", "furongian", 494.2, 491, "Ma",
    "Trilobite recovery; earliest cephalopods diversify.")
add("stage10-cambrian", "Cambrian Stage 10 (unnamed)", "Age", "furongian", 491, 485.4, "Ma",
    "Final Cambrian stage; transition to Ordovician biodiversification.")

add("ordovician", "Ordovician (Ordowices)", "Period", "paleozoic", 485.4, 443.8, "Ma",
    "Great Ordovician Biodiversification Event; first land plants; ends with mass extinction.")
add("early-ordovician", "Early Ordovician (Ordowices)", "Epoch", "ordovician", 485.4, 470.0, "Ma",
    "Biodiversification begins; graptolites and brachiopods flourish.")
add("tremadocian", "Tremadocian (Tremadog)", "Age", "early-ordovician", 485.4, 477.7, "Ma",
    "Conodonts and graptolites diversify; first planktonic ecosystems.")
add("floian", "Floian (Flo, Västergötland; GSSP at Hunneberg)", "Age", "early-ordovician", 477.7, 470.0, "Ma",
    "First bryozoans; corals begin to diversify.")
add("middle-ordovician", "Middle Ordovician (Ordowices)", "Epoch", "ordovician", 470.0, 458.4, "Ma",
    "Great Ordovician Biodiversification Event peaks.")
add("dapingian", "Dapingian (大坪)", "Age", "middle-ordovician", 470.0, 469.4, "Ma",
    "GOBE intensifies; cephalopods diversify as top marine predators.")
add("darriwilian", "Darriwilian (Darriwil)", "Age", "middle-ordovician", 469.4, 458.4, "Ma",
    "Peak of Great Ordovician Biodiversification; stromatoporoid reefs.")
add("late-ordovician", "Late Ordovician (Ordowices)", "Epoch", "ordovician", 458.4, 443.8, "Ma",
    "End-Ordovician glaciation and mass extinction; ~85% of marine species lost.")
add("sandbian", "Sandbian (Södra Sandby, Skåne)", "Age", "late-ordovician", 458.4, 453.0, "Ma",
    "Taconic orogeny; diverse brachiopod communities; GSSP at Fågelsång, east of Lund.")
add("katian", "Katian (Katy, Oklahoma)", "Age", "late-ordovician", 453.0, 445.2, "Ma",
    "Peak marine diversity; Gondwanan glaciation begins.")
add("hirnantian", "Hirnantian (Cwm Hirnant)", "Age", "late-ordovician", 445.2, 443.8, "Ma",
    "End-Ordovician mass extinction; rapid glaciation and sea level drop.")

add("silurian", "Silurian (Silures)", "Period", "paleozoic", 443.8, 419.2, "Ma",
    "Recovery from extinction; first vascular land plants; jawed fish appear.")
add("llandovery", "Llandovery (Llanymddyfri)", "Epoch", "silurian", 443.8, 433.4, "Ma",
    "Post-extinction recovery; graptolite diversification.")
add("rhuddanian", "Rhuddanian (Cefn-cerig Rhuddan)", "Age", "llandovery", 443.8, 440.8, "Ma",
    "Earliest Silurian; rapid recovery of graptolite faunas.")
add("aeronian", "Aeronian (Cwm-coed-Aeron)", "Age", "llandovery", 440.8, 438.5, "Ma",
    "Continued recovery; first land plant spores.")
add("telychian", "Telychian (Pen-lan-Telechi)", "Age", "llandovery", 438.5, 433.4, "Ma",
    "Graptolite diversity peak; first vascular plant fossils.")
add("wenlock", "Wenlock (Much Wenlock)", "Epoch", "silurian", 433.4, 427.4, "Ma",
    "First land plants with vascular tissue; coral reef expansion.")
add("sheinwoodian", "Sheinwoodian (Sheinton Brook)", "Age", "wenlock", 433.4, 430.5, "Ma",
    "Ireviken extinction event; reef ecosystems expand.")
add("homerian", "Homerian (Homer, Shropshire)", "Age", "wenlock", 430.5, 427.4, "Ma",
    "Mulde extinction event; eurypterids (sea scorpions) diversify.")
add("ludlow", "Ludlow (Ludlow, Shropshire)", "Epoch", "silurian", 427.4, 423.0, "Ma",
    "First terrestrial arachnids; brachiopod diversity peak.")
add("gorstian", "Gorstian (Gorst, Shropshire)", "Age", "ludlow", 427.4, 425.6, "Ma",
    "Lau extinction event; graptolite fauna turnover.")
add("ludfordian", "Ludfordian (Ludford, Shropshire)", "Age", "ludlow", 425.6, 423.0, "Ma",
    "First terrestrial arthropod traces; jawed fish diversify.")
add("pridoli", "Přídolí (Přídolí, Česko)", "Epoch", "silurian", 423.0, 419.2, "Ma",
    "First jawed fish diversify; transition toward Devonian.")

add("devonian", "Devonian (Devon)", "Period", "paleozoic", 419.2, 358.9, "Ma",
    "Age of Fishes; first forests, first insects, first amphibians.")
add("klonk-event", "Klonk GSSP (Silurian–Devonian boundary / Klonk, Česko)", "Age", "pridoli", 419.2, 419.2, "Ma",
    "First GSSP ever ratified (1972); Klonk, Czech Republic; defined by first appearance of graptolite Monograptus uniformis; marks base of Devonian.")
add("early-devonian", "Early Devonian (Devon)", "Epoch", "devonian", 419.2, 393.3, "Ma",
    "First seed plants; armored fish diversify.")
add("lochkovian", "Lochkovian (Lochkov, Praha)", "Age", "early-devonian", 419.2, 410.8, "Ma",
    "Earliest Devonian; jawed fish radiation continues.")
add("pragian", "Pragian (Praha)", "Age", "early-devonian", 410.8, 407.6, "Ma",
    "First true leaves (lycopsids); early vascular plants spread onto land.")
add("emsian", "Emsian (Bad Ems)", "Age", "early-devonian", 407.6, 393.3, "Ma",
    "First insects; ammonoids appear; widespread reef systems.")
add("middle-devonian", "Middle Devonian (Devon)", "Epoch", "devonian", 393.3, 382.7, "Ma",
    "First forests appear; ammonoids originate.")
add("eifelian", "Eifelian (Eifel)", "Age", "middle-devonian", 393.3, 387.7, "Ma",
    "Stromatoporoid-coral reefs peak; first seed ferns.")
add("givetian", "Givetian (Givet)", "Age", "middle-devonian", 387.7, 382.7, "Ma",
    "First forests (Archaeopteris); placoderms diversify.")
add("late-devonian", "Late Devonian (Devon)", "Epoch", "devonian", 382.7, 358.9, "Ma",
    "First tetrapods; Late Devonian extinction event (~75% of species).")
add("frasnian", "Frasnian (Frasnes-lez-Couvin)", "Age", "late-devonian", 382.7, 372.2, "Ma",
    "Massive reef systems; Frasnian-Famennian extinction (Kellwasser Event).")
add("famennian", "Famennian (Famenne)", "Age", "late-devonian", 372.2, 358.9, "Ma",
    "Post-extinction recovery; first tetrapod trackways; Hangenberg Event at end.")

add("carboniferous", "Carboniferous (carbō + ferre)", "Period", "paleozoic", 358.9, 298.9, "Ma",
    "Vast coal swamp forests; first reptiles; high atmospheric oxygen.")
add("mississippian", "Mississippian (Mississippi)", "SubPeriod", "carboniferous", 358.9, 323.4, "Ma",
    "Early Carboniferous; large crinoid and coral reefs; amphibians diversify.")
add("early-mississippian", "Early Mississippian (Mississippi)", "Epoch", "mississippian", 358.9, 346.7, "Ma",
    "Tournaisian age; recovery after Devonian extinction.")
add("tournaisian", "Tournaisian (Tournai / Doornik)", "Age", "early-mississippian", 358.9, 346.7, "Ma",
    "Post-Devonian recovery; crinoid meadows; early tetrapod diversification (Romer's Gap).")
add("middle-mississippian", "Middle Mississippian (Mississippi)", "Epoch", "mississippian", 346.7, 330.3, "Ma",
    "Viséan age; widespread limestone deposition; large coral reefs.")
add("visean", "Viséan (Visé)", "Age", "middle-mississippian", 346.7, 330.3, "Ma",
    "Extensive carbonate platforms; first large tetrapods; coal forests begin.")
add("late-mississippian", "Late Mississippian (Mississippi)", "Epoch", "mississippian", 330.3, 323.4, "Ma",
    "Serpukhovian age; glaciation begins in Gondwana.")
add("serpukhovian", "Serpukhovian (Серпухов)", "Age", "late-mississippian", 330.3, 323.4, "Ma",
    "Late Mississippian ice ages; sea level drops; first winged insects.")
add("pennsylvanian", "Pennsylvanian (Pennsylvania)", "SubPeriod", "carboniferous", 323.4, 298.9, "Ma",
    "Late Carboniferous; coal swamps peak; first reptiles appear.")
add("early-pennsylvanian", "Early Pennsylvanian (Pennsylvania)", "Epoch", "pennsylvanian", 323.4, 315.2, "Ma",
    "Bashkirian age; Pangaea begins to assemble.")
add("bashkirian", "Bashkirian (Башкирский ярус / Башҡортостан)", "Age", "early-pennsylvanian", 323.4, 315.2, "Ma",
    "First large coal swamps; Pangaea assembly accelerates; early reptile diversification.")
add("middle-pennsylvanian", "Middle Pennsylvanian (Pennsylvania)", "Epoch", "pennsylvanian", 315.2, 307, "Ma",
    "Moscovian age; giant insects thrive in high-oxygen atmosphere.")
add("moscovian", "Moscovian (Москва)", "Age", "middle-pennsylvanian", 315.2, 307, "Ma",
    "Giant dragonflies (Meganeura); atmospheric oxygen ~35%; vast coal swamp forests.")
add("late-pennsylvanian", "Late Pennsylvanian (Pennsylvania)", "Epoch", "pennsylvanian", 307, 298.9, "Ma",
    "Kasimovian–Gzhelian; earliest amniotes diversify; coal swamps decline.")
add("kasimovian", "Kasimovian (Касимов)", "Age", "late-pennsylvanian", 307, 303.7, "Ma",
    "Amniote reptiles diversify; first diapsids appear.")
add("gzhelian", "Gzhelian (Гжель)", "Age", "late-pennsylvanian", 303.7, 298.9, "Ma",
    "Coal swamps retreat as climate dries; Pangaea nearly complete.")

add("permian", "Permian (Пермь)", "Period", "paleozoic", 298.9, 251.9, "Ma",
    "Pangaea complete; therapsids (mammal ancestors) dominate; ends with the Great Dying.")
add("cisuralian", "Cisuralian (Цис-Урал)", "Epoch", "permian", 298.9, 274.4, "Ma",
    "Early Permian; diverse amphibian and reptile faunas.")
add("asselian", "Asselian (Ассель)", "Age", "cisuralian", 298.9, 293.52, "Ma",
    "Earliest Permian; glaciation continues in Gondwana.")
add("sakmarian", "Sakmarian (Сакмара)", "Age", "cisuralian", 293.52, 290.1, "Ma",
    "Pelycosaurs (sail-backed reptiles) diversify, including Dimetrodon.")
add("artinskian", "Artinskian (Артинск)", "Age", "cisuralian", 290.1, 283.3, "Ma",
    "Gondwanan glaciation wanes; conifers spread.")
add("kungurian", "Kungurian (Кунгур)", "Age", "cisuralian", 283.3, 274.4, "Ma",
    "Evaporite deposits; therapsids begin to appear.")
add("guadalupian", "Guadalupian (Guadalupe Mountains)", "Epoch", "permian", 274.4, 259.51, "Ma",
    "Middle Permian; therapsids rise to dominance; Capitanian extinction event.")
add("roadian", "Roadian (Road Canyon)", "Age", "guadalupian", 274.4, 266.9, "Ma",
    "Therapsids diversify; dinocephalians dominate.")
add("wordian", "Wordian (Word Formation)", "Age", "guadalupian", 266.9, 264.28, "Ma",
    "Reef ecosystems flourish; diverse fusulinid foraminifera.")
add("capitanian", "Capitanian (El Capitán)", "Age", "guadalupian", 264.28, 259.51, "Ma",
    "Capitanian mass extinction: major reef collapse and biodiversity loss.")
add("lopingian", "Lopingian (乐平 Lèpíng)", "Epoch", "permian", 259.51, 251.9, "Ma",
    "Late Permian; Permian–Triassic extinction: ~96% of marine species lost.")
add("wuchiapingian", "Wuchiapingian (吴家坪)", "Age", "lopingian", 259.51, 254.14, "Ma",
    "Post-Capitanian recovery; Dicynodonts become dominant herbivores.")
add("changhsingian", "Changhsingian (长兴)", "Age", "lopingian", 254.14, 251.9, "Ma",
    "The Great Dying: Siberian Traps volcanism triggers worst mass extinction in Earth history.")

# ═══════════════════════════════════════════════════════════════
# PHANEROZOIC — MESOZOIC ERA & PERIODS
# ═══════════════════════════════════════════════════════════════
add("mesozoic", "Mesozoic (Μέσος ζωή)", "Era", "phanerozoic", 251.9, 66, "Ma",
    "Age of Reptiles; dinosaurs, first mammals, first birds, first flowering plants.")

add("triassic", "Triassic (trias)", "Period", "mesozoic", 251.9, 201.4, "Ma",
    "Recovery from Permian extinction; first dinosaurs, first mammals, first pterosaurs.")
add("early-triassic", "Early Triassic (trias)", "Epoch", "triassic", 251.9, 246.7, "Ma",
    "Slow recovery from extinction; Lystrosaurus dominates terrestrial fauna.")
add("induan", "Induan (सिन्धु / Sindh)", "Age", "early-triassic", 251.9, 249.9, "Ma",
    "Earliest Triassic stage; extremely low biodiversity, harsh conditions.")
add("olenekian", "Olenekian (Оленёк)", "Age", "early-triassic", 249.9, 246.7, "Ma",
    "Marine ecosystems begin recovery; first ichthyosaurs appear.")
add("middle-triassic", "Middle Triassic (trias)", "Epoch", "triassic", 246.7, 237, "Ma",
    "Archosaurs diversify; first dinosauromorphs.")
add("anisian", "Anisian (Enns / Anisus)", "Age", "middle-triassic", 246.7, 241.5, "Ma",
    "Marine reptiles diversify; coral reefs re-establish.")
add("ladinian", "Ladinian (Ladins / Ladinisch)", "Age", "middle-triassic", 241.5, 237, "Ma",
    "First dinosauriform tracks; seed ferns and conifers dominate.")
add("late-triassic", "Late Triassic (trias)", "Epoch", "triassic", 237, 201.4, "Ma",
    "First true dinosaurs, mammals, and pterosaurs; Triassic–Jurassic extinction at end.")
add("carnian", "Carnian (Karnische Alpen)", "Age", "late-triassic", 237, 227, "Ma",
    "Carnian Pluvial Episode: major climate shift; first dinosaurs appear.")
add("norian", "Norian (Noricum)", "Age", "late-triassic", 227, 205.7, "Ma",
    "Dinosaurs diversify; first turtles and crocodylomorphs.")
add("rhaetian", "Rhaetian (Raetia / Rätisch)", "Age", "late-triassic", 205.7, 201.4, "Ma",
    "End-Triassic extinction opens ecological niches for dinosaurs.")

add("jurassic", "Jurassic (Jura)", "Period", "mesozoic", 201.4, 143.1, "Ma",
    "Dinosaurs dominate; first birds (Archaeopteryx); Pangaea breaks apart.")
add("early-jurassic", "Early Jurassic (Jura)", "Epoch", "jurassic", 201.4, 174.7, "Ma",
    "Dinosaurs diversify into dominant land animals; large marine reptiles.")
add("hettangian", "Hettangian (Hettange-Grande)", "Age", "early-jurassic", 201.4, 199.5, "Ma",
    "Post-extinction recovery; early dinosaur radiation.")
add("sinemurian", "Sinemurian (Semur-en-Auxois)", "Age", "early-jurassic", 199.5, 192.9, "Ma",
    "Early large sauropodomorphs; ammonite diversity increases.")
add("pliensbachian", "Pliensbachian (Pliensbach)", "Age", "early-jurassic", 192.9, 184.2, "Ma",
    "Warm climates; diverse marine ecosystems, ichthyosaurs abundant.")
add("toarcian", "Toarcian (Thouars)", "Age", "early-jurassic", 184.2, 174.7, "Ma",
    "Toarcian Oceanic Anoxic Event (Karoo-Ferrar volcanism); marine extinctions; widespread black shales.")
add("middle-jurassic", "Middle Jurassic (Jura)", "Epoch", "jurassic", 174.7, 161.5, "Ma",
    "Sauropods and theropods diversify; earliest flowering plant evidence.")
add("aalenian", "Aalenian (Aalen)", "Age", "middle-jurassic", 174.7, 170.9, "Ma",
    "Pangaea continues to rift; ammonites flourish.")
add("bajocian", "Bajocian (Bayeux)", "Age", "middle-jurassic", 170.9, 168.2, "Ma",
    "Diverse coral reefs; stegosaurs appear.")
add("bathonian", "Bathonian (Bath)", "Age", "middle-jurassic", 168.2, 165.3, "Ma",
    "First definitive mammals diversify; microcontinent formation.")
add("callovian", "Callovian (Kellaways)", "Age", "middle-jurassic", 165.3, 161.5, "Ma",
    "Marine transgression; ammonite diversity peak in Jurassic.")
add("late-jurassic", "Late Jurassic (Jura)", "Epoch", "jurassic", 161.5, 143.1, "Ma",
    "Giant sauropods; Archaeopteryx; Morrison Formation dinosaurs.")
add("oxfordian", "Oxfordian (Oxford)", "Age", "late-jurassic", 161.5, 154.8, "Ma",
    "Widespread coral reefs; large theropods like Allosaurus.")
add("kimmeridgian", "Kimmeridgian (Kimmeridge)", "Age", "late-jurassic", 154.8, 149.2, "Ma",
    "Rich marine ecosystems; source rocks for North Sea oil form.")
add("tithonian", "Tithonian (Τιθωνός)", "Age", "late-jurassic", 149.2, 143.1, "Ma",
    "Archaeopteryx; Solnhofen limestone; transition to Cretaceous.")

add("cretaceous", "Cretaceous (creta)", "Period", "mesozoic", 143.1, 66, "Ma",
    "Longest Mesozoic period; flowering plants rise; ends with asteroid impact (K-Pg).")
add("early-cretaceous", "Early Cretaceous (creta)", "Epoch", "cretaceous", 143.1, 100.5, "Ma",
    "Flowering plants diversify; feathered dinosaurs; continental drift accelerates.")
add("berriasian", "Berriasian (Berrias, Ardèche)", "Age", "early-cretaceous", 143.1, 137.05, "Ma",
    "Earliest Cretaceous; GSSP boundary still under discussion.")
add("valanginian", "Valanginian (Valangin, Neuchâtel)", "Age", "early-cretaceous", 137.05, 132.6, "Ma",
    "Weald clay environments; early angiosperms in fossil record.")
add("hauterivian", "Hauterivian (Hauterive, Neuchâtel)", "Age", "early-cretaceous", 132.6, 125.77, "Ma",
    "Iguanodon and early ornithopod diversity; warm global climate.")
add("barremian", "Barremian (Barrême)", "Age", "early-cretaceous", 125.77, 121.4, "Ma",
    "Las Hoyas and Jehol Biota; feathered theropods preserved.")
add("aptian", "Aptian (Apt, Provence)", "Age", "early-cretaceous", 121.4, 113.2, "Ma",
    "Oceanic Anoxic Event 1a; first diverse angiosperm floras.")
add("albian", "Albian (Aube / Alba)", "Age", "early-cretaceous", 113.2, 100.5, "Ma",
    "High sea levels; diverse ammonites; early social insects.")
add("late-cretaceous", "Late Cretaceous (creta)", "Epoch", "cretaceous", 100.5, 66, "Ma",
    "Tyrannosaurus, Triceratops; angiosperms dominant; K-Pg extinction.")
add("cenomanian", "Cenomanian (Le Mans / Cenomanum)", "Age", "late-cretaceous", 100.5, 93.9, "Ma",
    "Highest sea levels in Cretaceous; OAE 2 at boundary.")
add("turonian", "Turonian (Tours / Turones)", "Age", "late-cretaceous", 93.9, 89.8, "Ma",
    "Warmest period of Cretaceous; diverse reef ecosystems.")
add("coniacian", "Coniacian (Cognac)", "Age", "late-cretaceous", 89.8, 85.7, "Ma",
    "Continued warm climates; hadrosaur diversification begins.")
add("santonian", "Santonian (Saintes / Santones)", "Age", "late-cretaceous", 85.7, 83.6, "Ma",
    "Ceratopsian dinosaurs diversify; early modern bird lineages.")
add("campanian", "Campanian (Champagne, Charente)", "Age", "late-cretaceous", 83.6, 72.2, "Ma",
    "Rich dinosaur faunas worldwide; chalk deposits form.")
add("maastrichtian", "Maastrichtian (Maastricht / Mestreech)", "Age", "late-cretaceous", 72.2, 66, "Ma",
    "Final stage; Chicxulub impact ends Mesozoic; ~76% of species extinct.")

# ═══════════════════════════════════════════════════════════════
# PHANEROZOIC — CENOZOIC ERA & PERIODS
# ═══════════════════════════════════════════════════════════════
add("cenozoic", "Cenozoic (Καινός ζωή)", "Era", "phanerozoic", 66, 0, "Ma",
    "Age of Mammals; grasslands, primates, hominins; current era.")

add("paleogene", "Paleogene (παλαιός γένος)", "Period", "cenozoic", 66, 23.04, "Ma",
    "Mammals diversify rapidly after K-Pg extinction; first primates.")
add("paleocene", "Paleocene (παλαιός καινός)", "Epoch", "paleogene", 66, 56, "Ma",
    "Post-extinction recovery; mammals remain small but diversify.")
add("danian", "Danian (Danmark)", "Age", "paleocene", 66, 61.66, "Ma",
    "Earliest Cenozoic stage; mammals fill vacant ecological niches.")
add("selandian", "Selandian (Sjælland)", "Age", "paleocene", 61.66, 59.24, "Ma",
    "Warm climates; early primate evolution.")
add("thanetian", "Thanetian (Isle of Thanet)", "Age", "paleocene", 59.24, 56, "Ma",
    "Warming trend; diverse mammal faunas; London Clay formation.")
add("eocene", "Eocene (ἠώς καινός)", "Epoch", "paleogene", 56, 33.9, "Ma",
    "Warmest Cenozoic epoch; first modern mammal orders; early whales, horses, bats.")
add("ypresian", "Ypresian (Ieper / Ypres)", "Age", "eocene", 56, 48.07, "Ma",
    "Paleocene-Eocene Thermal Maximum (PETM); warmest global temperatures.")
add("lutetian", "Lutetian (Lutetia / Paris)", "Age", "eocene", 48.07, 41.03, "Ma",
    "Diversification of modern mammal families; early elephants.")
add("bartonian", "Bartonian (Barton-on-Sea)", "Age", "eocene", 41.03, 37.71, "Ma",
    "Gradual cooling begins; Antarctic ice sheet starts forming.")
add("priabonian", "Priabonian (Priabona)", "Age", "eocene", 37.71, 33.9, "Ma",
    "Grande Coupure extinction event in Europe; dramatic cooling.")
add("oligocene", "Oligocene (ὀλίγος καινός)", "Epoch", "paleogene", 33.9, 23.04, "Ma",
    "Cooler and drier; grasslands expand; modern mammal families establish.")
add("rupelian", "Rupelian (Rupel)", "Age", "oligocene", 33.9, 27.30, "Ma",
    "Antarctic ice sheet permanent; global cooling continues.")
add("chattian", "Chattian (Chatti / Chatten)", "Age", "oligocene", 27.30, 23.04, "Ma",
    "Late Oligocene warming; first deer and pigs appear.")

add("neogene", "Neogene (νέος γένος)", "Period", "cenozoic", 23.04, 2.58, "Ma",
    "Grasslands dominate; great apes evolve; Isthmus of Panama forms.")
add("miocene", "Miocene (μείων καινός)", "Epoch", "neogene", 23.04, 5.333, "Ma",
    "Kelp forests, grasslands; diverse apes; Messinian salinity crisis.")
add("aquitanian", "Aquitanian (Aquitaine)", "Age", "miocene", 23.04, 20.45, "Ma",
    "Early Miocene; warm climates; diverse marine mammals.")
add("burdigalian", "Burdigalian (Bordeaux / Burdigala)", "Age", "miocene", 20.45, 15.98, "Ma",
    "Mountain building (Alps, Himalayas); first great apes.")
add("langhian", "Langhian (Langhe)", "Age", "miocene", 15.98, 13.82, "Ma",
    "Mid-Miocene Climatic Optimum; widespread warmth.")
add("serravallian", "Serravallian (Serravalle Scrivia)", "Age", "miocene", 13.82, 11.63, "Ma",
    "Cooling resumes; East Antarctic ice sheet expands.")
add("tortonian", "Tortonian (Tortona)", "Age", "miocene", 11.63, 7.246, "Ma",
    "Mediterranean begins to close; hominoids disperse from Africa.")
add("messinian", "Messinian (Messina)", "Age", "miocene", 7.246, 5.333, "Ma",
    "Messinian Salinity Crisis: Mediterranean nearly dries up.")
add("pliocene", "Pliocene (πλεῖον καινός)", "Epoch", "neogene", 5.333, 2.58, "Ma",
    "Australopithecus; Arctic ice cap forms; Isthmus of Panama closes.")
add("zanclean", "Zanclean (Ζάγκλη / Messina)", "Age", "pliocene", 5.333, 3.6, "Ma",
    "Zanclean flood refills Mediterranean; Australopithecus afarensis.")
add("piacenzian", "Piacenzian (Piacenza)", "Age", "pliocene", 3.6, 2.58, "Ma",
    "Mid-Piacenzian Warm Period; early Homo?; Northern Hemisphere glaciation starts.")

add("quaternary", "Quaternary (quaternarius)", "Period", "cenozoic", 2.58, 0, "Ma",
    "Ice ages and interglacials; evolution and spread of Homo sapiens.")

# ── Pleistocene ──
add("pleistocene", "Pleistocene (πλεῖστος καινός)", "Epoch", "quaternary", 2.58, 0.0117, "Ma",
    "Repeated glaciations; megafauna; Homo erectus, Neanderthals, modern humans.")
add("gelasian", "Gelasian (γέλα)", "Age", "pleistocene", 2.58, 1.80, "Ma",
    "Earliest Pleistocene; Northern Hemisphere glaciation intensifies; early Homo.")
add("calabrian", "Calabrian (Calabria)", "Age", "pleistocene", 1.80, 0.774, "Ma",
    "Homo erectus disperses out of Africa; Brunhes-Matuyama reversal at end.")
add("chibanian", "Chibanian (千葉 Chiba)", "Age", "pleistocene", 0.774, 0.129, "Ma",
    "Homo heidelbergensis; Neanderthals evolve; major glacial cycles.")
add("late-pleistocene", "Late Pleistocene (πλεῖστος καινός)", "Age", "pleistocene", 0.129, 0.0117, "Ma",
    "Homo sapiens expands globally; Neanderthal extinction; Last Glacial Maximum.")

# ── Holocene ──
add("holocene", "Holocene (ὅλος καινός)", "Epoch", "quaternary", 11700, 0, "BP",
    "Current epoch; stable warm climate; rise of agriculture, civilization.")
add("greenlandian", "Greenlandian (Kalaallit Nunaat / Grønland)", "Age", "holocene", 11700, 8200, "BP",
    "Early Holocene; post-glacial warming; Mesolithic hunter-gatherers in Europe.")
add("northgrippian", "Northgrippian (NorthGRIP, Grønland)", "Age", "holocene", 8200, 4200, "BP",
    "Middle Holocene; 8.2 ka cold event; agriculture spreads through Europe.")
add("meghalayan", "Meghalayan (मेघालय Meghālaya / Khasi: Ri Khasi)", "Age", "holocene", 4200, 0, "BP",
    "Late Holocene; 4.2 ka drought; rise and fall of Bronze Age civilizations; present day; GSSP at Mawmluh Cave, Khasi Hills.")

# Anthropocene (informal — rejected by IUGS March 2024, but widely used)
add("anthropocene", "Anthropocene (informal / ἄνθρωπος καινός)", "Epoch", "quaternary", 1952, 0, "CE",
    "Proposed epoch marking dominant human influence on Earth systems; IUGS rejected formal ratification in March 2024; widely used informally in science and policy; proposed GSSP at Crawford Lake, Canada, based on nuclear fallout markers.")

# ═══════════════════════════════════════════════════════════════
# ARCHAEOLOGICAL / CULTURAL AGES (European & Scandinavian focus)
# ═══════════════════════════════════════════════════════════════

# --- Stone Age ---
add("stone-age", "Stone Age (Stenåldern / Steinzeit / Âge de pierre / Edad de Piedra / Età della Pietra / Steentijd / Каменный век)", "CulturalAge", "holocene", 3300000, 3300, "BCE",
    "Longest period of human prehistory; defined by use of stone tools. Three-age system by C.J. Thomsen.")
add("paleolithic", "Paleolithic / Old Stone Age (Paleolitikum / Äldre stenåldern / Altsteinzeit / Paléolithique / Paleolítico / Paleolitico / Палеолит)", "CulturalAge", "stone-age", 3300000, 10000, "BCE",
    "Oldest division; hunter-gatherer societies; development of stone tool technology.")
add("lower-paleolithic", "Lower Paleolithic (Äldre paleolitikum)", "CulturalAge", "paleolithic", 3300000, 300000, "BCE",
    "Homo habilis, Homo erectus; Oldowan and Acheulean tool industries.")
add("middle-paleolithic", "Middle Paleolithic (Mellersta paleolitikum)", "CulturalAge", "paleolithic", 300000, 50000, "BCE",
    "Neanderthals in Europe; Mousterian tool industry; first evidence of symbolic behavior.")
add("upper-paleolithic", "Upper Paleolithic (Yngre paleolitikum)", "CulturalAge", "paleolithic", 50000, 10000, "BCE",
    "Homo sapiens in Europe; cave art (Lascaux, Altamira); Aurignacian, Gravettian, Magdalenian cultures.")
add("bromme-culture", "Bromme Culture (Brommekulturen)", "CulturalAge", "upper-paleolithic", 11600, 10000, "BCE",
    "Late Paleolithic reindeer hunters at the edge of the Scandinavian ice sheet; earliest human presence in Sweden (Scania).")
add("ahrensburg-culture", "Ahrensburg Culture (Ahrensburgkulturen)", "CulturalAge", "upper-paleolithic", 10900, 9700, "BCE",
    "Late Paleolithic/early Mesolithic nomadic hunters from the North German Plain; migrated north via Jutland following retreating ice.")
add("mesolithic", "Mesolithic / Middle Stone Age (Mesolitikum / Mellersta stenåldern / Mittelsteinzeit / Mésolithique / Mesolítico / Mesolitico / Мезолит)", "CulturalAge", "stone-age", 10000, 4000, "BCE",
    "Post-glacial; microlithic tools; Scandinavia first settled ~9500 BCE. Maglemosian, Kongemose, Ertebølle cultures.")
add("fosna-hensbacka", "Fosna–Hensbacka Culture (Fosna–Hensbackakulturen)", "CulturalAge", "mesolithic", 8300, 7300, "BCE",
    "Early Mesolithic culture along the Norwegian and Swedish west coasts; descended from Ahrensburg tradition; coastal seal hunting and fishing.")
add("komsa-culture", "Komsa Culture (Komsakulturen)", "CulturalAge", "mesolithic", 10000, 6000, "BCE",
    "Early Mesolithic culture of northern Norway coast; sea-oriented seal hunters and fishermen; relatively crude stone tools compared to southern Fosna.")
add("maglemosian", "Maglemosian Culture (Maglemosekulturen)", "CulturalAge", "mesolithic", 9000, 6000, "BCE",
    "Early Mesolithic hunter-gatherer culture in southern Scandinavia and northern Germany; flint microliths, bone harpoons.")
add("kongemose", "Kongemose Culture (Kongemosekulturen)", "CulturalAge", "mesolithic", 6000, 5200, "BCE",
    "Middle Mesolithic in Denmark and southern Sweden; coastal adaptation, fishing, seal hunting.")
add("nostvet-lihult", "Nøstvet and Lihult Cultures (Nøstvetkulturen / Lihultkulturen)", "CulturalAge", "mesolithic", 6000, 4000, "BCE",
    "Middle-Late Mesolithic in most of southern Norway and Sweden; descendants of Fosna-Hensbacka; polished stone axes.")
add("ertebolleculture", "Ertebølle Culture (Ertebøllekulturen)", "CulturalAge", "mesolithic", 5400, 3950, "BCE",
    "Late Mesolithic in southern Scandinavia; first pottery, large shell middens, transition to agriculture.")
add("neolithic", "Neolithic / New Stone Age (Neolitikum / Yngre stenåldern / Jungsteinzeit / Néolithique / Neolítico / Neolitico / Неолит)", "CulturalAge", "stone-age", 4000, 2000, "BCE",
    "Agriculture, polished stone tools, pottery, permanent settlements. Funnelbeaker culture in Scandinavia (~4000–2700 BCE).")
add("funnelbeaker", "Funnelbeaker Culture (TRB)", "CulturalAge", "neolithic", 4000, 2700, "BCE",
    "First farming culture in Scandinavia; megalithic tombs (dolmens, passage graves); pottery with funnel-shaped rims.")
add("pitted-ware", "Pitted Ware Culture (Gropkeramisk kultur)", "CulturalAge", "neolithic", 3200, 2300, "BCE",
    "Concurrent hunter-gatherer-fisher culture in eastern Sweden, Gotland, and Finland; seal hunting, characteristic pitted pottery.")
add("battle-axe", "Battle Axe Culture (Boat Axe Culture)", "CulturalAge", "neolithic", 2800, 2300, "BCE",
    "Scandinavian variant of Corded Ware culture; single graves, polished stone battle axes, early Indo-European influences.")
add("nordic-neolithic-late", "Late Neolithic Scandinavia (Senneolitikum)", "CulturalAge", "neolithic", 2300, 1750, "BCE",
    "Transition to metalworking; flint daggers imitate bronze; Bell Beaker influences reach Scandinavia.")

# --- Chalcolithic (Copper Age) ---
add("chalcolithic", "Chalcolithic / Copper Age (Kopparåldern / Kupferzeit / Chalcolithique / Calcolítico / Calcolitico / Chalkolit / Χαλκολιθική)", "CulturalAge", "holocene", 3500, 2000, "BCE",
    "Transitional period; first metalworking (copper); Ötzi the Iceman; Corded Ware culture in Northern Europe.")

# --- Bronze Age ---
add("bronze-age", "Bronze Age (Bronsåldern / Bronzezeit / Âge du Bronze / Edad del Bronce / Età del Bronzo / Бронзовый век / Εποχή του Χαλκού)", "CulturalAge", "holocene", 3300, 1200, "BCE",
    "Defined by bronze metallurgy. Near East ~3300 BCE; Nordic Bronze Age begins ~1750 BCE.")
add("early-bronze-age", "Early Bronze Age (Äldre bronsåldern)", "CulturalAge", "bronze-age", 3300, 2000, "BCE",
    "Near East & Mediterranean: urbanization, writing systems, first empires.")
add("middle-bronze-age", "Middle Bronze Age (Mellersta bronsåldern)", "CulturalAge", "bronze-age", 2000, 1550, "BCE",
    "Minoan civilization peaks; Nordic Bronze Age begins (~1750 BCE); extensive trade networks.")
add("late-bronze-age", "Late Bronze Age (Yngre bronsåldern)", "CulturalAge", "bronze-age", 1550, 1200, "BCE",
    "Mycenaean Greece; New Kingdom Egypt; Late Bronze Age collapse (~1200 BCE).")
add("nordic-bronze-age", "Nordic Bronze Age (Nordisk bronsålder)", "CulturalAge", "bronze-age", 1700, 500, "BCE",
    "Scandinavian Bronze Age; elaborate burial mounds, rock carvings (hällristningar), sun chariot of Trundholm.")
add("nordic-bronze-early", "Early Nordic Bronze Age / Period I–III (Äldre bronsåldern)", "CulturalAge", "nordic-bronze-age", 1700, 1100, "BCE",
    "Oak coffin burials (Egtved Girl, Skrydstrup Woman); Trundholm sun chariot; wealth from amber trade.")
add("montelius-i", "Montelius Period I (Monteliusperiod I)", "CulturalAge", "nordic-bronze-early", 1700, 1500, "BCE",
    "Earliest Nordic Bronze Age; first bronze imports; flint daggers gradually replaced by bronze weapons.")
add("montelius-ii", "Montelius Period II (Monteliusperiod II)", "CulturalAge", "nordic-bronze-early", 1500, 1300, "BCE",
    "Peak of early bronze wealth; Egtved Girl burial (1370 BCE); Trundholm sun chariot (~1400 BCE); elaborate spiral ornaments and fibulae.")
add("montelius-iii", "Montelius Period III (Monteliusperiod III)", "CulturalAge", "nordic-bronze-early", 1300, 1100, "BCE",
    "Skrydstrup Woman burial; oak coffin burials continue; extensive amber trade networks with Mediterranean.")
add("nordic-bronze-late", "Late Nordic Bronze Age / Period IV–VI (Yngre bronsåldern)", "CulturalAge", "nordic-bronze-age", 1100, 500, "BCE",
    "Cremation replaces inhumation; lur horns; rock carvings peak; declining bronze imports.")
add("montelius-iv", "Montelius Period IV (Monteliusperiod IV)", "CulturalAge", "nordic-bronze-late", 1100, 900, "BCE",
    "Shift from inhumation to cremation; rock carvings (hällristningar) flourish; bronze lur horns crafted.")
add("montelius-v", "Montelius Period V (Monteliusperiod V)", "CulturalAge", "nordic-bronze-late", 900, 700, "BCE",
    "Elaborate ritual depositions in lakes and bogs; continued rock carving tradition; Hallstatt imports arrive.")
add("montelius-vi", "Montelius Period VI (Monteliusperiod VI)", "CulturalAge", "nordic-bronze-late", 700, 500, "BCE",
    "Final Bronze Age period; Hallstatt iron influence from Central Europe; transition to local iron production.")

# --- Iron Age ---
add("iron-age", "Iron Age (Järnåldern / Eisenzeit / Âge du Fer / Edad del Hierro / Età del Ferro / Железный век / Εποχή του Σιδήρου / עת הברזל)", "CulturalAge", "holocene", 1200, 1, "BCE",
    "Defined by iron smelting and tools. Near East ~1200 BCE; Scandinavia ~500 BCE.")
add("pre-roman-iron-age", "Pre-Roman Iron Age (Förromersk järnålder)", "CulturalAge", "iron-age", 500, 1, "BCE",
    "Iron working spreads to Scandinavia; bog ore smelting; Jastorf culture.")
add("pre-roman-iron-early", "Early Pre-Roman Iron Age (Äldre förromersk järnålder)", "CulturalAge", "pre-roman-iron-age", 500, 250, "BCE",
    "Transition from bronze; first local iron production from bog ore in southern Scandinavia.")
add("pre-roman-iron-late", "Late Pre-Roman Iron Age (Yngre förromersk järnålder)", "CulturalAge", "pre-roman-iron-age", 250, 1, "BCE",
    "Celtic La Tène influences; complex hillforts; Dejbjerg wagons; widespread bog iron production.")

# --- Roman & Migration Period ---
add("roman-iron-age", "Roman Iron Age (Romersk järnålder)", "CulturalAge", "holocene", 1, 400, "CE",
    "Roman influence on Germanic societies; runes develop; trade with the Roman Empire.")
add("early-roman-iron", "Early Roman Iron Age (Äldre romersk järnålder)", "CulturalAge", "roman-iron-age", 1, 200, "CE",
    "Increasing trade with Roman provinces; imported bronze vessels; first runic inscriptions.")
add("late-roman-iron", "Late Roman Iron Age (Yngre romersk järnålder)", "CulturalAge", "roman-iron-age", 200, 400, "CE",
    "Gold solidi flow north; Nydam boat (320 CE); elaborate weapon deposits in bogs.")
add("germanic-iron-age", "Germanic Iron Age (Germansk järnålder)", "CulturalAge", "holocene", 400, 790, "CE",
    "Post-Roman period in Scandinavia; divided into Early (Migration Period) and Late (Vendel/Merovingian) by Oscar Montelius.")
add("migration-period", "Migration Period (Folkvandringstiden / Völkerwanderung)", "CulturalAge", "germanic-iron-age", 400, 550, "CE",
    "Fall of Western Rome; Germanic peoples migrate across Europe; gold bracteates and collars in Scandinavia.")
add("migration-early", "Early Migration Period (Äldre folkvandringstiden)", "CulturalAge", "migration-period", 400, 475, "CE",
    "Huns invade Europe (375); Scandinavian gold hoards peak; elaborate gold collars (e.g. Ålleberg, Möne, Färjestaden).")
add("migration-late", "Late Migration Period (Yngre folkvandringstiden)", "CulturalAge", "migration-period", 475, 550, "CE",
    "Post-Roman gold scarcity; gilded bronze replaces gold; animal-style ornamentation (Style I) develops.")
add("vendel-period", "Vendel Period (Merovingian Period)", "CulturalAge", "germanic-iron-age", 550, 790, "CE",
    "Swedish golden age; Vendel and Valsgärde boat burials; elaborate animal-style ornamentation.")
add("vendel-early", "Early Vendel Period (Äldre vendeltiden)", "CulturalAge", "vendel-period", 550, 650, "CE",
    "Sutton Hoo parallels; Vendel I–VII boat graves near Uppsala; Style II animal ornamentation.")
add("vendel-late", "Late Vendel Period (Yngre vendeltiden)", "CulturalAge", "vendel-period", 650, 790, "CE",
    "Valsgärde boat burials continue; Style III ornamentation; Birka's proto-urban precursors; transition to Viking Age.")

# --- Viking Age ---
add("viking-age", "Viking Age (Vikingatiden)", "CulturalAge", "holocene", 793, 1100, "CE",
    "Norse expansion, raiding, trading, and settlement; Birka, Hedeby; Christianization of Scandinavia.")
add("early-viking-age", "Early Viking Age (Äldre vikingatiden)", "CulturalAge", "viking-age", 793, 900, "CE",
    "Raid on Lindisfarne (793); establishment of Norse trading centers; Oseberg ship burial.")
add("middle-viking-age", "Middle Viking Age (Mellersta vikingatiden)", "CulturalAge", "viking-age", 900, 1000, "CE",
    "Danelaw in England; Normandy settled; Icelandic settlement; Bluetooth's Denmark.")
add("late-viking-age", "Late Viking Age (Yngre vikingatiden)", "CulturalAge", "viking-age", 1000, 1100, "CE",
    "Christianization; end of Norse paganism; Cnut the Great's North Sea Empire.")

# --- Medieval Period ---
add("medieval-period", "Medieval Period (Medeltiden / Mittelalter / Moyen Âge / Edad Media / Medioevo / Средневековье / Μεσαίωνας)", "CulturalAge", "holocene", 1050, 1520, "CE",
    "Scandinavian medieval period; Christianity dominant; Hanseatic trade; Gothic cathedrals; Black Death (1349).")
add("early-medieval", "Early Medieval Period (Tidig medeltid)", "CulturalAge", "medieval-period", 1050, 1200, "CE",
    "Church consolidation; first Scandinavian dioceses; Romanesque architecture.")
add("high-medieval", "High Medieval Period (Högmedeltiden)", "CulturalAge", "medieval-period", 1200, 1350, "CE",
    "Hanseatic League; Gothic architecture; Kalmar Union precursors; population growth.")
add("late-medieval", "Late Medieval Period (Senmedeltiden)", "CulturalAge", "medieval-period", 1350, 1520, "CE",
    "Black Death aftermath; Kalmar Union (1397); Reformation approaches.")

# --- Early Modern ---
add("early-modern", "Early Modern Period (Tidigmodern tid)", "CulturalAge", "holocene", 1520, 1789, "CE",
    "Reformation; Vasa dynasty; Swedish Empire (stormaktstiden); Age of Enlightenment.")
add("early-vasa-era", "Early Vasa Era (Äldre Vasatiden)", "CulturalAge", "early-modern", 1523, 1611, "CE",
    "Gustav Vasa breaks from Kalmar Union; Protestant Reformation; hereditary monarchy established; Stockholm Bloodbath aftermath.")
add("reformation-era", "Reformation Era (Reformationstiden)", "CulturalAge", "early-vasa-era", 1527, 1600, "CE",
    "Protestant Reformation in Sweden (1527) and Denmark-Norway (1536); seizure of Catholic Church property; new church ordinances.")
add("swedish-empire", "Swedish Empire (Stormaktstiden)", "CulturalAge", "early-modern", 1611, 1721, "CE",
    "Sweden as great power; Thirty Years War; Baltic dominance; ends with Great Northern War.")
add("thirty-years-war", "Thirty Years' War Period (Trettioåriga kriget)", "CulturalAge", "swedish-empire", 1618, 1648, "CE",
    "Sweden enters as Protestant champion under Gustav II Adolf; Battle of Breitenfeld (1631); Peace of Westphalia (1648).")
add("caroline-era", "Caroline Era (Karolinska tiden)", "CulturalAge", "swedish-empire", 1654, 1718, "CE",
    "Absolute monarchy under Charles X, XI, XII; reduktion land reforms; Great Northern War ends Swedish empire.")
add("age-of-liberty", "Age of Liberty (Frihetstiden)", "CulturalAge", "early-modern", 1718, 1772, "CE",
    "Parliamentary rule after Charles XII; Hat and Cap party factions; Enlightenment science (Linnaeus, Celsius).")
add("gustavian-era", "Gustavian Era (Gustavianska tiden)", "CulturalAge", "early-modern", 1772, 1809, "CE",
    "Gustav III's coup restores royal power; patron of arts; Royal Opera and Royal Dramatic Theatre founded; assassinated 1792.")

# --- Modern Period ---
add("modern-period", "Modern Period (Moderna tiden)", "CulturalAge", "holocene", 1789, 0, "CE",
    "French Revolution to present; industrialization, nation-states, globalization.")
add("bernadotte-era", "Bernadotte Era / Union Period (Bernadottetiden / Unionstiden)", "CulturalAge", "modern-period", 1809, 1905, "CE",
    "New constitution (1809); French Marshal Bernadotte becomes Crown Prince (1810); Sweden-Norway union (1814–1905); loss of Finland to Russia.")
add("industrial-age", "Industrial Age (Industrialiseringen)", "CulturalAge", "modern-period", 1850, 1914, "CE",
    "Railways from 1850s; mass emigration to Americas (~1.3M Swedes); Alfred Nobel; rapid urbanization.")
add("contemporary", "Contemporary Period (Samtiden)", "CulturalAge", "modern-period", 1914, 0, "CE",
    "World Wars (neutral), welfare states (folkhemmet), digital revolution; Scandinavian social democracies.")

# ═══════════════════════════════════════════════════════════════
# BROADER EUROPEAN HISTORICAL PERIODS
# ═══════════════════════════════════════════════════════════════

# --- Classical Antiquity ---
add("archaic-greece", "Archaic Greece (Αρχαϊκή Ελλάδα)", "CulturalAge", "holocene", 800, 480, "BCE",
    "Rise of city-states (poleis); Greek colonization; development of the alphabet, Homer's epics, early philosophy.")
add("classical-greece", "Classical Greece (Κλασική Ελλάδα)", "CulturalAge", "holocene", 480, 323, "BCE",
    "Golden Age of Athens; Parthenon; Socrates, Plato, Aristotle; Athenian democracy; Peloponnesian War.")
add("hellenistic-period", "Hellenistic Period (Ελληνιστική περίοδος)", "CulturalAge", "holocene", 323, 31, "BCE",
    "Alexander the Great's empire fragments; spread of Greek culture across Mediterranean and Near East; Library of Alexandria.")
add("roman-republic", "Roman Republic (Res Publica Romana / Ρωμαϊκή Δημοκρατία / Roma Cumhuriyeti / Römische Republik)", "CulturalAge", "holocene", 509, 27, "BCE",
    "Roman expansion across Mediterranean; Punic Wars; Julius Caesar; transition to Empire.")
add("roman-empire", "Roman Empire (Imperium Romanum / Ρωμαϊκή Αυτοκρατορία / Roma İmparatorluğu / Römisches Reich / Империя Рима)", "CulturalAge", "holocene", 27, 476, "CE",
    "Pax Romana; peak Roman civilization; roads, aqueducts, law; Christianity becomes state religion (380 CE).")
add("late-antiquity", "Late Antiquity (Spätantike)", "CulturalAge", "holocene", 250, 750, "CE",
    "Transition from classical to medieval; fall of Western Rome (476); rise of Christianity; Byzantine Empire continues in East.")
add("hunnic-empire", "Hunnic Empire (Хунска империја / Hunnenreich / Birodalom hunok)", "CulturalAge", "holocene", 370, 469, "CE",
    "Nomadic steppe empire originating in Central Asia; swept west ~370 CE displacing Germanic peoples; Attila the Hun (434-453 CE) at peak; raided Balkans and Gaul; Battle of Catalaunian Plains (451 CE); dissolved rapidly after Attila's death (453 CE); possible relation to Xiongnu (匈奴) of Chinese records.")
add("byzantine-empire", "Byzantine Empire (Βυζαντινή Αυτοκρατορία / Byzantinska riket)", "CulturalAge", "holocene", 330, 1453, "CE",
    "Eastern Roman Empire; Constantinople capital; Justinian's Code; Hagia Sophia; Greek culture; Orthodox Christianity; fell to Ottoman Turks (1453).")
add("byzantine-early", "Early Byzantine Period (Πρώιμη Βυζαντινή Περίοδος)", "CulturalAge", "byzantine-empire", 330, 717, "CE",
    "Constantine founds Constantinople (330); Justinian I (527-565); Corpus Juris Civilis; Hagia Sophia (537); wars with Sasanian Persia; Arab sieges.")
add("byzantine-middle", "Middle Byzantine Period (Μέση Βυζαντινή Περίοδος)", "CulturalAge", "byzantine-empire", 717, 1204, "CE",
    "Iconoclasm controversy; Macedonian Renaissance; Great Schism (1054); Komnenian dynasty; Battle of Manzikert (1071); themes system.")
add("byzantine-late", "Late Byzantine Period (Ύστερη Βυζαντινή Περίοδος)", "CulturalAge", "byzantine-empire", 1204, 1453, "CE",
    "Fourth Crusade sacks Constantinople (1204); Latin Empire; Palaiologos restoration (1261); decline; Fall of Constantinople (1453) ends Roman continuity.")

# --- European Middle Ages (continental) ---
add("european-early-medieval", "Early Middle Ages (Europe)", "CulturalAge", "holocene", 476, 1000, "CE",
    "Fall of Western Rome (476); Merovingian and Carolingian kingdoms; spread of Christianity; feudalism develops.")
add("merovingian-period", "Merovingian Period (Frankish)", "CulturalAge", "european-early-medieval", 481, 751, "CE",
    "Merovingian dynasty rules Frankish kingdoms; Clovis I converts to Christianity; foundation of medieval France.")
add("carolingian-period", "Carolingian Period (Karolingerzeit / L'ère carolingienne)", "CulturalAge", "european-early-medieval", 751, 888, "CE",
    "Charlemagne crowned Emperor (800); Carolingian Renaissance; revival of learning, Latin scholarship, and arts.")
add("ottonian-period", "Ottonian Period (Ottonische Zeit)", "CulturalAge", "european-early-medieval", 919, 1024, "CE",
    "Holy Roman Empire under Otto I; Ottonian Renaissance; expansion of Christianity into central Europe.")
add("european-high-medieval", "High Middle Ages (Europe)", "CulturalAge", "holocene", 1000, 1300, "CE",
    "Crusades; Gothic cathedrals; universities founded (Bologna, Paris, Oxford); population growth; Magna Carta (1215).")
add("crusades-period", "Crusades Period (Korstågen / Les Croisades / الحروب الصليبية)", "CulturalAge", "european-high-medieval", 1095, 1291, "CE",
    "Series of religious wars for control of the Holy Land; First Crusade captures Jerusalem (1099); cultural exchange between East and West.")
add("twelfth-century-renaissance", "Renaissance of the 12th Century (Renaissance du XIIe siècle)", "CulturalAge", "european-high-medieval", 1100, 1200, "CE",
    "Revival of learning; translations of Greek and Arabic texts; founding of universities; scholasticism; Gothic architecture begins.")
add("european-late-medieval", "Late Middle Ages (Europe)", "CulturalAge", "holocene", 1300, 1500, "CE",
    "Black Death (1347-1351); Hundred Years' War; Great Western Schism; decline of feudalism; printing press (1440).")

# --- Renaissance & Early Modern Europe ---
add("renaissance", "Renaissance (Rinascimento)", "CulturalAge", "holocene", 1350, 1600, "CE",
    "Revival of classical learning and art; began in Italy (Florence); humanism, perspective painting, scientific inquiry; Michelangelo, Leonardo, Raphael.")
add("italian-renaissance", "Italian Renaissance (Rinascimento italiano)", "CulturalAge", "renaissance", 1350, 1550, "CE",
    "Florence, Venice, Rome as cultural centers; Medici patronage; Brunelleschi, Botticelli, Machiavelli, da Vinci.")
add("northern-renaissance", "Northern Renaissance (Nordisk renässans)", "CulturalAge", "renaissance", 1450, 1600, "CE",
    "Renaissance spreads north of Alps; Dürer, Erasmus, Holbein, Bruegel; printing revolution; Protestant Reformation begins.")
add("age-of-exploration", "Age of Exploration (Era dos Descobrimentos)", "CulturalAge", "holocene", 1415, 1600, "CE",
    "European maritime exploration; Columbus (1492), Vasco da Gama (1498), Magellan (1519); colonial empires begin.")
add("european-reformation", "European Reformation (Reformationen)", "CulturalAge", "holocene", 1517, 1648, "CE",
    "Luther's 95 Theses (1517); Protestant churches emerge; Counter-Reformation; Wars of Religion; Peace of Westphalia (1648).")
add("baroque-period", "Baroque Period (Barocken)", "CulturalAge", "holocene", 1600, 1750, "CE",
    "Dramatic, ornate art and architecture; Bernini, Caravaggio, Rubens, Bach, Vivaldi; absolutist monarchies.")
add("enlightenment", "Age of Enlightenment (Upplysningen / Aufklärung / Les Lumières)", "CulturalAge", "holocene", 1685, 1815, "CE",
    "Reason, science, individual rights; Voltaire, Rousseau, Kant, Locke; influence on American and French Revolutions.")
add("age-of-revolutions", "Age of Revolutions (Revolutionernas tid)", "CulturalAge", "holocene", 1775, 1848, "CE",
    "American Revolution (1775), French Revolution (1789), Napoleonic Wars, Revolutions of 1848; end of ancien régime.")
add("romanticism", "Romantic Period (Romantiken / Romantik)", "CulturalAge", "modern-period", 1790, 1850, "CE",
    "Reaction against Enlightenment rationalism; emphasis on emotion, nature, nationalism; Goethe, Byron, Beethoven, Delacroix.")
add("world-wars-era", "World Wars Era (Världskrigen)", "CulturalAge", "contemporary", 1914, 1945, "CE",
    "Two global conflicts and an interwar period that reshaped Europe; tens of millions killed; colonial empires begin to dissolve.")
add("world-war-i", "World War I (Första världskriget / Erster Weltkrieg)", "CulturalAge", "world-wars-era", 1914, 1918, "CE",
    "The Great War; trench warfare; fall of empires (Ottoman, Austro-Hungarian, Russian, German); Treaty of Versailles (1919).")
add("interwar-period", "Interwar Period (Mellankrigstiden)", "CulturalAge", "world-wars-era", 1918, 1939, "CE",
    "League of Nations; Weimar Republic; Great Depression (1929); rise of fascism in Italy, Germany, Spain; Spanish Civil War.")
add("world-war-ii", "World War II (Andra världskriget / Zweiter Weltkrieg)", "CulturalAge", "world-wars-era", 1939, 1945, "CE",
    "Global conflict; Nazi Germany, Holocaust; Allied victory; atomic bombs; United Nations founded (1945); Europe devastated.")
add("cold-war-era", "Cold War Era (Kalla kriget / Холодная война)", "CulturalAge", "contemporary", 1947, 1991, "CE",
    "East-West division; NATO vs Warsaw Pact; Iron Curtain; Berlin Wall (1961-1989); European integration begins (EEC 1957).")
add("european-integration", "European Integration (Europeisk integration)", "CulturalAge", "contemporary", 1957, 0, "CE",
    "Treaty of Rome (1957); EEC to EU; Schengen Area; Euro currency; expansion from 6 to 27+ member states.")

# --- Pre-Classical Aegean ---
add("minoan-civilization", "Minoan Civilization (Μινωικός πολιτισμός)", "CulturalAge", "holocene", 2700, 1450, "BCE",
    "First advanced European civilization; Knossos palace; Linear A script (undeciphered); bull-leaping; thalassocracy; Thera eruption.")
add("mycenaean-civilization", "Mycenaean Civilization (Μυκηναϊκός πολιτισμός)", "CulturalAge", "holocene", 1600, 1100, "BCE",
    "First mainland Greek civilization; Linear B script; fortified palaces (Mycenae, Tiryns, Pylos); Trojan War tradition; Bronze Age collapse.")
add("greek-dark-ages", "Greek Dark Ages (Ελληνικοί Σκοτεινοί Αιώνες)", "CulturalAge", "holocene", 1100, 800, "BCE",
    "Collapse of Mycenaean palatial civilization; loss of writing; population decline; Dorian migration; leads to Archaic Greece.")
add("kingdom-macedon", "Kingdom of Macedon (Βασίλειο της Μακεδονίας / Makedonija / Mazedonien)", "CulturalAge", "holocene", 808, 168, "BCE",
    "Ancient Greek kingdom in northern Greece; Argead dynasty; Philip II unified Greek city-states; Alexander the Great conquered Persia, Egypt, India (336-323 BCE); Antigonid dynasty; conquered by Rome at Battle of Pydna (168 BCE).")

# --- Celtic Civilizations ---
add("hallstatt-culture", "Hallstatt Culture (Hallstattkultur)", "CulturalAge", "holocene", 800, 450, "BCE",
    "Early Iron Age Celtic culture; salt mining center in Austria; elite chariot burials; first identifiable Celtic material culture.")
add("la-tene-culture", "La Tène Culture (La-Tène-Kultur)", "CulturalAge", "holocene", 450, 1, "BCE",
    "Mature Celtic civilization; characteristic art style; oppida proto-urban centers; spread from Switzerland across Europe.")
add("yamnaya", "Yamnaya Culture (Ямная культура / Pit Grave culture)", "CulturalAge", "holocene", 3300, 2600, "BCE",
    "Pontic-Caspian steppe pastoralists; Proto-Indo-European homeland hypothesis (Kurgan model); wheeled vehicles; horse domestication; massive westward migration transformed Bronze Age European gene pool (ancient DNA evidence, Haak et al. 2015).")
add("corded-ware", "Corded Ware Culture (Schnurkeramik / Stridsyxekultur)", "CulturalAge", "holocene", 2900, 2350, "BCE",
    "Widespread Chalcolithic-Early Bronze Age culture across northern/central Europe; derived partly from Yamnaya migration; single burial tradition; cord-impressed pottery; stone battle axes; Indo-European language spread vector.")

add("etruscan-civilization", "Etruscan Civilization (Rasenna/Rasna)", "CulturalAge", "holocene", 900, 27, "BCE",
    "Pre-Roman Italian civilization in Tuscany; sophisticated metalwork and tomb painting; influenced Roman religion, architecture, engineering.")

# --- Iberian Peninsula ---
add("visigothic-kingdom", "Visigothic Kingdom (Reino visigodo)", "CulturalAge", "holocene", 418, 721, "CE",
    "Germanic successor state controlling Iberia; Toledo capital; Liber Iudiciorum legal code; Arian then Catholic Christianity.")
add("al-andalus", "Al-Andalus (الأندلس)", "CulturalAge", "holocene", 711, 1492, "CE",
    "Islamic Iberia; Caliphate of Córdoba; convivencia; Alhambra, Mezquita; advances in science, medicine, philosophy.")
add("reconquista", "Reconquista (Reconquista / إسترداد)", "CulturalAge", "holocene", 722, 1492, "CE",
    "Christian reconquest of Iberia; Covadonga (722) to Fall of Granada (1492); shaped Spanish and Portuguese national identity.")
add("spanish-empire", "Spanish Empire (Imperio español)", "CulturalAge", "holocene", 1492, 1976, "CE",
    "First global empire; colonization of Americas and Philippines; 'empire on which the sun never sets'; Habsburg and Bourbon dynasties.")

# --- Italian States ---
add("lombard-kingdom", "Lombard Kingdom (Regnum Langobardorum)", "CulturalAge", "holocene", 568, 774, "CE",
    "Germanic kingdom in Italy after Roman fall; Lombard law; conquered by Charlemagne; origin of 'Lombardy'.")
add("republic-of-venice", "Republic of Venice (Serenissima Repubblica di Venezia)", "CulturalAge", "holocene", 697, 1797, "CE",
    "Over 1,100 years of continuous republican government; maritime empire; eastern Mediterranean trade monopoly; Arsenal; Doge system.")
add("papal-states", "Papal States (Stato Pontificio)", "CulturalAge", "holocene", 756, 1870, "CE",
    "Temporal domain of the Pope; central Italian territories; Papal diplomacy; key barrier to Italian unification.")
add("italian-unification", "Italian Unification (Risorgimento)", "CulturalAge", "holocene", 1815, 1871, "CE",
    "Unification movement; Garibaldi, Cavour, Mazzini; Kingdom of Italy proclaimed 1861; Rome annexed 1870.")

# --- Holy Roman Empire & Central Europe ---
add("holy-roman-empire", "Holy Roman Empire (Heiliges Römisches Reich)", "CulturalAge", "holocene", 962, 1806, "CE",
    "Central European polity; Imperial Diet; framework for German politics for 800+ years; 'neither Holy, nor Roman, nor an Empire'; dissolved by Napoleon.")
add("habsburg-monarchy", "Habsburg Monarchy (Habsburgermonarchie)", "CulturalAge", "holocene", 1282, 1918, "CE",
    "Dominant European dynasty; controlled Austria, Spain, Netherlands, Italy; Charles V ruled largest European empire; Catholic champions.")
add("austro-hungarian-empire", "Austro-Hungarian Empire (Österreichisch-Ungarische Monarchie)", "CulturalAge", "holocene", 1867, 1918, "CE",
    "Dual monarchy; second-largest European state; multi-ethnic tension; assassination of Franz Ferdinand triggers WWI.")

# --- Eastern Europe ---
add("first-bulgarian-empire", "First Bulgarian Empire (Първо българско царство)", "CulturalAge", "holocene", 681, 1018, "CE",
    "First Slavic state recognized by Byzantium; Simeon the Great; Cyrillic script origin; conquered by Basil II 'the Bulgar-Slayer'.")
add("second-bulgarian-empire", "Second Bulgarian Empire (Второ българско царство)", "CulturalAge", "holocene", 1185, 1396, "CE",
    "Asen dynasty revival; Tarnovo capital; fell to Ottoman conquest.")
add("kingdom-of-poland", "Kingdom of Poland (Królestwo Polskie)", "CulturalAge", "holocene", 1025, 1569, "CE",
    "Piast and Jagiellonian dynasties; Christianization (966); Copernicus; union with Lithuania.")
add("polish-lithuanian-commonwealth", "Polish-Lithuanian Commonwealth (Rzeczpospolita Obojga Narodów)", "CulturalAge", "holocene", 1569, 1795, "CE",
    "Largest European state of its era; elected monarchy; religious tolerance; Sarmatism; partitioned by Russia, Prussia, Austria.")
add("kingdom-of-hungary", "Kingdom of Hungary (Magyar Királyság)", "CulturalAge", "holocene", 1000, 1526, "CE",
    "St. Stephen I; buffer against Ottoman expansion; Battle of Mohács (1526) ends independence; major Central European power.")
add("grand-duchy-of-lithuania", "Grand Duchy of Lithuania (Lietuvos Didžioji Kunigaikštystė)", "CulturalAge", "holocene", 1236, 1569, "CE",
    "Last pagan state in Europe; largest European state in 15th century; encompassed Belarus, Ukraine, parts of Russia.")
add("kingdom-of-serbia", "Kingdom of Serbia (Краљевина Србија)", "CulturalAge", "holocene", 1217, 1346, "CE",
    "Nemanjić dynasty kingdom; autocephalous Serbian Orthodox Church (1219); cultural golden age; ends when Stefan Dušan proclaims the Serbian Empire in 1346.")

# --- Russian History ---
add("grand-duchy-moscow", "Grand Duchy of Moscow (Великое княжество Московское)", "CulturalAge", "holocene", 1263, 1547, "CE",
    "Rise of Moscow as successor to Kievan Rus'; Ivan III ends Mongol rule (1480); 'Third Rome' ideology.")
add("tsardom-of-russia", "Tsardom of Russia (Русское царство)", "CulturalAge", "holocene", 1547, 1721, "CE",
    "Ivan IV 'the Terrible'; Time of Troubles; Romanov dynasty begins (1613); expansion into Siberia.")
add("russian-empire", "Russian Empire (Российская империя)", "CulturalAge", "holocene", 1721, 1917, "CE",
    "Peter the Great's modernization; St. Petersburg; largest contiguous empire; Napoleonic Wars; emancipation of serfs (1861).")
add("soviet-union", "Soviet Union (Союз Советских Социалистических Республик)", "CulturalAge", "contemporary", 1922, 1991, "CE",
    "First communist state; superpower; industrialization; WWII Eastern Front; Space Race; Cold War; collapse reshapes world order.")

# --- Additional European periods ---
add("napoleonic-era", "Napoleonic Era (Ère napoléonienne)", "CulturalAge", "modern-period", 1799, 1815, "CE",
    "Napoleon reshapes European borders; Code Napoléon; Battle of Austerlitz, Trafalgar, Waterloo; Congress of Vienna.")
add("victorian-era", "Victorian Era (Viktorianska eran)", "CulturalAge", "modern-period", 1837, 1901, "CE",
    "British global hegemony; Industrial Revolution peak; British Empire at zenith; cultural, scientific, social transformation.")
add("british-empire", "British Empire (Brittiska imperiet)", "CulturalAge", "holocene", 1583, 1997, "CE",
    "Largest empire in history; shaped global language, law, trade; decolonization post-WWII; Commonwealth of Nations.")
add("dutch-golden-age", "Dutch Golden Age (Gouden Eeuw)", "CulturalAge", "holocene", 1588, 1672, "CE",
    "Dutch Republic as global trade power; VOC; Rembrandt, Vermeer; religious tolerance; scientific revolution.")
add("german-unification", "German Unification (Deutsche Einigung)", "CulturalAge", "modern-period", 1864, 1871, "CE",
    "Bismarck; Franco-Prussian War; German Empire proclaimed at Versailles; reshapes European power balance.")

# ═══════════════════════════════════════════════════════════════
# MAJOR MASS EXTINCTION EVENTS (cross-cutting markers)
# ═══════════════════════════════════════════════════════════════
add("end-ordovician-extinction", "End-Ordovician Extinction (Ordowices)", "Age", "late-ordovician", 445, 443, "Ma",
    "First of the Big Five; ~85% of marine species lost; caused by Gondwanan glaciation and sea-level fall.")
add("late-devonian-extinction", "Late Devonian Extinction (Devon)", "Age", "late-devonian", 375, 359, "Ma",
    "Second of the Big Five; ~75% of species lost over millions of years; reef ecosystems collapse.")
add("permian-triassic-extinction", "Permian–Triassic Extinction (The Great Dying / Пермь–trias)", "Age", "lopingian", 252, 251, "Ma",
    "Worst mass extinction: ~96% of marine and ~70% of land species; Siberian Traps volcanism.")
add("triassic-jurassic-extinction", "Triassic–Jurassic Extinction (trias–Jura)", "Age", "late-triassic", 201.5, 201.3, "Ma",
    "Fourth of the Big Five; ~80% of species lost; CAMP volcanism; opens way for dinosaur dominance.")
add("cretaceous-paleogene-extinction", "Cretaceous–Paleogene Extinction (K-Pg / Chicxulub, Yucatán)", "Age", "late-cretaceous", 66.05, 66, "Ma",
    "Fifth of the Big Five; Chicxulub asteroid impact; all non-avian dinosaurs extinct; ~76% of species lost.")
add("deccan-traps", "Deccan Traps Volcanism (दक्खन Dakhan)", "Age", "maastrichtian", 67, 65, "Ma",
    "One of Earth's largest volcanic events; ~1.5 million km² basalt flows in India; co-contributor to K-Pg extinction; climate disruption preceded and overlapped Chicxulub impact.")
add("chicxulub-impact", "Chicxulub Impact (Chicxulub, Yucatán / Maaya)", "Age", "maastrichtian", 66.05, 66, "Ma",
    "~10 km asteroid strikes Yucatán Peninsula; 180 km crater; impact winter; global wildfires; acid rain; tsunami; primary trigger of K-Pg mass extinction; iridium anomaly discovered by Alvarez et al. (1980).")
add("siberian-traps", "Siberian Traps (Сибирские траппы Sibirskiye trappy)", "Age", "lopingian", 252.2, 250.6, "Ma",
    "Largest known continental flood basalt; ~7 million km² lava; released massive CO₂ and SO₂; primary trigger of Permian–Triassic extinction; thermogenic carbon from coal and evaporite contact metamorphism.")
add("emeishan-traps", "Emeishan Traps (峨眉山暗色岩 Éméishān ànsèyán)", "Age", "guadalupian", 260, 259, "Ma",
    "Large igneous province in southwestern China (Sichuan, Yunnan, Guizhou); ~0.5 million km²; linked to Capitanian/end-Guadalupian extinction event; preceded Siberian Traps by ~8 Myr.")
add("camp-volcanism", "Central Atlantic Magmatic Province (CAMP)", "Age", "late-triassic", 201.6, 200.9, "Ma",
    "One of Earth's largest igneous provinces; erupted as Pangaea rifted; ~11 million km²; primary trigger of end-Triassic mass extinction; CO₂-driven warming and ocean acidification.")

# ═══════════════════════════════════════════════════════════════
# ADDITIONAL GEOLOGICAL / CLIMATE EVENTS
# ═══════════════════════════════════════════════════════════════
add("great-oxidation", "Great Oxidation Event (GOE)", "Age", "paleoproterozoic", 2400, 2060, "Ma",
    "Free oxygen accumulates in atmosphere for first time; mass die-off of anaerobic organisms; banded iron formations cease.")
add("huronian-glaciation", "Huronian Glaciation (Lake Huron)", "Age", "paleoproterozoic", 2400, 2100, "Ma",
    "First known Snowball Earth event; possibly triggered by Great Oxidation Event reducing methane greenhouse.")
add("lomagundi-jatuli", "Lomagundi–Jatuli Event (Lomagundi, Zimbabwe / Jatuli, Karelia)", "Age", "paleoproterozoic", 2220, 2060, "Ma",
    "Largest positive carbon isotope excursion in Earth history (δ¹³C up to +12‰); immediately follows GOE; indicates massive organic carbon burial; associated with first rise of atmospheric oxygen; global extent confirmed from Fennoscandia to southern Africa.")
add("great-unconformity", "Great Unconformity (Grand Canyon / Lipalian)", "Age", "neoproterozoic", 1000, 539, "Ma",
    "Global gap in the rock record between Precambrian basement and Cambrian strata; up to 1.2 billion years missing in places; cause debated: Snowball Earth glacial erosion, continental denudation, or Rodinia rifting; term coined by John Wesley Powell (1869); Lipalian interval of Walcott (1910).")
add("petm", "Paleocene–Eocene Thermal Maximum (PETM / παλαιός ἠώς)", "Age", "ypresian", 55.8, 55.6, "Ma",
    "Rapid global warming of 5–8 °C; massive carbon release; mammals disperse across continents.")
add("messinian-crisis", "Messinian Salinity Crisis (Messina)", "Age", "messinian", 5.96, 5.33, "Ma",
    "Mediterranean Sea nearly dries up due to tectonic closure of Strait of Gibraltar; massive evaporite deposits.")
add("last-glacial-max", "Last Glacial Maximum (LGM)", "Age", "late-pleistocene", 0.026, 0.019, "Ma",
    "Peak of last ice age ~26,000 years ago; ice sheets cover Scandinavia, Britain, northern Europe; sea level ~120 m lower.")
add("younger-dryas", "Younger Dryas (Dryas octopetala)", "Age", "late-pleistocene", 12900, 11700, "BP",
    "Abrupt return to glacial conditions for ~1,200 years; end marks start of Holocene; cause debated (meltwater pulse?).")
add("8.2ka-event", "8.2 ka Cold Event (Laurentide)", "Age", "northgrippian", 8200, 8000, "BP",
    "Sudden cooling for ~150 years; collapse of Laurentide ice sheet drains glacial lakes into Atlantic; disrupts thermohaline circulation.")
add("4.2ka-event", "4.2 ka Aridification Event (मेघालय Meghālaya)", "Age", "meghalayan", 4200, 3900, "BP",
    "Severe drought lasting ~200 years; contributes to collapse of Akkadian Empire, Old Kingdom Egypt, Harappan civilization.")

add("carnian-pluvial", "Carnian Pluvial Episode (CPE / Karnische Alpen)", "Age", "carnian", 234, 232, "Ma",
    "Major climate perturbation; ~2 Myr of increased rainfall globally; Wrangellia LIP volcanism as trigger; diversification of dinosaurs, conifers, corals; reef crisis; significant turnover in marine and terrestrial ecosystems.")
add("boring-billion", "Boring Billion (Dull Billion / Mesoproterozoic Stasis / μέσος πρότερος)", "Age", "proterozoic", 1800, 800, "Ma",
    "Informal name for ~1 billion years of apparent evolutionary and environmental stability; low atmospheric oxygen (~1-10% modern); subdued tectonic activity; minimal carbon isotope variation; recent work challenges 'boring' label.")

add("toba-catastrophe", "Toba Catastrophe (~74 ka / Toba, Sumatera)", "Age", "late-pleistocene", 0.074, 0.074, "Ma",
    "Supervolcanic eruption of Mount Toba, Sumatra (~74 ka); Volcanic Explosivity Index 8; ~2,800 km³ ejecta; volcanic winter; possible human population bottleneck (debated); largest eruption in last 2 million years.")

add("rodinia-assembly", "Rodinia Assembly (Grenville Orogeny / родина Rodina)", "Age", "stenian", 1100, 900, "Ma",
    "Assembly of supercontinent Rodinia via Grenville orogeny; included most of Earth's continental crust; name from Russian 'родина' (homeland); precursor configuration shaped later tectonic and glacial history.")
add("rodinia-breakup", "Rodinia Breakup (родина распад)", "Age", "tonian", 750, 633, "Ma",
    "Rifting and breakup of supercontinent Rodinia; opened Iapetus Ocean; weathering of newly exposed continental margins may have triggered Snowball Earth glaciations (Sturtian, Marinoan); led to formation of Gondwana.")
add("pangaea-assembly", "Pangaea Assembly (Πᾶν γαῖα / Variscan–Alleghenian)", "Age", "pennsylvanian", 335, 270, "Ma",
    "Assembly of Earth's most recent supercontinent from collision of Gondwana and Laurussia; Variscan/Hercynian and Alleghanian orogenies; enclosed Tethys Ocean; profoundly altered global climate and ocean circulation.")
add("pangaea-breakup", "Pangaea Breakup (Πᾶν γαῖα rift)", "Age", "early-jurassic", 200, 150, "Ma",
    "Rifting of Pangaea beginning in Late Triassic/Early Jurassic; separation into Laurasia and Gondwana; opening of Central Atlantic Ocean; CAMP volcanism associated with initial rifting; shaped modern continental configuration.")
add("oae-1a", "Oceanic Anoxic Event 1a (OAE 1a / Selli Event / Selli, Italia)", "Age", "aptian", 120, 119, "Ma",
    "Widespread ocean anoxia linked to Ontong Java Plateau volcanism; massive organic carbon burial; black shale deposition; major perturbation of global carbon cycle; significant marine biotic turnover.")
add("oae-2", "Oceanic Anoxic Event 2 (OAE 2 / Bonarelli Event / Bonarelli, Italia)", "Age", "cenomanian", 94.4, 93.9, "Ma",
    "Most severe Cretaceous oceanic anoxic event; global black shale deposition; ~27% of marine invertebrate genera extinct; linked to Caribbean LIP volcanism; major δ¹³C excursion used as global stratigraphic marker.")
add("isthmus-panama", "Isthmus of Panama Closure (Istmo de Panamá / GABI)", "Age", "piacenzian", 3.5, 2.8, "Ma",
    "Tectonic closure of Central American Seaway; diverted Atlantic/Pacific currents; strengthened Gulf Stream and thermohaline circulation; triggered Great American Biotic Interchange (GABI); contributed to Northern Hemisphere glaciation onset.")
add("mmct", "Mid-Miocene Climate Transition (MMCT)", "Age", "serravallian", 14.0, 13.8, "Ma",
    "Abrupt global cooling following Mid-Miocene Climatic Optimum; major expansion of East Antarctic ice sheet; global sea level drop; grasslands expand at expense of forests; key inflection point toward modern icehouse climate.")

# ═══════════════════════════════════════════════════════════════
# ADDITIONAL CULTURAL PERIODS (Sámi, Baltic, Finnish)
# ═══════════════════════════════════════════════════════════════
add("sami-prehistory", "Sámi Prehistory (Sámi ovdahistorjá)", "CulturalAge", "holocene", 8000, 1600, "BCE-CE",
    "Indigenous Sámi settlement of northern Fennoscandia; reindeer herding develops; Komsa and Fosna cultures; sieiddit (sacred sites).")
add("sami-modern", "Sámi Modern History (Sámi ođasáiggi historjá)", "CulturalAge", "holocene", 1600, 0, "CE",
    "Colonization and forced assimilation; Lapland witch trials; state borders divide Sápmi; Sámi parliaments (Norway 1989, Sweden 1993, Finland 1996); cultural revitalization.")
add("comb-ceramic", "Comb Ceramic Culture (Kamkeramisk kultur)", "CulturalAge", "neolithic", 3900, 2800, "BCE",
    "Widespread Neolithic culture across Finland and the Baltic; characteristic comb-stamped pottery; hunter-gatherer-fishers.")
add("asbestos-ceramic", "Asbestos Ceramic Period (Asbestikeramiikka / Finland)", "CulturalAge", "neolithic", 3500, 2000, "BCE",
    "Distinctive Finnish Neolithic pottery tempered with asbestos fibers; concurrent with Comb Ceramic in eastern Finland.")
add("nordic-iron-age-celtic", "Celtic Iron Age Influences in Scandinavia (Keltisk järnålderspåverkan)", "CulturalAge", "pre-roman-iron-age", 400, 200, "BCE",
    "La Tène art style reaches Scandinavia; Hjortspring boat; early hillforts in southern Sweden and Denmark.")
add("jastorf-culture", "Jastorf Culture (Jastorfkulturen)", "CulturalAge", "pre-roman-iron-age", 500, 100, "BCE",
    "Pre-Roman Iron Age culture of northern Germany and southern Scandinavia; first iron smelting from bog ore; cremation burials.")

# --- Viking Age sub-events ---
add("danelaw", "Danelaw Period (Danelagen)", "CulturalAge", "viking-age", 865, 954, "CE",
    "Norse-controlled territory in eastern and northern England; established after the Great Heathen Army; York as Viking capital.")
add("viking-iceland", "Settlement of Iceland (Landnám Íslands)", "CulturalAge", "viking-age", 870, 930, "CE",
    "Norse colonization of Iceland; Ingólfr Arnarson (874); Althing established 930 as one of the oldest parliaments.")
add("viking-normandy", "Norse Settlement of Normandy (Normandie / Norðmandí)", "CulturalAge", "middle-viking-age", 911, 1066, "CE",
    "Rollo receives Normandy from French king (911); Norse settlers adopt French language; William the Conqueror descends from Vikings.")
add("viking-rus", "Varangians and Kievan Rus' (Väringar / Киевская Русь)", "CulturalAge", "viking-age", 800, 1054, "CE",
    "Swedish Vikings (Varangians) establish trade routes through Russia; found Kyiv and Novgorod; Varangian Guard in Constantinople.")
add("norse-greenland", "Norse Greenland (Grænland / Grønland)", "CulturalAge", "viking-age", 985, 1450, "CE",
    "Erik the Red founds Eastern and Western Settlements (~985); Brattahlíð; launching point for Vinland voyages; Garðar diocese (northernmost in Christendom); population ~3,000-5,000; abandoned by ~1450; climate deterioration and trade isolation.")
add("norse-vinland", "Norse Vinland (Vínland)", "CulturalAge", "viking-age", 1000, 1021, "CE",
    "Leif Erikson reaches North America (~1000 CE); L'Anse aux Meadows, Newfoundland (UNESCO World Heritage Site); tree-ring dated to 1021 CE; first confirmed European presence in the Americas; sagas of Eiríks saga rauða and Grœnlendinga saga.")

# --- Medieval & Hanseatic ---
add("christianization-scandinavia", "Christianization of Scandinavia (Skandinaviens kristnande)", "CulturalAge", "viking-age", 960, 1150, "CE",
    "Gradual conversion: Denmark (~960, Harald Bluetooth), Norway (~1000, Olaf Tryggvason), Sweden (~1000, Olof Skötkonung); Uppsala temple destroyed ~1087.")
add("baltic-crusades", "Baltic Crusades Period (Nordliga korstågen)", "CulturalAge", "medieval-period", 1147, 1290, "CE",
    "Northern Crusades; Christianization of Baltic region; Teutonic Order; Swedish crusades to Finland.")
add("hanseatic-period", "Hanseatic Period in Scandinavia (Hansatiden / Hanse)", "CulturalAge", "medieval-period", 1250, 1450, "CE",
    "Hanseatic League dominates Baltic trade; German merchants in Visby, Bergen, Stockholm; Lübeck law adopted.")
add("black-death-scandinavia", "Black Death in Scandinavia (Digerdöden / Svartedauden)", "CulturalAge", "medieval-period", 1349, 1360, "CE",
    "Plague reaches Norway (1349), Sweden and Denmark; kills ~50-60% of Scandinavian population; abandoned farms (ödegårdar).")
add("kalmar-union", "Kalmar Union (Kalmarunionen)", "CulturalAge", "late-medieval", 1397, 1523, "CE",
    "Union of Denmark, Norway, and Sweden under one monarch; Queen Margrete I; dissolved by Gustav Vasa's rebellion.")
add("stockholm-bloodbath", "Stockholm Bloodbath (Stockholms blodbad)", "CulturalAge", "late-medieval", 1520, 1520, "CE",
    "Danish King Christian II executes ~80 Swedish nobles and clergy; triggers Gustav Vasa's rebellion and end of Kalmar Union.")

# --- Danish / Norwegian specific ---
add("danish-golden-age", "Danish Golden Age (Dansk guldalder)", "CulturalAge", "modern-period", 1800, 1850, "CE",
    "Cultural flourishing in Denmark: H.C. Andersen, Søren Kierkegaard, Bertel Thorvaldsen, C.W. Eckersberg; national romanticism.")
add("norway-independence", "Norwegian Independence (Norsk selvstendighet)", "CulturalAge", "modern-period", 1814, 1905, "CE",
    "Norwegian constitution (1814, Eidsvoll); forced union with Sweden; dissolution of union (1905); Haakon VII elected king.")
add("finland-grand-duchy", "Grand Duchy of Finland (Suomen suuriruhtinaskunta)", "CulturalAge", "modern-period", 1809, 1917, "CE",
    "Finland as autonomous Grand Duchy of Russia after Swedish loss (1809); Kalevala published (1835); Finnish nationalism; independence 1917.")
add("eocene-oligocene-extinction", "Eocene–Oligocene Extinction (Grande Coupure / Priabona)", "Age", "priabonian", 33.9, 33.7, "Ma",
    "Major faunal turnover in Europe; Asian mammals invade; dramatic cooling as Antarctic ice sheet forms.")
add("cambrian-explosion", "Cambrian Explosion (Cymru)", "Age", "cambrian", 538.8, 510, "Ma",
    "Most major animal phyla appear in fossil record within ~25 Myr; Burgess Shale, Chengjiang faunas; cause debated.")

# ═══════════════════════════════════════════════════════════════
# SOUTH AMERICAN HISTORICAL & CULTURAL PERIODS
# ═══════════════════════════════════════════════════════════════

# --- Pre-Columbian Civilizations ---
add("south-america-precolumbian", "Pre-Columbian South America (América del Sur precolombina)", "CulturalAge", "holocene", 14800, 1533, "BCE-CE",
    "Indigenous civilizations of South America before European contact; from Monte Verde (~14,800 BCE) through Norte Chico to the Inca Empire.")
add("norte-chico", "Norte Chico (Caral) Civilization", "CulturalAge", "south-america-precolumbian", 3000, 1800, "BCE",
    "Oldest known civilization in the Americas; Caral, Supe Valley, Peru; monumental architecture, quipu precursors; no pottery or writing.")
add("valdivia-culture", "Valdivia Culture (Cultura Valdivia)", "CulturalAge", "south-america-precolumbian", 3500, 1800, "BCE",
    "Early Formative culture on coast of Ecuador; some of the oldest pottery in the Americas; Venus figurines; early maize cultivation.")
add("chavin-culture", "Chavín Culture (Chavín de Huántar)", "CulturalAge", "south-america-precolumbian", 900, 200, "BCE",
    "Early Horizon unifying culture of Andean Peru; Chavín de Huántar temple complex; jaguar iconography; influence across highlands and coast.")
add("paracas-culture", "Paracas Culture (Cultura Paracas)", "CulturalAge", "south-america-precolumbian", 800, 100, "BCE",
    "Southern Peruvian coastal culture; extraordinary textiles and embroidery; cranial trepanation; Paracas Necropolis burials.")
add("nazca-culture", "Nazca Culture (Cultura Nazca)", "CulturalAge", "south-america-precolumbian", 100, 800, "BCE-CE",
    "Southern Peruvian desert; Nazca Lines geoglyphs; polychrome pottery; underground aqueducts (puquios).")
add("moche-civilization", "Moche Civilization (Civilización Moche / Mochica)", "CulturalAge", "south-america-precolumbian", 100, 700, "CE",
    "Northern Peruvian coast; Huaca del Sol and Huaca de la Luna; portrait vessels; Sipán royal tombs; advanced irrigation.")
add("tiwanaku-empire", "Tiwanaku Empire (Tiahuanaco / Tiwanaku)", "CulturalAge", "south-america-precolumbian", 300, 1000, "CE",
    "Andean civilization centered at Lake Titicaca, Bolivia; Gateway of the Sun; raised-field agriculture; altitude ~3,800 m.")
add("wari-empire", "Wari Empire (Huari)", "CulturalAge", "south-america-precolumbian", 600, 1000, "CE",
    "Middle Horizon Andean empire; administrative centers across Peru; road network predating Inca; terraced agriculture.")
add("chinchorro-culture", "Chinchorro Culture (Cultura Chinchorro)", "CulturalAge", "south-america-precolumbian", 7000, 1500, "BCE",
    "Atacama Desert coast (Chile/Peru); oldest artificial mummification in the world (~5000 BCE, predating Egypt); fishing and gathering; egalitarian society.")
add("recuay-culture", "Recuay Culture (Cultura Recuay)", "CulturalAge", "south-america-precolumbian", 200, 600, "CE",
    "Northern Peruvian highlands (Ancash); stone sculpture; kaolin pottery; underground galleries; warrior iconography; contemporaneous with Moche.")
add("lima-culture", "Lima Culture (Cultura Lima)", "CulturalAge", "south-america-precolumbian", 100, 650, "CE",
    "Central Peruvian coast; Huaca Pucllana and Huaca Huallamarca; interlocking adobe bricks ('librero' style); irrigation agriculture; fish and shellfish.")
add("lambayeque-sican", "Lambayeque / Sicán Culture (Cultura Lambayeque / Sicán)", "CulturalAge", "south-america-precolumbian", 750, 1375, "CE",
    "Northern Peru; Batán Grande and Túcume pyramids; Sicán Lord gold mask; master goldsmiths; Naylamp dynasty legend; conquered by Chimú.")
add("chimu-empire", "Chimú Empire (Imperio Chimú / Chimor)", "CulturalAge", "south-america-precolumbian", 900, 1470, "CE",
    "Late Intermediate kingdom of northern Peru; Chan Chan (largest adobe city); sophisticated metalwork; conquered by Inca.")
add("chachapoya", "Chachapoya Civilization (Civilización Chachapoya)", "CulturalAge", "south-america-precolumbian", 800, 1470, "CE",
    "Cloud Warriors of northern Peru; Kuélap fortress (stone citadel at 3,000 m); cliff tombs and sarcophagi; conquered by Inca; Revash mausolea.")
add("muisca-confederation", "Muisca Confederation (Muysca / Confederación Muisca)", "CulturalAge", "south-america-precolumbian", 600, 1541, "CE",
    "Chibcha-speaking confederation in Colombian highlands; gold and tumbaga metalwork; El Dorado legend; salt and emerald trade.")
add("tairona", "Tairona Civilization (Civilización Tairona)", "CulturalAge", "south-america-precolumbian", 200, 1600, "CE",
    "Sierra Nevada de Santa Marta, Colombia; Ciudad Perdida (Teyuna); stone terraces and stairways; gold and tumbaga work; ancestors of Kogi people.")
add("tierradentro", "Tierradentro Culture (Cultura de Tierradentro)", "CulturalAge", "south-america-precolumbian", 600, 900, "CE",
    "Underground hypogea (burial chambers) carved into volcanic rock, Colombia; painted geometric designs; UNESCO World Heritage Site; Páez territory.")
add("san-agustin-culture", "San Agustín Culture (Cultura de San Agustín)", "CulturalAge", "south-america-precolumbian", 100, 1350, "CE",
    "Pre-Columbian culture of southwestern Colombia; monumental stone sculptures and burial mounds; UNESCO World Heritage Site.")
add("mapuche-precolonial", "Mapuche (Pre-Colonial / Mapudungun)", "CulturalAge", "south-america-precolumbian", 600, 1550, "CE",
    "Indigenous people of south-central Chile and Argentina; agricultural and pastoral; fierce resistance to Inca and Spanish expansion.")
add("marajoara-culture", "Marajoara Culture (Cultura Marajoara)", "CulturalAge", "south-america-precolumbian", 400, 1300, "CE",
    "Marajó Island, Amazon estuary, Brazil; elaborate polychrome ceramics; earthen mounds (tesos); complex chiefdom; challenging 'virgin Amazon' myth.")
add("diaguita", "Diaguita Culture (Cultura Diaguita)", "CulturalAge", "south-america-precolumbian", 800, 1536, "CE",
    "Northwestern Argentina and Chilean Norte Chico; distinctive geometric pottery; terraced agriculture; fortified settlements (pucará); resisted Inca then Spanish.")
add("guarani-precolonial", "Guaraní (Pre-Colonial / Avañe'ẽ)", "CulturalAge", "south-america-precolumbian", 500, 1537, "CE",
    "Tupi-Guaraní peoples of Paraguay, Brazil, and Argentina; slash-and-burn agriculture; canoe navigation; religious migrations (Land Without Evil).")
add("selknam", "Selk'nam Period (Ona People)", "CulturalAge", "south-america-precolumbian", 8000, 1900, "BCE-CE",
    "Tierra del Fuego hunter-gatherer cultural tradition; Hain initiation ceremony; guanaco hunters; body painting; genocided during Patagonian sheep boom (late 1800s).")

# --- Inca Empire ---
add("inca-empire", "Inca Empire (Tawantinsuyu)", "CulturalAge", "south-america-precolumbian", 1438, 1533, "CE",
    "Largest pre-Columbian empire; Cusco as capital; Machu Picchu; quipu record-keeping; road system (Qhapaq Ñan); conquered by Pizarro.")
add("inca-expansion", "Inca Expansion Period (Hatun Tawantinsuyu)", "CulturalAge", "inca-empire", 1438, 1493, "CE",
    "Pachacuti and Túpac Inca Yupanqui expand Tawantinsuyu from Ecuador to Chile; conquer Chimú; build Machu Picchu.")
add("inca-huayna-capac", "Reign of Huayna Cápac (Wayna Qhapaq)", "CulturalAge", "inca-empire", 1493, 1527, "CE",
    "Empire at greatest extent; integration of conquered peoples; smallpox arrives before Spanish contact; death triggers civil war.")
add("inca-civil-war", "Inca Civil War (Atawallpa–Waskhar Awqanakuy)", "CulturalAge", "inca-empire", 1529, 1532, "CE",
    "War of succession between Atahualpa and Huáscar; weakens empire on eve of Spanish arrival; Atahualpa's generals capture Huáscar and Cusco.")

# --- Colonial Period ---
add("south-america-colonial", "Colonial South America (América del Sur colonial)", "CulturalAge", "holocene", 1492, 1825, "CE",
    "European colonization of South America; Spanish and Portuguese empires; encomienda and hacienda systems; Jesuit missions.")
add("spanish-conquest-sa", "Spanish Conquest of South America (Conquista de América del Sur)", "CulturalAge", "south-america-colonial", 1532, 1572, "CE",
    "Pizarro captures Atahualpa (1532); fall of Cusco (1533); Neo-Inca resistance at Vilcabamba until 1572; Potosí silver discovered (1545).")
add("portuguese-brazil-colonial", "Portuguese Colonial Brazil (Brasil Colonial)", "CulturalAge", "south-america-colonial", 1500, 1822, "CE",
    "Cabral claims Brazil (1500); sugar plantations; Atlantic slave trade; gold rush in Minas Gerais (1690s); Rio becomes capital (1763).")
add("viceroyalty-peru", "Viceroyalty of Peru (Virreinato del Perú)", "CulturalAge", "south-america-colonial", 1542, 1824, "CE",
    "Spanish colonial administration covering most of South America; Lima as capital; Potosí silver mines; encomienda; Baroque churches.")
add("viceroyalty-new-granada", "Viceroyalty of New Granada (Virreinato de Nueva Granada)", "CulturalAge", "south-america-colonial", 1717, 1819, "CE",
    "Spanish colony covering modern Colombia, Ecuador, Venezuela, Panama; Bogotá as capital; separated from Viceroyalty of Peru.")
add("viceroyalty-rio-plata", "Viceroyalty of the Río de la Plata (Virreinato del Río de la Plata)", "CulturalAge", "south-america-colonial", 1776, 1814, "CE",
    "Spanish colony covering modern Argentina, Uruguay, Paraguay, Bolivia; Buenos Aires as capital; cattle ranching; gaucho culture emerges.")
add("jesuit-missions-guarani", "Jesuit Missions of the Guaraní (Misiones Jesuíticas Guaraníes)", "CulturalAge", "south-america-colonial", 1609, 1767, "CE",
    "Jesuit reductions in Paraguay, Argentina, Brazil; autonomous theocratic communities; Guaraní autonomy; expelled 1767 by Spanish Crown.")
add("potosi-silver", "Silver Age of Potosí (Auge de la Plata de Potosí)", "CulturalAge", "south-america-colonial", 1545, 1800, "CE",
    "Cerro Rico, Potosí (Bolivia); one of the largest silver deposits ever; forced indigenous labor (mita); funded Spanish Empire; population peaked at ~200,000.")
add("tupac-amaru-rebellion", "Túpac Amaru II Rebellion (Rebelión de Túpac Amaru II)", "CulturalAge", "south-america-colonial", 1780, 1783, "CE",
    "Indigenous uprising against Spanish colonial rule in Peru and Bolivia; led by José Gabriel Condorcanqui; ~100,000 dead; precursor to independence.")

# --- Independence Era ---
add("south-america-independence", "South American Wars of Independence (Guerras de independencia hispanoamericanas)", "CulturalAge", "modern-period", 1808, 1833, "CE",
    "Liberation movements across South America; inspired by American and French Revolutions; Napoleonic invasion of Spain as catalyst.")
add("independence-argentina", "Argentine War of Independence (Guerra de Independencia Argentina)", "CulturalAge", "south-america-independence", 1810, 1818, "CE",
    "May Revolution (1810); Congress of Tucumán declares independence (1816); San Martín crosses the Andes; United Provinces of the Río de la Plata.")
add("independence-chile", "Chilean War of Independence (Guerra de la Independencia de Chile)", "CulturalAge", "south-america-independence", 1810, 1826, "CE",
    "First junta (1810); Patria Vieja and Reconquista; San Martín and O'Higgins victory at Chacabuco (1817); independence declared 1818.")
add("independence-gran-colombia", "Gran Colombia and Bolívar's Campaign (Campaña de Bolívar)", "CulturalAge", "south-america-independence", 1811, 1830, "CE",
    "Simón Bolívar liberates Venezuela, Colombia, Ecuador; Gran Colombia (1819-1831); Battle of Boyacá (1819); Sucre at Ayacucho (1824).")
add("independence-peru", "Peruvian War of Independence (Guerra de Independencia del Perú)", "CulturalAge", "south-america-independence", 1820, 1824, "CE",
    "San Martín declares independence (1821); Bolívar and Sucre complete liberation; Battle of Ayacucho (1824) ends Spanish rule in South America.")
add("independence-brazil", "Brazilian Independence (Independência do Brasil)", "CulturalAge", "south-america-independence", 1822, 1825, "CE",
    "Prince Pedro declares independence from Portugal (1822, 'Grito do Ipiranga'); Empire of Brazil established; Pedro I crowned Emperor.")
add("independence-uruguay", "Uruguayan Independence (Independencia del Uruguay)", "CulturalAge", "south-america-independence", 1811, 1828, "CE",
    "Artigas leads Oriental revolution; Cisplatine Province under Brazil; independence recognized 1828 (Treaty of Montevideo).")
add("independence-paraguay", "Paraguayan Independence (Independencia del Paraguay)", "CulturalAge", "south-america-independence", 1811, 1813, "CE",
    "Bloodless revolution (1811); one of the first South American nations to gain independence; Francia's isolationist dictatorship follows.")
add("independence-bolivia", "Bolivian Independence (Independencia de Bolivia)", "CulturalAge", "south-america-independence", 1809, 1825, "CE",
    "First Cry of Freedom in Chuquisaca (1809); Sucre defeats Spanish at Ayacucho; Republic of Bolivia named for Simón Bolívar (1825).")

# --- 19th Century South America ---
add("empire-brazil", "Empire of Brazil (Império do Brasil)", "CulturalAge", "modern-period", 1822, 1889, "CE",
    "Constitutional monarchy under Pedro I and Pedro II; coffee economy; abolition of slavery (Lei Áurea 1888); overthrown by military republic.")
add("gran-colombia", "Gran Colombia (La Gran Colombia)", "CulturalAge", "modern-period", 1819, 1831, "CE",
    "Union of Venezuela, Colombia, Ecuador, Panama under Bolívar; dissolved due to regional rivalries; Bolívar dies 1830.")
add("war-of-the-pacific", "War of the Pacific (Guerra del Pacífico)", "CulturalAge", "modern-period", 1879, 1884, "CE",
    "Chile vs. Bolivia and Peru over nitrate-rich Atacama; Chile victorious; Bolivia loses coastal access; shapes modern borders.")
add("war-of-triple-alliance", "War of the Triple Alliance (Guerra de la Triple Alianza / Guerra Guasu)", "CulturalAge", "modern-period", 1864, 1870, "CE",
    "Paraguay vs. Argentina, Brazil, Uruguay; most destructive war in South American history; Paraguay loses ~60-70% of its population.")
add("rubber-boom", "Amazon Rubber Boom (Ciclo da Borracha)", "CulturalAge", "modern-period", 1879, 1912, "CE",
    "Manaus and Belém prosper from rubber exports; Teatro Amazonas built; indigenous exploitation; ends when Asian plantations undercut prices.")

# --- 20th Century South America ---
add("south-america-20th", "20th-Century South America (América del Sur en el siglo XX)", "CulturalAge", "contemporary", 1914, 2000, "CE",
    "Urbanization, populism, military dictatorships, Cold War proxy conflicts, democratization; Peronism, Allende, Pinochet, Vargas.")
add("peronism-era", "Peronist Era (Argentina)", "CulturalAge", "south-america-20th", 1943, 1976, "CE",
    "Juan Perón and Evita; justicialismo; workers' rights and industrialization; exile, return, and military overthrow; enduring political movement.")
add("vargas-era", "Vargas Era (Brazil)", "CulturalAge", "south-america-20th", 1930, 1954, "CE",
    "Getúlio Vargas modernizes Brazil; Estado Novo dictatorship (1937-1945); industrialization; labor laws; suicide in office (1954).")
add("dirty-wars", "Dirty Wars (Southern Cone)", "CulturalAge", "south-america-20th", 1968, 1990, "CE",
    "Military dictatorships and state terrorism in Argentina, Chile, Uruguay, Brazil; Operation Condor; desaparecidos; ~60,000+ killed or disappeared.")
add("pinochet-chile", "Pinochet Regime (Chile)", "CulturalAge", "dirty-wars", 1973, 1990, "CE",
    "CIA-backed coup against Allende (1973); military dictatorship under Augusto Pinochet; neoliberal economic reforms; ~3,000 killed or disappeared.")
add("falklands-war", "Falklands War (Malvinas)", "CulturalAge", "south-america-20th", 1982, 1982, "CE",
    "Argentina invades British Falkland Islands; 74-day war; British victory; 649 Argentine and 255 British dead; accelerates fall of Argentine junta.")

# --- 21st Century & Contemporary ---
add("south-america-21st", "21st-Century South America (América del Sur en el siglo XXI)", "CulturalAge", "contemporary", 2000, 0, "CE",
    "Pink tide leftist governments; commodity boom; democratic consolidation; Mercosur and UNASUR; environmental challenges in Amazon.")
add("pink-tide", "Pink Tide (Marea Rosa)", "CulturalAge", "contemporary", 1998, 2015, "CE",
    "Wave of left-wing governments: Chávez (Venezuela), Lula (Brazil), Morales (Bolivia), Correa (Ecuador), Kirchner (Argentina); social programs, resource nationalism.")

# ═══════════════════════════════════════════════════════════════
# NORTH AMERICAN HISTORICAL & CULTURAL PERIODS
# ═══════════════════════════════════════════════════════════════

# --- Paleo-Indian & Archaic ---
add("north-america-precolumbian", "Pre-Columbian North America (América del Norte precolombina)", "CulturalAge", "holocene", 15000, 1492, "BCE-CE",
    "Indigenous civilizations of North America before European contact; from Clovis hunters to complex societies of Mesoamerica and the Southwest.")
add("monte-verde", "Monte Verde (Monteverde)", "CulturalAge", "south-america-precolumbian", 14800, 13800, "BCE",
    "Southern Chile; pre-Clovis archaeological site; evidence of human habitation ~14,800 BCE; challenges Clovis-first model; seaweed, mastodon remains; Tom Dillehay excavations.")
add("paleo-indians", "Paleo-Indian Period (Período Paleoindio)", "CulturalAge", "north-america-precolumbian", 15000, 8000, "BCE",
    "First peoples of the Americas; Clovis culture (~13,000 BP); mammoth and megafauna hunters; Folsom points; Beringia land bridge migration.")
add("clovis-culture", "Clovis Culture (Cultura Clovis)", "CulturalAge", "paleo-indians", 11500, 10800, "BCE",
    "Distinctive fluted projectile points; widespread across North America; associated with Pleistocene megafauna hunting; Blackwater Draw type site.")
add("folsom-culture", "Folsom Culture (Cultura Folsom)", "CulturalAge", "paleo-indians", 10800, 10200, "BCE",
    "Post-Clovis bison hunters on Great Plains; refined fluted points; Folsom, New Mexico type site; megafauna extinction.")
add("na-archaic-period", "Archaic Period (North America)", "CulturalAge", "north-america-precolumbian", 8000, 1000, "BCE",
    "Post-megafauna adaptation; diversified subsistence; ground stone tools; regional traditions develop across the continent.")
add("na-archaic-early", "Early Archaic (Arcaico Temprano)", "CulturalAge", "na-archaic-period", 8000, 5000, "BCE",
    "Adaptation to Holocene environments; Dalton and Kirk point traditions; increasing plant use; seasonal rounds.")
add("na-archaic-middle", "Middle Archaic (Arcaico Medio)", "CulturalAge", "na-archaic-period", 5000, 3000, "BCE",
    "Population growth; specialized tool kits; long-distance exchange networks begin; Poverty Point site (Louisiana).")
add("na-archaic-late", "Late Archaic (Arcaico Tardío)", "CulturalAge", "na-archaic-period", 3000, 1000, "BCE",
    "First pottery in Southeast; mound building begins; Poverty Point earthworks; early squash cultivation; copper tools in Great Lakes.")
add("poverty-point", "Poverty Point Culture (Cultura de Poverty Point)", "CulturalAge", "na-archaic-late", 1700, 1100, "BCE",
    "Massive earthwork complex in Louisiana; concentric ridges, Mound A (largest in North America at the time); long-distance trade network.")

# --- Mesoamerican Civilizations ---
add("mesoamerica", "Mesoamerican Civilizations (Civilizaciones Mesoamericanas)", "CulturalAge", "north-america-precolumbian", 2000, 1521, "BCE-CE",
    "Complex civilizations of Mexico and Central America; writing, calendars, monumental architecture, agriculture (maize, beans, squash).")
add("olmec", "Olmec Civilization (Ōlmēcah)", "CulturalAge", "mesoamerica", 1500, 400, "BCE",
    "Mother culture of Mesoamerica; colossal stone heads; San Lorenzo and La Venta; first Mesoamerican writing and calendar; rubber ball game.")
add("zapotec", "Zapotec Civilization (Binnizá)", "CulturalAge", "mesoamerica", 700, 1521, "BCE-CE",
    "Oaxaca Valley, Mexico; Monte Albán capital; earliest Mesoamerican writing system; 2,500-year continuous culture.")
add("teotihuacan", "Teotihuacán (Teōtīhuacān)", "CulturalAge", "mesoamerica", 100, 550, "CE",
    "Largest city in pre-Columbian Americas (~125,000 people); Pyramids of the Sun and Moon; Avenue of the Dead; influence across Mesoamerica.")
add("maya-classic", "Classic Maya Civilization (Maaya)", "CulturalAge", "mesoamerica", 250, 900, "CE",
    "City-states across Yucatán, Guatemala, Belize; hieroglyphic writing; Long Count calendar; Tikal, Palenque, Copán; mysterious collapse ~900 CE.")
add("maya-preclassic", "Preclassic Maya (Maya Preclásico)", "CulturalAge", "mesoamerica", 2000, 250, "BCE-CE",
    "Origins of Maya civilization; El Mirador massive pyramids; development of writing and calendar; early agriculture and village life.")
add("maya-postclassic", "Postclassic Maya (Maya Posclásico)", "CulturalAge", "mesoamerica", 900, 1521, "CE",
    "After Classic collapse; Chichén Itzá, Mayapán, K'iche' kingdoms; Kukulkán/Quetzalcoatl cult; Spanish conquest of Yucatán.")
add("toltec", "Toltec Empire (Imperio Tolteca / Tōltēcāyōtl)", "CulturalAge", "mesoamerica", 900, 1168, "CE",
    "Tula as capital; warrior culture; Quetzalcoatl legend; influence on Aztec ideology; feathered serpent imagery.")
add("aztec-empire", "Aztec Empire / Triple Alliance (Ēxcān Tlahtōlōyān)", "CulturalAge", "mesoamerica", 1428, 1521, "CE",
    "Tenochtitlán on Lake Texcoco (~200,000 people); Mexica Triple Alliance; human sacrifice; chinampas; conquered by Cortés 1521.")
add("aztec-rise", "Rise of the Aztecs (Ascenso de los Mexicas)", "CulturalAge", "mesoamerica", 1325, 1428, "CE",
    "Founding of Tenochtitlán (1325); Mexica as mercenaries and vassals; Triple Alliance formed with Texcoco and Tlacopan (1428).")
add("aztec-expansion", "Aztec Imperial Expansion (Expansión del Ēxcān Tlahtōlōyān)", "CulturalAge", "aztec-empire", 1428, 1502, "CE",
    "Itzcoatl, Moctezuma I, Ahuitzotl expand empire from Gulf to Pacific; flower wars; tribute system; Great Temple of Tenochtitlán.")
add("aztec-moctezuma-ii", "Reign of Moctezuma II (Motēcuhzōma Xōcoyōtzin)", "CulturalAge", "aztec-empire", 1502, 1520, "CE",
    "Empire at greatest extent; omens and prophecies; arrival of Cortés (1519); Moctezuma captured; dies during La Noche Triste (1520).")
add("mixtec", "Mixtec Civilization (Ñuu Dzahui / Civilización Mixteca)", "CulturalAge", "mesoamerica", 900, 1521, "CE",
    "Oaxaca highlands; codex tradition (only pre-Columbian books to survive); Lord Eight Deer; goldsmithing; competed with Zapotec and Aztec.")
add("purepecha", "Purépecha (Tarascan) Empire", "CulturalAge", "mesoamerica", 1300, 1530, "CE",
    "Western Mexico (Michoacán); never conquered by Aztecs; Tzintzuntzan capital; metalworking (copper, bronze); yácatas stepped pyramids.")
add("totonac", "Totonac Civilization (Civilización Totonaca / Tachiwin)", "CulturalAge", "mesoamerica", 300, 1521, "CE",
    "Veracruz Gulf coast; El Tajín with Pyramid of the Niches; Cempoala; allies of Cortés against Aztecs; voladores ceremony.")
add("epi-olmec", "Epi-Olmec Culture (Cultura Epi-Olmeca)", "CulturalAge", "mesoamerica", 300, 250, "BCE-CE",
    "Successor to Olmec in Veracruz; Tres Zapotes; La Mojarra stela with Long Count date; transitional between Olmec and Classic cultures.")

# --- Woodland & Mississippian (Eastern North America) ---
add("woodland-period", "Woodland Period (Período Woodland)", "CulturalAge", "north-america-precolumbian", 1000, 1000, "BCE-CE",
    "Eastern North America; introduction of pottery, mound building, and incipient agriculture; Adena and Hopewell traditions.")
add("adena-culture", "Adena Culture (Cultura Adena)", "CulturalAge", "woodland-period", 800, 100, "BCE",
    "Ohio Valley mound builders; conical burial mounds; Adena pipe; early cultivation of sunflower, squash; long-distance trade.")
add("hopewell-tradition", "Hopewell Tradition (Tradición Hopewell)", "CulturalAge", "woodland-period", 100, 500, "CE",
    "Middle Woodland; elaborate burial mounds and earthworks; Hopewell Interaction Sphere; obsidian, copper, shells traded across continent.")
add("mississippian-culture", "Mississippian Culture (Cultura Misisipiana)", "CulturalAge", "north-america-precolumbian", 800, 1600, "CE",
    "Complex chiefdoms across Southeast and Midwest; platform mounds; maize agriculture; Cahokia as largest city north of Mexico.")
add("cahokia", "Cahokia (Cahokia Mounds)", "CulturalAge", "mississippian-culture", 1050, 1350, "CE",
    "Largest pre-Columbian city north of Mexico (~20,000 people); Monks Mound (largest earthwork in Americas); Woodhenge; UNESCO World Heritage Site.")
add("fort-ancient", "Fort Ancient Culture (Cultura Fort Ancient)", "CulturalAge", "mississippian-culture", 1000, 1650, "CE",
    "Ohio Valley; maize-based agriculture; circular villages; Serpent Mound (Great Serpent Mound); distinct from Mississippian but contemporaneous.")
add("plaquemine", "Plaquemine Culture (Cultura Plaquemine)", "CulturalAge", "mississippian-culture", 1200, 1700, "CE",
    "Lower Mississippi Valley; platform mounds; evolved from Coles Creek; Winterville, Lake George sites; ancestral to Natchez.")

# --- Southwest Cultures ---
add("ancestral-pueblo", "Ancestral Puebloans (Anasazi)", "CulturalAge", "north-america-precolumbian", 100, 1600, "CE",
    "Four Corners region; cliff dwellings (Mesa Verde); Chaco Canyon great houses; kiva ceremonial architecture; maize, beans, squash agriculture.")
add("chaco-canyon", "Chaco Canyon Florescence (Chaco Canyon / Tségháhoodzání)", "CulturalAge", "ancestral-pueblo", 850, 1150, "CE",
    "Chaco Culture; great houses (Pueblo Bonito); road network; astronomical alignments; regional trade center; UNESCO World Heritage Site.")
add("hohokam", "Hohokam Culture (Huhugam)", "CulturalAge", "north-america-precolumbian", 300, 1450, "CE",
    "Southern Arizona; extensive canal irrigation (over 1,000 km); Snaketown; ball courts; Mesoamerican trade connections; ancestors of O'odham.")
add("mogollon", "Mogollon Culture (Cultura Mogollón)", "CulturalAge", "north-america-precolumbian", 200, 1450, "CE",
    "Southwestern mountains (Arizona, New Mexico, Chihuahua); pithouses to pueblos; Mimbres pottery with distinctive black-on-white designs.")

# --- Northwest Coast & Arctic ---
add("northwest-coast", "Northwest Coast Cultures (Kulturer vid nordvästkusten)", "CulturalAge", "north-america-precolumbian", 3000, 1774, "BCE-CE",
    "Pacific Northwest; Haida, Tlingit, Kwakwaka'wakw; cedar plank houses, totem poles, potlatch ceremonies; salmon-based economy; complex non-agricultural society.")
add("thule-culture", "Thule Culture (Thulekulturen)", "CulturalAge", "north-america-precolumbian", 200, 1600, "CE",
    "Arctic whale hunters; ancestors of modern Inuit; spread from Alaska across Canadian Arctic to Greenland; dog sleds, kayaks, umiaks.")
add("dorset-culture", "Dorset Culture (Tuniit)", "CulturalAge", "north-america-precolumbian", 500, 1500, "BCE-CE",
    "Paleo-Eskimo Arctic culture; replaced by Thule people; soapstone lamps, snow houses; miniature ivory carvings; no dog sleds or bows.")

# --- Plains & Mound Builders ---
add("plains-village", "Plains Village Period (Período de las Aldeas de las Llanuras)", "CulturalAge", "north-america-precolumbian", 1000, 1780, "CE",
    "Semi-sedentary farming communities on Great Plains; earth lodge villages; maize agriculture; Mandan, Hidatsa, Arikara, Pawnee, Wichita.")
add("iroquois-confederacy", "Haudenosaunee (Iroquois) Confederacy", "CulturalAge", "north-america-precolumbian", 1450, 1776, "CE",
    "Originally Five Nations (Mohawk, Oneida, Onondaga, Cayuga, Seneca; Tuscarora joined 1722); Great Law of Peace; longhouse society; influenced U.S. Constitution debates.")
add("taino", "Taíno Civilization (Civilización Taína)", "CulturalAge", "north-america-precolumbian", 1200, 1550, "CE",
    "Caribbean (Hispaniola, Puerto Rico, Cuba, Jamaica); first indigenous people encountered by Columbus; cacique chiefs; ball courts; zemí worship; decimated by colonization.")
add("kalinago", "Kalinago (Island Caribs)", "CulturalAge", "north-america-precolumbian", 1200, 1700, "CE",
    "Lesser Antilles (Dominica, St. Vincent, Grenada); skilled seafarers and warriors; resisted European colonization longest in Caribbean; cassava cultivation.")
add("saladoid", "Saladoid Culture (Cultura Saladoide)", "CulturalAge", "north-america-precolumbian", 500, 600, "BCE-CE",
    "Orinoco River origin; spread through Lesser Antilles to Puerto Rico; white-on-red pottery (Saladero type site); ancestral to Taíno; introduced agriculture to Caribbean.")
add("gran-cocle", "Gran Coclé Culture (Cultura Gran Coclé)", "CulturalAge", "north-america-precolumbian", 200, 1520, "CE",
    "Central Panama; Sitio Conte gold and polychrome ceramics; elaborate burial goods; goldwork (huacas); bridge between Mesoamerican and South American traditions.")
add("diquis", "Diquís Culture (Cultura Diquís)", "CulturalAge", "north-america-precolumbian", 700, 1530, "CE",
    "Southern Costa Rica; stone spheres (Las Bolas, UNESCO); gold figurines; complex chiefdoms; connection to Chibchan cultural area.")
add("cherokee-nation", "Cherokee Nation (Pre-Removal)", "CulturalAge", "north-america-precolumbian", 1540, 1838, "CE",
    "Southeast woodlands; one of 'Five Civilized Tribes'; Sequoyah's syllabary (1821); Cherokee Phoenix newspaper; Trail of Tears (1838).")

# --- European Exploration & Colonial ---
add("north-america-colonial", "Colonial North America (Nordamerika under kolonisationen)", "CulturalAge", "holocene", 1492, 1783, "CE",
    "European colonization of North America; Spanish, French, English, Dutch settlements; fur trade; displacement of indigenous peoples.")
add("spanish-exploration-na", "Spanish Exploration of North America (Exploración española de Norteamérica)", "CulturalAge", "north-america-colonial", 1492, 1600, "CE",
    "Columbus (1492); Ponce de León in Florida (1513); Coronado explores Southwest (1540); de Soto crosses Southeast; St. Augustine founded (1565).")
add("new-france", "New France (Nouvelle-France)", "CulturalAge", "north-america-colonial", 1534, 1763, "CE",
    "French colonial empire; Cartier, Champlain; Quebec (1608), Montreal (1642); fur trade; coureurs des bois; alliance with Huron-Wendat; ceded to Britain 1763.")
add("new-spain-north", "New Spain (Northern Frontier)", "CulturalAge", "north-america-colonial", 1521, 1821, "CE",
    "Spanish colonial frontier; missions and presidios; California missions (1769–1833); Santa Fe (1610); mestizo culture; Mexican independence ends era.")
add("thirteen-colonies", "Thirteen British Colonies (Tretton kolonierna)", "CulturalAge", "north-america-colonial", 1607, 1776, "CE",
    "Jamestown (1607), Plymouth (1620), Massachusetts Bay; tobacco and slavery in South; town meetings in New England; growing self-governance.")
add("new-netherland", "New Netherland (Nieuw-Nederland)", "CulturalAge", "north-america-colonial", 1614, 1667, "CE",
    "Dutch colony; New Amsterdam (Manhattan); fur trade with Lenape and Mohawk; diverse population; conquered by English (1664), becomes New York.")
add("french-indian-war", "French and Indian War (Guerre de la Conquête)", "CulturalAge", "north-america-colonial", 1754, 1763, "CE",
    "North American theater of Seven Years' War; British defeat France; Treaty of Paris (1763); France cedes Canada; sets stage for American Revolution.")

# --- American Revolution & Early Republic ---
add("american-revolution", "American Revolution (Amerikanska revolutionen)", "CulturalAge", "holocene", 1765, 1783, "CE",
    "Colonial resistance to British taxation; Declaration of Independence (1776); Revolutionary War; Treaty of Paris (1783); birth of the United States.")
add("early-american-republic", "Early American Republic (Tidiga amerikanska republiken)", "CulturalAge", "holocene", 1783, 1815, "CE",
    "Constitution ratified (1788); Bill of Rights; Washington, Adams, Jefferson; Louisiana Purchase (1803); War of 1812; westward expansion begins.")
add("jacksonian-era", "Jacksonian Era (Den jacksonianska eran)", "CulturalAge", "modern-period", 1828, 1850, "CE",
    "Andrew Jackson; expansion of white male suffrage; Indian Removal Act (1830); Trail of Tears; Manifest Destiny; Mexican-American War (1846-1848).")

# --- Westward Expansion & Civil War ---
add("antebellum-period", "Antebellum Period (Antebellumperioden)", "CulturalAge", "modern-period", 1815, 1861, "CE",
    "Pre-Civil War era; cotton kingdom and slave economy; abolitionist movement; Underground Railroad; Missouri Compromise; Compromise of 1850.")
add("american-civil-war", "American Civil War (Amerikanska inbördeskriget)", "CulturalAge", "modern-period", 1861, 1865, "CE",
    "Union vs. Confederacy; slavery as central cause; ~620,000 dead; Emancipation Proclamation (1863); Lee surrenders at Appomattox (1865).")
add("reconstruction", "Reconstruction Era (Rekonstruktionseran)", "CulturalAge", "modern-period", 1865, 1877, "CE",
    "Post-Civil War rebuilding; 13th-15th Amendments; freedmen's rights; Ku Klux Klan backlash; ends with Compromise of 1877; Jim Crow begins.")
add("gilded-age", "Gilded Age (Den förgyllda tidsåldern)", "CulturalAge", "modern-period", 1877, 1900, "CE",
    "Rapid industrialization; robber barons (Carnegie, Rockefeller, Vanderbilt); immigration waves; labor unrest; railroads; Native American displacement.")
add("mexican-american-war", "Mexican–American War (Intervención estadounidense en México)", "CulturalAge", "modern-period", 1846, 1848, "CE",
    "U.S. vs. Mexico; annexation of Texas as catalyst; Treaty of Guadalupe Hidalgo; Mexico cedes California, New Mexico, Arizona; ~55% of territory lost.")
add("california-gold-rush", "California Gold Rush (Guldrushen i Kalifornien)", "CulturalAge", "modern-period", 1848, 1855, "CE",
    "Gold discovered at Sutter's Mill (1848); ~300,000 migrants ('49ers); California statehood (1850); devastation of Native Californians; San Francisco boom.")
add("indian-wars", "Indian Wars (Indiankrigen)", "CulturalAge", "modern-period", 1860, 1890, "CE",
    "U.S. military campaigns against Indigenous nations; Sand Creek (1864); Little Bighorn (1876); Wounded Knee (1890); reservation system; Dawes Act.")
add("spanish-american-war", "Spanish–American War (Guerra hispano-estadounidense)", "CulturalAge", "modern-period", 1898, 1898, "CE",
    "U.S. vs. Spain; USS Maine; 'splendid little war'; U.S. gains Cuba, Puerto Rico, Guam, Philippines; emergence as world power.")

# --- Mexican History ---
add("mexican-history", "Mexican Historical Periods (Periodos históricos de México)", "CulturalAge", "holocene", 1521, 0, "CE",
    "Post-conquest Mexico; colonial New Spain, independence, revolution, and modern nation-state.")
add("colonial-mexico", "Colonial Mexico (New Spain)", "CulturalAge", "mexican-history", 1521, 1821, "CE",
    "Spanish viceroyalty; encomienda system; silver mining (Zacatecas, Guanajuato); Baroque art and architecture; mestizo and creole society.")
add("mexican-independence", "Mexican War of Independence (Guerra de Independencia de México)", "CulturalAge", "mexican-history", 1810, 1821, "CE",
    "Grito de Dolores (1810, Father Hidalgo); Morelos; Iturbide declares independence (1821); First Mexican Empire briefly established.")
add("mexican-republic-early", "Early Mexican Republic (Primera República Mexicana)", "CulturalAge", "mexican-history", 1824, 1876, "CE",
    "Federal republic; Texas independence (1836); Mexican-American War (1846-1848); loss of half territory; Benito Juárez; French Intervention; Maximilian.")
add("french-intervention-mexico", "French Intervention in Mexico (Segunda intervención francesa en México)", "CulturalAge", "mexican-history", 1861, 1867, "CE",
    "Napoleon III installs Maximilian as Emperor; Cinco de Mayo (1862, Battle of Puebla); Republican resistance under Juárez; Maximilian executed 1867.")
add("cristero-war", "Cristero War (Guerra Cristera)", "CulturalAge", "mexican-history", 1926, 1929, "CE",
    "Catholic uprising against anticlerical laws of Calles government; ~90,000 dead; arreglos settlement; shaped Church-state relations in Mexico.")
add("porfiriato", "Porfiriato (El Porfiriato)", "CulturalAge", "mexican-history", 1876, 1911, "CE",
    "Porfirio Díaz dictatorship; modernization, railways, foreign investment; extreme inequality; hacienda system; triggers revolution.")
add("mexican-revolution", "Mexican Revolution (Revolución Mexicana)", "CulturalAge", "mexican-history", 1910, 1920, "CE",
    "Madero, Villa, Zapata, Carranza, Obregón; 'Land and Liberty'; Constitution of 1917; agrarian reform; ~1-2 million dead.")
add("mexico-post-revolution", "Post-Revolutionary Mexico (México posrevolucionario)", "CulturalAge", "mexican-history", 1920, 2000, "CE",
    "PRI one-party rule (1929-2000); muralist movement (Rivera, Orozco, Siqueiros); oil nationalization (1938); NAFTA (1994); Zapatista uprising.")

# --- Canadian History ---
add("canadian-history", "Canadian Historical Periods (Périodes historiques du Canada)", "CulturalAge", "holocene", 1534, 0, "CE",
    "From French exploration through Confederation to modern multicultural nation.")
add("fur-trade-era", "Fur Trade Era (Ère de la traite des fourrures)", "CulturalAge", "canadian-history", 1600, 1870, "CE",
    "Hudson's Bay Company (1670) vs. North West Company; voyageurs; Métis people; York Factory; pemmican trade; shaped Canadian expansion westward.")
add("british-north-america", "British North America (Amérique du Nord britannique)", "CulturalAge", "canadian-history", 1763, 1867, "CE",
    "After Treaty of Paris; Quebec Act (1774); Loyalist migration; War of 1812; Rebellions of 1837; Responsible Government; path to Confederation.")
add("red-river-metis", "Red River and Métis Resistance (Résistance de la rivière Rouge et des Métis)", "CulturalAge", "canadian-history", 1869, 1885, "CE",
    "Louis Riel; Red River Resistance (1869-1870); Manitoba Act; North-West Rebellion (1885); Riel executed; Métis land rights; shaping of Western Canada.")
add("klondike-gold-rush", "Klondike Gold Rush (Ruée vers l'or du Klondike)", "CulturalAge", "canadian-history", 1896, 1899, "CE",
    "Gold discovered on Bonanza Creek, Yukon (1896); ~100,000 stampeders; Dawson City boom; Chilkoot Pass; Canadian sovereignty asserted in North.")
add("canadian-confederation", "Canadian Confederation (Confédération canadienne)", "CulturalAge", "canadian-history", 1867, 1931, "CE",
    "Dominion of Canada (1867); transcontinental railway (1885); Western settlement; Riel Rebellions; WWI and Vimy Ridge; Statute of Westminster (1931).")
add("modern-canada", "Modern Canada (Canada moderne)", "CulturalAge", "canadian-history", 1931, 0, "CE",
    "WWII; welfare state; Quiet Revolution in Quebec; Official Languages Act (1969); Charter of Rights (1982); multiculturalism; reconciliation with Indigenous peoples.")

# --- US 20th–21st Century ---
add("progressive-era", "Progressive Era (Progressiva eran)", "CulturalAge", "modern-period", 1896, 1920, "CE",
    "Reform movements; trust-busting (Roosevelt); women's suffrage (19th Amendment, 1920); muckraking journalism; conservation movement.")
add("roaring-twenties-na", "Roaring Twenties (North America)", "CulturalAge", "contemporary", 1920, 1929, "CE",
    "Jazz Age; Harlem Renaissance; Prohibition; economic boom; Model T; cultural modernism; ends with Wall Street Crash (1929).")
add("great-depression-na", "Great Depression (North America)", "CulturalAge", "contemporary", 1929, 1939, "CE",
    "Wall Street Crash; ~25% unemployment; Dust Bowl; New Deal (FDR); Social Security; transformation of federal government role.")
add("us-wwii", "United States in World War II (USA under andra världskriget)", "CulturalAge", "contemporary", 1941, 1945, "CE",
    "Pearl Harbor (1941); Arsenal of Democracy; D-Day (1944); Pacific island-hopping; Manhattan Project; atomic bombs on Hiroshima and Nagasaki (1945).")
add("us-cold-war", "Cold War (United States)", "CulturalAge", "contemporary", 1947, 1991, "CE",
    "Containment doctrine; Korean War (1950-53); McCarthyism; Cuban Missile Crisis (1962); Vietnam War; détente; Reagan buildup; fall of Berlin Wall (1989).")
add("us-civil-rights", "Civil Rights Movement (Medborgarrättsrörelsen)", "CulturalAge", "contemporary", 1954, 1968, "CE",
    "Brown v. Board (1954); Montgomery Bus Boycott; March on Washington (1963); Civil Rights Act (1964); Voting Rights Act (1965); MLK assassinated (1968).")
add("vietnam-war-era", "Vietnam War Era (Chiến tranh Việt Nam)", "CulturalAge", "contemporary", 1955, 1975, "CE",
    "U.S. involvement in Vietnam; Gulf of Tonkin (1964); Tet Offensive (1968); anti-war movement; Kent State; Fall of Saigon (1975); ~58,000 U.S. dead.")
add("space-race", "Space Race (Kapplöpningen till rymden)", "CulturalAge", "contemporary", 1957, 1975, "CE",
    "U.S.-Soviet competition; Sputnik (1957); Mercury, Gemini programs; Apollo 11 Moon landing (1969); NASA; Apollo-Soyuz (1975).")
add("post-911-era", "Post-9/11 Era (Eran efter 11 september)", "CulturalAge", "contemporary", 2001, 2021, "CE",
    "September 11 attacks; War on Terror; Afghanistan War (2001-2021); Iraq War (2003); Patriot Act; Department of Homeland Security; reshaping of U.S. foreign policy.")

# ═══════════════════════════════════════════════════════════════
# AFRICAN HISTORICAL & CULTURAL PERIODS
# ═══════════════════════════════════════════════════════════════

# --- Cradle of Humankind & Prehistoric ---
add("africa-prehistoric", "Prehistoric Africa (Förhistoriska Afrika)", "CulturalAge", "holocene", 3300000, 3100, "BCE",
    "Birthplace of Homo sapiens; earliest stone tools (Lomekwian ~3.3 Ma); earliest modern human behavior; rock art; Neolithic revolution in Sahara and Nile; transition to complex societies.")
add("african-early-stone-age", "African Early Stone Age (Afrikanska äldre stenåldern / ESA)", "CulturalAge", "africa-prehistoric", 3300000, 300000, "BCE",
    "Oldest stone tool traditions: Lomekwian (~3.3 Ma), Oldowan (~2.6 Ma, Homo habilis), Acheulean (~1.76 Ma, Homo erectus/heidelbergensis); hand axes; control of fire; covers c. 3.3 million to ~300,000 years ago. African archaeological periodization: ESA/MSA/LSA (distinct from European Paleolithic/Mesolithic/Neolithic framework).")
add("african-middle-stone-age", "African Middle Stone Age (Afrikanska mellersta stenåldern / MSA)", "CulturalAge", "africa-prehistoric", 300000, 30000, "BCE",
    "Emergence of Homo sapiens; Blombos Cave engravings (~75,000 BP); ochre use; shell beads; earliest evidence of symbolic thought and art.")
add("african-later-stone-age", "African Later Stone Age (Afrikanska senare stenåldern / LSA)", "CulturalAge", "africa-prehistoric", 50000, 2000, "BCE",
    "Microlithic tools; bow and arrow; San rock art (southern Africa); population diversification; expansion across continent.")
add("saharan-neolithic", "Saharan Neolithic (Green Sahara)", "CulturalAge", "africa-prehistoric", 7500, 3500, "BCE",
    "African Humid Period; cattle pastoralism; rock art at Tassili n'Ajjer; pottery; lakeside settlements; desertification drives migration to Nile.")
add("nile-predynastic", "Predynastic Nile Valley (مصر ما قبل الأسرات Miṣr mā qabl al-usrāt)", "CulturalAge", "africa-prehistoric", 5500, 3100, "BCE",
    "Badarian, Naqada I–III cultures; early agriculture; social stratification; Upper and Lower Egypt emerge; writing begins ~3200 BCE.")

# --- Ancient Egypt ---
add("ancient-egypt", "Ancient Egypt (Kemet / مصر القديمة)", "CulturalAge", "holocene", 3100, 30, "BCE",
    "One of the world's first civilizations; self-named km.t ('Black Land'); 3,000 years of pharaonic rule along the Nile; pyramids, hieroglyphs, monumental architecture.")
add("egypt-early-dynastic", "Early Dynastic Egypt (عصر الأسرات المبكر)", "CulturalAge", "ancient-egypt", 3100, 2686, "BCE",
    "Unification of Upper and Lower Egypt; Narmer/Menes; Memphis as capital; First and Second Dynasties; development of hieroglyphic writing.")
add("egypt-old-kingdom", "Old Kingdom of Egypt (الدولة القديمة ad-Dawla al-Qadīma)", "CulturalAge", "ancient-egypt", 2686, 2181, "BCE",
    "Age of the Pyramids; Djoser's Step Pyramid; Great Pyramid of Giza (Khufu); Sphinx; centralized pharaonic power; 3rd–6th Dynasties.")
add("egypt-first-intermediate", "First Intermediate Period (عصر الاضمحلال الأول)", "CulturalAge", "ancient-egypt", 2181, 2055, "BCE",
    "Collapse of central authority; regional rulers; famine and social upheaval; 7th–11th Dynasties; Herakleopolis vs. Thebes.")
add("egypt-middle-kingdom", "Middle Kingdom of Egypt (الدولة الوسطى ad-Dawla al-Wusṭā)", "CulturalAge", "ancient-egypt", 2055, 1650, "BCE",
    "Reunification under Mentuhotep II; classical Egyptian literature; Faiyum irrigation; trade with Nubia and Levant; 11th–13th Dynasties.")
add("egypt-second-intermediate", "Second Intermediate Period (Hyksos)", "CulturalAge", "ancient-egypt", 1650, 1550, "BCE",
    "Hyksos ('rulers of foreign lands') control Lower Egypt; introduce horse and chariot, composite bow; Theban resistance; 15th–17th Dynasties.")
add("egypt-new-kingdom", "New Kingdom of Egypt (الدولة الحديثة ad-Dawla al-Ḥadītha)", "CulturalAge", "ancient-egypt", 1550, 1069, "BCE",
    "Egypt's golden age; Valley of the Kings; Hatshepsut, Thutmose III, Akhenaten, Tutankhamun, Ramesses II; empire from Nubia to Syria.")
add("amarna-period", "Amarna Period (عصر العمارنة ʿAṣr al-ʿAmārna)", "CulturalAge", "egypt-new-kingdom", 1353, 1336, "BCE",
    "Akhenaten's religious revolution; monotheistic Atenism; new capital Akhetaten (Amarna); Nefertiti; distinctive art style; reversed after his death.")
add("ramesside-period", "Ramesside Period (عصر الرعامسة ʿAṣr ar-Raʿāmisa)", "CulturalAge", "egypt-new-kingdom", 1292, 1069, "BCE",
    "19th–20th Dynasties; Ramesses II (Battle of Kadesh, Abu Simbel); Sea Peoples invasions; gradual decline of Egyptian power.")
add("egypt-third-intermediate", "Third Intermediate Period (عصر الاضمحلال الثالث)", "CulturalAge", "ancient-egypt", 1069, 664, "BCE",
    "Fragmentation; Libyan and Nubian pharaohs; Shoshenq I (biblical Shishak); Theban high priests; 21st–25th Dynasties.")
add("egypt-late-period", "Late Period of Egypt (العصر المتأخر al-ʿAṣr al-Mutaʾakhkhir)", "CulturalAge", "ancient-egypt", 664, 332, "BCE",
    "Saite Renaissance (26th Dynasty); Persian conquests (27th, 31st Dynasties); last native dynasties; Nectanebo II last Egyptian pharaoh.")
add("ptolemaic-egypt", "Ptolemaic Egypt (مصر البطلمية / Πτολεμαϊκή Αίγυπτος)", "CulturalAge", "ancient-egypt", 332, 30, "BCE",
    "Alexander conquers Egypt (332 BCE); Ptolemaic dynasty; Library of Alexandria; Rosetta Stone; Cleopatra VII; annexed by Rome (30 BCE).")

# --- Nubia & Kush ---
add("nubia-kush", "Nubian and Kushite Civilizations (الحضارة النوبية والكوشية)", "CulturalAge", "holocene", 2500, 350, "BCE-CE",
    "Civilizations along Upper Nile (modern Sudan); rivals and successors of Egypt; pyramids of Meroë; iron production; distinct art and religion.")
add("kerma-culture", "Kingdom of Kerma (مملكة كرمة)", "CulturalAge", "nubia-kush", 2500, 1500, "BCE",
    "First major Nubian kingdom; capital at Kerma; monumental deffufas (mud-brick temples); wealthy burials; rival to Egyptian Middle Kingdom.")
add("kingdom-kush", "Kingdom of Kush (Napatan)", "CulturalAge", "nubia-kush", 1070, 300, "BCE",
    "Napata capital; 25th Dynasty pharaohs rule Egypt (Piye, Taharqa ~700 BCE); expelled by Assyrians; capital shifts to Meroe ~300 BCE.")
add("meroe", "Meroitic Period (الفترة المروية)", "CulturalAge", "nubia-kush", 270, 350, "BCE-CE",
    "Capital moves to Meroë; iron smelting center; Meroitic script (deciphered, but language only partially understood); over 200 pyramids; Kandake (queen) warriors; trade with Rome.")

# --- Horn of Africa ---
add("land-of-punt", "Land of Punt (أرض بونت Arḍ Būnt / Pwnt)", "CulturalAge", "holocene", 2500, 1000, "BCE",
    "Legendary trading partner of Egypt; source of incense, gold, ebony; Hatshepsut's expedition (~1470 BCE); location debated (Eritrea/Somalia/Djibouti).")
add("daamt", "Kingdom of D'mt (ዳዕማት Daʿmat)", "CulturalAge", "holocene", 980, 400, "BCE",
    "Early kingdom in Eritrea/northern Ethiopia; Sabaean cultural influences; Yeha temple; precursor to Aksumite civilization.")
add("aksum", "Kingdom of Aksum (መንግሥተ አክሱም Mangəśtä Aksūm)", "CulturalAge", "holocene", 100, 940, "CE",
    "Major trading empire; Adulis port; obelisks of Aksum; adopted Christianity (~330 CE, King Ezana); Ge'ez script; one of the 'four great empires' of antiquity.")
add("zagwe-dynasty", "Zagwe Dynasty (ዛጉዌ ሥርወ መንግሥት)", "CulturalAge", "holocene", 1137, 1270, "CE",
    "Ethiopian highland dynasty; rock-hewn churches of Lalibela (UNESCO); Christian kingdom; succeeded Aksumite decline.")
add("solomonic-dynasty", "Solomonic Dynasty (የሰለሞን ሥርወ መንግሥት)", "CulturalAge", "holocene", 1270, 1974, "CE",
    "Ethiopian ruling dynasty claiming descent from Solomon and Sheba; Kebra Nagast; Prester John legends; Gondar castles; Haile Selassie last emperor.")

# --- West Africa ---
add("west-africa-ancient", "Ancient West African Civilizations (Civilisations anciennes d'Afrique de l'Ouest)", "CulturalAge", "holocene", 1000, 1900, "BCE-CE",
    "Trans-Saharan trade; gold, salt, slaves; powerful empires and kingdoms; Islam spreads from 8th century; rich oral traditions and art.")
add("nok-culture", "Nok Culture (Nok-kulturen)", "CulturalAge", "west-africa-ancient", 1000, 300, "BCE-CE",
    "Central Nigeria; earliest known sub-Saharan terracotta sculptures; early iron smelting in West Africa; agricultural communities.")
add("ghana-empire", "Ghana Empire (Wagadu)", "CulturalAge", "west-africa-ancient", 300, 1200, "CE",
    "First great West African empire; gold-salt trade; Koumbi Saleh capital; 'Land of Gold'; Soninke people; weakened by Almoravids (~1076).")
add("mali-empire", "Mali Empire (Manden Kurufaba)", "CulturalAge", "west-africa-ancient", 1235, 1600, "CE",
    "Founded by Sundiata Keita; Mansa Musa's pilgrimage to Mecca (1324, richest person ever); Timbuktu university; Manding Charter.")
add("songhai-empire", "Songhai Empire (Songhay)", "CulturalAge", "west-africa-ancient", 1464, 1591, "CE",
    "Largest empire in African history; Sunni Ali, Askia Muhammad; Timbuktu, Djenné; conquered by Moroccan invasion (1591).")
add("kanem-bornu", "Kanem-Bornu Empire (Empire du Kanem-Bornou)", "CulturalAge", "west-africa-ancient", 700, 1900, "CE",
    "Lake Chad basin; one of longest-lasting African empires (~1,100 years); Sayfawa dynasty; trans-Saharan trade; Islam from 11th century.")
add("benin-kingdom", "Kingdom of Benin (Ọba N'Ẹdó)", "CulturalAge", "west-africa-ancient", 1180, 1897, "CE",
    "Edo people, southern Nigeria; Benin Bronzes (sophisticated lost-wax casting); Oba rulers; city walls; destroyed by British punitive expedition (1897).")
add("oyo-empire", "Oyo Empire (Ilú Ọ̀yọ́)", "CulturalAge", "west-africa-ancient", 1400, 1896, "CE",
    "Yoruba empire; powerful cavalry; Alaafin rulers; Atlantic trade; Oyo ile capital; influenced Yoruba diaspora culture in Americas.")
add("ashanti-empire", "Ashanti Empire (Asanteman / Asante Hene)", "CulturalAge", "west-africa-ancient", 1701, 1902, "CE",
    "Akan people, modern Ghana; Golden Stool; Osei Tutu I; gold trade; kente cloth; resisted British colonization; Anglo-Ashanti Wars.")
add("jolof-empire", "Jolof Empire (Buurba Jolof)", "CulturalAge", "west-africa-ancient", 1350, 1549, "CE",
    "Wolof confederacy in Senegal; former Mali vassal; major early Atlantic slave trade participant; dissolved at Battle of Danki (1549).")
add("kingdom-of-dahomey", "Kingdom of Dahomey (Danhomè)", "CulturalAge", "west-africa-ancient", 1600, 1904, "CE",
    "Fon people, modern Benin; Dahomey Amazons (Mino) all-female regiment; Vodun religion origin; major slave-trading state; fell to French 1892.")
add("mossi-kingdoms", "Mossi Kingdoms (Moogo)", "CulturalAge", "west-africa-ancient", 1050, 1896, "CE",
    "Upper Volta (Burkina Faso); Mogho Naaba supreme ruler; raided Timbuktu (1329); resisted Islamization; largest ethnic group in Burkina Faso today.")
add("hausa-city-states", "Hausa City-States (Ƙasashen Hausa)", "CulturalAge", "west-africa-ancient", 1000, 1808, "CE",
    "Northern Nigeria/Niger; Kano, Katsina, Zaria; trans-Saharan trade hubs; indigo-dyed cloth; Islamic learning; conquered by Fulani jihad (1804).")
add("sokoto-caliphate", "Sokoto Caliphate (خلافة صكتو Ḫilāfat Sokoto)", "CulturalAge", "west-africa-ancient", 1804, 1903, "CE",
    "Fulani jihad led by Usman dan Fodio; largest state in 19th-century Africa; Islamic scholarship; conquered by British (1903).")
add("timbuktu-golden-age", "Golden Age of Timbuktu (Âge d'or de Tombouctou)", "CulturalAge", "mali-empire", 1300, 1600, "CE",
    "Major intellectual center; Sankore University; 100,000+ manuscripts; Islamic scholarship; Ahmed Baba; gold-salt trade crossroads.")
add("ife-kingdom", "Kingdom of Ifẹ̀ (Ilé-Ifẹ̀)", "CulturalAge", "west-africa-ancient", 1000, 1420, "CE",
    "Sacred Yoruba city; naturalistic bronze and terracotta portrait heads (among finest art in world history); Ooni rulers; spiritual capital of all Yoruba people; influenced Benin Kingdom art tradition; Ife bronzes predate European Renaissance.")

# --- East & Southeast Africa ---
add("swahili-coast", "Swahili Coast Civilization (Ustaarabu wa Pwani ya Swahili)", "CulturalAge", "holocene", 100, 1500, "CE",
    "Indian Ocean trading cities; Kilwa, Mombasa, Zanzibar, Mogadishu; Swahili language (Bantu with Arabic loanwords); stone towns; gold, ivory, spice trade.")
add("kilwa-sultanate", "Kilwa Sultanate (Usultani wa Kilwa)", "CulturalAge", "swahili-coast", 960, 1513, "CE",
    "Wealthiest Swahili city-state; controlled gold trade from Great Zimbabwe; Great Mosque of Kilwa; copper coins; sacked by Portuguese (1505).")
add("great-zimbabwe", "Great Zimbabwe (Dzimba dza mabwe)", "CulturalAge", "holocene", 1100, 1450, "CE",
    "Largest stone structure in sub-Saharan Africa; name means 'houses of stone' in Shona; Great Enclosure; gold trade; ~18,000 inhabitants; inspired modern Zimbabwe's name.")
add("mutapa-empire", "Kingdom of Mutapa (Wene wa Mutapa)", "CulturalAge", "holocene", 1430, 1760, "CE",
    "Successor to Great Zimbabwe; controlled gold-producing region; Shona; Portuguese trade and interference; 'emperor of gold mines'.")
add("buganda-kingdom", "Kingdom of Buganda (Obwakabaka bwa Buganda)", "CulturalAge", "holocene", 1300, 1966, "CE",
    "Central Uganda; Lake Victoria; Kabaka rulers; sophisticated political system; resisted and then accommodated British; integral to modern Uganda.")
add("zanzibar-sultanate", "Zanzibar Sultanate (Usultani wa Zanzibar)", "CulturalAge", "holocene", 1856, 1964, "CE",
    "Independent from Oman after Said bin Sultan's death (1856); dominated East African slave trade; world's leading clove producer; Anglo-Zanzibar War (38 min); merged into Tanzania.")
add("bunyoro-kitara", "Bunyoro-Kitara Empire (Obukama bwa Bunyoro-Kitara)", "CulturalAge", "holocene", 1300, 1899, "CE",
    "Successor to legendary Chwezi Empire; Babiito dynasty; one of most powerful Great Lakes kingdoms; Omukama Kabalega resisted British; restored 1993.")
add("adal-sultanate", "Adal Sultanate (سلطنة عدل Salṭanat ʿAdal)", "CulturalAge", "holocene", 1415, 1577, "CE",
    "Somali-Harari Islamic state; Imam Ahmad ibn Ibrahim al-Ghazi's jihad conquered vast Ethiopian territory (1529); controlled parts of Somalia, Ethiopia, Djibouti.")
add("ajuran-sultanate", "Ajuran Sultanate (Dawladda Ajuuraan)", "CulturalAge", "holocene", 1200, 1700, "CE",
    "Africa's only known hydraulic empire; monopolized Shebelle/Jubba rivers; Indian Ocean trade; repelled Portuguese; limestone wells still in use today.")

# --- Southern Africa ---
add("mapungubwe", "Kingdom of Mapungubwe (Mmuso wa Mapungubwe)", "CulturalAge", "holocene", 1075, 1220, "CE",
    "First major southern African kingdom; gold trade; distinctive golden rhinoceros; social stratification; predecessor to Great Zimbabwe; UNESCO site.")
add("zulu-kingdom", "Zulu Kingdom (uMbuso kaZulu)", "CulturalAge", "holocene", 1816, 1897, "CE",
    "Founded by Shaka Zulu; revolutionary military tactics (iklwa spear, impi regiments); Mfecane/Difaqane upheaval; Anglo-Zulu War (1879, Isandlwana).")
add("mfecane", "Mfecane/Difaqane (umFecane / Lifaqane)", "CulturalAge", "holocene", 1815, 1840, "CE",
    "Period of widespread chaos and migration in southern Africa; triggered by Zulu expansion; Ndebele, Swazi, Sotho, Nguni states formed.")
add("rozwi-empire", "Rozwi Empire (Rozvi)", "CulturalAge", "holocene", 1684, 1834, "CE",
    "Shona state; Changamire Dombo expelled Portuguese from Zambezi; revived monumental stone architecture; fell to Ndebele during Mfecane.")
add("ndebele-kingdom", "Ndebele Kingdom (Mthwakazi)", "CulturalAge", "holocene", 1823, 1894, "CE",
    "Founded by Mzilikazi, former Shaka lieutenant; crossed Limpopo to Matabeleland; Lobengula; fell to British South Africa Company (1893).")
add("basotho-kingdom", "Basotho Kingdom (Lesotho)", "CulturalAge", "holocene", 1822, 1966, "CE",
    "Moshoeshoe I united Mfecane refugees; Thaba Bosiu stronghold; defeated British at Viervoet and Berea; secured British protection 1868; independent 1966.")
add("maravi-confederacy", "Maravi Confederacy (Malaui)", "CulturalAge", "holocene", 1480, 1720, "CE",
    "Namesake of modern Malawi; Kalonga rulers from Mankhamba; ivory and iron trade with Swahili and Portuguese; Zimba raiders.")
add("khoisan-pastoral", "Khoisan Pastoral Period (Khoisan-pastoral perioden)", "CulturalAge", "africa-prehistoric", 2000, 1652, "BCE-CE",
    "Khoikhoi pastoralists and San hunter-gatherers; southern Africa; earliest inhabitants; click languages; rock art tradition spanning millennia.")

# --- Central Africa ---
add("bantu-expansion", "Bantu Expansion (Uenezi wa Wabantu)", "CulturalAge", "holocene", 1000, 500, "BCE-CE",
    "One of the largest migrations in human history; Bantu-speaking peoples spread from Cameroon/Nigeria across central, eastern, and southern Africa; iron, agriculture, languages.")
add("kongo-kingdom", "Kingdom of Kongo (Wene wa Kongo)", "CulturalAge", "holocene", 1390, 1914, "CE",
    "Central Africa (modern Angola, DRC, Congo); Mbanza Kongo capital; early contact with Portugal (1483); conversion to Christianity; Atlantic slave trade devastation.")
add("luba-kingdom", "Luba Kingdom (Bulopwe / Royaume Luba)", "CulturalAge", "holocene", 1585, 1889, "CE",
    "Central Congo basin; sophisticated governance (balopwe sacred kingship); memory boards (lukasa); influence on Lunda and other kingdoms.")
add("lunda-empire", "Lunda Empire (Mwaant Yaav / Empire Lunda)", "CulturalAge", "holocene", 1665, 1887, "CE",
    "Offshoot of Luba; vast territory across central-southern Africa; long-distance trade; influenced political systems across a wide region.")
add("kingdom-of-rwanda", "Kingdom of Rwanda (Ubwami bw'u Rwanda)", "CulturalAge", "holocene", 1500, 1961, "CE",
    "Most centralized Great Lakes kingdom; divine Mwami; Kigeri IV Rwabugiri expanded beyond modern borders; colonial Belgium racialized Hutu-Tutsi; monarchy abolished 1961.")
add("kingdom-of-burundi", "Kingdom of Burundi (Ubwami bw'Urundi)", "CulturalAge", "holocene", 1680, 1966, "CE",
    "Ganwa royal dynasty (neither Hutu nor Tutsi); Mwezi IV Gisabo resisted Germans; direct territorial continuation of pre-colonial state; monarchy ended by coup 1966.")

# --- Madagascar ---
add("merina-kingdom", "Merina Kingdom (Fanjakan'Imerina)", "CulturalAge", "holocene", 1540, 1897, "CE",
    "Dominated Madagascar; Andrianampoinimerina unified kingdom; Radama I gained British recognition; Antananarivo capital; fell to French colonization 1895-97.")

# --- Sudan ---
add("funj-sultanate", "Funj Sultanate of Sennar (سلطنة سنار)", "CulturalAge", "holocene", 1504, 1821, "CE",
    "Blue Sultanate; 300+ years; central to Islamization of Sudan; defeated Ottomans at Hannik (1585); major trading city; fell to Muhammad Ali's Egypt 1821.")
add("darfur-sultanate", "Sultanate of Darfur (سلطنة دارفور)", "CulturalAge", "holocene", 1603, 1916, "CE",
    "Keira dynasty; Islam state religion; Darb al-Arba'in trade route to Egypt; nearly twice the size of France at peak; colonial neglect root of modern conflict.")

# --- North Africa (Post-Ancient) ---
add("north-africa-islamic", "Islamic North Africa (شمال أفريقيا الإسلامي)", "CulturalAge", "holocene", 647, 1830, "CE",
    "Arab conquest of the Maghreb; Berber dynasties; al-Andalus connections; Fatimids, Almohads, Marinids, Hafsids, Ottomans.")
add("umayyad-maghreb", "Umayyad Conquest of the Maghreb (الفتح الأموي للمغرب)", "CulturalAge", "north-africa-islamic", 647, 750, "CE",
    "Arab armies conquer North Africa; fall of Carthage (698); Berber resistance (Kahina); springboard for conquest of Iberia (711).")
add("almoravid", "Almoravid Dynasty (المرابطون al-Murābiṭūn)", "CulturalAge", "north-africa-islamic", 1040, 1147, "CE",
    "Berber dynasty from Sahara; conquered Morocco, western Algeria, al-Andalus; Marrakech founded (1070); trans-Saharan gold trade.")
add("almohad", "Almohad Caliphate (الموحدون al-Muwaḥḥidūn)", "CulturalAge", "north-africa-islamic", 1121, 1269, "CE",
    "Berber reformist dynasty; largest Berber empire; Koutoubia Mosque, Giralda; controlled Maghreb and al-Andalus; defeated at Las Navas de Tolosa (1212).")
add("fatimid-caliphate-africa", "Fatimid Caliphate (North Africa)", "CulturalAge", "north-africa-islamic", 909, 1171, "CE",
    "Ismaili Shia caliphate; founded in Tunisia; conquered Egypt, founded Cairo (969); Al-Azhar University; rivaled Abbasid Baghdad.")
add("vandal-kingdom", "Vandal Kingdom (Regnum Vandalorum)", "CulturalAge", "holocene", 429, 534, "CE",
    "Germanic kingdom in North Africa; Gaiseric captured Carthage (439); sacked Rome (455); controlled Tunisia, Sardinia, Corsica; defeated by Belisarius 534.")
add("idrisid-dynasty", "Idrisid Dynasty (الأدارسة)", "CulturalAge", "north-africa-islamic", 788, 974, "CE",
    "Morocco's first independent Islamic dynasty; descendant of Prophet Muhammad; son Idris II founded Fez (808); Al-Qarawiyyin (oldest university); Sharifian precedent.")
add("marinid-dynasty", "Marinid Dynasty (المرينيون)", "CulturalAge", "north-africa-islamic", 1244, 1465, "CE",
    "Zenata Berbers; Fez golden age; Morocco's first madrasas; Ibn Khaldun and Ibn Battuta products of this milieu; defeated at Rio Salado (1340).")
add("hafsid-dynasty", "Hafsid Dynasty (الحفصيون)", "CulturalAge", "north-africa-islamic", 1229, 1574, "CE",
    "Ruled Ifriqiya (Tunisia, Libya, Algeria) 345 years; al-Mustansir proclaimed Caliph after Mongol sack of Baghdad; fell to Ottomans 1574.")
add("barbary-states", "Barbary States (إيالات بربرية / États barbaresques)", "CulturalAge", "north-africa-islamic", 1516, 1830, "CE",
    "Ottoman-aligned North African regencies; Algiers, Tunis, Tripoli; corsair piracy; Barbary Wars with U.S.; French conquest of Algiers (1830).")

# --- Colonialism & Independence ---
add("scramble-for-africa", "Scramble for Africa (Kugawanywa kwa Afrika / La course au clocher)", "CulturalAge", "modern-period", 1881, 1914, "CE",
    "European partition of Africa; Berlin Conference (1884-85); only Ethiopia and Liberia remain independent; arbitrary borders; exploitation of resources and peoples.")
add("colonial-africa", "Colonial Africa (Koloniala Afrika)", "CulturalAge", "modern-period", 1884, 1966, "CE",
    "European colonial rule; British, French, Portuguese, Belgian, German, Italian, Spanish territories; extraction economies; forced labor; resistance movements.")
add("atlantic-slave-trade", "Atlantic Slave Trade (Maafa / تجارة الرقيق عبر الأطلسي)", "CulturalAge", "holocene", 1501, 1867, "CE",
    "Forced transportation of ~12.5 million Africans to the Americas; devastating demographic and social impact; abolished progressively through 19th century.")
add("congo-free-state", "Congo Free State (État indépendant du Congo)", "CulturalAge", "colonial-africa", 1885, 1908, "CE",
    "Personal colony of Leopold II of Belgium; rubber terror; forced labor; hand amputations; estimated 1-10 million dead; international outcry.")
add("mau-mau-uprising", "Mau Mau Uprising (Mau Mau / Kĩmaathi)", "CulturalAge", "colonial-africa", 1952, 1960, "CE",
    "Kikuyu-led rebellion against British rule in Kenya; detention camps; Jomo Kenyatta; catalyst for Kenyan independence (1963).")
add("african-independence", "African Independence Movements (Afrikanska självständighetsrörelserna)", "CulturalAge", "contemporary", 1951, 1994, "CE",
    "Wave of decolonization; Ghana first sub-Saharan (1957, Nkrumah); Year of Africa (1960, 17 nations); last: South Africa apartheid ends (1994).")
add("pan-africanism", "Pan-African Movement (Panafrikanska rörelsen)", "CulturalAge", "modern-period", 1900, 1963, "CE",
    "Du Bois, Garvey, Nkrumah, Nyerere; Pan-African Congresses; négritude; Organization of African Unity founded (1963); African unity ideology.")
add("apartheid", "Apartheid South Africa (Apartheid Suid-Afrika)", "CulturalAge", "contemporary", 1948, 1994, "CE",
    "Institutionalized racial segregation; ANC resistance; Sharpeville (1960); Soweto (1976); Mandela imprisoned 27 years; free elections 1994.")
add("rwandan-genocide", "Rwandan Genocide (Jenoside yakorewe Abatutsi)", "CulturalAge", "contemporary", 1994, 1994, "CE",
    "~800,000 Tutsi and moderate Hutu killed in 100 days; international failure to intervene; RPF ends genocide; Gacaca justice; reconciliation.")
add("african-union-era", "African Union Era (الاتحاد الأفريقي / Union africaine)", "CulturalAge", "contemporary", 2002, 0, "CE",
    "AU succeeds OAU (2002); Agenda 2063; peacekeeping missions; AfCFTA free trade area (2021); economic growth; demographic dividend; challenges remain.")

# ═══════════════════════════════════════════════════════════════
# ASIAN HISTORICAL & CULTURAL PERIODS
# ═══════════════════════════════════════════════════════════════

# --- Indus Valley & South Asia (Ancient) ---
add("south-asia-history", "South Asian Historical Periods (दक्षिण एशिया के ऐतिहासिक काल)", "CulturalAge", "holocene", 7000, 0, "BCE-CE",
    "From Mehrgarh Neolithic through Indus Valley, Vedic, Mauryan, Mughal to modern India, Pakistan, Bangladesh, Sri Lanka.")
add("mehrgarh", "Mehrgarh (مہرگڑھ Mehrgaṛh)", "CulturalAge", "south-asia-history", 7000, 2500, "BCE",
    "Neolithic site in Balochistan; one of earliest farming settlements in South Asia; precursor to Indus Valley; dentistry evidence ~7000 BCE.")
add("indus-valley", "Indus Valley Civilization (सिन्धु घाटी सभ्यता)", "CulturalAge", "south-asia-history", 3300, 1300, "BCE",
    "Harappa, Mohenjo-daro; urban planning, drainage systems; undeciphered script; ~5 million people; one of three earliest civilizations.")
add("indus-early", "Early Harappan Phase (प्रारंभिक हड़प्पा काल / ابتدائی ہڑپہ دور)", "CulturalAge", "indus-valley", 3300, 2600, "BCE",
    "Pre-urban phase; small farming communities; Ravi and Kot Diji cultures; early pottery and copper tools; transition to urban phase c. 2600 BCE; sites include Rehman Dheri and Amri.")
add("indus-mature", "Mature Harappan Phase (परिपक्व हड़प्पा काल / پختہ ہڑپہ دور)", "CulturalAge", "indus-valley", 2600, 1900, "BCE",
    "Peak of Indus civilization; standardized weights and measures; Great Bath of Mohenjo-daro; trade with Mesopotamia; citadel-lower town layout.")
add("indus-late", "Late Harappan Phase (उत्तर हड़प्पा काल / آخری ہڑپہ دور)", "CulturalAge", "indus-valley", 1900, 1300, "BCE",
    "Post-urban decline; abandonment of major cities; Cemetery H and Gandhara Grave cultures; localization of material culture; climate change and monsoon shifts implicated in collapse; possible continuity into early Vedic culture.")
add("vedic-period", "Vedic Period (वैदिक काल)", "CulturalAge", "south-asia-history", 1500, 500, "BCE",
    "Composition of the Vedas (Rigveda ~1500 BCE); Sanskrit; varna system; Aryan migration debate; transition from pastoral to settled agriculture.")
add("vedic-early", "Early Vedic Period (पूर्व वैदिक काल Pūrva Vaidika Kāl)", "CulturalAge", "vedic-period", 1500, 1000, "BCE",
    "Rigveda composition; pastoral-nomadic society; Indra worship; tribal kingdoms (janapadas); Punjab region focus.")
add("vedic-late", "Late Vedic Period (उत्तर वैदिक काल Uttara Vaidika Kāl)", "CulturalAge", "vedic-period", 1000, 500, "BCE",
    "Expansion to Ganges plain; Painted Grey Ware; Upanishads; emergence of Buddhism and Jainism; Mahajanapadas (16 great kingdoms).")
add("maurya-empire", "Maurya Empire (मौर्य साम्राज्य)", "CulturalAge", "south-asia-history", 322, 185, "BCE",
    "First pan-Indian empire; Chandragupta Maurya; Ashoka the Great (~268-232 BCE); edicts of non-violence; Arthashastra; Pataliputra capital.")
add("ashoka", "Reign of Ashoka (अशोक का शासनकाल / 𑀅𑀲𑁄𑀓 Asoka)", "CulturalAge", "maurya-empire", 268, 232, "BCE",
    "Greatest Mauryan emperor; Kalinga War conversion to Buddhism; rock and pillar edicts; Lion Capital (Indian national emblem); spread of Dharma.")
add("gandhara", "Gandhara Civilization (گندھارا / गन्धार Gandhāra)", "CulturalAge", "south-asia-history", 600, 1021, "BCE-CE",
    "Northwest Pakistan/eastern Afghanistan; Greco-Buddhist art synthesis; Taxila university; Alexander's campaigns; Kushan patronage; Hindu Shahi; fell to Ghaznavids.")
add("kushan-empire", "Kushan Empire (कुषाण साम्राज्य Kuṣāṇa)", "CulturalAge", "south-asia-history", 30, 375, "CE",
    "Central Asian origin; Kanishka I; Gandhara Buddhist art (Greco-Buddhist); Silk Road trade; Mathura and Peshawar; spread Buddhism to China.")
add("gupta-empire", "Gupta Empire (गुप्त साम्राज्य)", "CulturalAge", "south-asia-history", 320, 550, "CE",
    "Golden Age of India; Chandragupta I, Samudragupta, Chandragupta II; Aryabhata (mathematics/astronomy); Kalidasa; Nalanda University; decimal system.")
add("satavahana", "Satavahana Dynasty (शातवाहन / సాతవాహన Śātavāhana)", "CulturalAge", "south-asia-history", 100, 220, "BCE-CE",
    "Major Deccan power; bridge between Maurya and Gupta; Amaravati stupa; Prakrit patronage; controlled trade routes between north and south India.")
add("pallava-dynasty", "Pallava Dynasty (பல்லவ மரபு Pallava Marapu)", "CulturalAge", "south-asia-history", 275, 897, "CE",
    "South Indian dynasty; Shore Temple and Pancha Rathas at Mamallapuram (UNESCO); Pallava script influenced Southeast Asian scripts; Dravidian architecture.")
add("chalukya-dynasty", "Chalukya Dynasty (ಚಾಲುಕ್ಯ ರಾಜವಂಶ Cāḷukya)", "CulturalAge", "south-asia-history", 543, 1190, "CE",
    "Major Deccan empire; Badami, Western and Eastern Chalukyas; Pattadakal temples (UNESCO); rival to Pallavas and Cholas; Kannada literary tradition.")
add("chola-dynasty", "Chola Dynasty (சோழ மரபு Cōḻa)", "CulturalAge", "south-asia-history", 300, 1279, "BCE-CE",
    "Tamil Nadu; one of longest-ruling dynasties; Rajaraja I, Rajendra I; naval power; Brihadeeswarar Temple; influence across Southeast Asia.")
add("pala-empire", "Pala Empire (পাল সাম্রাজ্য Pāla Sāmrājya)", "CulturalAge", "south-asia-history", 750, 1174, "CE",
    "Eastern India (Bengal-Bihar); last major Buddhist empire in India; Nalanda and Vikramashila universities; Pala school of art; tantric Buddhism.")
add("delhi-sultanate", "Delhi Sultanate (دلی سلطنت / दिल्ली सल्तनत)", "CulturalAge", "south-asia-history", 1206, 1526, "CE",
    "Five successive Islamic dynasties ruling from Delhi; Qutub Minar; repelled Mongol invasions; Slave, Khalji, Tughlaq, Sayyid, Lodi dynasties.")
add("vijayanagara", "Vijayanagara Empire (ವಿಜಯನಗರ ಸಾಮ್ರಾಜ್ಯ Vijayanagara)", "CulturalAge", "south-asia-history", 1336, 1646, "CE",
    "Hindu empire of southern India; Hampi capital (UNESCO); resisted Bahmani/Deccan sultanates; patronized Telugu, Kannada, Tamil literature.")
add("mughal-empire", "Mughal Empire (مغلیہ سلطنت / मुग़ल सल्तनत)", "CulturalAge", "south-asia-history", 1526, 1857, "CE",
    "Babur, Akbar, Shah Jahan, Aurangzeb; Taj Mahal; religious tolerance (Akbar's Din-i Ilahi); zenith of Indo-Islamic architecture; ~25% of world GDP.")
add("mughal-golden-age", "Mughal Golden Age (مغلیہ سلطنت کا عروج)", "CulturalAge", "mughal-empire", 1556, 1707, "CE",
    "Akbar through Aurangzeb; Taj Mahal (1632-53); Red Fort; miniature painting; administrative reforms; territorial peak under Aurangzeb.")
add("maratha-empire", "Maratha Empire (मराठा साम्राज्य)", "CulturalAge", "south-asia-history", 1674, 1818, "CE",
    "Shivaji Maharaj; Hindu Padshahi; challenged Mughal decline; Peshwa era; confederacy; Battle of Panipat (1761); eventually fell to British.")
add("sikh-empire", "Sikh Empire (ਸਿੱਖ ਰਾਜ / Sarkar-e-Khalsa)", "CulturalAge", "south-asia-history", 1799, 1849, "CE",
    "Maharaja Ranjit Singh; Punjab-based empire; secular governance; Khalsa army; Kohinoor diamond; Anglo-Sikh Wars; annexed by British East India Company.")
add("british-raj", "British Raj (ब्रिटिश राज)", "CulturalAge", "south-asia-history", 1858, 1947, "CE",
    "Direct British Crown rule; railways; English education; Bengal famine (1943); Indian National Congress; Muslim League; independence movement.")
add("indian-independence", "Indian Independence Movement (भारतीय स्वतंत्रता आन्दोलन)", "CulturalAge", "british-raj", 1885, 1947, "CE",
    "INC founded (1885); Swadeshi; Gandhi's satyagraha; Salt March (1930); Quit India (1942); Partition; independence August 15, 1947.")
add("south-asia-modern", "Modern South Asia (आधुनिक दक्षिण एशिया)", "CulturalAge", "contemporary", 1947, 0, "CE",
    "Partition of India and Pakistan; Bangladesh liberation (1971); Sri Lankan civil war; nuclear powers; IT revolution; world's largest democracy.")

# --- Sri Lanka ---
add("anuradhapura-kingdom", "Anuradhapura Kingdom (අනුරාධපුර රාජධානිය)", "CulturalAge", "south-asia-history", 377, 1017, "BCE-CE",
    "First major Sinhalese kingdom; 1,400-year rule; center of Theravada Buddhism; massive irrigation works (tanks); UNESCO World Heritage site.")
add("polonnaruwa-kingdom", "Polonnaruwa Kingdom (පොළොන්නරුව රාජධානිය)", "CulturalAge", "south-asia-history", 1055, 1212, "CE",
    "Second Sinhalese capital after Chola expulsion; Parakramabahu the Great; superior irrigation systems; Gal Vihara Buddha statues; UNESCO site.")
add("kingdom-of-kandy", "Kingdom of Kandy (මහනුවර රාජධානිය)", "CulturalAge", "south-asia-history", 1469, 1815, "CE",
    "Last independent Sinhalese monarchy; resisted Portuguese and Dutch for centuries; Temple of the Tooth Relic (Sri Dalada Maligawa); fell to British 1815.")

# --- Nepal ---
add("licchavi-nepal", "Licchavi Kingdom of Nepal (लिच्छवि राजवंश)", "CulturalAge", "south-asia-history", 400, 750, "CE",
    "Golden Period of Nepal; earliest inscriptions (Manadeva, 464 CE); connected Kathmandu Valley to Indian subcontinent trade and culture.")
add("malla-nepal", "Malla Kingdoms of Nepal (मल्ल राजवंश)", "CulturalAge", "south-asia-history", 1200, 1768, "CE",
    "600-year rule; split into Kathmandu, Bhaktapur, Lalitpur after 1482; Newar civilization flourished; extraordinary pagoda temple architecture.")

# --- Bangladesh/Bengal ---
add("sena-dynasty", "Sena Dynasty (সেন রাজবংশ)", "CulturalAge", "south-asia-history", 1097, 1225, "CE",
    "Unified all of Bengal; Hindu revival after Buddhist Pala rule; Jayadeva's Gita Govinda; established Bengali caste system.")
add("bengal-sultanate", "Bengal Sultanate (বাংলা সালতানাত)", "CulturalAge", "south-asia-history", 1342, 1538, "CE",
    "Independent Islamic state; 'richest country to trade with'; first Bengali court language recognition; distinctive Bengali-Islamic architecture.")

# --- China ---
add("china-history", "Chinese Historical Periods (中国历史时期 Zhōngguó lìshǐ shíqī)", "CulturalAge", "holocene", 7000, 0, "BCE-CE",
    "From Neolithic cultures through dynastic cycle to modern People's Republic; continuous civilization spanning 5,000+ years.")
add("chinese-neolithic", "Chinese Neolithic Cultures (中国新石器时代文化 Zhōngguó xīn shíqì shídài wénhuà)", "CulturalAge", "china-history", 7000, 2070, "BCE",
    "Yangshao (painted pottery), Longshan (black pottery), Liangzhu (jade); rice and millet cultivation; proto-cities; foundations of Chinese civilization.")
add("xia-dynasty", "Xia Dynasty (夏朝 Xià Cháo)", "CulturalAge", "china-history", 2070, 1600, "BCE",
    "First Chinese dynasty (semi-legendary); Yu the Great; flood control; Erlitou culture; bronze vessels; transition from Neolithic to Bronze Age.")
add("shang-dynasty", "Shang Dynasty (商朝 Shāng Cháo)", "CulturalAge", "china-history", 1600, 1046, "BCE",
    "First historically verified dynasty; oracle bone inscriptions (earliest Chinese writing); bronze ritual vessels; Anyang capital; ancestor worship.")
add("zhou-dynasty", "Zhou Dynasty (周朝 Zhōu Cháo)", "CulturalAge", "china-history", 1046, 256, "BCE",
    "Longest Chinese dynasty; Mandate of Heaven concept; feudal system; divided into Western Zhou and Eastern Zhou (Spring and Autumn, Warring States).")
add("spring-autumn", "Spring and Autumn Period (春秋時代 Chūnqiū)", "CulturalAge", "zhou-dynasty", 771, 476, "BCE",
    "Confucius (551-479), Laozi (Daoism), Sun Tzu; Hundred Schools of Thought begins; hegemonic states; iron technology spreads.")
add("warring-states", "Warring States Period (戰國時代 Zhànguó)", "CulturalAge", "zhou-dynasty", 475, 221, "BCE",
    "Seven major states; Mencius, Zhuangzi, Legalism (Han Feizi); crossbow, cavalry; mass armies; ends with Qin unification.")
add("qin-dynasty", "Qin Dynasty (秦朝 Qín Cháo)", "CulturalAge", "china-history", 221, 206, "BCE",
    "First unified Chinese empire; Qin Shi Huang; Great Wall begun; Terracotta Army; standardized weights, measures, writing; Legalist rule; burned books.")
add("han-dynasty", "Han Dynasty (漢朝 Hàn Cháo)", "CulturalAge", "china-history", 206, 220, "BCE-CE",
    "Golden age; Confucianism as state ideology; Silk Road opens (Zhang Qian); paper invented; civil service exams; ~60 million people; 'Han Chinese' identity.")
add("han-western", "Western Han (西漢 Xī Hàn)", "CulturalAge", "han-dynasty", 206, 9, "BCE",
    "Emperor Wu expands empire; Silk Road trade; Sima Qian's Records of the Grand Historian; Confucian academy; Chang'an capital.")
add("han-eastern", "Eastern Han (東漢 Dōng Hàn)", "CulturalAge", "han-dynasty", 25, 220, "CE",
    "Restored Han; Luoyang capital; Buddhism arrives; invention of paper (Cai Lun, 105 CE); seismograph (Zhang Heng); Yellow Turban Rebellion.")
add("three-kingdoms", "Three Kingdoms Period (三國時代 Sānguó)", "CulturalAge", "china-history", 220, 280, "CE",
    "Wei, Shu, Wu; Cao Cao, Liu Bei, Sun Quan, Zhuge Liang; Romance of the Three Kingdoms; one of most romanticized eras in Chinese culture.")
add("six-dynasties", "Six Dynasties / Northern and Southern Dynasties (六朝/南北朝)", "CulturalAge", "china-history", 220, 589, "CE",
    "300-year era of division; Jin, Sixteen Kingdoms, Northern and Southern Dynasties; Buddhism takes root; Wang Xizhi calligraphy; ethnic integration of steppe peoples.")
add("sixteen-kingdoms", "Sixteen Kingdoms (十六國/五胡十六國)", "CulturalAge", "six-dynasties", 304, 439, "CE",
    "Non-Han peoples (Xiongnu, Xianbei, Di, Qiang, Jie) establish kingdoms across northern China; reshapes Chinese demographics and culture.")
add("sui-dynasty", "Sui Dynasty (隋朝 Suí Cháo)", "CulturalAge", "china-history", 581, 618, "CE",
    "Reunification after centuries of division; Grand Canal construction; Great Wall rebuilt; civil service exams restored; overextension leads to collapse.")
add("tang-dynasty", "Tang Dynasty (唐朝 Táng Cháo)", "CulturalAge", "china-history", 618, 907, "CE",
    "Golden age of Chinese civilization; Chang'an largest city in world; Li Bai, Du Fu (poetry); Wu Zetian (only female emperor); cosmopolitan culture; Silk Road peak.")
add("five-dynasties", "Five Dynasties and Ten Kingdoms (五代十國 Wǔdài Shíguó)", "CulturalAge", "china-history", 907, 960, "CE",
    "Fragmentation after Tang; five rapid northern dynasties; ten southern kingdoms; political chaos; printing technology spreads; prelude to Song reunification.")
add("song-dynasty", "Song Dynasty (宋朝 Sòng Cháo)", "CulturalAge", "china-history", 960, 1279, "CE",
    "Economic revolution; movable type printing; gunpowder weapons; compass; paper money; Neo-Confucianism; landscape painting; commercial economy.")
add("song-northern", "Northern Song (北宋 Běi Sòng)", "CulturalAge", "song-dynasty", 960, 1127, "CE",
    "Kaifeng capital; Su Shi (poet); Shen Kuo (polymath); Dream Pool Essays; commercial revolution; lost north to Jurchen Jin dynasty.")
add("jin-jurchen", "Jin Dynasty (Jurchen, 金朝)", "CulturalAge", "china-history", 1115, 1234, "CE",
    "Jurchen conquest of northern China; sinicized administration; rivalry with Southern Song; fell to Mongols; predecessor to Manchu Qing.")
add("liao-dynasty", "Liao Dynasty (遼朝)", "CulturalAge", "china-history", 916, 1125, "CE",
    "Khitan empire; 'Cathay' derives from Khitan; dual administration (nomadic + Chinese); Chanyuan Treaty with Song (1004); own writing system.")
add("western-xia", "Western Xia (西夏)", "CulturalAge", "china-history", 1038, 1227, "CE",
    "Tangut empire controlling Hexi Corridor (Silk Road); unique Tangut script; three-way balance with Song and Liao/Jin; annihilated by Mongols.")
add("song-southern", "Southern Song (南宋 Nán Sòng)", "CulturalAge", "song-dynasty", 1127, 1279, "CE",
    "Hangzhou capital ('above is heaven, below is Hangzhou'); maritime trade; Zhu Xi Neo-Confucianism; fell to Mongol Yuan dynasty.")
add("yuan-dynasty", "Yuan Dynasty (Mongol)", "CulturalAge", "china-history", 1271, 1368, "CE",
    "Kublai Khan; Mongol rule over China; Marco Polo visits; Grand Canal extended; Yuan drama; paper money inflation; ethnic hierarchy.")
add("ming-dynasty", "Ming Dynasty (明朝 Míng Cháo)", "CulturalAge", "china-history", 1368, 1644, "CE",
    "Han Chinese restoration; Forbidden City (Beijing); Zheng He voyages (1405-33); Great Wall rebuilt; porcelain golden age; novel tradition flourishes.")
add("zheng-he", "Zheng He Voyages (郑和下西洋 Zhèng Hé xià Xīyáng)", "CulturalAge", "ming-dynasty", 1405, 1433, "CE",
    "Seven grand maritime expeditions; treasure ships; reached East Africa, Arabia, Southeast Asia; then China turned inward; ended oceanic exploration.")
add("qing-dynasty", "Qing Dynasty (清朝 Qīng Cháo)", "CulturalAge", "china-history", 1644, 1912, "CE",
    "Manchu rule; largest Qing territory; Kangxi, Qianlong emperors; Opium Wars; Taiping Rebellion (~20-30M dead); Century of Humiliation; fall to revolution.")
add("qing-golden-age", "High Qing Era (康乾盛世 Kāng-Qián shèngshì)", "CulturalAge", "qing-dynasty", 1661, 1796, "CE",
    "Kangxi-Yongzheng-Qianlong; population doubles to 300M; territorial expansion (Tibet, Xinjiang, Taiwan); literary inquisition; Dream of the Red Chamber.")
add("opium-wars", "Opium Wars Era (鸦片战争 Yāpiàn Zhànzhēng)", "CulturalAge", "qing-dynasty", 1839, 1860, "CE",
    "First (1839-42) and Second (1856-60) Opium Wars; Treaty of Nanjing; Hong Kong ceded; unequal treaties; Summer Palace burned; forced opening.")
add("republic-of-china", "Republic of China (中華民國 Zhōnghuá Mínguó)", "CulturalAge", "china-history", 1912, 1949, "CE",
    "Sun Yat-sen; warlord era; Northern Expedition; Nanjing decade; Second Sino-Japanese War (1937-45); Chinese Civil War; Chiang Kai-shek retreats to Taiwan.")
add("prc", "People's Republic of China (中华人民共和国 Zhōnghuá Rénmín Gònghéguó)", "CulturalAge", "contemporary", 1949, 0, "CE",
    "Mao Zedong; Great Leap Forward; Cultural Revolution (1966-76); Deng Xiaoping reforms (1978); economic miracle; world's second-largest economy.")
add("taiwan-japanese", "Taiwan under Japanese Rule (台灣日治時期)", "CulturalAge", "japan-history", 1895, 1945, "CE",
    "Japan's first colony (Treaty of Shimonoseki); Republic of Formosa (1895); modernized infrastructure; cultural suppression; shaped modern Taiwanese identity.")
add("roc-taiwan", "ROC on Taiwan (中華民國在臺灣)", "CulturalAge", "contemporary", 1949, 0, "CE",
    "KMT retreat to Taiwan; White Terror; martial law (1949-1987); economic miracle (Four Asian Tigers); democratization; first direct presidential election (1996).")

# --- Japan ---
add("japan-history", "Japanese Historical Periods (日本の歴史時代 Nihon no rekishi jidai)", "CulturalAge", "holocene", 14000, 0, "BCE-CE",
    "From Jōmon hunter-gatherers through samurai shoguns to modern economic power; island civilization with unique cultural synthesis.")
add("jomon", "Jōmon Period (縄文時代 Jōmon jidai)", "CulturalAge", "japan-history", 14000, 300, "BCE",
    "Hunter-gatherer-fishers; world's oldest pottery (~16,000 BP); cord-marked ceramics; Sannai-Maruyama settlement; dogu figurines; 10,000+ year span.")
add("yayoi", "Yayoi Period (弥生時代 Yayoi jidai)", "CulturalAge", "japan-history", 300, 250, "BCE-CE",
    "Wet-rice agriculture from Korean peninsula; bronze and iron tools; social stratification; Yoshinogari site; foundation of Japanese agricultural society.")
add("kofun", "Kofun Period (古墳時代 Kofun jidai)", "CulturalAge", "japan-history", 250, 538, "CE",
    "Keyhole-shaped burial mounds; Yamato court emergence; introduction of Chinese writing; haniwa clay figures; imperial lineage established.")
add("asuka-period", "Asuka Period (飛鳥時代 Asuka jidai)", "CulturalAge", "japan-history", 538, 710, "CE",
    "Buddhism arrives; Prince Shōtoku; Taika Reform (645); Ritsuryō legal codes; Chinese-style centralized government; Hōryū-ji temple.")
add("nara-period", "Nara Period (奈良時代 Nara jidai)", "CulturalAge", "japan-history", 710, 794, "CE",
    "First permanent capital at Nara; Kojiki and Nihon Shoki (earliest histories); Tōdai-ji Great Buddha; Buddhist monastery power grows.")
add("heian-period", "Heian Period (平安時代 Heian jidai)", "CulturalAge", "japan-history", 794, 1185, "CE",
    "Kyoto capital; Tale of Genji (Murasaki Shikibu, world's first novel); Fujiwara regents; kana script; refined court culture; samurai class rises.")
add("kamakura-shogunate", "Kamakura Period (鎌倉時代 Kamakura jidai)", "CulturalAge", "japan-history", 1185, 1333, "CE",
    "First shogunate (Minamoto Yoritomo); samurai government; Zen Buddhism; Mongol invasions repelled (1274, 1281, 'kamikaze'); warrior culture.")
add("muromachi-period", "Muromachi Period (室町時代 Muromachi jidai)", "CulturalAge", "japan-history", 1336, 1573, "CE",
    "Ashikaga shogunate; Noh theater; tea ceremony; Zen gardens (Ryōan-ji); Ōnin War (1467); Sengoku (Warring States) era begins.")
add("sengoku", "Sengoku Period (戦国時代 Sengoku jidai)", "CulturalAge", "japan-history", 1467, 1615, "CE",
    "Warring States; Oda Nobunaga, Toyotomi Hideyoshi, Tokugawa Ieyasu (three unifiers); firearms arrive (1543); castles; samurai warfare peak.")
add("azuchi-momoyama", "Azuchi-Momoyama Period (安土桃山時代)", "CulturalAge", "sengoku", 1573, 1603, "CE",
    "Nobunaga and Hideyoshi era; grand castles (Azuchi, Osaka); Sen no Rikyū tea ceremony; Namban trade with Europeans; Korea invasions (1592-98).")
add("edo-period", "Edo Period (江戸時代 Edo jidai / Tokugawa)", "CulturalAge", "japan-history", 1603, 1868, "CE",
    "Tokugawa shogunate; 250 years of peace; sakoku isolation; Edo (Tokyo) grows to 1M+; kabuki, ukiyo-e, haiku; rigid social hierarchy; merchant culture.")
add("meiji-era", "Meiji Era (明治時代 Meiji jidai)", "CulturalAge", "japan-history", 1868, 1912, "CE",
    "Meiji Restoration; rapid modernization/industrialization; Meiji Constitution (1889); Sino-Japanese War (1894-95); Russo-Japanese War (1904-05); world power.")
add("taisho-era", "Taishō Era (大正時代)", "CulturalAge", "japan-history", 1912, 1926, "CE",
    "Japan's brief democratic flowering; party-led cabinets; universal male suffrage (1925); modern culture (cinema, radio); Great Kantō Earthquake (1923).")
add("imperial-japan", "Early Shōwa / Militarist Japan (昭和)", "CulturalAge", "japan-history", 1926, 1945, "CE",
    "Militarism rises; Manchuria invasion (1931); Second Sino-Japanese War; Pearl Harbor; Pacific War; atomic bombs; surrender.")
add("postwar-japan", "Postwar Japan (戦後日本 Sengo Nihon)", "CulturalAge", "contemporary", 1945, 0, "CE",
    "U.S. occupation; new constitution; economic miracle; world's 2nd largest economy (1968-2010); Sony, Toyota; anime/manga cultural export; aging society.")
add("ryukyu-kingdom", "Ryukyu Kingdom (琉球王国 / Ruuchuu)", "CulturalAge", "japan-history", 1429, 1879, "CE",
    "Independent maritime kingdom (Okinawa); trade hub connecting China, Japan, Korea, SE Asia; Shuri Castle (UNESCO); dual subordination after Satsuma 1609; annexed by Meiji Japan.")

# --- Korea ---
add("korea-history", "Korean Historical Periods (한국 역사 시대 / 韓國歷史時代)", "CulturalAge", "holocene", 2333, 0, "BCE-CE",
    "From legendary Gojoseon through Three Kingdoms, Goryeo, Joseon to modern divided peninsula.")
add("gojoseon", "Gojoseon (고조선 / 古朝鮮)", "CulturalAge", "korea-history", 2333, 108, "BCE",
    "First Korean kingdom (legendary founding by Dangun); bronze culture; Wiman Joseon; conquered by Han China (108 BCE); Korean identity origins.")
add("three-kingdoms-korea", "Three Kingdoms of Korea (삼국시대 / 三國時代)", "CulturalAge", "korea-history", 57, 668, "BCE-CE",
    "Goguryeo (north, military), Baekje (southwest, maritime), Silla (southeast); Buddhism adopted; tomb murals; cultural exchange with Japan and China.")
add("gaya-confederacy", "Gaya Confederacy (가야/加耶)", "CulturalAge", "korea-history", 42, 562, "CE",
    "City-states in Nakdong River basin; peninsula's iron-working center; gayageum zither invented; absorbed by Silla; Kim Yu-sin was Gaya descendant.")
add("silla-unified", "Unified Silla (통일신라 / 統一新羅)", "CulturalAge", "korea-history", 668, 935, "CE",
    "Silla unifies peninsula with Tang alliance; Gyeongju capital; Bulguksa Temple; golden age of Korean Buddhism; Seokguram Grotto.")
add("balhae", "Balhae (Bohai)", "CulturalAge", "korea-history", 698, 926, "CE",
    "Northern successor to Goguryeo; ruled Manchuria and northern Korea; 'Flourishing Land in the East'; fell to Khitan Liao; claimed by both Korean and Chinese histories.")
add("later-three-kingdoms", "Later Three Kingdoms (후삼국시대)", "CulturalAge", "korea-history", 892, 936, "CE",
    "Silla collapses; Later Baekje and Later Goguryeo arise; Wang Geon unifies under Goryeo (936); origin of name 'Korea'.")
add("goryeo-dynasty", "Goryeo Dynasty (고려 / 高麗)", "CulturalAge", "korea-history", 918, 1392, "CE",
    "Origin of name 'Korea'; celadon ceramics; Tripitaka Koreana (woodblock Buddhist canon); movable metal type (1234, before Gutenberg); Mongol invasions.")
add("joseon-dynasty", "Joseon Dynasty (조선 / 朝鮮)", "CulturalAge", "korea-history", 1392, 1897, "CE",
    "Neo-Confucian state; Sejong the Great invents Hangul (1443); Gyeongbokgung Palace; Imjin War (Japanese invasions, 1592-98); 500-year dynasty.")
add("joseon-golden-age", "Joseon Golden Age (조선 세종대왕 시대 / 朝鮮 世宗大王 時代)", "CulturalAge", "joseon-dynasty", 1418, 1494, "CE",
    "Sejong the Great; Hangul alphabet (1443); rain gauge, sundials, water clocks; Jang Yeong-sil (inventor); agricultural treatises; Confucian scholarship.")
add("korean-empire", "Korean Empire (대한제국/大韓帝國)", "CulturalAge", "korea-history", 1897, 1910, "CE",
    "Emperor Gojong proclaims empire; Gwangmu Reform; modernization; 'Daehan' origin of South Korea's name; annexed by Japan 1910.")
add("japanese-occupation-korea", "Japanese Occupation of Korea (일제강점기 / 日帝強占期)", "CulturalAge", "korea-history", 1910, 1945, "CE",
    "Annexation by Japan; cultural suppression; forced labor; comfort women; March 1st Movement (1919); Korean language banned; liberation with WWII end.")
add("korea-modern", "Modern Korea (Divided)", "CulturalAge", "contemporary", 1945, 0, "CE",
    "Division at 38th parallel; Korean War (1950-53); North Korea (DPRK); South Korea's 'Miracle on the Han River'; K-pop, Samsung; DMZ.")

# --- Southeast Asia ---
add("southeast-asia-history", "Southeast Asian Historical Periods (ประวัติศาสตร์เอเชียตะวันออกเฉียงใต้)", "CulturalAge", "holocene", 1000, 0, "BCE-CE",
    "Maritime and mainland kingdoms; Indianization and Sinicization; spice trade; colonial era; modern ASEAN nations.")
add("funan", "Kingdom of Funan (扶南 Fúnán / នគរភ្នំ)", "CulturalAge", "southeast-asia-history", 100, 550, "CE",
    "Earliest known Indianized kingdom in mainland Southeast Asia; Mekong Delta; maritime trade hub; Hinduism and Buddhism; Óc Eo port city.")
add("chenla-kingdom", "Kingdom of Chenla (真臘 Zhēnlà / ចេនឡា Chenla / ប្រទេសកម្ពុជា)", "CulturalAge", "southeast-asia-history", 550, 802, "CE",
    "Khmer predecessor state; successor to Funan in mainland Southeast Asia; fragmented c. 706 CE into Land Chenla (upper) and Water Chenla (lower); Jayavarman II unified and proclaimed devaraja (god-king), founding the Khmer Empire in 802 CE.")
add("champa", "Kingdom of Champa (Chăm Pa / 占婆 Zhànpó)", "CulturalAge", "southeast-asia-history", 192, 1832, "CE",
    "Hindu-Buddhist kingdom in central/southern Vietnam; Cham towers (Mỹ Sơn); maritime trade; rivalry with Khmer and Đại Việt; Austronesian people.")
add("srivijaya", "Srivijaya Empire (ศรีวิชัย / Śrīvijaya)", "CulturalAge", "southeast-asia-history", 650, 1377, "CE",
    "Maritime empire based in Sumatra; controlled Malacca Strait; Buddhist center (Nalanda connections); Malay language spread; spice trade.")
add("dongson-culture", "Đông Sơn Culture (Văn hóa Đông Sơn / 東山文化)", "CulturalAge", "southeast-asia-history", 600, 200, "BCE-CE",
    "Bronze Age culture of northern Vietnam's Red River Delta; elaborate bronze drums (trống đồng Đông Sơn); wet-rice cultivation; maritime trade; Heger Type I drums found from Indonesia to southern China; foundation of Vietnamese Bronze Age identity.")
add("ban-chiang", "Ban Chiang (บ้านเชียง)", "CulturalAge", "southeast-asia-history", 3600, 200, "BCE",
    "Prehistoric site in northeast Thailand; UNESCO World Heritage Site; early bronze metallurgy (debated dating); distinctive red-painted pottery; rice agriculture; challenges 'diffusion from China' model of Southeast Asian metalworking.")

add("dvaravati", "Dvaravati Kingdom (ทวารวดี Thawārawadī)", "CulturalAge", "southeast-asia-history", 550, 1050, "CE",
    "Mon Buddhist kingdom in central Thailand; Theravada Buddhism center; Dharmachakra (Wheel of Law) sculptures; absorbed by Khmer and later Thai kingdoms.")
add("khmer-empire", "Khmer Empire (ចក្រភពខ្មែរ)", "CulturalAge", "southeast-asia-history", 802, 1431, "CE",
    "Angkor Wat and Angkor Thom; Jayavarman II, Suryavarman II, Jayavarman VII; hydraulic engineering; largest pre-industrial city; Hindu-Buddhist synthesis.")
add("pagan-kingdom", "Pagan Kingdom (ပုဂံ ပြည် Pugaṃ Pyi)", "CulturalAge", "southeast-asia-history", 849, 1297, "CE",
    "First unified Myanmar/Burma; Anawrahta; 10,000+ Buddhist temples at Bagan; Theravada Buddhism; Pali scriptures; Mongol invasion ends dynasty.")
add("majapahit", "Majapahit Empire (Kerajaan Majapahit / ꦩꦗꦥꦲꦶꦠ꧀)", "CulturalAge", "southeast-asia-history", 1293, 1527, "CE",
    "Java-based Hindu-Buddhist empire; Gajah Mada (prime minister); Nagarakretagama poem; controlled much of maritime Southeast Asia; Indonesian national heritage.")
add("sukhothai", "Sukhothai Kingdom (อาณาจักรสุโขทัย Anāčhak Sukhōthai)", "CulturalAge", "southeast-asia-history", 1238, 1438, "CE",
    "First Thai kingdom; King Ramkhamhaeng; Thai script created; Theravada Buddhism state religion; Si Satchanalai ceramics; foundation of Thai identity.")
add("ayutthaya", "Ayutthaya Kingdom (อาณาจักรอยุธยา Anāčhak Ayutthayā)", "CulturalAge", "southeast-asia-history", 1351, 1767, "CE",
    "Siamese kingdom; cosmopolitan capital; trade with China, Japan, Europe; 33 kings; destroyed by Burma (1767); predecessor to modern Thailand.")
add("malacca-sultanate", "Malacca Sultanate (Kesultanan Melayu Melaka)", "CulturalAge", "southeast-asia-history", 1400, 1511, "CE",
    "Strategic Strait of Malacca; spread of Islam in maritime Southeast Asia; Malay court culture; fell to Portuguese (1511); origin of modern Malaysia.")
add("dai-viet", "Đại Việt (大越)", "CulturalAge", "southeast-asia-history", 1009, 1802, "CE",
    "Vietnamese state; Lý, Trần, Lê dynasties; repelled Mongol invasions (3 times); Confucian governance; Temple of Literature (1070); southward expansion.")
# --- Myanmar (post-Pagan) ---
add("toungoo-dynasty", "Toungoo Dynasty (တောင်ငူ ခေတ်)", "CulturalAge", "southeast-asia-history", 1510, 1752, "CE",
    "Reunified Burma; under Bayinnaung created largest empire in Southeast Asian history; conquered Ava, Lan Na, Siam, Lan Xang.")
add("konbaung-dynasty", "Konbaung Dynasty (ကုန်းဘောင် ခေတ်)", "CulturalAge", "southeast-asia-history", 1752, 1885, "CE",
    "Last Burmese dynasty; destroyed Ayutthaya (1767); defeated four Qing invasions; fell to British in three Anglo-Burmese Wars.")

# --- Thailand (post-Ayutthaya) ---
add("lan-na-kingdom", "Lan Na Kingdom (ล้านนา)", "CulturalAge", "southeast-asia-history", 1292, 1558, "CE",
    "Northern Thai kingdom centered on Chiang Mai; distinct Lan Na script and culture; resisted Mongol incursions; eventually absorbed into Siam.")
add("rattanakosin", "Rattanakosin Kingdom (อาณาจักรรัตนโกสินทร์)", "CulturalAge", "southeast-asia-history", 1782, 1932, "CE",
    "Chakri dynasty; Bangkok capital; Siam's modernization; only Southeast Asian nation to avoid colonization; precursor to modern Thailand.")

# --- Vietnam (specific dynasties) ---
add("ly-dynasty", "Lý Dynasty (Nhà Lý/李朝)", "CulturalAge", "dai-viet", 1010, 1225, "CE",
    "Founded Thăng Long (Hanoi); established centralized Vietnamese state; drove out Chinese influence; laid foundation for Vietnamese nationhood.")
add("tran-dynasty", "Trần Dynasty (Nhà Trần/陳朝)", "CulturalAge", "dai-viet", 1226, 1400, "CE",
    "Repelled three Mongol invasions under Trần Hưng Đạo; chữ Nôm writing system; golden age of Vietnamese literature.")
add("later-le-dynasty", "Later Lê Dynasty (Nhà Hậu Lê/後黎朝)", "CulturalAge", "dai-viet", 1428, 1789, "CE",
    "Longest-ruling Vietnamese dynasty (360 years); Lê Lợi expelled Ming Chinese; Hồng Đức law code with progressive women's rights.")
add("nguyen-dynasty", "Nguyễn Dynasty (Nhà Nguyễn/阮朝)", "CulturalAge", "southeast-asia-history", 1802, 1945, "CE",
    "Last Vietnamese dynasty; unified all modern Vietnam; Imperial City of Huế (UNESCO); French protectorate from 1883.")

# --- Indonesia ---
add("sailendra-dynasty", "Sailendra Dynasty (Wangsa Syailendra)", "CulturalAge", "southeast-asia-history", 750, 850, "CE",
    "Buddhist dynasty of Central Java; built Borobudur, largest Buddhist monument in the world (UNESCO); connected to Srivijaya.")
add("mataram-hindu", "Mataram Kingdom (Kerajaan Mataram Kuno)", "CulturalAge", "southeast-asia-history", 732, 1006, "CE",
    "Hindu-Shaivite kingdom of Central Java; built Prambanan temple complex (UNESCO); rival/coexistent with Sailendra.")
add("singhasari", "Singhasari Kingdom (Kerajaan Singhasari)", "CulturalAge", "southeast-asia-history", 1222, 1292, "CE",
    "East Javanese kingdom; conquered Srivijaya; predecessor to Majapahit; Ken Angrok's unification of Javanese territories.")
add("mataram-islamic", "Mataram Sultanate (Kesultanan Mataram Islam)", "CulturalAge", "southeast-asia-history", 1587, 1755, "CE",
    "Last major independent Javanese kingdom; Sultan Agung; shaped Javanese culture (gamelan, batik, wayang kulit); split into Yogyakarta and Surakarta.")

# --- Cambodia (post-Angkor) ---
add("longvek-period", "Post-Angkor / Longvek Period (សម័យលង្វែក)", "CulturalAge", "southeast-asia-history", 1431, 1594, "CE",
    "Capital moved to Longvek after Angkor's fall; maritime trade hub with European, Chinese, Japanese communities; fell to Ayutthaya 1594.")

# --- Laos ---
add("lan-xang", "Lan Xang Kingdom (ລ້ານຊ້າງ)", "CulturalAge", "southeast-asia-history", 1353, 1707, "CE",
    "Kingdom of a Million Elephants; largest Lao state; Theravada Buddhism; golden age under Sourigna Vongsa; split into three kingdoms 1707; foundational to Lao identity.")

# --- Philippines ---
add("kingdom-of-tondo", "Kingdom of Tondo (Kaharian ng Tondo)", "CulturalAge", "southeast-asia-history", 900, 1589, "CE",
    "One of oldest Philippine polities; Laguna Copperplate Inscription (900 CE); Luzon trade with China; fell to Spanish colonization.")
add("sultanate-of-sulu", "Sultanate of Sulu (Kasultanan sin Sulu)", "CulturalAge", "southeast-asia-history", 1405, 1915, "CE",
    "Maritime Islamic power; controlled Sulu Sea and parts of Borneo; resisted Spanish colonization for centuries; sophisticated naval capabilities.")
add("sultanate-of-maguindanao", "Sultanate of Maguindanao (Kasultanan nu Magindanaw)", "CulturalAge", "southeast-asia-history", 1500, 1888, "CE",
    "Largest Islamic state in the Philippines; controlled most of Mindanao at peak; Sultan Kudarat's legendary resistance against Spain.")

add("colonial-southeast-asia", "Colonial Southeast Asia (Kolonial Sydostasien)", "CulturalAge", "southeast-asia-history", 1511, 1957, "CE",
    "Portuguese Malacca (1511); Dutch East Indies; Spanish Philippines; French Indochina; British Burma/Malaya; only Thailand never colonized.")
add("southeast-asia-modern", "Modern Southeast Asia (Sydostasien i modern tid)", "CulturalAge", "contemporary", 1945, 0, "CE",
    "Independence movements; Vietnam Wars; Khmer Rouge; ASEAN (1967); Asian Tigers; Reformasi; economic growth; 680+ million people.")

# --- Central Asia & Steppe ---
add("central-asia-history", "Central Asian Historical Periods (Орта Азия тарихи / تاریخ آسیای مرکزی)", "CulturalAge", "holocene", 3500, 0, "BCE-CE",
    "Steppe nomads, Silk Road oasis cities; Scythians, Turks, Mongols; convergence zone of civilizations.")
add("scythians", "Scythian Period (Σκύθαι / Скифы Skify)", "CulturalAge", "central-asia-history", 900, 200, "BCE",
    "Iranian nomadic warriors; horse archery; animal-style gold art; kurgans (burial mounds); Herodotus accounts; influenced Greek and Persian worlds.")
add("xiongnu", "Xiongnu Empire (匈奴 Xiōngnú)", "CulturalAge", "central-asia-history", 209, 91, "BCE-CE",
    "First great steppe empire; Modu Chanyu; prompted Chinese Great Wall; Silk Road intermediaries; possible ancestors of Huns; Han dynasty rival; split into Northern and Southern Xiongnu 48 CE.")
add("silk-road-era", "Silk Road Era (丝绸之路 / Ipek Yolu / طريق الحرير)", "CulturalAge", "central-asia-history", 130, 1453, "BCE-CE",
    "Trans-Eurasian trade network; Zhang Qian (130 BCE); Sogdian merchants; Samarkand, Bukhara, Kashgar; ideas, religions, diseases, technologies exchanged.")
add("gokturk-khaganate", "Göktürk Khaganate (𐰜𐰇𐰛:𐱅𐰇𐰼𐰜 Kök Türük / 突厥)", "CulturalAge", "central-asia-history", 552, 744, "CE",
    "First Turkic empire; Orkhon inscriptions (oldest Turkic writing); controlled Silk Road; split into Eastern and Western; influenced all later Turkic states.")
add("tibetan-empire", "Tibetan Empire (བོད་ཆེན་པོ Böchen / 吐蕃 Tǔbō)", "CulturalAge", "central-asia-history", 618, 842, "CE",
    "Songtsen Gampo unifies Tibet; rivaled Tang China; controlled Silk Road oases; Lhasa established; Buddhism adopted; Tibetan script created; fragmented after 842.")
add("sakya-tibet", "Sakya Period of Tibet (ས་སྐྱ་པ/薩迦派)", "CulturalAge", "central-asia-history", 1244, 1354, "CE",
    "Sakya lamas govern Tibet under Mongol patronage; 'priest-patron' (yon-mchod) relationship; Sakya Pandita's submission to Mongols (1244).")
add("phagmodrupa-tibet", "Phagmodrupa Dynasty (ཕག་མོ་གྲུ་པ/帕木竹巴)", "CulturalAge", "central-asia-history", 1354, 1642, "CE",
    "Re-established Tibetan autonomous rule; Changchub Gyaltsen revitalized Tibetan culture; Tsongkhapa founds Gelug school; Dalai Lama institution emerges.")
add("sogdiana", "Sogdiana (Sogdian City-States)", "CulturalAge", "central-asia-history", 500, 800, "CE",
    "Premier Silk Road merchant civilization; Samarkand, Bukhara; Sogdian lingua franca of trade; alphabet influenced Central Asian scripts; rose in Tang government.")
add("mongol-empire", "Mongol Empire (ᠶᠡᠬᠡ ᠮᠣᠩᠭᠣᠯ ᠤᠯᠤᠰ / Их Монгол Улс / Yeke Mongol Ulus)", "CulturalAge", "central-asia-history", 1206, 1368, "CE",
    "Genghis Khan; largest contiguous land empire in history; Pax Mongolica; postal system (yam); religious tolerance; connected East and West.")
add("chagatai-khanate", "Chagatai Khanate (چغتای خانات)", "CulturalAge", "central-asia-history", 1226, 1687, "CE",
    "Mongol successor state; Chagatai Khan's line; Aral Sea to Altai Mountains; Turkicized; Chagatai Turkic literary language; lost Transoxiana to Timurids.")
add("ilkhanate", "Ilkhanate (ایلخانان)", "CulturalAge", "central-asia-history", 1256, 1335, "CE",
    "Mongol successor state; Hulagu Khan; sack of Baghdad (1258) ends Abbasid Caliphate; defeated at Ain Jalut (1260); converted to Islam under Ghazan.")
add("golden-horde", "Golden Horde (Алтын Орда/Улус Джучи)", "CulturalAge", "central-asia-history", 1227, 1502, "CE",
    "Mongol successor state; Jochi's line; ruled Eurasian steppe and Russia ('Tatar Yoke'); Sarai capitals; converted to Islam; fragmented into successor khanates.")
add("northern-yuan", "Northern Yuan (北元)", "CulturalAge", "central-asia-history", 1368, 1635, "CE",
    "Borjigin clan continues ruling Mongolia after Yuan collapse; Dayan Khan reunifies tribes; ended when seal passed to Manchu Later Jin (1635).")
add("dzungar-khanate", "Dzungar Khanate (準噶爾汗國)", "CulturalAge", "central-asia-history", 1634, 1758, "CE",
    "Last great nomadic empire; Oirat Mongols; contested Tibet; fought Qing; destruction by Qianlong (1755-58) shaped borders of modern China.")
add("timurid-empire", "Timurid Empire (تیموریان Tīmūriyān)", "CulturalAge", "central-asia-history", 1370, 1507, "CE",
    "Timur (Tamerlane); Samarkand as cultural capital; Timurid Renaissance; Ulugh Beg observatory; Persian-Turkic culture; ancestor of Mughal dynasty.")
add("khwarazmian-empire", "Khwarazmian Empire (خوارزمشاهیان)", "CulturalAge", "central-asia-history", 1077, 1231, "CE",
    "Turkic Muslim empire; execution of Mongol diplomats triggered Genghis Khan's devastating invasion (1219); destruction of Merv, Samarkand, Bukhara.")
add("ghaznavid-empire", "Ghaznavid Empire (غزنویان)", "CulturalAge", "central-asia-history", 977, 1186, "CE",
    "Turkic dynasty from Ghazna; Mahmud of Ghazni's 17 expeditions into India; patron of Ferdowsi's Shahnameh; launched Islam into the subcontinent.")
add("ghurid-dynasty", "Ghurid Dynasty (غوریان)", "CulturalAge", "central-asia-history", 1175, 1215, "CE",
    "Eastern Persian dynasty from Ghor; Muhammad of Ghor's conquest of India (Tarain, 1192); Minaret of Jam (UNESCO); founded Delhi Sultanate.")
add("great-game", "The Great Game (Большая игра Bolʹshaya igra / بازی بزرگ)", "CulturalAge", "central-asia-history", 1830, 1907, "CE",
    "British-Russian rivalry for Central Asian influence; Afghanistan as buffer state; Russian conquest of khanates; Anglo-Afghan Wars; espionage.")
add("durrani-empire", "Durrani Empire (د درانیانو واکمني Da Durrāniyāno Wākmani)", "CulturalAge", "central-asia-history", 1747, 1826, "CE",
    "Ahmad Shah Durrani ('Father of Afghanistan'); Pashtun empire from Khorasan to Punjab; Kohinoor diamond; foundation of modern Afghan state.")

# --- Middle East / West Asia ---
add("mesopotamia", "Mesopotamian Civilizations (بلاد الرافدين)", "CulturalAge", "holocene", 6500, 539, "BCE",
    "Cradle of civilization; between Tigris and Euphrates; writing, law, mathematics, astronomy; from Ubaid through Sumer to Neo-Babylonian.")
add("ubaid-period", "Ubaid Period (دور العبيد)", "CulturalAge", "mesopotamia", 6500, 3800, "BCE",
    "Pre-Sumerian Mesopotamian culture; first irrigation agriculture; distinctive painted pottery; Eridu (oldest city in Sumerian tradition); 'ubaid-style temples; foundation for Sumerian civilization.")
add("uruk-period", "Uruk Period (دور الوركاء)", "CulturalAge", "mesopotamia", 4000, 3100, "BCE",
    "Birth of civilization; world's first city Uruk (~40,000 people); invention of cuneiform writing (~3400 BCE); cylinder seals; monumental architecture (White Temple); state formation; Warka Vase.")

add("sumer", "Sumerian Civilization (𒆠𒂗𒄀 ki-en-gi)", "CulturalAge", "mesopotamia", 3500, 2004, "BCE",
    "First civilization; cuneiform writing; city-states (Ur, Uruk, Lagash); ziggurats; Epic of Gilgamesh; wheel, plow, sailboat; sexagesimal math.")
add("akkadian-empire", "Akkadian Empire (𒀀𒅗𒁲𒆠 māt Akkadī)", "CulturalAge", "mesopotamia", 2334, 2154, "BCE",
    "Sargon of Akkad; first known empire in history; Akkadian language; centralized bureaucracy; trade networks from Indus to Mediterranean.")
add("babylon-old", "Old Babylonian Period (العصر البابلي القديم)", "CulturalAge", "mesopotamia", 1894, 1595, "BCE",
    "Hammurabi's Code (~1754 BCE, most complete surviving ancient law code); Babylonian mathematics; astronomy; Marduk worship; fell to Hittite raid.")
add("assyrian-empire", "Assyrian Empire (𒀸𒋗𒁺𒆠 māt Aššur)", "CulturalAge", "mesopotamia", 2025, 609, "BCE",
    "Neo-Assyrian peak (911-609 BCE); Nineveh, Nimrud; Ashurbanipal's library; brutal military; iron weapons; siege warfare; reliefs; conquered Egypt.")
add("neo-babylonian", "Neo-Babylonian Empire (الإمبراطورية البابلية الحديثة)", "CulturalAge", "mesopotamia", 626, 539, "BCE",
    "Nebuchadnezzar II; Hanging Gardens; Ishtar Gate; Babylonian captivity of Jews; astronomical records; fell to Persian Cyrus the Great.")
add("phoenicia", "Phoenician Civilization (Φοινίκη / 𐤊𐤍𐤏𐤍 Kanaʿan)", "CulturalAge", "holocene", 1500, 300, "BCE",
    "Maritime city-states (Tyre, Sidon, Byblos); invented the alphabet (~1050 BCE); purple dye; Mediterranean trade and colonization; founded Carthage (~814 BCE).")
add("carthage", "Carthaginian Empire (𐤒𐤓𐤕 𐤇𐤃𐤔𐤕 Qart-ḥadašt)", "CulturalAge", "holocene", 814, 146, "BCE",
    "Phoenician colony becomes western Mediterranean power; Hannibal Barca; Punic Wars with Rome; destroyed by Rome (146 BCE); North Africa, Iberia, Sicily.")
add("ancient-israel", "Ancient Israel (יִשְׂרָאֵל Yisrā'ēl)", "CulturalAge", "holocene", 1200, 586, "BCE",
    "Iron Age Levant; tribal confederation; United Monarchy under David and Solomon; First Temple; split into Israel and Judah; Babylonian exile (586 BCE); Hebrew Bible origins.")
add("hittite-empire", "Hittite Empire (𒄩𒀜𒌅𒊭 Ḫattuša)", "CulturalAge", "holocene", 1650, 1180, "BCE",
    "Anatolian Bronze Age power; Hattusa capital; Battle of Kadesh with Egypt (1274 BCE); iron technology; Treaty of Kadesh (earliest known peace treaty); cuneiform.")
add("elamite-civilization", "Elamite Civilization (تمدن ایلام/Haltamti)", "CulturalAge", "holocene", 3200, 539, "BCE",
    "Major Mesopotamian contemporary in southwest Iran; Susa, Anshan; Proto-Elamite script; Chogha Zanbil ziggurat (UNESCO); language isolate; influenced Achaemenid culture.")
add("mitanni", "Mitanni Kingdom (ميتاني)", "CulturalAge", "holocene", 1550, 1260, "BCE",
    "Hurrian-speaking state in northern Syria/Anatolia with Indo-Aryan ruling elite; diplomatic peer of Egypt and Hittites; profoundly influenced Hittite religion.")
add("urartu", "Urartu / Kingdom of Van (Biainili/Ուրարտու)", "CulturalAge", "holocene", 860, 585, "BCE",
    "Iron Age kingdom in Armenian highlands; rival to Assyria; founded Erebuni (modern Yerevan, 782 BCE); hydraulic engineering; biblical 'Ararat' cognate.")
add("median-empire", "Median Empire (مادها)", "CulturalAge", "holocene", 678, 549, "BCE",
    "First Iranian empire; destroyed Assyrian Empire (Nineveh, 612 BCE) with Babylon; Ecbatana capital; predecessor to Achaemenid Persia.")
add("achaemenid-empire", "Achaemenid Persian Empire (هخامنشیان / Haxāmanišiya)", "CulturalAge", "holocene", 550, 330, "BCE",
    "Cyrus the Great, Darius I, Xerxes; largest empire to date; Persepolis; Royal Road; satrapy system; Zoroastrianism; defeated by Alexander.")
add("seleucid-empire", "Seleucid Empire (Αυτοκρατορία των Σελευκιδών / الإمبراطورية السلوقية)", "CulturalAge", "holocene", 312, 63, "BCE",
    "Hellenistic successor state; Seleucus I; Antioch capital; Greek culture in Near East; Maccabean revolt; fragmented; fell to Rome and Parthia.")
add("parthian-empire", "Parthian Empire (شاهنشاهی اشکانی Šāhanšāhī-ye Aškānī)", "CulturalAge", "holocene", 247, 224, "BCE-CE",
    "Iranian Arsacid dynasty; rival to Rome; Silk Road trade; Ctesiphon capital; horse archers; Carrhae victory over Crassus (53 BCE).")
add("sasanian-empire", "Sasanian Empire (ساسانیان / Ērānšahr)", "CulturalAge", "holocene", 224, 651, "CE",
    "Last pre-Islamic Persian empire; Zoroastrian state religion; Ctesiphon arch; rivalry with Rome/Byzantium; chess, polo; Academy of Gondishapur.")
add("islamic-golden-age", "Islamic Golden Age (العصر الذهبي للإسلام)", "CulturalAge", "holocene", 750, 1258, "CE",
    "Abbasid Caliphate; House of Wisdom (Baghdad); al-Khwarizmi (algebra); Ibn Sina (medicine); optics, chemistry, astronomy; translation movement; ended by Mongol sack of Baghdad.")
add("rashidun-caliphate", "Rashidun Caliphate (الخلافة الراشدة)", "CulturalAge", "holocene", 632, 661, "CE",
    "Four 'rightly guided' caliphs; Abu Bakr, Umar, Uthman, Ali; rapid Islamic expansion; conquest of Persia and Byzantine Levant; Quran compiled; Sunni-Shia split origins.")
add("umayyad-caliphate", "Umayyad Caliphate (الخلافة الأموية)", "CulturalAge", "holocene", 661, 750, "CE",
    "First hereditary Islamic dynasty; Damascus capital; expansion from Spain to Indus; Dome of the Rock; Great Mosque of Damascus; Arabic as administrative language.")
add("abbasid-caliphate", "Abbasid Caliphate (الخلافة العباسية)", "CulturalAge", "holocene", 750, 1258, "CE",
    "Baghdad founded (762); cosmopolitan capital; House of Wisdom; Paper from China; One Thousand and One Nights; fragmented after 10th century; Mongols destroy Baghdad (1258).")
add("fatimid-caliphate", "Fatimid Caliphate (الخلافة الفاطمية al-Ḫilāfa al-Fāṭimiyya)", "CulturalAge", "holocene", 909, 1171, "CE",
    "Ismaili Shia caliphate; founded Cairo (969); Al-Azhar University; rival to Abbasids and Umayyads of Córdoba; cultural and scientific achievements.")
add("seljuk-empire", "Seljuk Empire (Büyük Selçuklu Devleti)", "CulturalAge", "holocene", 1037, 1194, "CE",
    "Turkic Sunni Muslim empire; Battle of Manzikert (1071, opened Anatolia); Nizam al-Mulk; madrasas; triggered First Crusade; Persian cultural patronage.")
add("ayyubid-dynasty", "Ayyubid Dynasty (الدولة الأيوبية)", "CulturalAge", "holocene", 1171, 1260, "CE",
    "Saladin (Salah ad-Din); recaptured Jerusalem (1187); Kurdish dynasty; Egypt and Syria; chivalric reputation; succeeded by Mamluks.")
add("mamluk-sultanate", "Mamluk Sultanate (سلطنة المماليك)", "CulturalAge", "holocene", 1250, 1517, "CE",
    "Slave-soldier dynasty ruling Egypt and Syria; defeated Mongols at Ain Jalut (1260); Cairo cultural center; Mamluk architecture; fell to Ottomans.")
add("ottoman-empire", "Ottoman Empire (Osmanlı İmparatorluğu / الدولة العثمانية / Οθωμανική Αυτοκρατορία / Osmanlı Devleti / Османска империя / Otoman İmparatorluğu)", "CulturalAge", "holocene", 1299, 1922, "CE",
    "One of longest-lasting empires; Constantinople conquered (1453); Suleiman the Magnificent; three continents; millet system; Hagia Sophia mosque; 'Sick Man of Europe'; dissolved after WWI.")
add("ottoman-golden-age", "Ottoman Golden Age (Osmanlı İmparatorluğu'nun Yükselme Devri)", "CulturalAge", "ottoman-empire", 1453, 1566, "CE",
    "Mehmed II to Suleiman; Constantinople/Istanbul capital; Topkapi Palace; Sinan (architect); legal reforms (Kanuni); naval dominance in Mediterranean.")
add("safavid-iran", "Safavid Empire (دولت صفویه / Dowlat-e Safaviye)", "CulturalAge", "holocene", 1501, 1736, "CE",
    "Shia Islam as state religion of Iran; Isfahan ('half the world'); Shah Abbas I; Persian carpet golden age; rivalry with Ottomans and Mughals.")
add("afsharid-dynasty", "Afsharid Dynasty (افشاریان)", "CulturalAge", "holocene", 1736, 1796, "CE",
    "Nader Shah, 'last great Asiatic conqueror'; reunified Iran; invaded Mughal India (1739), looted Peacock Throne and Koh-i-Noor diamond.")
add("zand-dynasty", "Zand Dynasty (زندیه)", "CulturalAge", "holocene", 1751, 1794, "CE",
    "Karim Khan Zand ('Advocate of the People'); Shiraz capital; Arg of Karim Khan; most humane Iranian ruler of Islamic era; Kurdish Lak origin.")
add("qajar-dynasty", "Qajar Dynasty (سلسله قاجار Silsile-ye Qājār)", "CulturalAge", "holocene", 1789, 1925, "CE",
    "Iranian dynasty; Tehran capital; Constitutional Revolution (1906); oil concessions to Britain; modernization struggles; replaced by Pahlavi dynasty.")
# --- Arabian Peninsula (pre-Islamic) ---
# --- Ancient Near East / Levant (pre-Classical) ---
add("natufian", "Natufian Culture (الثقافة النطوفية / Natufien)", "CulturalAge", "holocene", 12500, 9500, "BCE",
    "Levantine Epipaleolithic culture; first sedentary or semi-sedentary settlements; wild cereal harvesting with sickle blades; Ain Mallaha (Eynan), Wadi en-Natuf; transition to agriculture; dog domestication.")
add("gobekli-tepe", "Göbekli Tepe (گۆبەکلی تەپە / Portasar)", "CulturalAge", "holocene", 9500, 8000, "BCE",
    "World's oldest known megalithic temple complex; T-shaped limestone pillars with animal reliefs; pre-agricultural ritual center; Şanlıurfa Province, Turkey; UNESCO World Heritage Site (2018); revolutionized Neolithic understanding.")
add("ppna", "Pre-Pottery Neolithic A (PPNA / العصر الحجري الحديث ما قبل الفخار أ)", "CulturalAge", "holocene", 10000, 8700, "BCE",
    "Earliest Neolithic in the Levant; Jericho tower and wall; sedentary villages without pottery; wild and early domesticated cereals; skull cult; round houses; 'Neolithic Revolution' begins.")
add("ppnb", "Pre-Pottery Neolithic B (PPNB / العصر الحجري الحديث ما قبل الفخار ب)", "CulturalAge", "holocene", 8700, 6500, "BCE",
    "Levantine Neolithic; rectangular multi-room houses; domesticated wheat, barley, sheep, goats, cattle; Ain Ghazal statues; Çayönü; long-distance obsidian trade; plaster skulls; population boom.")
add("catalhoyuk", "Çatalhöyük (Çatal Höyük)", "CulturalAge", "holocene", 7500, 5700, "BCE",
    "Neolithic proto-city in central Anatolia; ~3,000-8,000 inhabitants; roof-entry houses without streets; elaborate wall paintings and reliefs; Mother Goddess figurines; UNESCO World Heritage Site (2012); James Mellaart and Ian Hodder excavations.")
add("dilmun", "Dilmun (دلمون / Telmun)", "CulturalAge", "holocene", 3000, 538, "BCE",
    "Ancient civilization on Bahrain and eastern Arabia; major Sumerian trading partner; described in Epic of Gilgamesh as paradise; Barbar temples; Qal'at al-Bahrain (UNESCO); freshwater springs; royal burial mounds.")

add("sabaean-kingdom", "Sabaean Kingdom / Sheba (مملكة سبأ)", "CulturalAge", "holocene", 1000, 275, "BCE-CE",
    "Dominant South Arabian kingdom; Ma'rib Great Dam; frankincense and myrrh trade ('Arabia Felix'); biblical Queen of Sheba; deity Almaqah.")
add("himyarite-kingdom", "Himyarite Kingdom (مملكة حمير)", "CulturalAge", "holocene", 110, 525, "BCE-CE",
    "Unified Yemen; royal conversion to Judaism (4th century); Zafar capital; fell to Aksumite-Byzantine alliance; critical pre-Islamic Arabian history.")
add("nabataean-kingdom", "Nabataean Kingdom (المملكة النبطية)", "CulturalAge", "holocene", 168, 106, "BCE-CE",
    "Arab kingdom centered on Petra (UNESCO); water engineering masters; controlled incense trade routes; Al-Khazneh; annexed by Rome as Arabia Petraea.")

# --- Caucasus ---
add("kingdom-of-armenia", "Kingdom of Armenia (Հայաստանի Թագավորություն)", "CulturalAge", "holocene", 331, 428, "BCE-CE",
    "Orontid, Artaxiad, Arsacid dynasties; Tigranes the Great; first nation to adopt Christianity (301 CE); bridge between Roman and Persian worlds.")
add("cilician-armenia", "Cilician Armenia (Կիլիկիա Հայոց Թագավորություն)", "CulturalAge", "holocene", 1080, 1375, "CE",
    "Armenian kingdom-in-exile; key Crusader ally; last Christian state in Levant; major trade hub (port of Ayas); fell to Mamluks 1375.")
add("kingdom-of-georgia", "Kingdom of Georgia (საქართველოს სამეფო)", "CulturalAge", "holocene", 1008, 1490, "CE",
    "David IV the Builder and Queen Tamar; dominant Caucasian Christian power; pan-Caucasian empire; Shota Rustaveli's 'The Knight in the Panther's Skin'.")

add("modern-middle-east", "Modern Middle East (الشرق الأوسط الحديث / خاورمیانه مدرن)", "CulturalAge", "contemporary", 1918, 0, "CE",
    "Ottoman collapse; Sykes-Picot; mandates; Israel founded (1948); oil economy; Arab-Israeli conflicts; Iranian Revolution (1979); Gulf Wars; Arab Spring.")

# ═══════════════════════════════════════════════════════════════
# OCEANIAN HISTORICAL & CULTURAL PERIODS
# ═══════════════════════════════════════════════════════════════

# --- Australia ---
add("oceania-history", "Oceanian Historical Periods (Oceaniens historiska perioder)", "CulturalAge", "holocene", 65000, 0, "BCE-CE",
    "Oldest continuous cultures on Earth; Aboriginal Australians, Melanesian, Polynesian, Micronesian peoples; maritime mastery; colonial disruption.")
add("aboriginal-australia", "Aboriginal Australian Periods (Aboriginsk australisk historia)", "CulturalAge", "oceania-history", 65000, 1788, "BCE-CE",
    "Oldest continuous civilization; Dreamtime/Dreaming; rock art (Kakadu, Kimberley); fire-stick farming; ~250 language groups; 65,000+ years.")
add("aboriginal-early", "Early Aboriginal Period (Tidig aboriginsk period)", "CulturalAge", "aboriginal-australia", 65000, 10000, "BCE",
    "First Australians arrive (~65,000 BP); Lake Mungo burials (~42,000 BP); megafauna coexistence and extinction; continent-wide spread; earliest rock art.")
add("aboriginal-holocene", "Aboriginal Holocene Period (Aboriginsk holocen period)", "CulturalAge", "aboriginal-australia", 10000, 1788, "BCE-CE",
    "Sea level rise creates modern coastline; Torres Strait Islands separate; intensification; fish traps (Brewarrina ~40,000 years); complex trade networks; songlines.")
add("budj-bim", "Budj Bim Cultural Landscape (Budj Bim / Gunditjmara)", "CulturalAge", "aboriginal-australia", 6600, 1788, "BCE-CE",
    "Gunditjmara people, Victoria; world's oldest aquaculture system (~6,600 years); eel traps and stone channels; permanent stone dwellings; UNESCO World Heritage Site (2019).")
add("torres-strait-islanders", "Torres Strait Islander Culture (Ailan Kastom)", "CulturalAge", "oceania-history", 8000, 0, "BCE-CE",
    "Melanesian peoples of Torres Strait Islands; distinct from Aboriginal Australians; seafaring; horticulture; Tombstone Opening ceremonies; star lore navigation.")
add("australian-colonial", "Colonial Australia (Koloniala Australien)", "CulturalAge", "oceania-history", 1788, 1901, "CE",
    "First Fleet (1788); penal colony; frontier wars; gold rushes (1850s); pastoralism; Stolen Generations begin; six colonies; White Australia policy roots.")
add("australian-federation", "Federation and Modern Australia (Australiens federation och modern tid)", "CulturalAge", "oceania-history", 1901, 0, "CE",
    "Commonwealth of Australia (1901); Gallipoli (1915); White Australia policy (ended 1973); Mabo decision (1992); Sorry Day; multiculturalism.")

# --- Melanesia ---
add("melanesia-history", "Melanesian Civilizations (Melanesiska civilisationer)", "CulturalAge", "oceania-history", 50000, 0, "BCE-CE",
    "Oldest Pacific settlement; Papua New Guinea highlands agriculture (~7000 BCE); diverse cultures; Kuk Swamp; Lapita pottery tradition.")
add("sahul-settlement", "Settlement of Sahul (Bosättningen av Sahul)", "CulturalAge", "melanesia-history", 50000, 30000, "BCE",
    "First humans in New Guinea/Australia (connected as Sahul); maritime crossing from Sunda; earliest evidence of ocean voyaging by humans.")
add("png-highlands", "Papua New Guinea Highlands Cultures (Ol kalsa bilong hailans)", "CulturalAge", "melanesia-history", 40000, 1930, "BCE-CE",
    "Diverse highland societies; 850+ languages; sweet potato revolution (~1600 CE); sing-sing gatherings; kina shell currency; first European contact 1930s.")
add("kuk-early-agriculture", "Kuk Early Agriculture (Kuk Swamp / Kuk taim bilong gaden)", "CulturalAge", "melanesia-history", 7000, 4000, "BCE",
    "Kuk Swamp, PNG highlands; independent invention of agriculture; banana, taro, yam cultivation; drainage ditches; one of world's earliest farming sites.")
add("ancient-fiji", "Ancient Fiji (Viti Makawa)", "CulturalAge", "melanesia-history", 1300, 1874, "BCE-CE",
    "Settled by Lapita people ~1300 BCE; complex chiefdom system; cannibal culture; drua double-hulled canoes; cultural crossroads of Melanesia and Polynesia.")
add("lapita-culture", "Lapita Culture (Lapita-kulturen)", "CulturalAge", "oceania-history", 1600, 500, "BCE",
    "Ancestral Polynesian culture; distinctive dentate-stamped pottery; originated Bismarck Archipelago; spread to Fiji, Tonga, Samoa; skilled navigators.")

# --- Polynesia ---
add("polynesia-history", "Polynesian Civilizations (Polynesiska civilisationer)", "CulturalAge", "oceania-history", 1500, 0, "BCE-CE",
    "Greatest maritime expansion in human history; settled Pacific from Tonga/Samoa to Hawaiʻi, Easter Island, New Zealand; navigation by stars, currents, birds.")
add("polynesia-ancestral", "Ancestral Polynesia (Tonga & Samoa)", "CulturalAge", "polynesia-history", 1500, 200, "BCE",
    "Tonga settled ~1500 BCE, Samoa ~1000 BCE; development of Polynesian culture, language, navigation; chiefdom societies; kava traditions.")
add("polynesia-expansion", "Polynesian Expansion (Te Hekenga-ā-Polynesia)", "CulturalAge", "polynesia-history", 200, 1200, "CE",
    "Long-pause then rapid expansion; Marquesas (~300 CE), Hawaiʻi (~1000 CE), Rapa Nui (~1200 CE); double-hulled canoes; star navigation.")
add("rapa-nui", "Rapa Nui (Easter Island)", "CulturalAge", "polynesia-history", 1200, 1722, "CE",
    "Moai statues (~900 carved); ahu platforms; rongorongo script (undeciphered); ecological transformation; European contact (1722).")
add("cook-islands-settlement", "Cook Islands Settlement (Kūki 'Āirani)", "CulturalAge", "polynesia-history", 800, 1595, "CE",
    "Settlement from Society Islands; coral architecture; lagoon aquaculture; Rarotonga seat of power; pre-European contact societies.")
add("tuamotu-settlement", "Tuamotu Settlement (Tuāmotu)", "CulturalAge", "polynesia-history", 900, 1595, "CE",
    "Settlement of remote atolls; pearl diving; celestial navigation mastery; coral-atoll adaptation; pre-European contact societies.")
add("ancient-hawaii", "Ancient Hawaiʻi (Hawaiʻi kahiko)", "CulturalAge", "polynesia-history", 1000, 1795, "CE",
    "Settlement from Marquesas/Tahiti; ahupuaʻa land management; heiau temples; kapu system; taro cultivation; fish ponds; ali'i chiefs.")
add("hawaiian-kingdom", "Kingdom of Hawaiʻi (Aupuni Mōʻī o Hawaiʻi)", "CulturalAge", "polynesia-history", 1795, 1893, "CE",
    "Kamehameha I unifies islands; constitutional monarchy; Hawaiian Renaissance; written language; sugar plantations; overthrown by U.S.-backed coup (1893).")
add("tui-manua", "Tuʻi Manuʻa (Tupu o Manuʻa)", "CulturalAge", "polynesia-history", 1000, 1904, "CE",
    "Ancient Samoan paramount chieftainship; Manuʻa Islands (Taʻū, Ofu, Olosega); oldest Polynesian title; legendary Tagaloa origin; ceded to U.S. 1904.")
add("tui-tonga-empire", "Tuʻi Tonga Empire (Puleʻanga Tuʻi Tonga)", "CulturalAge", "polynesia-history", 950, 1865, "CE",
    "Maritime empire spanning central Pacific; Tongatapu capital; Haʻamonga trilithon; influenced Samoa, Fiji, Niue; one of Polynesia's largest polities.")

# --- Micronesia ---
add("micronesia-history", "Micronesian Civilizations (Mikronesiska civilisationer)", "CulturalAge", "oceania-history", 2000, 0, "BCE-CE",
    "Thousands of small islands; skilled navigators; Carolinian stick charts; varied cultures from Palau to Marshall Islands.")
add("nan-madol", "Nan Madol (Nahnihmw Madol)", "CulturalAge", "micronesia-history", 1180, 1628, "CE",
    "Megalithic city built on artificial islets, Pohnpei; 'Venice of the Pacific'; basalt log-cabin architecture; Saudeleur dynasty; UNESCO site.")
add("palau-earthworks", "Palau Earthwork Era (Belau a terraces)", "CulturalAge", "micronesia-history", 1200, 1600, "CE",
    "Monumental earthwork terraces on Babeldaob; largest earthworks in Oceania; hillside terracing for agriculture and defense; stone villages; bai meeting houses.")
add("marshallese-navigation", "Marshallese Navigation Tradition (Wāppepe in M̧ajeļ)", "CulturalAge", "micronesia-history", 500, 1900, "CE",
    "Stick chart navigation (mattang, meddo, rebbelib); wave piloting; outrigger canoes; settlement of remote atolls; unique ocean-reading knowledge.")
add("chamorro-ancient", "Ancient Chamorro (CHamoru)", "CulturalAge", "micronesia-history", 1500, 1668, "BCE-CE",
    "Mariana Islands (Guam, Saipan); latte stone pillars; rice cultivation unique in Pacific; proa sailing canoes; matrilineal society; Spanish colonization begins 1668.")

# --- New Zealand / Aotearoa ---
add("aotearoa-history", "Aotearoa / New Zealand History (Hītori o Aotearoa)", "CulturalAge", "oceania-history", 1250, 0, "CE",
    "Last major landmass settled by humans; Māori culture; Treaty of Waitangi (1840); bicultural nation.")
add("maori-settlement", "Māori Settlement Period (Te Wā o te Taenga Mai)", "CulturalAge", "aotearoa-history", 1250, 1500, "CE",
    "East Polynesian voyagers arrive; moa hunting; early pā (fortified villages); adaptation to temperate climate; kūmara cultivation.")
add("maori-classic", "Classic Māori Period (Te Ao Māori Tawhito)", "CulturalAge", "aotearoa-history", 1500, 1769, "CE",
    "Elaborate pā fortifications; whakairo (carving); tā moko (tattoo); haka; complex tribal (iwi) society; inter-tribal warfare; greenstone (pounamu) trade.")
add("new-zealand-colonial", "Colonial New Zealand (Aotearoa i koroniana)", "CulturalAge", "aotearoa-history", 1769, 1907, "CE",
    "Cook arrives (1769); sealers, whalers; Musket Wars; Treaty of Waitangi (1840); New Zealand Wars (1845-72); gold rushes; Dominion status (1907).")
add("new-zealand-modern", "Modern New Zealand (Aotearoa hou)", "CulturalAge", "aotearoa-history", 1907, 0, "CE",
    "Women's suffrage (1893, first nation); Gallipoli; welfare state; Māori Renaissance; nuclear-free (1987); Treaty settlements; multicultural Aotearoa.")

# --- Colonial & Modern Pacific ---
add("colonial-pacific", "Colonial Pacific (Koloniala Stilla havet)", "CulturalAge", "oceania-history", 1521, 1975, "CE",
    "Magellan (1521); Spanish, British, French, German, Japanese, American colonial claims; copra trade; nuclear testing (Bikini, Moruroa); independence wave.")
add("pacific-nuclear-era", "Pacific Nuclear Testing Era (Essais nucléaires dans le Pacifique)", "CulturalAge", "colonial-pacific", 1946, 1996, "CE",
    "Bikini Atoll (1946); 315+ nuclear tests in Pacific; Marshall Islands, French Polynesia, Christmas Island; health and environmental devastation; ban movement.")
add("pacific-independence", "Pacific Island Independence (Stillahavsnationernas självständighet)", "CulturalAge", "contemporary", 1962, 0, "CE",
    "Western Samoa first (1962); Fiji, PNG, Vanuatu, Kiribati follow; Pacific Islands Forum; climate change existential threat; 'Blue Pacific' identity.")

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
lines.append(f'    dcterms:description "{len(DATA)} entries covering the geologic time scale from Hadean eon (4600 Ma) to present, including Scandinavian, European, and South American cultural/historical periods."@en ;')
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
    elif unit == "BCE-CE":
        lines.append(f'    time:hasBeginning [ rdfs:label "{start} BCE" ] ;')
        if end == 0:
            lines.append(f'    time:hasEnd [ rdfs:label "Present" ] ;')
        else:
            lines.append(f'    time:hasEnd [ rdfs:label "{end} CE" ] ;')
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
    elif unit == "BCE-CE":
        item["time:hasBeginning"] = f"{d['start']} BCE"
        item["time:hasEnd"] = "Present" if d["end"] == 0 else f"{d['end']} CE"
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
    "dcterms:description": f"{len(DATA)} entries covering the geologic time scale from Hadean eon (4600 Ma) to present, including Scandinavian, European, and South American cultural/historical periods.",
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
