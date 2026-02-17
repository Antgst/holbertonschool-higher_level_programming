
# 🚀 Module API REST — Cheatsheet

---

# 🔹 Bases HTTP

### Structure d’une requête
```
METHODE /chemin HTTP/1.1
Headers

Body
```

### Structure d’une réponse
```
HTTP/1.1 200 OK
Headers

Body
```

### Méthodes courantes
- GET → Récupérer
- POST → Créer
- PUT → Remplacer
- DELETE → Supprimer

### Codes importants
- 200 OK
- 201 Created
- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 500 Internal Server Error

---

# 🔹 Commandes curl

```
curl --version
curl http://example.com
curl -I https://api.com
curl -X POST -d "cle=valeur" https://api.com
curl https://api.com | jq
```

Flags :
- -I → headers uniquement
- -X → spécifier méthode
- -d → envoyer données
- -H → ajouter header

---

# 🔹 Python requests

```
import requests

response = requests.get(url)
response.status_code
data = response.json()
```

Export CSV :

```
import csv
csv.DictWriter()
```

---

# 🔹 http.server — Essentiel

- Hériter de BaseHTTPRequestHandler
- Implémenter do_GET()
- Utiliser :
  - send_response()
  - send_header()
  - end_headers()
  - wfile.write()

---

# 🔹 Flask — Essentiel

Initialisation :
```
app = Flask(__name__)
```

Route :
```
@app.route("/chemin", methods=["GET", "POST"])
```

Réponse JSON :
```
return jsonify(data), 200
```

Route dynamique :
```
/users/<username>
```

---

# 🔹 Authentification

## Basic Auth
- Flask-HTTPAuth
- Hash des mots de passe (generate_password_hash)

## JWT
- Flask-JWT-Extended
- @jwt_required()
- request.get_json()
- get_jwt_identity()

Toujours retourner :
- 401 → Erreur d’authentification
- 403 → Erreur d’autorisation

---

# 🔹 Règles de sécurité

- Ne jamais stocker les mots de passe en clair
- Utiliser une SECRET_KEY robuste
- Valider les JSON entrants
- Gérer tokens manquants / invalides
- Protéger correctement les routes admin

---

# 🔥 Principes backend fondamentaux

- Cycle Client → Serveur → Réponse
- Communication stateless
- Codes HTTP cohérents
- Routing clair
- Endpoints sécurisés
- Réponses JSON structurées

Maîtrise ces points → Tu maîtrises les bases du backend.
