#!/usr/bin/python3
"""
task_02_requests.py

Fetch and process posts from JSONPlaceholder using the requests library.

This module provides two functions:
- fetch_and_print_posts(): fetches all posts and prints the HTTP status code
  then prints the title of each post.
- fetch_and_save_posts(): fetches all posts and saves
selected fields (id, title, body)
  into a CSV file named 'posts.csv'.
"""


import requests
import csv

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    '''Fetch all posts from JSONPlaceholder and print their titles.

    Behavior:
    - Sends a GET request to the JSONPlaceholder /posts endpoint.
    - Prints the HTTP status code in the format: "Status Code: <code>".
    - If the request is successful (status code 200), parses the response JSON
      and prints the title of each post (one per line).'''

    r = requests.get(URL)
    print(f"Status Code: {r.status_code}")

    if r.status_code != 200:
        return

    data = r.json()
    for post in data:
        print(post.get("title", ""))


def fetch_and_save_posts():
    """Fetch all posts from JSONPlaceholder and save them to a CSV file.

    Behavior:
    - Sends a GET request to the JSONPlaceholder /posts endpoint.
    - If the request is successful (status code 200),
    builds a list of dictionaries,
      each containing: id, title, body.
    - Writes the list into 'posts.csv' using csv.DictWriter with columns:
      id, title, body."""

    r = requests.get(URL)

    if r.status_code != 200:
        return

    posts_list = [
        {
            "id": post.get("id"),
            "title": post.get("title"),
            "body": post.get("body"),
        }
        for post in r.json()
    ]

    with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldname=["id", "title", "body"])
        writer.writehader()
        writer.writrows(posts_list)
