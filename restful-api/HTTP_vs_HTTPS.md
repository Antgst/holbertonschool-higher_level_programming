# Basics of HTTP/HTTPS -- Summary (FR & EN)

------------------------------------------------------------------------

# 🇫🇷 VERSION FRANÇAISE

## 1) Différence entre HTTP et HTTPS

HTTP (HyperText Transfer Protocol) est un protocole de communication
permettant l'échange de données entre un client (navigateur) et un
serveur web. Les données sont transmises en clair, sans chiffrement.

HTTPS (HyperText Transfer Protocol Secure) n'est pas un protocole
différent : il s'agit de HTTP fonctionnant au-dessus d'une couche de
sécurité SSL/TLS. HTTPS ajoute le chiffrement des données,
l'authentification du serveur via certificat numérique et la garantie
d'intégrité des données.

### Différences principales :

-   **HTTP** : données non chiffrées (port 80)
-   **HTTPS** : données chiffrées via SSL/TLS (port 443)
-   HTTPS protège contre l'interception, la modification et les attaques
    man-in-the-middle

------------------------------------------------------------------------

## 2) Structure d'une requête et d'une réponse HTTP

### Structure d'une requête HTTP :

1.  **Request Line** : Méthode + Chemin + Version HTTP\
2.  **Headers** : informations supplémentaires (Host, Content-Type,
    etc.)\
3.  Ligne vide\
4.  **Body (optionnel)** : données envoyées au serveur (POST/PUT)

### Exemple :

``` http
POST /api/users HTTP/1.1
Host: example.com
Content-Type: application/json

{
  "name": "Antoine"
}
```

``` http
GET /index.html HTTP/1.1
Host: example.com
User-Agent: Chrome
Accept: text/html
```

------------------------------------------------------------------------

### Structure d'une réponse HTTP :

1.  **Status Line** : Version HTTP + Code + Message\
2.  **Headers** : métadonnées de la réponse\
3.  Ligne vide\
4.  **Body** : contenu retourné (HTML, JSON, etc.)

### Exemple :

``` http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": 1,
  "name": "Antoine"
}
```

------------------------------------------------------------------------

## 3) Méthodes HTTP courantes

-   **GET** -- Récupère une ressource sans modifier les données (ex :
    charger une page web)
-   **POST** -- Envoie des données pour créer une ressource (ex :
    création d'utilisateur)
-   **PUT** -- Met à jour ou remplace une ressource existante (ex :
    modification de profil)
-   **DELETE** -- Supprime une ressource existante (ex : suppression de
    compte)

------------------------------------------------------------------------

## 4) Codes de statut HTTP courants

### Catégorisation des codes HTTP

Les codes de statut HTTP sont classés par familles selon leur premier
chiffre :

-   **1xx** : Information
-   **2xx** : Succès
-   **3xx** : Redirection
-   **4xx** : Erreur côté client
-   **5xx** : Erreur côté serveur

Cette classification permet d'identifier rapidement la nature de la
réponse retournée par le serveur.

### Codes courants :

-   **200 -- OK** : La requête a été traitée avec succès\
-   **201 -- Created** : Une nouvelle ressource a été créée avec succès\
-   **301 -- Moved Permanently** : La ressource a été déplacée vers une
    nouvelle URL\
-   **404 -- Not Found** : La ressource demandée n'existe pas sur le
    serveur\
-   **500 -- Internal Server Error** : Une erreur interne empêche le
    serveur de traiter la requête

------------------------------------------------------------------------

# 🇬🇧 ENGLISH VERSION

## 1) Difference between HTTP and HTTPS

HTTP (HyperText Transfer Protocol) is a communication protocol used
between a client (browser) and a web server. Data is transmitted in
plain text.

HTTPS (HyperText Transfer Protocol Secure) is not a different protocol.
It is HTTP running over a secure SSL/TLS layer. HTTPS provides data
encryption, server authentication via digital certificate, and data
integrity protection.

### Main differences:

-   **HTTP**: unencrypted data (port 80)
-   **HTTPS**: encrypted data via SSL/TLS (port 443)
-   HTTPS protects against interception, tampering, and
    man-in-the-middle attacks

------------------------------------------------------------------------

## 2) Structure of an HTTP request and response

### HTTP Request structure:

1.  **Request Line**: Method + Path + HTTP Version\
2.  **Headers**: additional metadata\
3.  Blank line\
4.  **Body (optional)**: data sent to the server

### Example:

``` http
POST /api/users HTTP/1.1
Host: example.com
Content-Type: application/json

{
  "name": "Antoine"
}
```

------------------------------------------------------------------------

### HTTP Response structure:

1.  **Status Line**: HTTP Version + Status Code + Message\
2.  **Headers**: response metadata\
3.  Blank line\
4.  **Body**: returned content

### Example:

``` http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": 1,
  "name": "Antoine"
}
```

------------------------------------------------------------------------

## 3) Common HTTP methods

-   **GET** -- Retrieves a resource without modifying data (e.g.,
    fetching a web page)
-   **POST** -- Sends data to create a resource (e.g., creating a user)
-   **PUT** -- Updates or replaces an existing resource (e.g., updating
    a profile)
-   **DELETE** -- Removes an existing resource (e.g., deleting an
    account)

------------------------------------------------------------------------

## 4) Common HTTP status codes

### HTTP Status Code Classification

HTTP status codes are grouped into categories based on their first
digit:

-   **1xx**: Informational\
-   **2xx**: Success\
-   **3xx**: Redirection\
-   **4xx**: Client error\
-   **5xx**: Server error

This classification helps quickly identify the nature of the server's
response.

### Common codes:

-   **200 -- OK**: The request was successfully processed\
-   **201 -- Created**: A new resource was successfully created\
-   **301 -- Moved Permanently**: The resource has been redirected to a
    new URL\
-   **404 -- Not Found**: The requested resource does not exist\
-   **500 -- Internal Server Error**: The server encountered an internal
    error
