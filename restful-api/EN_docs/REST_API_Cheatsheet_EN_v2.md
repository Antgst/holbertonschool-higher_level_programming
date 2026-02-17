# 🚀 REST API Module — Cheatsheet

---

# 🔹 HTTP Basics

### Request Structure
```
METHOD /path HTTP/1.1
Headers

Body
```

### Response Structure
```
HTTP/1.1 200 OK
Headers

Body
```

### Common Methods
- GET → Retrieve
- POST → Create
- PUT → Replace
- DELETE → Remove

### Important Status Codes
- 200 OK
- 201 Created
- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 500 Internal Server Error

---

# 🔹 curl Commands

```
curl --version
curl http://example.com
curl -I https://api.com
curl -X POST -d "key=value" https://api.com
curl https://api.com | jq
```

Flags:
- -I → headers only
- -X → specify method
- -d → send data
- -H → add header

---

# 🔹 Python requests

```
import requests

response = requests.get(url)
response.status_code
data = response.json()
```

Export CSV:

```
import csv
csv.DictWriter()
```

---

# 🔹 http.server Essentials

- Inherit from BaseHTTPRequestHandler
- Implement do_GET()
- Use:
  - send_response()
  - send_header()
  - end_headers()
  - wfile.write()

---

# 🔹 Flask Essentials

Initialize app:
```
app = Flask(__name__)
```

Route:
```
@app.route("/path", methods=["GET", "POST"])
```

JSON response:
```
return jsonify(data), 200
```

Dynamic route:
```
/users/<username>
```

---

# 🔹 Authentication

## Basic Auth
- Flask-HTTPAuth
- Hash passwords (generate_password_hash)

## JWT
- Flask-JWT-Extended
- @jwt_required()
- request.get_json()
- get_jwt_identity()

Always return:
- 401 → Authentication errors
- 403 → Authorization errors

---

# 🔹 Security Rules

- Never store plain passwords
- Use strong SECRET_KEY
- Validate input JSON
- Handle missing/invalid tokens
- Protect admin routes properly

---

# 🔥 Core Backend Principles

- Client → Server → Response cycle
- Stateless communication
- Proper HTTP codes
- Clear routing
- Secure endpoints
- Structured JSON responses

Master these → You understand backend fundamentals.
