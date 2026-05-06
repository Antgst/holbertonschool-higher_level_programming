# 📘 Python - Server-Side Rendering

## 📌 Description

Server-side rendering is a powerful technique where web pages are generated on the server and sent to the client as fully formed HTML. This contrasts with client-side rendering, where the browser builds the web page using JavaScript and dynamic data. Through this project, you will learn how to implement SSR using Python and Flask, leveraging the Jinja templating engine to create dynamic, efficient, and SEO-friendly web applications.



### Learning Objectives

- Understand the concepts of server-side rendering and how it differs from client-side rendering.

- Learn the benefits of using server-side rendering in web development.

- Implement SSR in Python using the Flask framework.

- Utilize Jinja templating engine to dynamically generate HTML pages.

- Read and display data from various sources including JSON, CSV, and SQLite databases.

- Handle dynamic content and user inputs in web applications.



### What to Expect

In this project, you will build a Flask application that serves web pages using server-side rendering techniques. You will start by creating basic templates and gradually move towards integrating dynamic content from multiple data sources. By the end of the project, you will have a comprehensive understanding of SSR, templating, and how to build efficient, scalable web applications.



### Resources

- **MDN Web Docs on Server-Side Web Development:** [MDN Server-Side Web Development](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side)

- **Client-side vs. Server-side vs. Pre-rendering for Web Apps:** [Templating Engines in Web Development](https://www.toptal.com/developers/front-end/client-side-vs-server-side-pre-rendering)

- **Flask Documentation:** [Flask Official Documentation](https://flask.palletsprojects.com/en/stable/)

- **Python JSON Documentation:** [Python JSON Documentation](https://docs.python.org/3/library/json.html)

- **Python CSV Documentation:** [Python CSV Documentation](https://docs.python.org/3/library/csv.html)

- **Python SQLite Documentation:** [Python SQLite Documentation](https://docs.python.org/3/library/sqlite3.html)

- **Jinja2 Documentation:** [Jinja2 Documentation](https://jinja.palletsprojects.com/en/latest/)



This project will equip you with the skills needed to implement server-side rendering in your web applications, making them more efficient, SEO-friendly, and easy to maintain.

---

## 📚 Resources

_No resources detected._

---

## 🎯 Learning Objectives

_No learning objectives detected._

---

## ✅ Requirements

_No requirements detected._

---

## ⚙️ Setup

_No specific setup detected._

---

## 🧠 Quiz

_No quiz detected in the exported HTML._


---

## 🧩 Tasks

<details>
<summary>0. Creating a Simple Templating Program</summary>

**Files:**

- [`template.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-server_side_rendering/template.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-server_side_rendering`

**Task details:**

```text
0. Creating a Simple Templating Program
In this task, you will create a Python function that generates personalized invitation files from a template with placeholders and a list of objects. Each output file should be named sequentially, starting from 1. You will also implement specific error handling for various edge cases.
Objective
Understand how to use string templating in Python.
Implement file operations for reading templates and writing output files.
Handle various edge cases and errors gracefully.
Instructions
Create the Template:
Use the provided template with placeholders for
name
,
event_title
,
event_date
, and
event_location
.
Define the Data:
Use the provided list of objects as your data source.
Write the Templating Function:
Define a function named
generate_invitations
that takes two parameters:
template
and
attendees
.
Check Input Types:
Verify that
template
is a string and
attendees
is a list of dictionaries.
If
template
is not a string or
attendees
is not a list of dictionaries, log an error message and terminate the function.
Handle Empty Inputs:
Check if the template is empty and log an error message if it is.
Check if the attendees list is empty and log an error message if it is.
Process Each Attendee:
Iterate over the list of attendees and replace the placeholders in the template with the corresponding values from each attendee's dictionary.
If a value is missing, replace it with "N/A".
Generate Output Files:
Write the processed template to output files named
output_X.txt
, where
X
is the index of the attendee starting from 1.
Specific Error Handling Behaviors:
Empty Template:
If the template is empty, log an error message, "Template is empty, no output files generated." and terminate without creating any files.
Empty List of Objects:
If the list of objects is empty, log a message, "No data provided, no output files generated." and terminate without creating any files.
Missing Data in Object:
If an object is missing data for any of the placeholders, replace the missing data with the text "N/A" in the output file. For example, if
event_date
is missing, it should appear as "event_date: N/A" in the output.
Invalid Input Types:
If the input template is not a string or the list is not a list of dictionaries, log an error message indicating the type of invalid input and terminate the function.
Template File:
template.txt
Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team
Example Data for Testing:
attendees = [
    {
"name"
:
"Alice"
,
"event_title"
:
"Python Conference"
,
"event_date"
:
"2023-07-15"
,
"event_location"
:
"New York"
},
    {
"name"
:
"Bob"
,
"event_title"
:
"Data Science Workshop"
,
"event_date"
:
"2023-08-20"
,
"event_location"
:
"San Francisco"
},
    {
"name"
:
"Charlie"
,
"event_title"
:
"AI Summit"
,
"event_date"
:
None
,
"event_location"
:
"Boston"
}
]
Example Main File to Test the Program:
# Main file content
from
task_00_intro
import
generate_invitations
# Read the template from a file
with
open
(
'template.txt'
,
'r'
)
as
file:
    template_content = file.read()
# List of attendees
attendees = [
    {
"name"
:
"Alice"
,
"event_title"
:
"Python Conference"
,
"event_date"
:
"2023-07-15"
,
"event_location"
:
"New York"
},
    {
"name"
:
"Bob"
,
"event_title"
:
"Data Science Workshop"
,
"event_date"
:
"2023-08-20"
,
"event_location"
:
"San Francisco"
},
    {
"name"
:
"Charlie"
,
"event_title"
:
"AI Summit"
,
"event_date"
:
None
,
"event_location"
:
"Boston"
}
]
# Call the function with the template and attendees list
generate_invitations(template_content, attendees)
Hints:
Use Python's string
replace
method to substitute placeholders with actual values.
Use
os.path.exists
to check if a file already exists before writing.
Use
try
and
except
blocks to handle potential errors gracefully.
Resources:
Python String Methods
:
Python Official Documentation
File Handling in Python
:
Python Official Documentation
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-server_side_rendering
File:
task_00_intro.py
Score of the task
10
/10
pts
100.0%
0
correction requests
My GitHub
Connect GitHub
Connect as:
Disconnect
Repository
Select a repository…
Folder (optional)
Run the correction
QA Review
×
0. Creating a Simple Templating Program
Commit used:
User:
---
URL:
Click here
ID:
---
Author:
---
Subject:
---
Date:
---
×
Students who are done with "0. Creating a Simple Templating Program"
```

</details>

<details>
<summary>1. Creating a Basic HTML Template in Flask</summary>

**Files:**

- [`task_01_jinja.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-server_side_rendering/task_01_jinja.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-server_side_rendering`

**Task details:**

```text
1. Creating a Basic HTML Template in Flask
In this task, you will build a basic Flask application that serves a web page using a Jinja template. You will create a simple HTML template that includes various elements like headings, paragraphs, and lists, and learn how to render it as a web page using Flask. Additionally, you will learn to create reusable templates for headers and footers to promote code reusability and consistency across multiple pages.
Objective
Set up a Flask environment and create a basic Flask application.
Design HTML templates using Jinja for dynamic content rendering.
Implement reusable components in templates to maintain consistent layout across pages.
Instructions
Set Up Your Flask Environment:
Ensure Python is installed on your system.
Install Flask using pip:
sh
 pip install Flask
Create a Basic Flask Application:
In your project directory, create a Python file named
task_01_jinja.py
.
Write a basic Flask application with a route that renders an HTML template.
from
flask
import
Flask, render_template

   app = Flask(__name__)
@app.route(
'/'
)
def
home
():
return
render_template(
'index.html'
)
if
__name__ ==
'__main__'
:
       app.run(debug=
True
, port=
5000
)
Design Your HTML Template:
In a
templates
folder within your project directory, create an HTML file named
index.html
.
Design a simple HTML page with a heading (
<h1>
), a paragraph (
<p>
), and an unordered list (
<ul>
with
<li>
items).
Content for
index.html
:
<!doctype
html
>
<
html
lang
=
"en"
>
<
head
>
<
title
>
My Flask App
</
title
>
</
head
>
<
body
>
<
h1
>
Welcome to My Flask App
</
h1
>
<
p
>
This is a simple Flask application.
</
p
>
<
ul
>
<
li
>
Flask
</
li
>
<
li
>
HTML
</
li
>
<
li
>
Templates
</
li
>
</
ul
>
</
body
>
</
html
>
Render the Template in Flask:
Use Flask's
render_template
function to render the HTML template when the corresponding route is accessed.
Create Reusable Header and Footer Templates:
In the
templates
folder, create two new HTML files:
header.html
and
footer.html
.
Design simple but distinct layouts for the header and footer, and include navigation links (Home, About, Contact) to all pages into header file.
Content for
header.html
:
<
header
>
<
h1
>
My Flask App
</
h1
>
</
header
>
Content for
footer.html
:
<
footer
>
<
p
>
&copy;
2024 My Flask App
</
p
>
</
footer
>
Design Multiple Pages with Shared Header and Footer:
Create additional HTML pages
about.html
and
contact.html
.
In each of these pages (
index.html
,
about.html
and
contact.html
), include the header and footer templates without duplicating their code.
Add specific tags for each page:
In
about.html
, include an
<h1>
tag with the text "About Us" and a paragraph (
<p>
) with content describing the page.
In
contact.html
, include an
<h1>
tag with the text "Contact Us" and a paragraph (
<p>
) with content for the contact page.
Modify Flask Routes:
Add new routes in your Flask application corresponding to the additional pages you created.
@app.route(
'/about'
)
def
about
():
return
render_template(
'about.html'
)
@app.route(
'/contact'
)
def
contact
():
return
render_template(
'contact.html'
)
Hints:
Ensure your Flask application runs on port 5000.
Use the
render_template
function from Flask to render HTML templates.
Utilize Jinja's
{% include %}
statement to include reusable components like headers and footers.
Resources:
Flask Quickstart:
Flask Quickstart
HTML Basics:
HTML Tutorial on W3Schools
Flask Templating with Jinja:
Flask Templating
Jinja Template Inheritance:
Jinja Template Inheritance
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-server_side_rendering
File:
task_01_jinja.py
Score of the task
4
/4
pts
100.0%
0
correction requests
My GitHub
Connect GitHub
Connect as:
Disconnect
Repository
Select a repository…
Folder (optional)
Run the correction
QA Review
×
1. Creating a Basic HTML Template in Flask
Commit used:
User:
---
URL:
Click here
ID:
---
Author:
---
Subject:
---
Date:
---
×
Students who are done with "1. Creating a Basic HTML Template in Flask"
```

</details>

<details>
<summary>2. Creating a Dynamic Template with Loops and Conditions in Flask</summary>

**Files:**

- [`task_02_logic.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-server_side_rendering/task_02_logic.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-server_side_rendering`

**Task details:**

```text
2. Creating a Dynamic Template with Loops and Conditions in Flask
In this task, you will enhance your Flask application by integrating dynamic content into your HTML templates using Jinja's loop and conditional constructs. You will read a list of items from a JSON file and display them dynamically on a web page.
Objective
Use Jinja's loop and conditional constructs to dynamically render content in HTML templates.
Read and parse JSON data in Python.
Integrate dynamic content into your Flask application.
Instructions
Prepare Your Flask Application:
Continue using the Flask application you created in the previous exercises.
Ensure you have a basic understanding of Jinja's templating syntax.
Create a Dynamic Template:
In your
templates
folder, create a new HTML template named
items.html
with "Items List" for the title.
This template should include a loop to iterate over a list of items and display each item.
Items must be displayed as an
unordered list
.
Add a conditional statement to display a message "
No items found
" if the list is empty.
Define the Data for the Template:
In your project directory, create a file named
items.json
.
Populate
items.json
with a list of items:
{
"items"
:
[
"Python Book"
,
"Flask Mug"
,
"Jinja Sticker"
]
}
Experiment with different lists, including an empty list, to see how your template responds.
Add a Route in Flask:
Create a new route
/items
in your Flask application to render the
items.html
template with the list of items.
Use Python's
json
module to read the data from
items.json
.
Pass the list of items to the template for rendering.
Data for Testing:
{
"items"
:
[
"Python Book"
,
"Flask Mug"
,
"Jinja Sticker"
]
}
Hints:
Use Python's
json
module to read data from the JSON file.
Utilize Jinja's
{% for %}
loop to iterate over the list of items in the template.
Use the
{% if %}
statement to conditionally display the message when the list is empty.
Define the new route
/items
in your Flask application and use the
render_template
function to pass the list of items to
items.html
.
Resources:
Jinja Template Designer Documentation:
Jinja Template Designer Documentation
Flask Templating with Jinja:
Flask Templating
Testing Your Application:
After setting up the dynamic template and route, run your Flask application and navigate to the new route.  Verify that the list of items is correctly displayed on the page. Test with different lists, including an empty list, to ensure that the conditional statement works as expected.
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-server_side_rendering
File:
task_02_logic.py
Score of the task
2
/2
pts
100.0%
0
correction requests
My GitHub
Connect GitHub
Connect as:
Disconnect
Repository
Select a repository…
Folder (optional)
Run the correction
QA Review
×
2. Creating a Dynamic Template with Loops and Conditions in Flask
Commit used:
User:
---
URL:
Click here
ID:
---
Author:
---
Subject:
---
Date:
---
×
Students who are done with "2. Creating a Dynamic Template with Loops and Conditions in Flask"
```

</details>

<details>
<summary>3. Displaying Data from JSON or CSV Files in Flask</summary>

**Files:**

- [`task_03_files.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-server_side_rendering/task_03_files.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-server_side_rendering`

**Task details:**

```text
3. Displaying Data from JSON or CSV Files in Flask
In this task, you will build a feature in your Flask application to read and display product data from two different data formats: JSON and CSV. You will create a single HTML template that can display data from either file type, depending on a query parameter provided in the URL. You will add functionality to your Flask application to filter product data based on an optional
id
query parameter. Additionally, you will handle edge cases such as invalid
source
parameter values or when the specified
id
is not found in the data.
Objective
Read and parse data from JSON and CSV files.
Use query parameters in Flask to determine data sources and filter criteria.
Implement error handling for invalid inputs and missing data.
Render dynamic data in HTML templates using Jinja.
Instructions
Prepare Data Files:
Create a JSON file (
products.json
) containing a list of products, each with an
id
,
name
,
category
, and
price
.
Example JSON
content
format:
[
{
"id"
:
1
,
"name"
:
"Laptop"
,
"category"
:
"Electronics"
,
"price"
:
799.99
}
,
{
"id"
:
2
,
"name"
:
"Coffee Mug"
,
"category"
:
"Home Goods"
,
"price"
:
15.99
}
]
Create a CSV file (
products.csv
) with similar data, using columns for
id
,
name
,
category
, and
price
.
Example CSV
content
:
id
,name,category,price
 1,Laptop,Electronics,799.99
 2,Coffee Mug,Home Goods,15.99
Create a Dynamic Template:
In your
templates
folder, create an HTML template
product_display.html
for displaying the product data.
Design the template to display the data in a table format with headings for Name, Category, and Price.
Modify Flask Application:
In
task_03_files.py
, create a route in your Flask application that accepts a
source
query parameter (values
json
or
csv
) and an optional
id
.
Depending on the
source
parameter, read and parse data from the corresponding file.
Implement logic to filter data by the specified
id
if provided. If
id
is not provided, display all products.
Pass the parsed data to the
product_display.html
template for rendering.
Implement File Reading Logic:
Write functions to read and parse data from both JSON and CSV files.
Ensure the data is converted into a format that can be easily displayed by the template.
Handle Edge Cases:
If
source
is neither
json
nor
csv
, return a "Wrong source" error message in the template.
If
id
is provided but not found in the file, display a "Product not found" error message in the template.
Modify the
product_display.html
template to handle and display error messages if necessary.
Hints:
Use Python's
json
module to read data from the JSON file.
Use Python's
csv
module to read data from the CSV file.
Utilize Flask's
request.args
to get query parameters.
Use Jinja's templating features to conditionally display error messages and dynamic data.
Resources:
Reading JSON and CSV in Python:
JSON:
JSON in Python
CSV:
CSV File Reading and Writing
Flask Request Object:
Flask Request Object
Query Parameters in Flask:
Flask Request Object
Error Handling in Flask:
Flask Error Handling
Testing Your Application:
Test your application with various scenarios:
Access URLs like
http://localhost:5000/products?source=json
,
http://localhost:5000/products?source=csv
, and
http://localhost:5000/products?source=xml
(invalid source).
Test with and without the
id
parameter, and with both valid and invalid
id
values.
Verify that the application correctly filters data, displays all products when no
id
is provided, and shows appropriate error messages for edge cases.
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-server_side_rendering
File:
task_03_files.py
Score of the task
5
/5
pts
100.0%
0
correction requests
My GitHub
Connect GitHub
Connect as:
Disconnect
Repository
Select a repository…
Folder (optional)
Run the correction
QA Review
×
3. Displaying Data from JSON or CSV Files in Flask
Commit used:
User:
---
URL:
Click here
ID:
---
Author:
---
Subject:
---
Date:
---
×
Students who are done with "3. Displaying Data from JSON or CSV Files in Flask"
```

</details>

<details>
<summary>4. Extending Dynamic Data Display to Include SQLite in Flask</summary>

**Files:**

- [`Name your SQLite database file`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-server_side_rendering/Name your SQLite database file)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-server_side_rendering`

**Task details:**

```text
4. Extending Dynamic Data Display to Include SQLite in Flask
Building on the previous exercise, you will now add the functionality to fetch and display data from a SQLite database in your Flask application. The application should allow users to choose between JSON, CSV, and SQL (SQLite database) as data sources using the
source
query parameter.
Objective
Set up and interact with a SQLite database in a Flask application.
Extend existing functionality to handle multiple data sources.
Implement error handling for database-related issues.
Instructions
Database Setup:
SQLite Database File:
Name your SQLite database file
products.db
.
Table Structure:
Create a
Products
table with columns:
id
(primary key),
name
,
price
,
category
.
Example Data:
Insert the following data into the
Products
table:
id
: 1,
name
: "Laptop",
price
: 799.99,
category
: "Electronics"
id
: 2,
name
: "Coffee Mug",
price
: 15.99,
category
: "Home Goods"
Use the following script to create and populate the database:
import
sqlite3
def
create_database
():
       conn = sqlite3.connect(
'products.db'
)
       cursor = conn.cursor()
       cursor.execute(
'''
           CREATE TABLE IF NOT EXISTS Products (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               category TEXT NOT NULL,
               price REAL NOT NULL
           )
       '''
)
       cursor.execute(
'''
           INSERT INTO Products (id, name, category, price)
           VALUES
           (1, 'Laptop', 'Electronics', 799.99),
           (2, 'Coffee Mug', 'Home Goods', 15.99)
       '''
)
       conn.commit()
       conn.close()
if
__name__ ==
'__main__'
:
       create_database()
Modify the Existing Dynamic Template:
Use the same HTML template (
product_display.html
) created in Task 3 for displaying product data.
Implement SQLite Data Source:
Extend the existing Flask route to handle
source=sql
as a query parameter.
Implement logic to fetch data from the SQLite database when this parameter is used.
Ensure that the same template is used to display data regardless of the source.
Handle Error Cases:
As in Task 3, display a "Wrong source" error message if an invalid
source
is provided.
Implement appropriate error handling for database-related errors.
Hints:
Use Python's
sqlite3
module to interact with the SQLite database.
Define a function to read data from the SQLite database and convert it into a format suitable for rendering in the template.
Use Flask's
request.args
to get the
source
query parameter and determine the data source.
Resources:
Flask-SQLAlchemy:
Flask-SQLAlchemy
SQLite in Python:
SQLite3 Module
Testing Your Application:
Test your application with the URL query parameter set to
json
,
csv
, and
sql
to ensure that the correct data is displayed for each source. Verify that the application can handle and display errors appropriately for invalid sources or database issues.
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-server_side_rendering
File:
task_04_db.py
Score of the task
9
/9
pts
100.0%
0
correction requests
My GitHub
Connect GitHub
Connect as:
Disconnect
Repository
Select a repository…
Folder (optional)
Run the correction
QA Review
×
4. Extending Dynamic Data Display to Include SQLite in Flask
Commit used:
User:
---
URL:
Click here
ID:
---
Author:
---
Subject:
---
Date:
---
×
Students who are done with "4. Extending Dynamic Data Display to Include SQLite in Flask"
```

</details>


---

## 🧪 Testing

Use the provided task examples and Holberton checker to validate the project.

---

## 👤 Author

Project from Holberton School.

README generated with Antoine's README Factory workflow.
