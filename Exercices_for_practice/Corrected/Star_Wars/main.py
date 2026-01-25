#!/usr/bin/python3
"""
EXERCICE PYTHON - L’ACADÉMIE JEDI (STAR WARS)

Objectif :
Manipuler des structures de données Python (listes, dictionnaires, tuples)
et les combiner dans un mini-scénario.

Consignes :
- Lis chaque partie.
- Ne modifie pas les données de départ (sauf quand c’est demandé).
- Remplace chaque TODO par ton code.
- Lance le script pour vérifier tes affichages.
"""

# PARTIE 1: MANIPULATION DE LISTES
# --------------------------------

padawans = [
    "Luke Skywalker", "Rey", "Ahsoka Tano", "Ezra Bridger",
    "Cal Kestis", "Kanan Jarrus", "Grogu", "Barriss Offee"
]

# TODO 1: Ajoute "Anakin Skywalker" à la fin de la liste.
# Indice: méthode de liste
# print("Liste padawans :", padawans)
padawans.append("Anakin Skywalker")
print(padawans)
print("---------------------------------------")

# TODO 2: Supprime "Barriss Offee" de la liste.
# Attention: ne supprime que si présent.
if "Barriss Offee" in padawans:
    padawans.remove("Barriss Offee")
print(padawans)
print("---------------------------------------")

# TODO 3: Affiche les 4 premiers padawans (slicing).
# Résultat attendu: une liste de 4 éléments
print(padawans[0:4])
print("---------------------------------------")

# TODO 4: Affiche une version triée par ordre alphabétique (sans modifier la liste d’origine).
print(sorted(padawans))
print("---------------------------------------")


# PARTIE 2: MANIPULATION DE DICTIONNAIRES
# --------------------------------------

# Dictionnaire associant un personnage à son alignement
# (oui, certains choix sont volontairement simplifiés pour l’exercice)
side = {
    "Luke Skywalker": "Lumière",
    "Rey": "Lumière",
    "Ahsoka Tano": "Lumière",
    "Ezra Bridger": "Lumière",
    "Cal Kestis": "Lumière",
    "Kanan Jarrus": "Lumière",
    "Grogu": "Lumière",
    "Anakin Skywalker": "Ombre"
}

# TODO 5: Ajoute "Obi-Wan Kenobi" en "Lumière".
side["Obi-Wan Kenobi"] = "Lumière"
print(side)
print("---------------------------------------")

# TODO 6: Crée un dictionnaire qui compte le nombre de personnages par alignement.
# Résultat attendu (exemple de forme): {"Lumière": X, "Ombre": Y}
# Indice: parcours des values() + get()
nombre_persos = {}
for force in side.values():
    nombre_persos[force] = nombre_persos.get(force, 0) + 1
print(nombre_persos)
print("---------------------------------------")

# TODO 7: Affiche tous les personnages "Lumière", un par ligne (format libre mais clair).
for key, value in side.items():
    if value == "Lumière":
        print(key)
print("---------------------------------------")


# PARTIE 3: MANIPULATION DE TUPLES
# -------------------------------

# Un pouvoir est représenté par un tuple: (nom, catégorie, niveau)
# niveau: 1 (simple) -> 5 (très difficile)
pouvoirs = [
    ("Télékinésie", "Force", 2),
    ("Persuasion Jedi", "Esprit", 3),
    ("Saut amplifié", "Force", 1),
    ("Éclair de Force", "Sith", 4),
    ("Guérison", "Lumière", 5),
    ("Vision", "Esprit", 3),
]

# TODO 8: Crée une liste contenant uniquement les noms des pouvoirs (dans l’ordre actuel).
power_names = []
for power, team, level in pouvoirs:
    power_names.append(power)
print(power_names)
print("---------------------------------------")

# TODO 9: Crée une liste des pouvoirs “faciles” (niveau <= 2), contenant uniquement les noms.
easy_powers = []
for power, team, level in pouvoirs:
    if level <= 2:
        easy_powers.append(power)
print(easy_powers)
print("---------------------------------------")

# TODO 10: Trie les pouvoirs par niveau (du plus faible au plus élevé) et affiche le résultat.
# Indice: sorted(..., key=...)
ord_power = []
ord_power = sorted(pouvoirs, key=lambda x: x[2])
print(ord_power)
print("---------------------------------------")


# PARTIE 4: COMBINAISON DES STRUCTURES
# -----------------------------------

# Dictionnaire associant un personnage à ses caractéristiques
# Format: "nom": (âge, "rang", ["compétence1", "compétence2", ...])
ordre = {
    "Luke Skywalker": (19, "Chevalier", ["Sabre", "Télékinésie", "Pilotage"]),
    "Rey": (20, "Initiée", ["Bâton", "Télékinésie"]),
    "Ahsoka Tano": (17, "Padawan", ["Sabre", "Agilité"]),
    "Obi-Wan Kenobi": (25, "Maître", ["Sabre", "Stratégie", "Persuasion Jedi"]),
}

# TODO 11: Ajoute la compétence "Méditation" à "Obi-Wan Kenobi".
# Attention: la valeur est un tuple -> tu dois reconstruire le tuple correctement.
age, rank, powers = ordre["Obi-Wan Kenobi"]
powers.append("Méditation")
ordre["Obi-Wan Kenobi"] = (age, rank, powers)
print(ordre)
print("---------------------------------------")

# TODO 12: Crée une liste de tous les "Maître" (noms uniquement).
masters_list = []
for key, value in ordre.items():
    if value[1] == "Maître":
        masters_list.append(key)
print(masters_list)
print("---------------------------------------")

# TODO 13: Crée un dictionnaire qui compte combien de personnages maîtrisent chaque compétence.
# Résultat attendu (forme): {"Sabre": 3, "Télékinésie": 2, ...}
# Indice: double boucle + dico.get()
table = {}
for value in ordre.values():
    for comp in value[2]:
        table[comp] = table.get(comp, 0) + 1
print(table)
print("---------------------------------------")


# DÉFI BONUS: TOURNOI DE PODRACING
# -------------------------------

coureurs = [
    {"nom": "Anakin Skywalker", "équipe": "Tatooine", "tours": [57, 57, 60]},
    {"nom": "Sebulba", "équipe": "Dug", "tours": [56, 60, 61]},
    {"nom": "Gasgano", "équipe": "Xexto", "tours": [60, 60, 60]},
    {"nom": "Ratts Tyerell", "équipe": "Aleena", "tours": [62, 58, 59]},
]

# TODO 14: Calcule le temps total de chaque coureur, ajoute-le dans la clé "total".
# Exemple: coureur["total"] = ...
# Puis détermine le vainqueur (total le plus petit) et affiche son nom.
vainqueur = None
meilleur_temps = float("inf")
for coureur in coureurs:
    total = sum(coureur["tours"])
    coureur["total"] = total
    if total < meilleur_temps:
        meilleur_temps = total
        vainqueur = coureur["nom"]
print(vainqueur)
print("---------------------------------------")

# TODO 15: Calcule le temps moyen par équipe.
# Résultat attendu (forme): {"Tatooine": XX.XX, "Dug": XX.XX, ...}
# Règle: moyenne des moyennes (moyenne des tours par coureur, puis moyenne par équipe)
# Option: arrondis à 2 décimales.
scores_equipes = {}
for coureur in coureurs:
    equipe = coureur["équipe"]
    moyenne = sum(coureur["tours"]) / len(coureur["tours"])
    scores_equipes.setdefault(equipe, []).append(moyenne)
temps_moyen_equipe = {equipe: round(sum(moyennes) / len(moyennes), 2) for equipe, moyennes in scores_equipes.items()}
print(temps_moyen_equipe)
print("---------------------------------------")
