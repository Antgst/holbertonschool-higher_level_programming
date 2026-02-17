
# T1 — Consume Data from an API using curl

## Introduction

curl (Client URL) est un outil en ligne de commande permettant de transférer des données vers ou depuis un serveur via différents protocoles (HTTP, HTTPS, FTP, etc.).  
Il est largement utilisé pour tester des APIs REST, diagnostiquer des problèmes serveur et manipuler des requêtes HTTP directement depuis le terminal.

Cette T1 vise à apprendre à consommer une API via curl.

---

# 🎯 Objectifs

À la fin de cet exercice, l’étudiant doit être capable de :

- Installer et vérifier curl
- Exécuter une requête HTTP simple
- Interagir avec une API publique
- Lire et interpréter une réponse JSON
- Utiliser des options avancées (-I, -X, -d)
- Comprendre la structure d’une réponse API

---

# 🛠 Installation et vérification

Commande de vérification :

```
curl --version
```

Résultat attendu :
- Version installée
- Protocoles supportés (HTTP, HTTPS…)
- Fonctionnalités activées (SSL, IPv6, etc.)

---

# 🌍 Requête simple

Exemple :

```
curl http://example.com
```

Objectif :
- Vérifier qu’une requête HTTP fonctionne
- Observer le contenu HTML retourné

---

# 📡 Consommation d’une API (JSONPlaceholder)

API publique utilisée :
https://jsonplaceholder.typicode.com/

## Requête GET

```
curl https://jsonplaceholder.typicode.com/posts
```

Résultat attendu :
- Tableau JSON
- Chaque objet contient :
  - userId
  - id
  - title
  - body

Notion importante :
- Les APIs REST retournent généralement du JSON.

---

# 📄 Récupérer uniquement les headers

```
curl -I https://jsonplaceholder.typicode.com/posts
```

Option utilisée :
- `-I` → affiche uniquement les headers

Permet d’observer :
- Code de statut (200 OK)
- Content-Type
- Cache-Control
- Server
- Date

---

# ✏️ Requête POST

```
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

Options utilisées :
- `-X POST` → spécifie la méthode HTTP
- `-d` → envoie des données dans le body

Résultat attendu :
- JSON retourné avec un nouvel id (souvent 101)
- Simulation de création de ressource

Important :
JSONPlaceholder ne sauvegarde pas réellement les données. Il simule la création.

---

# 🧠 Notions importantes

## 1️⃣ curl est un client HTTP

Il permet de :
- Tester des endpoints
- Simuler des requêtes frontend
- Debugger une API backend

## 2️⃣ Flags essentiels

- `-I` → headers uniquement
- `-X` → spécifier méthode HTTP
- `-d` → envoyer des données
- `-H` → ajouter un header personnalisé
- `| jq` → formater proprement du JSON

Exemple :

```
curl https://jsonplaceholder.typicode.com/posts | jq
```

---

# 📊 Ce que l’évaluateur vérifie

- Tu sais utiliser curl sans interface graphique
- Tu comprends la différence GET / POST
- Tu sais lire une réponse JSON
- Tu sais identifier un code de statut
- Tu comprends la relation méthode → action API

---

# 🚀 Conclusion

curl est un outil fondamental pour tout développeur backend.

Maîtriser :
- Les requêtes HTTP
- Les headers
- Les méthodes
- Le JSON

est indispensable pour travailler avec des APIs REST, tester des endpoints Flask, ou diagnostiquer des erreurs serveur.
