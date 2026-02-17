# T4 — Develop a Simple API using Python with Flask

## Introduction

Flask is a lightweight web framework for Python, widely used to develop REST APIs and small to medium-sized web applications.

Unlike `http.server`, Flask provides:
- A simple routing system
- Clean request and response handling
- Simplified JSON management
- A structure closer to a real backend

This T4 aims to build a simple REST API using Flask.

---

# 🎯 Objectives

At the end of this exercise, the student should be able to:

- Install and configure Flask
- Run a development server
- Define and manage routes (endpoints)
- Return JSON using `jsonify`
- Handle dynamic routes
- Process POST requests
- Implement proper error handling

---

# 🛠 Setup

## Installation

```
pip install Flask
```

## Minimal Structure

- Import Flask
- Instantiate the application:
  ```
  app = Flask(__name__)
  ```
- Run the server:
  ```
  flask --app task_04_flask.py run
  ```

Server accessible at:
```
http://localhost:5000
```

---

# 📡 Expected Endpoints

## 1️⃣ Root Route `/`

Expected return:
```
Welcome to the Flask API!
```

---

## 2️⃣ Endpoint `/data`

- Returns the list of usernames stored in memory
- Uses `jsonify()`
- Expected structure:
  ```
  ["jane", "john"]
  ```

Users are stored in a dictionary:

```
users = {
  "jane": {...},
  "john": {...}
}
```

---

## 3️⃣ Endpoint `/status`

Expected return:
```
OK
```

Used to verify that the API is working.

---

## 4️⃣ Dynamic Endpoint `/users/<username>`

- Uses a dynamic Flask route
- Returns the full object corresponding to the username

Example response:
```
{
  "username": "jane",
  "name": "Jane",
  "age": 28,
  "city": "Los Angeles"
}
```

If the user does not exist:

- Status code 404
- Response:
```
{"error": "User not found"}
```

---

# ✏️ Handling POST Requests

## Endpoint `/add_user`

- Method: POST
- Uses:
  ```
  request.get_json()
  ```

## Expected Behavior

1️⃣ Invalid JSON  
→ 400  
```
{"error": "Invalid JSON"}
```

2️⃣ Missing username  
→ 400  
```
{"error": "Username is required"}
```

3️⃣ Username already exists  
→ 409  
```
{"error": "Username already exists"}
```

4️⃣ Success  
→ 201  
```
{
  "message": "User added",
  "user": {...}
}
```

---

# 🧠 Important Concepts

## 1️⃣ Routing with Decorators

Routes are defined using:

```
@app.route("/path", methods=["GET", "POST"])
```

Each route corresponds to a function.

---

## 2️⃣ Dynamic Routes

Flask allows:

```
/users/<username>
```

The parameter is automatically passed to the function.

---

## 3️⃣ jsonify()

- Automatically converts a Python dictionary into JSON
- Sets the `Content-Type: application/json` header

---

## 4️⃣ HTTP Status Code Handling

Possible return:

```
return jsonify({...}), 201
```

Flask allows easily associating a status code with a response.

---

## 5️⃣ In-Memory Storage

Data is stored in a Python dictionary.
⚠️ It disappears when the server restarts.

---

# 📊 What the Evaluator Checks

- Functional Flask server
- Properly defined routes
- Well-formed JSON
- Robust error handling
- Consistent HTTP status codes (200, 201, 400, 404, 409)
- Clear logical separation of endpoints

---

# 🚀 Expected Results

| Endpoint | Result |
|----------|--------|
| `/` | Welcome to the Flask API! |
| `/data` | List of usernames |
| `/status` | OK |
| `/users/<username>` | User object or 404 |
| `/add_user` (POST) | 201 or appropriate error |

---

# 🏁 Conclusion

This T4 marks the transition from a basic HTTP server to a real backend framework.

It introduces:
- Structured routing
- Simplified JSON handling
- Dynamic routes
- POST requests
- Proper error management

It is a solid foundation for building complete REST APIs with Flask.
