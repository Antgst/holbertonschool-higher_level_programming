# T3 — Develop a Simple API using Python with http.server

## Introduction

The `http.server` module is part of Python’s standard library.  
It allows you to create a simple HTTP server without external dependencies.

Although it is not intended for production use, it helps to understand the basics:
- how a web server works
- handling HTTP requests
- basic routing
- sending JSON responses

This T3 aims to build a minimal API to understand backend fundamentals.

---

# 🎯 Objectives

At the end of this exercise, the student should be able to:

- Create an HTTP server using `http.server`
- Handle different HTTP requests (mainly GET)
- Implement multiple endpoints
- Return properly formatted JSON
- Handle errors (404 Not Found)
- Define headers correctly

---

# 🛠 Server Setup

## Expected Steps

1. Create a class inheriting from:
   ```
   http.server.BaseHTTPRequestHandler
   ```

2. Implement the method:
   ```
   do_GET(self)
   ```

3. Start the server on port 8000

Expected test:
```
http://localhost:8000
```

Response:
```
Hello, this is a simple API!
```

---

# 📡 Endpoint Handling

Routing relies on:

```
self.path
```

Depending on the value of `self.path`, the response changes.

---

## Root Endpoint `/`

Expected response:
```
Hello, this is a simple API!
```

Content-Type:
```
text/plain
```

---

## Endpoint `/data`

Expected JSON response:

```
{"name": "John", "age": 30, "city": "New York"}
```

Important points:

- Convert the Python dictionary to JSON using:
  ```
  json.dumps()
  ```
- Define the header:
  ```
  Content-Type: application/json
  ```

---

## Endpoint `/status`

Expected response:
```
OK
```

Used to verify that the API is working.

---

## Endpoint `/info` (if implemented)

Possible response:
```
{"version": "1.0", "description": "A simple API built with http.server"}
```

---

# ❌ Error Handling

If an undefined endpoint is called:

- Return the code:
  ```
  404
  ```
- Message:
  ```
  Endpoint not found
  ```

Useful methods:

- `send_response()`
- `send_header()`
- `end_headers()`

---

# 🧠 Important Concepts

## 1️⃣ Request → Response Cycle

- The client sends a request
- The server executes `do_GET`
- The server sends:
  - Status code
  - Headers
  - Body

---

## 2️⃣ Structure of an HTTP Response

Mandatory order:

1. `send_response(status_code)`
2. `send_header(...)`
3. `end_headers()`
4. Write the body using:
   ```
   self.wfile.write()
   ```

---

## 3️⃣ JSON in Python

- Python dictionary → JSON string:
  ```
  json.dumps()
  ```

- JSON must be sent as bytes:
  ```
  .encode()
  ```

---

## 4️⃣ Key Understanding

This T3 helps to understand:

- How a web server works internally
- How to route a request
- How to manually construct an HTTP response
- Why frameworks like Flask simplify this process

---

# 📊 What the evaluator checks

- You can create a functional HTTP server
- You understand routing via `self.path`
- You can properly return JSON
- You can define correct headers
- You can properly handle a 404 error
- You respect the request → response structure

---

# 🚀 Expected Result

| Endpoint | Result |
|----------|--------|
| `/` | Hello, this is a simple API! |
| `/data` | JSON with name, age, city |
| `/status` | OK |
| Unknown endpoint | 404 + message |

---

# 🏁 Conclusion

This T3 introduces building an API without a framework.

It helps understand fundamental concepts:
- HTTP handling
- Routing
- JSON
- Status codes
- Headers

It is a key step before using more advanced frameworks like Flask.
