# 📘 Python - More Data Structures: Set, Dictionary

## 📌 Description

_No description detected._

---

## 📚 Resources

**Read or watch**:



- [Data structures](https://docs.python.org/3/tutorial/datastructures.html)

- [Lambda, filter, reduce and map](https://python-course.eu/advanced-python/lambda-filter-reduce-map.php)

- [Learn to Program 12 Lambda Map Filter Reduce](https://www.youtube.com/watch?v=1GAC6KQUPeg)



**man or help**:



- `python3`

---

## 🎯 Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), __without the help of Google__:



### General



- Why Python programming is awesome

- What are sets and how to use them

- What are the most common methods of set and how to use them

- When to use sets versus lists

- How to iterate into a set

- What are dictionaries and how to use them

- When to use dictionaries versus lists or sets

- What is a key in a dictionary

- How to iterate over a dictionary

- What is a lambda function

- What are the map, reduce and filter functions

---

## ✅ Requirements

### General



- Allowed editors: `vi`, `vim`, `emacs`

- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)

- All your files should end with a new line

- The first line of all your files should be exactly `#!/usr/bin/python3`

- A `README.md` file, at the root of the folder of the project, is mandatory

- Your code should use the pycodestyle (version 2.7.*)

- All your files must be executable

- The length of your files will be tested using `wc`

---

## ⚙️ Setup

_No specific setup detected._

---

## 🧠 Quiz

<details>
<summary>Question #0</summary>

**Question:** What do these lines print?

**Available answers:**

- `id`
- `'id'`
- `a['id']`
- `89`
- `John`

**Answer:** `89`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #1</summary>

**Question:** What do these lines print?

**Available answers:**

- `id`
- `'id'`
- `a['id']`
- `89`
- `John`

**Answer:** `89`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #2</summary>

**Question:** What do these lines print?

**Available answers:**

- `'age'`
- `Not found`
- `89`
- `12`
- `Nothing`

**Answer:** `Nothing`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #3</summary>

**Question:** What do these lines print?

**Available answers:**

- `'age'`
- `Nothing`
- `0`
- `89`

**Answer:** `0`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #4</summary>

**Question:** What do these lines print?

**Available answers:**

- `'projects'`
- `[1, 2, 3, 4]`
- `[1]`
- `list`
- `Nothing`

**Answer:** `[1, 2, 3, 4]`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #5</summary>

**Question:** What do these lines print?

**Available answers:**

- `4`
- `[4]`
- `[1, 2, 3, 4]`
- `3`
- `[3]`

**Answer:** `4`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #6</summary>

**Question:** What do these lines print?

**Available answers:**

- `89`
- `[ { 'id': 82, 'name': "Bob" }, { 'id': 83, 'name': "Amy" } ]`
- `Amy`
- `Bob`
- `Nothing`

**Answer:** `Amy`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #7</summary>

**Question:** What do these lines print?

**Available answers:**

- `1 2 3`
- `0 1 2 3`
- `0 1 2`

**Answer:** `0 1 2`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #8</summary>

**Question:** What do these lines print?

**Available answers:**

- `1 2 3`
- `0 1 2 3`
- `1 2 3 4`

**Answer:** `1 2 3`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #9</summary>

**Question:** What do these lines print?

**Available answers:**

- `0 1 2 3`
- `0 1 2 3 5`
- `1 2 3`
- `1 2 3 4`

**Answer:** `1 2 3 4`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #10</summary>

**Question:** What do these lines print?

**Available answers:**

- `0 1 2 3`
- `1 2 3 4`
- `1 3 4 2`
- `1 3 4 2 0`

**Answer:** `1 3 4 2`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #11</summary>

**Question:** What do these lines print?

**Available answers:**

- `0 1 2 3`
- `1 2 3 4`
- `Hello Holberton School 98`

**Answer:** `Hello Holberton School 98`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>


---

## 🧩 Tasks

<details>
<summary>0. Squared simple</summary>

**Files:**

- [`0-square_matrix_simple.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/0-square_matrix_simple.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-more_data_structures`

**Task details:**

```text
0. Squared simple
Write a function that computes the square value of all integers of a matrix.
Prototype:
def square_matrix_simple(matrix=[]):
matrix
is a 2 dimensional array
Returns a new matrix:
Same size as
matrix
Each value should be the square of the value of the input
Initial matrix should not be modified
You are not allowed to import any module
You are allowed to use regular loops,
map
, etc.
guillaume
@ubuntu
:~/
$
cat
0
-main.py
#!/usr/bin/python3
square_matrix_simple = __import__(
'0-square_matrix_simple'
).square_matrix_simple

matrix = [
    [
1
,
2
,
3
],
    [
4
,
5
,
6
],
    [
7
,
8
,
9
]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

guillaume
@ubuntu
:~/
$
./
0
-main.py
[[
1
,
4
,
9
], [
16
,
25
,
36
], [
49
,
64
,
81
]]
[[
1
,
2
,
3
], [
4
,
5
,
6
], [
7
,
8
,
9
]]
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-more_data_structures
File:
0-square_matrix_simple.py
Score of the task
11
/11
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
Get a sandbox
QA Review
×
0. Squared simple
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
Students who are done with "0. Squared simple"
×
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>1. Search and replace</summary>

**Files:**

- [`1-search_replace.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/1-search_replace.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-more_data_structures`

**Task details:**

```text
1. Search and replace
Write a function that replaces all occurrences of an element by another in a new list.
Prototype:
def search_replace(my_list, search, replace):
my_list
is the initial list
search
is the element to replace in the list
replace
is the new element
You are not allowed to import any module
guillaume
@ubuntu
:~/
$
cat
1
-main.py
#!/usr/bin/python3
search_replace = __import__(
'1-search_replace'
).search_replace

my_list = [
1
,
2
,
3
,
4
,
5
,
4
,
2
,
1
,
1
,
4
,
89
]
new_list = search_replace(my_list,
2
,
89
)

print(new_list)
print(my_list)

guillaume
@ubuntu
:~/
$
./
1
-main.py
[
1
,
89
,
3
,
4
,
5
,
4
,
89
,
1
,
1
,
4
,
89
]
[
1
,
2
,
3
,
4
,
5
,
4
,
2
,
1
,
1
,
4
,
89
]
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-more_data_structures
File:
1-search_replace.py
Score of the task
11
/11
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
Get a sandbox
QA Review
×
1. Search and replace
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
Students who are done with "1. Search and replace"
×
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>2. Unique addition</summary>

**Files:**

- [`2-uniq_add.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/2-uniq_add.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-more_data_structures`

**Task details:**

```text
2. Unique addition
Write a function that adds all unique integers in a list (only once for each integer).
Prototype:
def uniq_add(my_list=[]):
You are not allowed to import any module
guillaume
@ubuntu
:~/
$
cat
2
-main.py
#!/usr/bin/python3
uniq_add = __import__(
'2-uniq_add'
).uniq_add

my_list = [
1
,
2
,
3
,
1
,
4
,
2
,
5
]
result = uniq_add(my_list)
print(
"Result: {:d}"
.format(result))

guillaume
@ubuntu
:~/
$
./
2
-main.py
Result
:
15
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-more_data_structures
File:
2-uniq_add.py
Score of the task
13
/13
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
Get a sandbox
QA Review
×
2. Unique addition
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
Students who are done with "2. Unique addition"
×
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>3. Present in both</summary>

**Files:**

- [`3-common_elements.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/3-common_elements.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-more_data_structures`

**Task details:**

```text
3. Present in both
Write a function that returns a set of common elements in two sets.
Prototype:
def common_elements(set_1, set_2):
You are not allowed to import any module
guillaume
@ubuntu
:~/
$
cat
3
-main.py
#!/usr/bin/python3
common_elements = __import__(
'3-common_elements'
).common_elements

set_1 = {
"Python"
,
"C"
,
"Javascript"
}
set_2 = {
"Bash"
,
"C"
,
"Ruby"
,
"Perl"
}
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))

guillaume
@ubuntu
:~/
$
./
3
-main.py
[
'C'
]
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-more_data_structures
File:
3-common_elements.py
Score of the task
13
/13
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
Get a sandbox
QA Review
×
3. Present in both
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
Students who are done with "3. Present in both"
×
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>4. Only differents</summary>

**Files:**

- [`4-only_diff_elements.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/4-only_diff_elements.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-more_data_structures`

**Task details:**

```text
4. Only differents
Write a function that returns a set of all elements present in only one set.
Prototype:
def only_diff_elements(set_1, set_2):
You are not allowed to import any module
guillaume
@ubuntu
:~/
$
cat
4
-main.py
#!/usr/bin/python3
only_diff_elements = __import__(
'4-only_diff_elements'
).only_diff_elements

set_1 = {
"Python"
,
"C"
,
"Javascript"
}
set_2 = {
"Bash"
,
"C"
,
"Ruby"
,
"Perl"
}
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))

guillaume
@ubuntu
:~/
$
./
4
-main.py
[
'Bash'
,
'Javascript'
,
'Perl'
,
'Python'
,
'Ruby'
]
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-more_data_structures
File:
4-only_diff_elements.py
Score of the task
13
/13
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
Get a sandbox
QA Review
×
4. Only differents
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
Students who are done with "4. Only differents"
×
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>5. Number of keys</summary>

**Files:**

- [`5-number_keys.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/5-number_keys.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-more_data_structures`

**Task details:**

```text
5. Number of keys
Write a function that returns the number of keys in a dictionary.
Prototype:
def number_keys(a_dictionary):
You are not allowed to import any module
guillaume
@ubuntu
:~/
$
cat
5
-main.py
#!/usr/bin/python3
number_keys = __import__(
'5-number_keys'
).number_keys

a_dictionary = {
'language'
:
"C"
,
'number'
:
13
,
'track'
:
"Low level"
}
nb_keys = number_keys(a_dictionary)
print(
"Number of keys: {:d}"
.format(nb_keys))

guillaume
@ubuntu
:~/
$
./
5
-main.py
Number
of
keys:
3
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-more_data_structures
File:
5-number_keys.py
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
Get a sandbox
QA Review
×
5. Number of keys
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
Students who are done with "5. Number of keys"
×
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>6. Print sorted dictionary</summary>

**Files:**

- [`6-print_sorted_dictionary.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/6-print_sorted_dictionary.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-more_data_structures`

**Task details:**

```text
6. Print sorted dictionary
Write a function that prints a dictionary by ordered keys.
Prototype:
def print_sorted_dictionary(a_dictionary):
You can assume that all keys are strings
Keys should be sorted by alphabetic order
Only sort keys of the first level (don't sort keys of a dictionary inside the main dictionary)
Dictionary values can have any type
You are not allowed to import any module
guillaume
@ubuntu
:~/
$
cat
6
-main.py
#!/usr/bin/python3
print_sorted_dictionary = __import__(
'6-print_sorted_dictionary'
).print_sorted_dictionary

a_dictionary = {
'language'
:
"C"
,
'Number'
:
89
,
'track'
:
"Low level"
,
'ids'
: [
1
,
2
,
3
] }
print_sorted_dictionary(a_dictionary)

guillaume
@ubuntu
:~/
$
./
6
-main.py
Number
:
89
ids:
[
1
,
2
,
3
]
language:
C
track:
Low
level
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-more_data_structures
File:
6-print_sorted_dictionary.py
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
Get a sandbox
QA Review
×
6. Print sorted dictionary
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
Students who are done with "6. Print sorted dictionary"
×
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>7. Update dictionary</summary>

**Files:**

- [`7-update_dictionary.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/7-update_dictionary.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-more_data_structures`

**Task details:**

```text
7. Update dictionary
Write a function that replaces or adds key/value in a dictionary.
Prototype:
def update_dictionary(a_dictionary, key, value):
key
argument will be always a string
value
argument will be any type
If a key exists in the dictionary, the value will be replaced
If a key doesn't exist in the dictionary, it will be created
You are not allowed to import any module
guillaume@ubuntu:~/$ cat 7-main.py
#!/usr/bin/python3
update_dictionary = __import__('7-update_dictionary').update_dictionary
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language':
"C"
, 'number': 89, 'track':
"Low level"
}
new_dict = update_dictionary(a_dictionary, 'language',
"Python"
)
print_sorted_dictionary(new_dict)
print(
"--"
)
print_sorted_dictionary(a_dictionary)

print(
"--"
)
print(
"--"
)

new_dict = update_dictionary(a_dictionary, 'city',
"San Francisco"
)
print_sorted_dictionary(new_dict)
print(
"--"
)
print_sorted_dictionary(a_dictionary)
guillaume@ubuntu:~/$ ./7-main.py
language: Python
number: 89
track: Low level
--
language: Python
number: 89
track: Low level
--
--
city: San Francisco
language: Python
number: 89
track: Low level
--
city: San Francisco
language: Python
number: 89
track: Low level
guillaume@ubuntu:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-more_data_structures
File:
7-update_dictionary.py
Score of the task
11
/11
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
Get a sandbox
QA Review
×
7. Update dictionary
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
Students who are done with "7. Update dictionary"
×
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>8. Simple delete by key</summary>

**Files:**

- [`8-simple_delete.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/8-simple_delete.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-more_data_structures`

**Task details:**

```text
8. Simple delete by key
Write a function that deletes a key in a dictionary.
Prototype:
def simple_delete(a_dictionary, key=""):
key
argument will be always a string
If a key doesn't exist, the dictionary won't change
You are not allowed to import any module
guillaume@ubuntu:~/$ cat 8-main.py
#!/usr/bin/python3
simple_delete = __import__('8-simple_delete').simple_delete
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language':
"C"
, 'Number': 89, 'track':
"Low"
, 'ids': [1, 2, 3] }
new_dict = simple_delete(a_dictionary, 'track')
print_sorted_dictionary(a_dictionary)
print(
"--"
)
print_sorted_dictionary(new_dict)

print(
"--"
)
print(
"--"
)
new_dict = simple_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print(
"--"
)
print_sorted_dictionary(new_dict)
guillaume@ubuntu:~/$ ./8-main.py
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
--
--
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
guillaume@ubuntu:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-more_data_structures
File:
8-simple_delete.py
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
Get a sandbox
QA Review
×
8. Simple delete by key
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
Students who are done with "8. Simple delete by key"
×
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>9. Multiply by 2</summary>

**Files:**

- [`9-multiply_by_2.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/9-multiply_by_2.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-more_data_structures`

**Task details:**

```text
9. Multiply by 2
Write a function that returns a new dictionary with all values multiplied by 2
Prototype:
def multiply_by_2(a_dictionary):
You can assume that all values are only integers
Returns a new dictionary
You are not allowed to import any module
guillaume
@ubuntu
:~/
$
cat
9
-main.py
#!/usr/bin/python3
multiply_by_2 = __import__(
'9-multiply_by_2'
).multiply_by_2
print_sorted_dictionary = \
    __import__(
'6-print_sorted_dictionary'
).print_sorted_dictionary

a_dictionary = {
'John'
:
12
,
'Alex'
:
8
,
'Bob'
:
14
,
'Mike'
:
14
,
'Molly'
:
16
}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print(
"--"
)
print_sorted_dictionary(new_dict)

guillaume
@ubuntu
:~/
$
./
9
-main.py
Alex
:
8
Bob
:
14
John
:
12
Mike
:
14
Molly
:
16
--
Alex
:
16
Bob
:
28
John
:
24
Mike
:
28
Molly
:
32
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-more_data_structures
File:
9-multiply_by_2.py
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
Get a sandbox
QA Review
×
9. Multiply by 2
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
Students who are done with "9. Multiply by 2"
×
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>10. Best score</summary>

**Files:**

- [`10-best_score.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/10-best_score.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-more_data_structures`

**Task details:**

```text
10. Best score
Write a function that returns a key with the biggest integer value.
Prototype:
def best_score(a_dictionary):
You can assume that all values are only integers
If no score found, return
None
You can assume all students have a different score
You are not allowed to import any module
guillaume
@ubuntu
:~/
$
cat
10
-main.py
#!/usr/bin/python3
best_score = __import__(
'10-best_score'
).best_score

a_dictionary = {
'John'
:
12
,
'Bob'
:
14
,
'Mike'
:
14
,
'Molly'
:
16
,
'Adam'
:
10
}
best_key = best_score(a_dictionary)
print(
"Best score: {}"
.format(best_key))

best_key = best_score(
None
)
print(
"Best score: {}"
.format(best_key))

guillaume
@ubuntu
:~/
$
./
10
-main.py
Best
score:
Molly
Best
score:
None
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-more_data_structures
File:
10-best_score.py
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
Get a sandbox
QA Review
×
10. Best score
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
Students who are done with "10. Best score"
×
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>11. Multiply by using map</summary>

**Files:**

- [`11-multiply_list_map.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/11-multiply_list_map.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-more_data_structures`

**Task details:**

```text
11. Multiply by using map
Write a function that returns a list with all values multiplied by a number without using any loops.
Prototype:
def multiply_list_map(my_list=[], number=0):
Returns a new list:
Same length as
my_list
Each value should be multiplied by
number
Initial list should not be modified
You are not allowed to import any module
You have to use
map
Your file should be max 3 lines
guillaume
@ubuntu
:~/
$
cat
11
-main.py
#!/usr/bin/python3
multiply_list_map = __import__(
'11-multiply_list_map'
).multiply_list_map

my_list = [
1
,
2
,
3
,
4
,
6
]
new_list = multiply_list_map(my_list,
4
)
print(new_list)
print(my_list)

guillaume
@ubuntu
:~/
$
./
11
-main.py
[
4
,
8
,
12
,
16
,
24
]
[
1
,
2
,
3
,
4
,
6
]
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-more_data_structures
File:
11-multiply_list_map.py
Score of the task
11
/11
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
Get a sandbox
QA Review
×
11. Multiply by using map
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
Students who are done with "11. Multiply by using map"
×
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>12. Roman to Integer</summary>

**Files:**

- [`12-roman_to_int.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/12-roman_to_int.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-more_data_structures`

**Task details:**

```text
12. Roman to Integer
Technical interview preparation
:
You are not allowed to google anything
Whiteboard first
Create a function
def roman_to_int(roman_string):
that converts a
Roman numeral
to an integer.
You can assume the number will be between 1 to 3999.
def roman_to_int(roman_string)
must return an integer
If the
roman_string
is not a string or
None
, return 0
guillaume@ubuntu:~/$ cat
12
-main.py
#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int =
__import__
(
'12-roman_to_int'
).roman_to_int

roman_number =
"X"
print
(
"{} = {}"
.
format
(roman_number, roman_to_int(roman_number)))

roman_number =
"VII"
print
(
"{} = {}"
.
format
(roman_number, roman_to_int(roman_number)))

roman_number =
"IX"
print
(
"{} = {}"
.
format
(roman_number, roman_to_int(roman_number)))

roman_number =
"LXXXVII"
print
(
"{} = {}"
.
format
(roman_number, roman_to_int(roman_number)))

roman_number =
"DCCVII"
print
(
"{} = {}"
.
format
(roman_number, roman_to_int(roman_number)))

guillaume@ubuntu:~/$ ./
12
-main.py
X =
10
VII =
7
IX =
9
LXXXVII =
87
DCCVII =
707
guillaume@ubuntu:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-more_data_structures
File:
12-roman_to_int.py
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
Get a sandbox
QA Review
×
12. Roman to Integer
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
Students who are done with "12. Roman to Integer"
×
Recommended Sandboxes
Loading...
```

</details>


---

## 🧪 Testing

Use the provided task examples and Holberton checker to validate the project.

---

## 👤 Author

Project from Holberton School.

README generated with Antoine's README Factory workflow.
