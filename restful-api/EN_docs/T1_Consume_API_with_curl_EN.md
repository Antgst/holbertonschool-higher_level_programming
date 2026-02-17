# T1 — Consume Data from an API using curl

## Introduction

curl (Client URL) is a command-line tool used to transfer data to or from a server using various protocols (HTTP, HTTPS, FTP, etc.).  
It is widely used to test REST APIs, diagnose server issues, and manipulate HTTP requests directly from the terminal.

This T1 aims to teach how to consume an API using curl.

---

# 🎯 Objectives

At the end of this exercise, the student should be able to:

- Install and verify curl
- Execute a simple HTTP request
- Interact with a public API
- Read and interpret a JSON response
- Use advanced options (-I, -X, -d)
- Understand the structure of an API response

---

# 🛠 Installation and Verification

Verification command:

```
curl --version
```

Expected result:
- Installed version
- Supported protocols (HTTP, HTTPS…)
- Enabled features (SSL, IPv6, etc.)

---

# 🌍 Simple Request

Example:

```
curl http://example.com
```

Objective:
- Verify that an HTTP request works
- Observe the returned HTML content

---

# 📡 Consuming an API (JSONPlaceholder)

Public API used:
https://jsonplaceholder.typicode.com/

## GET Request

```
curl https://jsonplaceholder.typicode.com/posts
```

Expected result:
- JSON array
- Each object contains:
  - userId
  - id
  - title
  - body

Important concept:
- REST APIs generally return JSON.

---

# 📄 Retrieve Only Headers

```
curl -I https://jsonplaceholder.typicode.com/posts
```

Option used:
- `-I` → display headers only

Allows observation of:
- Status code (200 OK)
- Content-Type
- Cache-Control
- Server
- Date

---

# ✏️ POST Request

```
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

Options used:
- `-X POST` → specify HTTP method
- `-d` → send data in the body

Expected result:
- JSON response with a new id (often 101)
- Resource creation simulation

Important:
JSONPlaceholder does not actually save data. It simulates creation.

---

# 🧠 Important Concepts

## 1️⃣ curl is an HTTP client

It allows you to:
- Test endpoints
- Simulate frontend requests
- Debug a backend API

## 2️⃣ Essential Flags

- `-I` → headers only
- `-X` → specify HTTP method
- `-d` → send data
- `-H` → add custom header
- `| jq` → format JSON output

Example:

```
curl https://jsonplaceholder.typicode.com/posts | jq
```

---

# 📊 What the evaluator checks

- You can use curl without a graphical interface
- You understand the difference between GET and POST
- You can read a JSON response
- You can identify a status code
- You understand the relationship method → API action

---

# 🚀 Conclusion

curl is a fundamental tool for any backend developer.

Mastering:
- HTTP requests
- Headers
- Methods
- JSON

is essential for working with REST APIs, testing Flask endpoints, or diagnosing server errors.
