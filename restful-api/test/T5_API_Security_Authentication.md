
# T5 — API Security and Authentication Techniques

## Introduction

La sécurité des APIs est essentielle lorsqu’une application est exposée à Internet.  
Sans mécanismes de protection, une API peut être vulnérable à :

- Accès non autorisé aux données
- Altération des données
- Attaques par déni de service
- Usurpation d’identité

Cette T5 vise à implémenter des mécanismes d’authentification et de contrôle d’accès dans une API Flask.

---

# 🎯 Objectifs

À la fin de cet exercice, l’étudiant doit être capable de :

- Comprendre l’importance de la sécurité API
- Différencier authentification et autorisation
- Implémenter une Basic Authentication
- Implémenter une authentification par JWT
- Protéger des routes avec des décorateurs
- Mettre en place un contrôle d’accès basé sur les rôles (RBAC)
- Gérer correctement les erreurs d’authentification (401 obligatoire)

---

# 🔐 Concepts clés

## 1️⃣ Authentification vs Autorisation

- **Authentification** → Vérifie l’identité (qui es-tu ?)
- **Autorisation** → Vérifie les permissions (as-tu le droit ?)

---

# 🛠 Basic Authentication (Flask-HTTPAuth)

## Installation

```
pip install Flask-HTTPAuth
```

## Stockage des utilisateurs

Les utilisateurs sont stockés en mémoire :

```
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}
```

## Sécurité des mots de passe

Utilisation de :

- `generate_password_hash()`
- `check_password_hash()`

---

## Route protégée Basic

Endpoint :

```
/basic-protected
```

Méthode : GET  
Authentification : Basic

Résultat attendu :

- Sans credentials → 401 Unauthorized
- Avec credentials valides → "Basic Auth: Access Granted"

---

# 🔑 JWT Authentication (Flask-JWT-Extended)

## Installation

```
pip install Flask-JWT-Extended
```

## Configuration

- Définir une SECRET_KEY forte
- Initialiser JWTManager

---

## Endpoint `/login`

Méthode : POST

Reçoit :

```
{
  "username": "user1",
  "password": "password"
}
```

Si valide :

```
{
  "access_token": "<JWT_TOKEN>"
}
```

Le token contient :
- Identité utilisateur
- Rôle

---

## Route protégée JWT

Endpoint :

```
/jwt-protected
```

Décorateur :

```
@jwt_required()
```

Résultat attendu :

- Sans token → 401
- Token invalide → 401
- Token valide → "JWT Auth: Access Granted"

---

# 👑 Role-Based Access Control (RBAC)

## Endpoint `/admin-only`

- Protégé par JWT
- Vérifie que le rôle = admin

Résultats attendus :

- Token user → 403 Forbidden  
  ```
  {"error": "Admin access required"}
  ```

- Token admin →  
  ```
  "Admin Access: Granted"
  ```

---

# ⚠️ Gestion stricte des erreurs

TOUTES les erreurs d’authentification doivent retourner :

```
401 Unauthorized
```

Cas concernés :

- Token manquant
- Token invalide
- Token expiré
- Token mal formé
- Token révoqué

Utilisation de handlers personnalisés :

```
@jwt.unauthorized_loader
@jwt.invalid_token_loader
@jwt.expired_token_loader
@jwt.revoked_token_loader
@jwt.needs_fresh_token_loader
```

Chaque handler doit retourner :

```
return jsonify({"error": "..."}), 401
```

⚠️ Important pour passer les tests automatiques.

---

# 🧠 Notions importantes

## 1️⃣ JWT (JSON Web Token)

Un JWT contient :

- Header
- Payload (identité, rôle…)
- Signature

Il permet :
- Authentification stateless
- Transmission sécurisée d’informations signées

---

## 2️⃣ Sécurité minimale requise

- Mots de passe hashés
- SECRET_KEY robuste
- Vérification systématique des rôles
- Codes HTTP corrects (401 vs 403)

---

# 📊 Ce que l’évaluateur vérifie

- Basic Auth fonctionnelle
- JWT correctement généré
- Routes protégées correctement
- Vérification des rôles admin
- Gestion stricte des erreurs 401
- Respect exact des codes HTTP attendus

---

# 🚀 Résultats attendus

| Endpoint | Résultat |
|----------|----------|
| `/basic-protected` sans credentials | 401 |
| `/basic-protected` valide | Access Granted |
| `/login` valide | JWT Token |
| `/jwt-protected` sans token | 401 |
| `/jwt-protected` valide | Access Granted |
| `/admin-only` user | 403 |
| `/admin-only` admin | Admin Access: Granted |

---

# 🏁 Conclusion

Cette T5 introduit les bases fondamentales de la sécurité API :

- Authentification Basic
- Authentification JWT
- Gestion des rôles
- Gestion des erreurs normalisée

C’est une étape critique vers la création d’APIs sécurisées prêtes à être exposées publiquement.
