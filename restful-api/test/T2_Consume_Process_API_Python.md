
# T2 — Consuming and Processing Data from an API using Python

## Introduction

Python est largement utilisé pour interagir avec des APIs grâce à sa lisibilité et à son écosystème riche en bibliothèques.  
La bibliothèque `requests` simplifie les communications HTTP et permet d’envoyer des requêtes vers des services web.  
Une fois les données récupérées, Python permet de les manipuler facilement (JSON, CSV, etc.).

Cette T2 vise à apprendre à consommer une API en Python, traiter les données JSON, puis les convertir dans un format structuré.

---

# 🎯 Objectifs

À la fin de cet exercice, l’étudiant doit être capable de :

- Installer et utiliser la bibliothèque `requests`
- Envoyer une requête HTTP GET en Python
- Vérifier un code de statut HTTP
- Parser une réponse JSON
- Manipuler des données structurées
- Exporter des données vers un fichier CSV

---

# 🛠 Installation

Si nécessaire :

```
pip install requests
```

---

# 📡 Récupération de données depuis une API

API utilisée :
https://jsonplaceholder.typicode.com/

## Requête GET

Utilisation de :

```
requests.get()
```

Retour :
- Objet `Response`
- Accès aux propriétés :
  - `status_code`
  - `headers`
  - `text`
  - `json()`

---

# 🧩 Fonction 1 — fetch_and_print_posts()

## Ce qui est attendu

- Envoyer une requête GET vers `/posts`
- Afficher le status code :
  
  Exemple attendu :
  ```
  Status Code: 200
  ```

- Si succès (200) :
  - Parser la réponse avec `.json()`
  - Itérer sur les posts
  - Afficher uniquement les titres

## Notions importantes

- `.json()` convertit automatiquement la réponse en objet Python
- Le JSON retourné est une liste de dictionnaires
- Chaque post contient :
  - userId
  - id
  - title
  - body

---

# 🧠 Traitement du JSON

Le JSON retourné par l’API est converti en :

```
list[dict]
```

Chaque élément de la liste représente un post.

Manipulations possibles :
- Boucle `for`
- List comprehension
- Accès aux clés via `post["title"]`

---

# 📁 Fonction 2 — fetch_and_save_posts()

## Ce qui est attendu

- Envoyer la même requête GET
- Vérifier le status code
- Structurer les données sous forme de :

```
[
  {"id": ..., "title": ..., "body": ...},
  ...
]
```

- Écrire les données dans un fichier `posts.csv`
- Colonnes attendues :
  - id
  - title
  - body

---

# 📄 Écriture CSV

Utilisation du module standard :

```
csv.DictWriter
```

Avantages :
- Génère automatiquement les headers
- Écrit chaque dictionnaire comme une ligne
- Compatible avec données structurées

Résultat attendu :
- Fichier `posts.csv`
- Une ligne par post
- Colonnes cohérentes

---

# 📊 Ce que l’évaluateur vérifie

- Tu sais utiliser `requests.get()`
- Tu comprends le rôle du `status_code`
- Tu sais parser du JSON
- Tu sais transformer des données API en structure exploitable
- Tu sais exporter vers un format standard (CSV)
- Tu respectes la séparation des fonctions

---

# 🚀 Résultat attendu

Après exécution :

```
Status Code: 200
sunt aut facere repellat provident occaecati excepturi optio reprehenderit
qui est esse
...
```

Et création du fichier :

```
posts.csv
```

Contenant les colonnes :
- id
- title
- body

---

# 🏁 Conclusion

Cette T2 introduit :

- L’utilisation réelle d’une API en Python
- Le traitement de données JSON
- La transformation vers un format structuré

C’est une compétence fondamentale pour tout développement backend ou traitement de données issu d’un service web.
