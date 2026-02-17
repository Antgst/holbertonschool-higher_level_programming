# Consume Data from an API using curl (FR & EN)

------------------------------------------------------------------------

# 🇫🇷 VERSION FRANÇAISE

## 🎯 Objectif

Démontrer la capacité à :

-   Vérifier que `curl` est installé
-   Récupérer le contenu d'une page web
-   Consommer une API REST (GET)
-   Inspecter les headers d'une réponse HTTP
-   Envoyer des données via POST
-   Interpréter les résultats obtenus

------------------------------------------------------------------------

## 1) Vérifier l'installation de curl

### Commande

``` bash
curl --version
```

### Résultat attendu

-   Affichage de la version installée
-   Liste des protocoles supportés (HTTP, HTTPS, etc.)

------------------------------------------------------------------------

## 2) Récupérer une page web (GET)

### Commande

``` bash
curl http://example.com
```

### Résultat attendu

-   Affichage du HTML brut de la page (body de la réponse)

------------------------------------------------------------------------

## 3) Récupérer des données depuis une API (GET JSON)

### Commande

``` bash
curl https://jsonplaceholder.typicode.com/posts
```

### Résultat attendu

-   Retour d'un tableau JSON
-   Chaque objet contient généralement :
    -   `userId`
    -   `id`
    -   `title`
    -   `body`

### Interprétation

Cela confirme que l'endpoint est accessible et retourne des données JSON
structurées.

------------------------------------------------------------------------

## 4) Inspecter uniquement les headers

### Commande

``` bash
curl -I https://jsonplaceholder.typicode.com/posts
```

### Résultat attendu

-   Affichage uniquement des headers
-   Présence du status code (ex: `HTTP/1.1 200 OK`)
-   `Content-Type`
-   Date, Server, etc.

### Interprétation

Permet d'analyser les métadonnées HTTP sans télécharger le contenu.

------------------------------------------------------------------------

## 5) Envoyer des données via POST

### Commande

``` bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

### Résultat attendu

-   Retour d'un objet JSON simulant la création
-   Généralement :
    -   `title`: "foo"
    -   `body`: "bar"
    -   `userId`: "1"
    -   `id`: 101

### Interprétation

-   `-X POST` définit la méthode HTTP
-   `-d` envoie les données dans le body
-   JSONPlaceholder simule la création sans sauvegarde réelle

------------------------------------------------------------------------

## ✅ Conclusion (FR)

Je sais :

-   Exécuter des requêtes GET et POST avec curl
-   Lire et interpréter une réponse JSON
-   Inspecter les headers HTTP
-   Comprendre la structure d'un échange client-serveur

------------------------------------------------------------------------

# 🇬🇧 ENGLISH VERSION

## 🎯 Objective

Demonstrate the ability to:

-   Verify curl installation
-   Fetch a webpage
-   Consume a REST API (GET)
-   Inspect HTTP response headers
-   Send data using POST
-   Interpret server responses

------------------------------------------------------------------------

## 1) Check curl installation

### Command

``` bash
curl --version
```

### Expected result

-   Displays installed curl version
-   Lists supported protocols (HTTP, HTTPS, etc.)

------------------------------------------------------------------------

## 2) Fetch a webpage (GET)

### Command

``` bash
curl http://example.com
```

### Expected result

-   Returns the raw HTML content (response body)

------------------------------------------------------------------------

## 3) Fetch data from an API (GET JSON)

### Command

``` bash
curl https://jsonplaceholder.typicode.com/posts
```

### Expected result

-   Returns a JSON array
-   Each object contains:
    -   `userId`
    -   `id`
    -   `title`
    -   `body`

### Interpretation

Confirms the endpoint is reachable and returns structured JSON data.

------------------------------------------------------------------------

## 4) Fetch headers only

### Command

``` bash
curl -I https://jsonplaceholder.typicode.com/posts
```

### Expected result

-   Displays only HTTP headers
-   Includes status code (e.g., `HTTP/1.1 200 OK`)
-   `Content-Type`
-   Date, Server, etc.

### Interpretation

Useful for analyzing HTTP metadata without downloading the body.

------------------------------------------------------------------------

## 5) Send data using POST

### Command

``` bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

### Expected result

-   Returns a JSON object simulating creation
-   Typically:
    -   `title`: "foo"
    -   `body`: "bar"
    -   `userId`: "1"
    -   `id`: 101

### Interpretation

-   `-X POST` specifies the HTTP method
-   `-d` sends data in the request body
-   JSONPlaceholder simulates creation without persistence

------------------------------------------------------------------------

## ✅ Conclusion (EN)

I can:

-   Perform GET and POST requests using curl
-   Read and interpret JSON responses
-   Inspect HTTP headers
-   Understand client-server interaction structure
