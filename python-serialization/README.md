# ðŸ“˜ Python - Serialization

## ðŸ“Œ Description

_No description detected._

---

## ðŸ“š Resources

_No resources detected._

---

## ðŸŽ¯ Learning Objectives

_No learning objectives detected._

---

## âœ… Requirements

_No requirements detected._

---

## âš™ï¸ Setup

_No specific setup detected._

---

## ðŸ§  Quiz

_No quiz detected in the exported HTML._


---

## ðŸ§© Tasks

<details>
<summary>0. Basic Serialization</summary>

**Files:**

- [`task_00_basic_serialization.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-serialization/task_00_basic_serialization.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-serialization`

**Task details:**

```text
0. Basic Serialization
Create a basic serialization module that adds the functionality to serialize a Python dictionary to a JSON file and deserialize the JSON file to recreate the Python Dictionary.
Instructions:
Write a Python module named
task_00_basic_serialization.py
with the following functions:
def
serialize_and_save_to_file
(
data, filename
):
# Your code here to serialize and save data to the specified file
pass
def
load_and_deserialize
(
filename
):
# Your code here to load and deserialize data from the specified file
pass
The function
serialize_and_save_to_file
take 2 parameters:
data
: A Python Dictionary with data
filename
: The filename of the output JSON file.
If the output file already exists it should be replaced.
The function
load_and_deserialize
take 1
parameters
:
filename
: The filename of the input JSON file
This function returns a Python Dictionary with the deserialized JSON data from the file.
Execution Output Example:
#!/usr/bin/env python3
from
task_00_basic_serialization
import
load_and_deserialize, serialize_and_save_to_file
# Sample data to be serialized
data_to_serialize = {
"name"
:
"John Doe"
,
"age"
:
30
,
"city"
:
"New York"
}
# Serialize the data to JSON and save it to a file
serialize_and_save_to_file(data_to_serialize,
'data.json'
)
# Output: The data has been serialized and saved to 'data.json'
print
(
"Data serialized and saved to 'data.json'."
)
# Load and deserialize data from 'data.json'
deserialized_data = load_and_deserialize(
'data.json'
)
# Output: The deserialized data
print
(
"Deserialized Data:"
)
print
(deserialized_data)
Data serialized and saved to
'data.json'
.
Deserialized Data:
{
'name'
:
'John Doe'
,
'age'
: 30,
'city'
:
'New York'
}
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-serialization
File:
task_00_basic_serialization.py
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
Select a repositoryâ€¦
Folder (optional)
Run the correction
QA Review
Ã—
0. Basic Serialization
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
Ã—
Students who are done with "0. Basic Serialization"
```

</details>

<details>
<summary>1. Pickling Custom Classes</summary>

**Files:**

- [`task_01_pickle.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-serialization/task_01_pickle.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-serialization`

**Task details:**

```text
1. Pickling Custom Classes
Learn how to serialize and deserialize custom Python objects using the
pickle
module.
Instructions:
1 - Create a custom Python class named
CustomObject
. This class should have the following attributes:
name
(a string)
age
(an integer)
is_student
(a boolean)
Additionally, the class should have a method
display
method to print out the object's attributes with the following format:
Name:
John
Age:
25
Is
Student:
True
2 - Implement two methods within this class:
serialize(self, filename)
: This method will take a filename as its parameter. Using the
pickle
module, it will serialize the current instance of the object and save it to the provided filename.
@classmethod
deserialize(cls, filename)
: This class method will take a filename as its parameter. Using the
pickle
module, it will load and return an instance of the
CustomObject
from the provided filename.
3 - Save your code in a file named
task_01_pickle.py
.
Make sure to handle possible exceptions for non-existent or malformed files. If this happens, the methods should return
None
Sample Test:
#!/usr/bin/env python3
from
task_01_pickle
import
CustomObject
# Create an instance of CustomObject
obj = CustomObject(name=
"John"
, age=
25
, is_student=
True
)
print
(
"Original Object:"
)
obj.display()
# Serialize the object
obj.serialize(
"object.pkl"
)
# Deserialize the object into a new instance
new_obj = CustomObject.deserialize(
"object.pkl"
)
print
(
"\nDeserialized Object:"
)
new_obj.display()
Output:
Original
Object
:
Name:
John
Age:
25
Is
Student:
True
Deserialized
Object
:
Name:
John
Age:
25
Is
Student:
True
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-serialization
File:
task_01_pickle.py
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
Select a repositoryâ€¦
Folder (optional)
Run the correction
QA Review
Ã—
1. Pickling Custom Classes
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
Ã—
Students who are done with "1. Pickling Custom Classes"
```

</details>

<details>
<summary>2. Converting CSV Data to JSON Format</summary>

**Files:**

- [`task_02_csv.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-serialization/task_02_csv.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-serialization`

**Task details:**

```text
2. Converting CSV Data to JSON Format
The objective of this exercise is to gain experience in reading data from one format (CSV) and converting it into another format (JSON) using serialization techniques.
Instructions:
Begin by importing the required modules:
import
csv
import
json
Define a function named
convert_csv_to_json
that takes the CSV filename as its parameter and writes the JSON data to
data.json
.
Inside this function:
Use Python's
csv
module to open the CSV file and read the data. Use the
DictReader
class to convert each row into a dictionary.
Serialize the list of dictionaries using the
json
module.
Write the serialized JSON data to
data.json
.
The function should return
True
if the conversion was successful.
Handle exceptions, such as
file not found
. Function should return
False
in this case.
Save your work in
task_02_csv.py
.
Testing Your Code:
#!/usr/bin/env python3
from
task_02_csv
import
convert_csv_to_json

csv_file =
"data.csv"
convert_csv_to_json(csv_file)
print
(
f"Data from
{csv_file}
has been converted to data.json"
)
$ python3 main_02_csv.py
Data from data.csv has been converted to data.json
CSV Dataset (
data.csv
) example:
name,age,city
John,
28
,
New
York
Alice,
24
,Los Angeles
Bob,
22
,Chicago
Eve,
30
,San Francisco
After the conversion, the resulting
data.json
file should contain:
[
{
"name"
:
"John"
,
"age"
:
"28"
,
"city"
:
"New York"
}
,
{
"name"
:
"Alice"
,
"age"
:
"24"
,
"city"
:
"Los Angeles"
}
,
{
"name"
:
"Bob"
,
"age"
:
"22"
,
"city"
:
"Chicago"
}
,
{
"name"
:
"Eve"
,
"age"
:
"30"
,
"city"
:
"San Francisco"
}
]
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-serialization
File:
task_02_csv.py
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
Select a repositoryâ€¦
Folder (optional)
Run the correction
QA Review
Ã—
2. Converting CSV Data to JSON Format
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
Ã—
Students who are done with "2. Converting CSV Data to JSON Format"
```

</details>

<details>
<summary>3. Serializing and Deserializing with XML</summary>

**Files:**

- [`task_03_xml.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-serialization/task_03_xml.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-serialization`

**Task details:**

```text
3. Serializing and Deserializing with XML
In this exercise we'll explore serialization and deserialization using XML as an alternative format to JSON.
Instructions:
Begin by importing the required modules. You can use the
xml.etree.ElementTree
module which is a part of Python's standard library for XML processing:
import
xml.etree.ElementTree
as
ET
Define two main functions:
serialize_to_xml(dictionary, filename)
: This will take a Python dictionary and a filename as parameters. It should serialize the dictionary into XML and save it to the given filename.
deserialize_from_xml(filename)
: This will take a filename as its parameter, read the XML data from that file, and return a deserialized Python dictionary.
For
serialize_to_xml
:
Create a root element, e.g.,
<data>
.
Iterate through the dictionary items and add them as child elements to the root.
Write the XML tree to the provided filename using the
ET.ElementTree
class.
For
deserialize_from_xml
:
Parse the XML file using
ET.parse
.
Navigate through the XML elements to reconstruct the dictionary.
Return the constructed dictionary.
Be cautious about data types. XML doesn't differentiate between numbers and strings, etc., like Python does. You might need to manage type conversions.
Save your work in
task_03_xml.py
.
Testing Your Code:
#!/usr/bin/env python3
from
task_03_xml
import
serialize_to_xml, deserialize_from_xml
def
main
():
    sample_dict = {
'name'
:
'John'
,
'age'
:
'28'
,
'city'
:
'New York'
}

    xml_file =
"data.xml"
serialize_to_xml(sample_dict, xml_file)
print
(
f"Dictionary serialized to
{xml_file}
"
)

    deserialized_data = deserialize_from_xml(xml_file)
print
(
"\nDeserialized Data:"
)
print
(deserialized_data)
if
__name__ ==
"__main__"
:
    main()
Output:
Dictionary serialized to
data
.xml

Deserialized Data:
{
'name'
:
'John'
,
'age'
:
'28'
,
'city'
:
'New York'
}
data.xml
<
data
>
<
name
>
John
</
name
>
<
age
>
28
</
age
>
<
city
>
New York
</
city
>
</
data
>
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-serialization
File:
task_03_xml.py
Score of the task
3
/3
pts
100.0%
0
correction requests
My GitHub
Connect GitHub
Connect as:
Disconnect
Repository
Select a repositoryâ€¦
Folder (optional)
Run the correction
QA Review
Ã—
3. Serializing and Deserializing with XML
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
Ã—
Students who are done with "3. Serializing and Deserializing with XML"
```

</details>


---

## ðŸ§ª Testing

Use the provided task examples and Holberton checker to validate the project.

---

## ðŸ‘¤ Author

Project from Holberton School.

README generated with Antoine's README Factory workflow.
