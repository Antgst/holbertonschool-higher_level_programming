#!/usr/bin/python3
# Exercice Python - Inheritance & Abstract Classes
# Univers : Créatures du Seigneur des Anneaux

"""
OBJECTIF:
Créer un système de créatures magiques en utilisant :
- l'héritage
- les classes abstraites
- les méthodes abstraites
- l'encapsulation

CONSIGNES GÉNÉRALES:
- Respecte la POO (attributs privés, getters/setters)
- Utilise ABC et abstractmethod
- Ne modifie pas le code de test
- Complète uniquement les parties indiquées par TODO

"""

from abc import ABC, abstractmethod
import random


class CreatureMagique(ABC):
    """
    Classe abstraite représentant une créature magique
    """

    def __init__(self, nom, dangerosite):
        """
        Attributs:
        - nom (str)
        - dangerosite (int entre 1 et 10)
        Tous les attributs doivent être privés
        """
        # TODO
        pass

    @property
    def nom(self):
        # TODO
        pass

    @property
    def dangerosite(self):
        # TODO
        pass

    @abstractmethod
    def attaquer(self):
        """
        Méthode abstraite
        Chaque créature attaque différemment
        """
        pass

    @abstractmethod
    def decrire(self):
        """
        Méthode abstraite
        Retourne une description de la créature
        """
        pass


class Dragon(CreatureMagique):
    """
    Classe Dragon héritant de CreatureMagique
    """

    def __init__(self, nom, dangerosite, couleur_flamme):
        """
        Attribut supplémentaire:
        - couleur_flamme (str)
        """
        # TODO:
        pass

    def attaquer(self):
        """
        Affiche une attaque basée sur le feu
        """
        # TODO
        pass

    def decrire(self):
        """
        Retourne une description complète du dragon
        """
        # TODO
        pass


class Elfe(CreatureMagique):
    """
    Classe Elfe héritant de CreatureMagique
    """

    def __init__(self, nom, dangerosite, clan):
        """
        Attribut supplémentaire:
        - clan (str)
        """
        # TODO
        pass

    def attaquer(self):
        """
        Affiche une attaque basée sur l'arc ou la magie
        """
        # TODO
        pass

    def decrire(self):
        """
        Retourne une description complète de l'elfe
        """
        # TODO
        pass


class Balrog(CreatureMagique):
    """
    Classe Balrog - démon de feu et d'ombre
    """

    def __init__(self, nom, dangerosite, arme):
        """
        Attribut supplémentaire:
        - arme (str): fouet enflammé, épée de feu, etc.
        """
        # TODO:
        pass

    def attaquer(self):
        """
        Attaque avec feu et ténèbres
        """
        # TODO
        pass

    def decrire(self):
        """
        Retourne une description complète du Balrog
        """
        # TODO
        pass


class Nazgul(CreatureMagique):
    """
    Classe Nazgul - Spectres de l'Anneau
    """

    def __init__(self, nom, dangerosite, monture):
        """
        Attribut supplémentaire:
        - monture (str): cheval noir ou créature ailée
        """
        # TODO
        pass

    def attaquer(self):
        """
        Attaque avec cri spectral et lame maudite
        """
        # TODO
        pass

    def decrire(self):
        """
        Retourne une description complète du Nazgûl
        """
        # TODO
        pass


class Orque(CreatureMagique):
    """
    Classe Orque - serviteurs de Sauron
    """

    def __init__(self, nom, dangerosite, tribu):
        """
        Attribut supplémentaire:
        - tribu (str): Moria, Mordor, Isengard, etc.
        """
        # TODO
        pass

    def attaquer(self):
        """
        Attaque brutale et sauvage
        """
        # TODO
        pass

    def decrire(self):
        """
        Retourne une description complète de l'Orque
        """
        # TODO
        pass


class Ent(CreatureMagique):
    """
    Classe Ent - bergers d'arbres
    """

    def __init__(self, nom, dangerosite, foret):
        """
        Attribut supplémentaire:
        - foret (str): forêt d'origine
        """
        # TODO
        pass

    def attaquer(self):
        """
        Attaque lente mais puissante
        """
        # TODO
        pass

    def decrire(self):
        """
        Retourne une description complète de l'Ent
        """
        # TODO
        pass


class Araignee(CreatureMagique):
    """
    Classe Araignée - descendantes d'Ungoliant (comme Shelob)
    """

    def __init__(self, nom, dangerosite, venin):
        """
        Attribut supplémentaire:
        - venin (str): type de venin
        """
        # TODO
        pass

    def attaquer(self):
        """
        Attaque avec morsure venimeuse et toile
        """
        # TODO
        pass

    def decrire(self):
        """
        Retourne une description complète de l'Araignée
        """
        # TODO
        pass


class Troll(CreatureMagique):
    """
    Classe Troll - créatures massives et stupides
    """

    def __init__(self, nom, dangerosite, type_troll):
        """
        Attribut supplémentaire:
        - type_troll (str): des cavernes, des montagnes, de pierre, etc.
        """
        # TODO
        pass

    def attaquer(self):
        """
        Attaque brutale et désordonnée
        """
        # TODO
        pass

    def decrire(self):
        """
        Retourne une description complète du Troll
        """
        # TODO: retourner la description
        pass


class Bestiaire:
    """
    Classe qui gère un ensemble de créatures magiques
    """

    def __init__(self):
        """
        Attribut:
        - creatures (liste)
        """
        # TODO
        pass

    def ajouter_creature(self, creature):
        """
        Ajoute une créature au bestiaire
        Vérifie que c'est bien une instance de CreatureMagique
        """
        # TODO
        pass

    def afficher_creatures(self):
        """
        Affiche la description de toutes les créatures
        """
        # TODO
        pass

    def attaque_generale(self):
        """
        Toutes les créatures du bestiaire attaquent
        """
        # TODO
        pass


class Boromir(CreatureMagique):
    """
    Classe Boromir - Homme du Gondor, capitaine valeureux mais maudit
    """

    def __init__(self, nom, dangerosite, arme):
        """
        Attribut supplémentaire:
        - arme (str): épée, cor du Gondor, etc.
        """
        # TODO:
        # 1. Appeler le constructeur parent
        # 2. Créer attribut privé __arme
        pass

    def attaquer(self):
        """
        Attaque courageuse mais souvent fatale
        Génère des dégâts aléatoires entre 1 et dangerosite * 7
        Choisit aléatoirement entre "épée", "bouclier", "cor du Gondor"

        PARTICULARITÉ: 95% de chances de mourir en attaquant!
        - Si random <= 0.95 (95%): Boromir meurt percé de flèches
        - Sinon (5%): attaque normale avec possibilité d'échec critique si dégâts <= 6
        """
        # TODO: implémenter l'attaque de Boromir avec 95% de mort
        # Utiliser random.random() qui retourne un nombre entre 0 et 1
        # Si random.random() <= 0.95: Boromir meurt
        # Sinon: attaque normale
        pass

    def decrire(self):
        """
        Retourne une description complète de Boromir
        Format: "Homme du Gondor [nom]: dangerosité [X], armé de [arme]"
        """
        # TODO: retourner la description
        pass

if __name__ == "__main__":
    # NE PAS MODIFIER CE CODE DE TEST

    # Créatures originales
    dragon = Dragon("Smaug", 9, "rouge")
    elfe = Elfe("Legolas", 4, "Sylvestre")

    # Nouvelles créatures LOTR
    balrog = Balrog("Durin's Bane", 10, "fouet enflammé")
    nazgul = Nazgul("Witch-king d'Angmar", 9, "créature ailée")
    orque = Orque("Uglúk", 5, "Isengard")
    ent = Ent("Sylvebarbe", 7, "Fangorn")
    araignee = Araignee("Shelob", 8, "paralysant")
    troll = Troll("Grimbold", 6, "des cavernes")

    # Création du bestiaire
    bestiaire = Bestiaire()
    bestiaire.ajouter_creature(dragon)
    bestiaire.ajouter_creature(elfe)
    bestiaire.ajouter_creature(balrog)
    bestiaire.ajouter_creature(nazgul)
    bestiaire.ajouter_creature(orque)
    bestiaire.ajouter_creature(ent)
    bestiaire.ajouter_creature(araignee)
    bestiaire.ajouter_creature(troll)

    print("\n=== BESTIAIRE DE LA TERRE DU MILIEU ===")
    print("\n--- Créatures enregistrées ---")
    bestiaire.afficher_creatures()

    print("\n--- Attaques individuelles ---")
    dragon.attaquer()
    elfe.attaquer()
    balrog.attaquer()
    nazgul.attaquer()

    print("\n--- Attaque générale ! ---")
    bestiaire.attaque_generale()

    # Ajouter Boromir
    boromir = Boromir("Boromir fils de Denethor", 6, "épée et bouclier")

    # Création du bestiaire
    bestiaire = Bestiaire()
    # ... (ajouts existants)
    bestiaire.ajouter_creature(boromir)

    # ... (reste du code)

    print("\n--- Test spécial Boromir (va-t-il survivre?) ---")
    for i in range(5):
        print(f"\nTentative {i+1}:")
        boromir.attaquer()
