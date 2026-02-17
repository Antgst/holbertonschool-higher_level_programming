
# T0 — Basics of HTTP / HTTPS

## Introduction

HTTP (HyperText Transfer Protocol) est le protocole fondamental utilisé pour la communication entre un client (navigateur, application) et un serveur web.  
HTTPS (HTTP Secure) est la version sécurisée de HTTP, utilisant le chiffrement TLS/SSL pour protéger les données échangées.

Cette T0 vise à poser les bases nécessaires à la compréhension des APIs REST et du fonctionnement du web.

---

## Objectifs

- Différencier HTTP et HTTPS
- Comprendre la structure d’une requête HTTP
- Comprendre la structure d’une réponse HTTP
- Identifier et expliquer les méthodes HTTP courantes
- Identifier et interpréter les codes de statut HTTP

---

## Différences entre HTTP et HTTPS

### HTTP
- Données transmises en clair
- Port 80
- Aucune protection contre interception ou modification

### HTTPS
- Données chiffrées via TLS/SSL
- Port 443
- Protection contre interception, modification et attaques Man-in-the-Middle
- Authentification via certificat numérique

---

## Structure d’une requête HTTP

Une requête HTTP est composée de :
1. Ligne de requête
2. Headers
3. Ligne vide
4. Body (optionnel)

### Exemple :

```
GET /index.html HTTP/1.1
Host: example.com
User-Agent: Chrome
Accept: text/html
```

---

## Structure d’une réponse HTTP

Une réponse HTTP contient :
1. Ligne de statut
2. Headers
3. Ligne vide
4. Body

### Exemple :

```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1024

<html>...</html>
```

---

## Méthodes HTTP courantes

- **GET** — Récupérer une ressource (ex: charger une page web)
- **POST** — Envoyer des données (ex: créer une ressource)
- **PUT** — Remplacer une ressource existante
- **DELETE** — Supprimer une ressource

---

## Codes de statut HTTP

- **200** — OK (Requête réussie)
- **201** — Created (Ressource créée)
- **301** — Moved Permanently (Redirection)
- **400** — Bad Request (Requête mal formée)
- **401** — Unauthorized (Authentification requise)
- **403** — Forbidden (Accès refusé)
- **404** — Not Found (Ressource inexistante)
- **500** — Internal Server Error (Erreur serveur)

---

## Conclusion

HTTP est le protocole fondamental du web.  
HTTPS en est la version sécurisée utilisant TLS pour protéger les échanges.

Comprendre leur fonctionnement est indispensable pour travailler avec des APIs REST et développer des applications web sécurisées.
