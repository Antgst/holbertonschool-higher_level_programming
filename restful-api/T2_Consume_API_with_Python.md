# Consuming and Processing Data from an API using Python (FR & EN)

------------------------------------------------------------------------

# 🇫🇷 VERSION FRANÇAISE

## 🎯 Objectif

Démontrer la capacité à :

-   Utiliser la bibliothèque `requests` pour envoyer des requêtes HTTP
-   Lire et analyser une réponse HTTP
-   Parser et manipuler des données JSON en Python
-   Structurer des données
-   Exporter des données vers un fichier CSV

------------------------------------------------------------------------

## 1) Installation de la bibliothèque requests

### Commande

``` bash
pip install requests
```

------------------------------------------------------------------------

## 2) Récupérer des données depuis une API (GET)

Créer un script Python utilisant :

``` python
requests.get()
```

Endpoint utilisé :

    https://jsonplaceholder.typicode.com/posts

------------------------------------------------------------------------

## 3) Fonction fetch_and_print_posts()

### Comportement attendu

-   Effectuer une requête GET vers l'API
-   Afficher le status code :

```{=html}
<!-- -->
```
    Status Code: 200

-   Si la requête est réussie :
    -   Utiliser `.json()` pour parser la réponse
    -   Parcourir les données JSON
    -   Afficher uniquement les titres des posts

### Exemple de sortie attendue

    Status Code: 200
    sunt aut facere repellat provident occaecati excepturi optio reprehenderit
    qui est esse
    ea molestias quasi exercitationem repellat qui ipsa sit aut
    ...

------------------------------------------------------------------------

## 4) Fonction fetch_and_save_posts()

### Comportement attendu

-   Effectuer une requête GET vers l'API
-   Si succès :
    -   Structurer les données sous forme de liste de dictionnaires
    -   Chaque dictionnaire contient :
        -   id
        -   title
        -   body
-   Utiliser le module `csv`
-   Écrire les données dans un fichier `posts.csv`
-   Colonnes :
    -   id
    -   title
    -   body

------------------------------------------------------------------------

## 📄 Résultat attendu

-   Affichage du status code 200
-   Impression des titres des posts
-   Création d'un fichier `posts.csv`
-   Chaque ligne correspond à un post récupéré depuis l'API

------------------------------------------------------------------------

## ✅ Conclusion (FR)

Je sais :

-   Envoyer des requêtes HTTP avec Python
-   Utiliser `.json()` pour parser une réponse
-   Manipuler des structures de données Python
-   Convertir des données JSON en CSV
-   Structurer un script modulaire avec fonctions

------------------------------------------------------------------------

# 🇬🇧 ENGLISH VERSION

## 🎯 Objective

Demonstrate the ability to:

-   Use the `requests` library to send HTTP requests
-   Read and interpret HTTP responses
-   Parse and manipulate JSON data in Python
-   Structure data programmatically
-   Export structured data into CSV format

------------------------------------------------------------------------

## 1) Install requests library

### Command

``` bash
pip install requests
```

------------------------------------------------------------------------

## 2) Fetch data from an API (GET)

Write a Python script using:

``` python
requests.get()
```

Endpoint:

    https://jsonplaceholder.typicode.com/posts

------------------------------------------------------------------------

## 3) Function fetch_and_print_posts()

### Expected behavior

-   Send a GET request to the API
-   Print the status code:

```{=html}
<!-- -->
```
    Status Code: 200

-   If successful:
    -   Parse the response using `.json()`
    -   Iterate over the JSON data
    -   Print only the titles of the posts

### Expected output example

    Status Code: 200
    sunt aut facere repellat provident occaecati excepturi optio reprehenderit
    qui est esse
    ea molestias quasi exercitationem repellat qui ipsa sit aut
    ...

------------------------------------------------------------------------

## 4) Function fetch_and_save_posts()

### Expected behavior

-   Send a GET request to the API
-   If successful:
    -   Structure data into a list of dictionaries
    -   Each dictionary contains:
        -   id
        -   title
        -   body
-   Use Python's `csv` module
-   Write the data into a file named `posts.csv`
-   Columns:
    -   id
    -   title
    -   body

------------------------------------------------------------------------

## 📄 Expected Result

-   Status code 200 displayed
-   Titles printed to the console
-   A `posts.csv` file created
-   Each row corresponds to a post fetched from the API

------------------------------------------------------------------------

## ✅ Conclusion (EN)

I can:

-   Send HTTP requests using Python
-   Parse JSON responses using `.json()`
-   Manipulate structured Python data
-   Convert JSON data into CSV format
-   Write modular Python functions
