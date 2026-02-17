
# T3 — Develop a Simple API using Python with http.server

## Introduction

Le module `http.server` fait partie de la bibliothèque standard Python.  
Il permet de créer un serveur HTTP simple sans dépendance externe.

Même s’il n’est pas destiné à la production, il permet de comprendre les bases :
- fonctionnement d’un serveur web
- gestion des requêtes HTTP
- routing basique
- envoi de réponses JSON

Cette T3 vise à construire une API minimaliste pour comprendre les fondamentaux du backend.

---

# 🎯 Objectifs

À la fin de cet exercice, l’étudiant doit être capable de :

- Créer un serveur HTTP avec `http.server`
- Gérer différentes requêtes HTTP (GET principalement)
- Implémenter plusieurs endpoints
- Retourner du JSON correctement formaté
- Gérer les erreurs (404 Not Found)
- Définir les headers correctement

---

# 🛠 Mise en place du serveur

## Étapes attendues

1. Créer une classe héritant de :
   ```
   http.server.BaseHTTPRequestHandler
   ```

2. Implémenter la méthode :
   ```
   do_GET(self)
   ```

3. Démarrer le serveur sur le port 8000

Test attendu :
```
http://localhost:8000
```

Réponse :
```
Hello, this is a simple API!
```

---

# 📡 Gestion des Endpoints

Le routing repose sur :

```
self.path
```

Selon la valeur de `self.path`, la réponse change.

---

## Endpoint racine `/`

Réponse attendue :
```
Hello, this is a simple API!
```

Content-Type :
```
text/plain
```

---

## Endpoint `/data`

Réponse JSON attendue :

```
{"name": "John", "age": 30, "city": "New York"}
```

Points importants :

- Convertir le dictionnaire Python en JSON avec :
  ```
  json.dumps()
  ```
- Définir le header :
  ```
  Content-Type: application/json
  ```

---

## Endpoint `/status`

Réponse attendue :
```
OK
```

Permet de vérifier que l’API fonctionne.

---

## Endpoint `/info` (si implémenté)

Réponse possible :
```
{"version": "1.0", "description": "A simple API built with http.server"}
```

---

# ❌ Gestion des erreurs

Si un endpoint non défini est appelé :

- Retourner le code :
  ```
  404
  ```
- Message :
  ```
  Endpoint not found
  ```

Méthodes utiles :

- `send_response()`
- `send_header()`
- `end_headers()`

---

# 🧠 Notions importantes

## 1️⃣ Cycle requête → réponse

- Le client envoie une requête
- Le serveur exécute `do_GET`
- Le serveur envoie :
  - Status code
  - Headers
  - Body

---

## 2️⃣ Structure d’une réponse HTTP

Ordre obligatoire :

1. `send_response(status_code)`
2. `send_header(...)`
3. `end_headers()`
4. Écriture du body avec :
   ```
   self.wfile.write()
   ```

---

## 3️⃣ JSON en Python

- Dictionnaire Python → JSON string :
  ```
  json.dumps()
  ```

- JSON doit être envoyé en bytes :
  ```
  .encode()
  ```

---

## 4️⃣ Compréhension clé

Cette T3 permet de comprendre :

- Comment un serveur web fonctionne en interne
- Comment router une requête
- Comment construire une réponse HTTP manuellement
- Pourquoi les frameworks comme Flask simplifient ce processus

---

# 📊 Ce que l’évaluateur vérifie

- Tu sais créer un serveur HTTP fonctionnel
- Tu comprends le routing via `self.path`
- Tu sais renvoyer du JSON correctement
- Tu sais définir les bons headers
- Tu sais gérer une erreur 404 proprement
- Tu respectes la structure requête → réponse

---

# 🚀 Résultat attendu

| Endpoint | Résultat |
|----------|----------|
| `/` | Hello, this is a simple API! |
| `/data` | JSON avec name, age, city |
| `/status` | OK |
| Endpoint inconnu | 404 + message |

---

# 🏁 Conclusion

Cette T3 introduit la création d’une API sans framework.

Elle permet de comprendre les bases fondamentales :
- gestion HTTP
- routing
- JSON
- status codes
- headers

C’est une étape clé avant d’utiliser des frameworks plus avancés comme Flask.
