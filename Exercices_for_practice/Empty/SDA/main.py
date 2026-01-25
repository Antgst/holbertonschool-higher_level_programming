#!/usr/bin/python3
"""
EXERCICE PYTHON - LA QUÊTE DE L'ANNEAU (SEIGNEUR DES ANNEAUX)

Objectif :
Survoler la majorité des notions Python vues récemment :
- listes, tuples, sets, dict
- slicing, compréhensions
- fonctions, exceptions
- ord / chr, split / join
- tri, statistiques simples

Consigne clé :
👉 Chaque TODO rappelle les DONNÉES DE DÉPART utiles pour éviter de remonter le fichier.
"""

from random import randint, seed
seed(42)

# ============================================================
# DONNÉES DE DÉPART (NE PAS MODIFIER)
# ============================================================

FELLOWSHIP = [
    "Frodo", "Sam", "Merry", "Pippin",
    "Aragorn", "Legolas", "Gimli", "Boromir", "Gandalf"
]

RACES = {
    "Frodo": "Hobbit", "Sam": "Hobbit", "Merry": "Hobbit", "Pippin": "Hobbit",
    "Aragorn": "Man", "Boromir": "Man",
    "Legolas": "Elf",
    "Gimli": "Dwarf",
    "Gandalf": "Maia"
}

JOURNEY = [
    ("The Shire", 0),
    ("Bree", 160),
    ("Rivendell", 450),
    ("Moria", 660),
    ("Lothlórien", 780),
    ("Rohan", 1040),
    ("Gondor", 1320),
    ("Mordor", 1510),
    ("Mount Doom", 1540),
]

INVENTORY = {
    "lembas": 12,
    "pipe-weed": 3,
    "mallorn_leaf": 0,
    "mithril": 1,
    "athelas": 2,
    "rope": 1,
    "dagger": 4,
    "coins": 0,
}

RUNE_CODES = [77, 101, 108, 108, 111, 110, 33]

EVENTS = [
    "Frodo|ring_seen|Bree",
    "Gandalf|late|Shire",
    "Aragorn|guide|Bree",
    "Boromir|fall|Amon Hen",
    "Gimli|axe|Moria",
    "Legolas|bow|Moria",
    "Sam|loyal|Everywhere",
    "Pippin||Moria",
    "Unknown|spy|Isengard",
]

# ============================================================
# PARTIE A — FONCTIONS
# ============================================================

def is_known(member, races):
    """Return True si member est dans races."""
    # CONTEXTE DONNÉES:
    # - member : string (ex: "Frodo")
    # - races : dict RACES (clé = nom, valeur = race)
    # TODO A1: retourne True/False sans try/except

def safe_int(value, default=0):
    """Convertit value en int, sinon default."""
    # CONTEXTE DONNÉES:
    # - value : n'importe quel type (str, None, int…)
    # - default : int par défaut
    # TODO A2: gérer ValueError ET TypeError uniquement

def summarize_steps(journey):
    """Retourne {lieu: distance}."""
    # CONTEXTE DONNÉES:
    # - journey : liste de tuples (str, int)
    #   ex: ("Bree", 160)
    # TODO A3: dict comprehension obligatoire

# ============================================================
# PARTIE B — LISTES & SLICING
# ============================================================

# CONTEXTE DONNÉES:
# - FELLOWSHIP = liste de 9 noms
# TODO B1: crée une COPIE indépendante de FELLOWSHIP

# CONTEXTE DONNÉES:
# - fellowship_copy contient "Boromir"
# TODO B2: remplace "Boromir" par "Faramir" (même index)

# CONTEXTE DONNÉES:
# - les 4 premiers membres de FELLOWSHIP sont des Hobbits
# TODO B3: extrais-les avec slicing

# CONTEXTE DONNÉES:
# - FELLOWSHIP : liste de strings
# TODO B4: crée names_upper en MAJUSCULES (list comprehension)


# CONTEXTE DONNÉES:
# - RACES associe chaque membre à une race
# TODO B5: liste de tuples (nom, race) pour Hobbit ou Man
duo_pairs = None


# ============================================================
# PARTIE C — DICT / SET / TRI
# ============================================================

# CONTEXTE DONNÉES:
# - RACES.values() contient toutes les races
# TODO C1: crée un set des races uniques
unique_races = None

# CONTEXTE DONNÉES:
# - plusieurs membres peuvent partager une race
# TODO C2: dict {race: nombre}
count_by_race = None

# CONTEXTE DONNÉES:
# - FELLOWSHIP ne doit PAS être modifiée
# TODO C3: liste triée alphabétiquement
sorted_by_name = None

# CONTEXTE DONNÉES:
# - RACES[nom] donne la race
# TODO C4: tri par (race, nom)
sorted_by_race_then_name = None


# ============================================================
# PARTIE D — STRINGS / ORD / CHR
# ============================================================

# CONTEXTE DONNÉES:
# - RUNE_CODES = liste d'entiers ASCII
# TODO D1: transforme en string avec chr()
rune_message = None

# CONTEXTE DONNÉES:
# - mot de base: "ring"
# TODO D2: décale chaque lettre de +1 (ord/chr)
elvish_tag = None

# CONTEXTE DONNÉES:
# - rune_message et elvish_tag existent
# TODO D3: f-string "{rune_message} Tag={elvish_tag}"
summary_line = None


# ============================================================
# PARTIE E — PARSING & EXCEPTIONS
# ============================================================

valid_events = []
unknown_count = 0
empty_action_count = 0

# CONTEXTE DONNÉES:
# - EVENTS : strings "member|action|place"
# - RACES : membres connus
# TODO E1:
# - split '|'
# - ignore membre inconnu
# - ignore action vide
# - append dict sinon
# - utiliser safe_int AU MOINS une fois
pass


# ============================================================
# PARTIE F — SIMULATION
# ============================================================

fatigue_by_member = {}
top3_fatigued = []
average_fatigue_by_race = {}

# CONTEXTE DONNÉES:
# - JOURNEY[-1] contient la distance finale
# TODO F1: récupère la distance finale
final_distance = None

# CONTEXTE DONNÉES:
# - fatigue = distance // 100 + randint(0, 3)
# TODO F2: construire fatigue_by_member
pass

# CONTEXTE DONNÉES:
# - fatigue_by_member dict
# TODO F3: top 3 fatigues décroissantes
pass

# CONTEXTE DONNÉES:
# - RACES associe membre → race
# TODO F4:
# - moyenne par race
# - arrondir à 2 décimales
pass


# ============================================================
# PARTIE G — INVENTAIRE
# ============================================================

def add_item(inv, item, qty=1):
    # CONTEXTE DONNÉES:
    # - inv = INVENTORY
    # TODO G1: qty invalide ou négatif → ValueError
    pass


def consume_item(inv, item, qty=1):
    # CONTEXTE DONNÉES:
    # - si stock insuffisant → False
    # TODO G2: pas de KeyError
    pass


# CONTEXTE DONNÉES:
# - lembas = 12
# - dagger = 4
# - coins = 0
# TODO G3:
# - +5 lembas
# - -2 dagger
# - -999 coins (doit échouer)
pass


# ============================================================
# ASSERTS FINAUX
# ============================================================

# CONTEXTE DONNÉES:
# - FELLOWSHIP ne doit jamais changer
# TODO Z1: ajoute 6 asserts max (invariants)
pass
