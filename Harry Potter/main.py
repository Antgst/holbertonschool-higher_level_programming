#!/usr/bin/python3
"""
EXERCICE PYTHON - LE MONDE MAGIQUE DE HARRY POTTER

Dans cet exercice, vous allez manipuler des structures de données Python 
(listes, dictionnaires et tuples) pour créer et gérer différents aspects
du monde magique de Harry Potter.
"""

# PARTIE 1: MANIPULATION DE LISTES
# --------------------------------

# Voici une liste des élèves de Poudlard
eleves_poudlard = ["Harry Potter", "Hermione Granger", "Ron Weasley", "Drago Malfoy", 
                  "Neville Londubat", "Luna Lovegood", "Ginny Weasley", "Cho Chang"]

# TODO: Ajoutez "Cedric Diggory" à la liste des élèves
eleves_poudlard.append("Cedric Diggory")
print("---------------------------------------")

# TODO: Supprimez "Drago Malfoy" de la liste
eleves_poudlard.remove("Drago Malfoy")
print("---------------------------------------")

# TODO: Affichez les 3 premiers élèves de la liste
print("les 3 premiers eleves :", eleves_poudlard[:3])
print("---------------------------------------")

# TODO: Triez la liste des élèves par ordre alphabétique et affichez-la
print("Liste des éleves triées :", sorted(eleves_poudlard))
print("---------------------------------------")
# eleves_poudlard.sort()
# print("Liste triée :", eleves_poudlard)

# PARTIE 2: MANIPULATION DE DICTIONNAIRES
# --------------------------------------

# Voici un dictionnaire qui associe les élèves à leur maison
maisons = {
    "Harry Potter": "Gryffondor",
    "Hermione Granger": "Gryffondor",
    "Ron Weasley": "Gryffondor",
    "Draco Malfoy": "Serpentard",
    "Luna Lovegood": "Serdaigle",
    "Cho Chang": "Serdaigle",
    "Cedric Diggory": "Poufsouffle",
    "Neville Londubat": "Gryffondor"
}

# TODO: Ajoutez Ginny Weasley à la maison Gryffondor
maisons["Ginny Weasley"] = "Gryffondor"

# TODO: Créez un dictionnaire comptant le nombre d'élèves par maison
# Résultat attendu: {"Gryffondor": 5, "Serpentard": 1, "Serdaigle": 2, "Poufsouffle": 1}
compte_maisons = {}
for casa in maisons.values():
    compte_maisons[casa] = compte_maisons.get(casa, 0) + 1
print("Nombre d'éleves par maison :", compte_maisons)
print("---------------------------------------")

# TODO: Affichez tous les élèves de Gryffondor
for key, value in maisons.items():
    if value == "Gryffondor":
        print("Les éleves de Gryffondor sont :", key)
print("---------------------------------------")

# PARTIE 3: MANIPULATION DE TUPLES
# -------------------------------

# Les sorts sont représentés par des tuples (nom_du_sort, effet, difficulté)
# La difficulté est notée de 1 (facile) à 5 (très difficile)
sorts = [
    ("Wingardium Leviosa", "Fait léviter des objets", 2),
    ("Expelliarmus", "Désarme l'adversaire", 3),
    ("Expecto Patronum", "Repousse les Détraqueurs", 5),
    ("Accio", "Attire un objet vers le lanceur", 2),
    ("Avada Kedavra", "Sort mortel impardonnable", 5)
]

# TODO: Créez une liste contenant uniquement les noms des sorts
sorts_names = []
for sort, effet, difficulty in sorts:
    sorts_names.append(sort)
print("Les sorts sont :", sorts_names)
print("---------------------------------------")

# TODO: Créez une liste des sorts faciles (difficulté <= 2)
sorts_difficulty = []
for sort, effet, difficulty in sorts:
    if difficulty <= 2:
        sorts_difficulty.append(sort)
print("Les sorts les plus simples sont :", sorts_difficulty)
print("---------------------------------------")

# TODO: Triez les sorts par niveau de difficulté (du plus facile au plus difficile)
ord_spells = []
# for sort, effet, difficulty in sorts:
#    for difficulty in sorts:
#        sorts_difficulty_sorted.sort()
ord_spells = sorted(sorts, key=lambda x: x[2])
print("Les sorts triés par difficulté sont :", ord_spells)
print("---------------------------------------")


# PARTIE 4: COMBINAISON DES STRUCTURES
# ----------------------------------

# Dictionnaire associant des personnages à leurs caractéristiques
# Format: {"nom": (âge, "rôle", ["compétence1", "compétence2", ...])}
personnages = {
    "Albus Dumbledore": (115, "Directeur", ["Métamorphose", "Sortilèges", "Duel"]),
    "Severus Rogue": (38, "Professeur", ["Potions", "Occlumancie", "Sortilèges"]),
    "Minerva McGonagall": (70, "Professeur", ["Métamorphose", "Duel"]),
    "Rubeus Hagrid": (65, "Garde-chasse", ["Créatures magiques"])
}

# TODO: Ajoutez une nouvelle compétence "Transplanage" à Albus Dumbledore
age, role, competences = personnages["Albus Dumbledore"]
competences.append("Transplanage")
personnages["Albus Dumbledore"] = (age, role, competences)
print("Liste des compétences: ", personnages)
print("---------------------------------------")

# TODO: Créez une liste de tous les professeurs
prof_list = []
for key, value in personnages.items():
    if value[1] == "Professeur":
        prof_list.append(key)
print("Voici la liste de vous de vous professeur :", prof_list)
print("---------------------------------------")

# TODO: Créez un dictionnaire qui compte le nombre de personnages maîtrisant chaque compétence
# Résultat attendu: {"Métamorphose": 2, "Sortilèges": 2, "Duel": 2, "Potions": 1, ...}
dico = {}
for value in personnages.values():
    for comp in value[2]:
        dico[comp] = dico.get(comp, 0) + 1
print("Voici la liste :", dico)
print("---------------------------------------")

# DÉFI BONUS: LE TOURNOI DES TROIS SORCIERS
# ----------------------------------------

champions = [
    {"nom": "Harry Potter", "école": "Poudlard", "scores": [8, 7, 9]},
    {"nom": "Cedric Diggory", "école": "Poudlard", "scores": [7, 8, 6]},
    {"nom": "Viktor Krum", "école": "Durmstrang", "scores": [9, 6, 8]},
    {"nom": "Fleur Delacour", "école": "Beauxbâtons", "scores": [6, 9, 7]}
]

# TODO: Calculez le score total de chaque champion et déterminez le vainqueur du tournoi
vainqueur = None
meilleur_score = 0
for champion in champions:
    total = sum(champion["scores"])
    champion["score_total"] = total
    if total > meilleur_score:
        meilleur_score = total
        vainqueur = champion["nom"]
print("Vainqueur du tournoi :", vainqueur)
print("---------------------------------------")

# TODO: Créez un dictionnaire qui indique le score moyen obtenu par chaque école
scores_ecoles = {}
for champion in champions:
    ecole = champion["école"]
    moyenne = sum(champion["scores"]) / len(champion["scores"])
    scores_ecoles.setdefault(ecole, []).append(moyenne)
scores_moyens_ecoles = {ecole: round(sum(moyennes) / len(moyennes), 2) for ecole, moyennes in scores_ecoles.items()}
print("Scores moyens par école :", scores_moyens_ecoles)
print("---------------------------------------")