# T0 — Basics of HTTP / HTTPS

## Introduction

HTTP (HyperText Transfer Protocol) is the fundamental protocol used for communication between a client (browser, application) and a web server.  
HTTPS (HTTP Secure) is the secure version of HTTP, using TLS/SSL encryption to protect the exchanged data.

This T0 aims to establish the foundational knowledge required to understand REST APIs and how the web works.

---

## Objectives

- Differentiate HTTP and HTTPS
- Understand the structure of an HTTP request
- Understand the structure of an HTTP response
- Identify and explain common HTTP methods
- Identify and interpret HTTP status codes

---

## Differences Between HTTP and HTTPS

### HTTP
- Data transmitted in plain text
- Port 80
- No protection against interception or modification

### HTTPS
- Data encrypted via TLS/SSL
- Port 443
- Protection against interception, modification, and Man-in-the-Middle attacks
- Authentication via digital certificate

---

## Structure of an HTTP Request

An HTTP request is composed of:
1. Request line
2. Headers
3. Blank line
4. Body (optional)

### Example:

```
GET /index.html HTTP/1.1
Host: example.com
User-Agent: Chrome
Accept: text/html
```

---

## Structure of an HTTP Response

An HTTP response contains:
1. Status line
2. Headers
3. Blank line
4. Body

### Example:

```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1024

<html>...</html>
```

---

## Common HTTP Methods

- **GET** — Retrieve a resource (e.g., load a web page)
- **POST** — Send data (e.g., create a resource)
- **PUT** — Replace an existing resource
- **DELETE** — Delete a resource

---

## HTTP Status Codes

- **200** — OK (Request successful)
- **201** — Created (Resource created)
- **301** — Moved Permanently (Redirection)
- **400** — Bad Request (Malformed request)
- **401** — Unauthorized (Authentication required)
- **403** — Forbidden (Access denied)
- **404** — Not Found (Resource does not exist)
- **500** — Internal Server Error (Server error)

---

## Conclusion

HTTP is the fundamental protocol of the web.  
HTTPS is its secure version using TLS to protect data exchanges.

Understanding how they work is essential for working with REST APIs and developing secure web applications.
