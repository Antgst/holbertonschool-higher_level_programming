# T2 — Consuming and Processing Data from an API using Python

## Introduction

Python is widely used to interact with APIs thanks to its readability and its rich ecosystem of libraries.  
The `requests` library simplifies HTTP communication and allows sending requests to web services.  
Once the data is retrieved, Python makes it easy to manipulate it (JSON, CSV, etc.).

This T2 aims to teach how to consume an API in Python, process JSON data, and convert it into a structured format.

---

# 🎯 Objectives

At the end of this exercise, the student should be able to:

- Install and use the `requests` library
- Send an HTTP GET request in Python
- Check an HTTP status code
- Parse a JSON response
- Manipulate structured data
- Export data to a CSV file

---

# 🛠 Installation

If necessary:

```
pip install requests
```

---

# 📡 Retrieving Data from an API

API used:
https://jsonplaceholder.typicode.com/

## GET Request

Using:

```
requests.get()
```

Returns:
- `Response` object
- Access to properties:
  - `status_code`
  - `headers`
  - `text`
  - `json()`

---

# 🧩 Function 1 — fetch_and_print_posts()

## Expected Behavior

- Send a GET request to `/posts`
- Print the status code:
  
  Expected example:
  ```
  Status Code: 200
  ```

- If successful (200):
  - Parse the response using `.json()`
  - Iterate over the posts
  - Print only the titles

## Important Concepts

- `.json()` automatically converts the response into a Python object
- The returned JSON is a list of dictionaries
- Each post contains:
  - userId
  - id
  - title
  - body

---

# 🧠 Processing JSON

The JSON returned by the API is converted into:

```
list[dict]
```

Each element of the list represents a post.

Possible manipulations:
- `for` loop
- List comprehension
- Access keys via `post["title"]`

---

# 📁 Function 2 — fetch_and_save_posts()

## Expected Behavior

- Send the same GET request
- Check the status code
- Structure the data as:

```
[
  {"id": ..., "title": ..., "body": ...},
  ...
]
```

- Write the data into a `posts.csv` file
- Expected columns:
  - id
  - title
  - body

---

# 📄 Writing CSV

Using the standard module:

```
csv.DictWriter
```

Advantages:
- Automatically generates headers
- Writes each dictionary as a row
- Compatible with structured data

Expected result:
- `posts.csv` file
- One row per post
- Consistent columns

---

# 📊 What the evaluator checks

- You can use `requests.get()`
- You understand the role of `status_code`
- You can parse JSON
- You can transform API data into a usable structure
- You can export to a standard format (CSV)
- You respect function separation

---

# 🚀 Expected Result

After execution:

```
Status Code: 200
sunt aut facere repellat provident occaecati excepturi optio reprehenderit
qui est esse
...
```

And creation of the file:

```
posts.csv
```

Containing the columns:
- id
- title
- body

---

# 🏁 Conclusion

This T2 introduces:

- Real API usage in Python
- JSON data processing
- Transformation into a structured format

It is a fundamental skill for backend development or data processing from a web service.
