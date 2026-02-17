# T5 — API Security and Authentication Techniques

## Introduction

API security is essential when an application is exposed to the Internet.  
Without protection mechanisms, an API can be vulnerable to:

- Unauthorized access to data
- Data alteration
- Denial-of-service attacks
- Identity impersonation

This T5 aims to implement authentication and access control mechanisms in a Flask API.

---

# 🎯 Objectives

At the end of this exercise, the student should be able to:

- Understand the importance of API security
- Differentiate authentication and authorization
- Implement Basic Authentication
- Implement JWT authentication
- Protect routes using decorators
- Set up Role-Based Access Control (RBAC)
- Properly handle authentication errors (401 required)

---

# 🔐 Key Concepts

## 1️⃣ Authentication vs Authorization

- **Authentication** → Verifies identity (who are you?)
- **Authorization** → Verifies permissions (are you allowed?)

---

# 🛠 Basic Authentication (Flask-HTTPAuth)

## Installation

```
pip install Flask-HTTPAuth
```

## User Storage

Users are stored in memory:

```
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}
```

## Password Security

Using:

- `generate_password_hash()`
- `check_password_hash()`

---

## Protected Basic Route

Endpoint:

```
/basic-protected
```

Method: GET  
Authentication: Basic

Expected result:

- Without credentials → 401 Unauthorized
- With valid credentials → "Basic Auth: Access Granted"

---

# 🔑 JWT Authentication (Flask-JWT-Extended)

## Installation

```
pip install Flask-JWT-Extended
```

## Configuration

- Define a strong SECRET_KEY
- Initialize JWTManager

---

## Endpoint `/login`

Method: POST

Receives:

```
{
  "username": "user1",
  "password": "password"
}
```

If valid:

```
{
  "access_token": "<JWT_TOKEN>"
}
```

The token contains:
- User identity
- Role

---

## JWT Protected Route

Endpoint:

```
/jwt-protected
```

Decorator:

```
@jwt_required()
```

Expected result:

- Without token → 401
- Invalid token → 401
- Valid token → "JWT Auth: Access Granted"

---

# 👑 Role-Based Access Control (RBAC)

## Endpoint `/admin-only`

- Protected with JWT
- Verifies that role = admin

Expected results:

- User token → 403 Forbidden  
  ```
  {"error": "Admin access required"}
  ```

- Admin token →  
  ```
  "Admin Access: Granted"
  ```

---

# ⚠️ Strict Error Handling

ALL authentication errors must return:

```
401 Unauthorized
```

Cases concerned:

- Missing token
- Invalid token
- Expired token
- Malformed token
- Revoked token

Using custom handlers:

```
@jwt.unauthorized_loader
@jwt.invalid_token_loader
@jwt.expired_token_loader
@jwt.revoked_token_loader
@jwt.needs_fresh_token_loader
```

Each handler must return:

```
return jsonify({"error": "..."}), 401
```

⚠️ Important to pass automated tests.

---

# 🧠 Important Concepts

## 1️⃣ JWT (JSON Web Token)

A JWT contains:

- Header
- Payload (identity, role…)
- Signature

It allows:
- Stateless authentication
- Secure transmission of signed information

---

## 2️⃣ Minimum Security Requirements

- Hashed passwords
- Strong SECRET_KEY
- Systematic role verification
- Correct HTTP status codes (401 vs 403)

---

# 📊 What the Evaluator Checks

- Functional Basic Auth
- Properly generated JWT
- Correctly protected routes
- Admin role verification
- Strict handling of 401 errors
- Exact respect of expected HTTP status codes

---

# 🚀 Expected Results

| Endpoint | Result |
|----------|--------|
| `/basic-protected` without credentials | 401 |
| `/basic-protected` valid | Access Granted |
| `/login` valid | JWT Token |
| `/jwt-protected` without token | 401 |
| `/jwt-protected` valid | Access Granted |
| `/admin-only` user | 403 |
| `/admin-only` admin | Admin Access: Granted |

---

# 🏁 Conclusion

This T5 introduces the fundamental bases of API security:

- Basic Authentication
- JWT Authentication
- Role management
- Standardized error handling

It is a critical step toward building secure APIs ready to be publicly exposed.
