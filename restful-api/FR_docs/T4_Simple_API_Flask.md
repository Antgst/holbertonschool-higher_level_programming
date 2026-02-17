
# T4 — Develop a Simple API using Python with Flask

## Introduction

Flask est un framework web léger pour Python, très utilisé pour développer des APIs REST et des applications web de petite à moyenne taille.

Contrairement à `http.server`, Flask fournit :
- Un système de routing simple
- Une gestion propre des requêtes et réponses
- Une gestion facilitée du JSON
- Une structure plus proche d’un vrai backend

Cette T4 vise à construire une API REST simple avec Flask.

---

# 🎯 Objectifs

À la fin de cet exercice, l’étudiant doit être capable de :

- Installer et configurer Flask
- Lancer un serveur de développement
- Définir et gérer des routes (endpoints)
- Retourner du JSON avec `jsonify`
- Gérer des routes dynamiques
- Traiter des requêtes POST
- Implémenter une gestion d’erreurs propre

---

# 🛠 Mise en place

## Installation

```
pip install Flask
```

## Structure minimale

- Importer Flask
- Instancier l’application :
  ```
  app = Flask(__name__)
  ```
- Lancer le serveur :
  ```
  flask --app task_04_flask.py run
  ```

Serveur accessible sur :
```
http://localhost:5000
```

---

# 📡 Endpoints attendus

## 1️⃣ Route racine `/`

Retour attendu :
```
Welcome to the Flask API!
```

---

## 2️⃣ Endpoint `/data`

- Retourne la liste des usernames stockés en mémoire
- Utilisation de `jsonify()`
- Structure attendue :
  ```
  ["jane", "john"]
  ```

Les utilisateurs sont stockés dans un dictionnaire :

```
users = {
  "jane": {...},
  "john": {...}
}
```

---

## 3️⃣ Endpoint `/status`

Retour attendu :
```
OK
```

Permet de vérifier que l’API fonctionne.

---

## 4️⃣ Endpoint dynamique `/users/<username>`

- Utilise une route dynamique Flask
- Retourne l’objet complet correspondant au username

Exemple réponse :
```
{
  "username": "jane",
  "name": "Jane",
  "age": 28,
  "city": "Los Angeles"
}
```

Si l’utilisateur n’existe pas :

- Code 404
- Réponse :
```
{"error": "User not found"}
```

---

# ✏️ Gestion des requêtes POST

## Endpoint `/add_user`

- Méthode : POST
- Utilisation de :
  ```
  request.get_json()
  ```

## Comportement attendu

1️⃣ JSON invalide  
→ 400  
```
{"error": "Invalid JSON"}
```

2️⃣ Username manquant  
→ 400  
```
{"error": "Username is required"}
```

3️⃣ Username déjà existant  
→ 409  
```
{"error": "Username already exists"}
```

4️⃣ Succès  
→ 201  
```
{
  "message": "User added",
  "user": {...}
}
```

---

# 🧠 Notions importantes

## 1️⃣ Routing avec décorateurs

Les routes sont définies avec :

```
@app.route("/path", methods=["GET", "POST"])
```

Chaque route correspond à une fonction.

---

## 2️⃣ Routes dynamiques

Flask permet :

```
/users/<username>
```

Le paramètre est automatiquement passé à la fonction.

---

## 3️⃣ jsonify()

- Convertit automatiquement un dictionnaire Python en JSON
- Définit le header `Content-Type: application/json`

---

## 4️⃣ Gestion des codes HTTP

Retour possible :

```
return jsonify({...}), 201
```

Flask permet d’associer facilement un status code à la réponse.

---

## 5️⃣ Stockage en mémoire

Les données sont conservées dans un dictionnaire Python.
⚠️ Elles disparaissent au redémarrage du serveur.

---

# 📊 Ce que l’évaluateur vérifie

- Serveur Flask fonctionnel
- Routes correctement définies
- JSON bien formé
- Gestion des erreurs robuste
- Codes HTTP cohérents (200, 201, 400, 404, 409)
- Bonne séparation logique des endpoints

---

# 🚀 Résultats attendus

| Endpoint | Résultat |
|----------|----------|
| `/` | Welcome to the Flask API! |
| `/data` | Liste des usernames |
| `/status` | OK |
| `/users/<username>` | Objet utilisateur ou 404 |
| `/add_user` (POST) | 201 ou erreur adaptée |

---

# 🏁 Conclusion

Cette T4 marque le passage d’un serveur HTTP basique à un framework backend réel.

Elle introduit :
- Le routing structuré
- La gestion simplifiée du JSON
- Les routes dynamiques
- Les requêtes POST
- La gestion propre des erreurs

C’est une base solide pour développer des APIs REST complètes avec Flask.
