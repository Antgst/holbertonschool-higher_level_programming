# ðŸ“˜ Python - Exceptions

## ðŸ“Œ Description

_No description detected._

---

## ðŸ“š Resources

**Read or watch**:



- [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)

- [Learn to Program 11 Static & Exception Handling](https://www.youtube.com/watch?v=7vbgD-3s-w4) (*starting at minute 7*)

---

## ðŸŽ¯ Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), __without the help of Google__:



### General



- Why Python programming is awesome

- What's the difference between errors and exceptions

- What are exceptions and how to use them

- When do we need to use exceptions

- How to correctly handle an exception

- What's the purpose of catching exceptions

- How to raise a builtin exception

- When do we need to implement a clean-up action after an exception

---

## âœ… Requirements

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

## âš™ï¸ Setup

_No specific setup detected._

---

## ðŸ§  Quiz

_No quiz detected in the exported HTML._


---

## ðŸ§© Tasks

<details>
<summary>0. Safe list printing</summary>

**Files:**

- [`0-safe_print_list.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-exceptions/0-safe_print_list.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-exceptions`

**Task details:**

```text
0. Safe list printing
Write a function that prints
x
elements of a list.
Prototype:
def safe_print_list(my_list=[], x=0):
my_list
can contain any type (integer, string, etc.)
All elements must be printed on the same line followed by a new line.
x
represents the number of elements to print
x
can be bigger than the length of
my_list
Returns the real number of elements printed
You have to use
try: / except:
You are not allowed to import any module
You are not allowed to use
len()
guillaume
@ubuntu
:~/
$
cat
0
-main.py
#!/usr/bin/python3
safe_print_list = __import__(
'0-safe_print_list'
).safe_print_list

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
]

nb_print = safe_print_list(my_list,
2
)
print(
"nb_print: {:d}"
.format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print(
"nb_print: {:d}"
.format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) +
2
)
print(
"nb_print: {:d}"
.format(nb_print))

guillaume
@ubuntu
:~/
$
./
0
-main.py
12
nb_print:
2
12345
nb_print:
5
12345
nb_print:
5
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-exceptions
File:
0-safe_print_list.py
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
Select a repositoryâ€¦
Folder (optional)
Run the correction
Get a sandbox
QA Review
Ã—
0. Safe list printing
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
Students who are done with "0. Safe list printing"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>1. Safe printing of an integers list</summary>

**Files:**

- [`1-safe_print_integer.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-exceptions/1-safe_print_integer.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-exceptions`

**Task details:**

```text
1. Safe printing of an integers list
Write a function that prints an integer with
"{:d}".format()
.
Prototype:
def safe_print_integer(value):
value
can be any type (integer, string, etc.)
The integer should be printed followed by a new line
Returns
True
if
value
has been correctly printed (it means the
value
is an integer)
Otherwise, returns
False
You have to use
try: / except:
You have to use
"{:d}".format()
to print as integer
You are not allowed to import any module
You are not allowed to use
type()
guillaume
@ubuntu
:~/
$
cat
1
-main.py
#!/usr/bin/python3
safe_print_integer = __import__(
'1-safe_print_integer'
).safe_print_integer

value =
89
has_been_print = safe_print_integer(value)
if
not
has_been_print:
print(
"{} is not an integer"
.format(value))

value = -
89
has_been_print = safe_print_integer(value)
if
not
has_been_print:
print(
"{} is not an integer"
.format(value))

value =
"School"
has_been_print = safe_print_integer(value)
if
not
has_been_print:
print(
"{} is not an integer"
.format(value))

guillaume
@ubuntu
:~/
$
./
1
-main.py
89
-
89
School
is
not
an integer
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-exceptions
File:
1-safe_print_integer.py
Score of the task
14
/14
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
Get a sandbox
QA Review
Ã—
1. Safe printing of an integers list
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
Students who are done with "1. Safe printing of an integers list"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>2. Print and count integers</summary>

**Files:**

- [`2-safe_print_list_integers.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-exceptions/2-safe_print_list_integers.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-exceptions`

**Task details:**

```text
2. Print and count integers
Write a function that prints the first
x
elements of a list and only integers.
Prototype:
def safe_print_list_integers(my_list=[], x=0):
my_list
can contain any type (integer, string, etc.)
All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
x
represents the number of elements to access in
my_list
x
can be bigger than the length of
my_list
- if it's the case, an exception is expected to occur
Returns the real number of integers printed
You have to use
try: / except:
You have to use
"{:d}".format()
to print an integer
You are not allowed to import any module
You are not allowed to use
len()
guillaume
@ubuntu
:~/
$
cat
2
-main.py
#!/usr/bin/python3
safe_print_list_integers = \
    __import__(
'2-safe_print_list_integers'
).safe_print_list_integers

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
]

nb_print = safe_print_list_integers(my_list,
2
)
print(
"nb_print: {:d}"
.format(nb_print))

my_list = [
1
,
2
,
3
,
"School"
,
4
,
5
, [
1
,
2
,
3
]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print(
"nb_print: {:d}"
.format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) +
2
)
print(
"nb_print: {:d}"
.format(nb_print))

guillaume
@ubuntu
:~/
$
./
2
-main.py
12
nb_print:
2
12345
nb_print:
5
12345Traceback (most recent call last):
File
"./2-main.py"
, line
14
,
in
<
module
>
    nb_print = safe_print_list_integers(my_list, len(my_list) +
2
)
File
"//2-safe_print_list_integers.py"
, line
7
,
in
safe_print_list_integers
    print(
"{:d}"
.format(my_list[i]),
end
=
""
)
IndexError
: list index out of range
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-exceptions
File:
2-safe_print_list_integers.py
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
Select a repositoryâ€¦
Folder (optional)
Run the correction
Get a sandbox
QA Review
Ã—
2. Print and count integers
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
Students who are done with "2. Print and count integers"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>3. Integers division with debug</summary>

**Files:**

- [`3-safe_print_division.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-exceptions/3-safe_print_division.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-exceptions`

**Task details:**

```text
3. Integers division with debug
Write a function that divides 2 integers and prints the result.
Prototype:
def safe_print_division(a, b):
You can assume that
a
and
b
are integers
The result of the division should print on the
finally:
section preceded by
Inside result:
Returns the value of the division, otherwise:
None
You have to use
try: / except: / finally:
You have to use
"{}".format()
to print the result
You are not allowed to import any module
guillaume
@ubuntu
:~/
$
cat
3
-main.py
#!/usr/bin/python3
safe_print_division = __import__(
'3-safe_print_division'
).safe_print_division

a =
12
b =
2
result = safe_print_division(a, b)
print(
"{:d} / {:d} = {}"
.format(a, b, result))

a =
12
b =
0
result = safe_print_division(a, b)
print(
"{:d} / {:d} = {}"
.format(a, b, result))

guillaume
@ubuntu
:~/
$
./
3
-main.py
Inside
result:
6.0
12
/
2
=
6.0
Inside
result:
None
12
/
0
=
None
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-exceptions
File:
3-safe_print_division.py
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
Select a repositoryâ€¦
Folder (optional)
Run the correction
Get a sandbox
QA Review
Ã—
3. Integers division with debug
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
Students who are done with "3. Integers division with debug"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>4. Divide a list</summary>

**Files:**

- [`4-list_division.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-exceptions/4-list_division.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-exceptions`

**Task details:**

```text
4. Divide a list
Write a function that divides element by element 2 lists.
Prototype:
def list_division(my_list_1, my_list_2, list_length):
my_list_1
and
my_list_2
can contain any type (integer, string, etc.)
list_length
can be bigger than the length of both lists
Returns a new list (length =
list_length
) with all divisions
If 2 elements can't be divided, the division result should be equal to
0
If an element is not an integer or float:
print:
wrong type
If the division can't be done (
/0
):
print:
division by 0
If
my_list_1
or
my_list_2
is too short
print:
out of range
You have to use
try: / except: / finally:
You are not allowed to import any module
guillaume@ubuntu:~/$ cat
4
-main.py
#!/usr/bin/python3
list_division =
__import__
(
'4-list_division'
).list_division

my_l_1 = [
10
,
8
,
4
]
my_l_2 = [
2
,
4
,
4
]
result = list_division(my_l_1, my_l_2,
max
(
len
(my_l_1),
len
(my_l_2)))
print
(result)
print
(
"--"
)

my_l_1 = [
10
,
8
,
4
,
4
]
my_l_2 = [
2
,
0
,
"H"
,
2
,
7
]
result = list_division(my_l_1, my_l_2,
max
(
len
(my_l_1),
len
(my_l_2)))
print
(result)

guillaume@ubuntu:~/$ ./
4
-main.py
[
5.0
,
2.0
,
1.0
]
--
division by
0
wrong
type
out of
range
[
5.0
,
0
,
0
,
2.0
,
0
]
guillaume@ubuntu:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-exceptions
File:
4-list_division.py
Score of the task
16
/16
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
Get a sandbox
QA Review
Ã—
4. Divide a list
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
Students who are done with "4. Divide a list"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>5. Raise exception</summary>

**Files:**

- [`5-raise_exception.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-exceptions/5-raise_exception.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-exceptions`

**Task details:**

```text
5. Raise exception
Write a function that raises a type exception.
Prototype:
def raise_exception():
You are not allowed to import any module
guillaume
@ubuntu
:~/
$
cat
5
-main.py
#!/usr/bin/python3
raise_exception = __import__(
'5-raise_exception'
).raise_exception
try:
raise_exception()
except
TypeError
as
te:
print(
"Exception raised"
)

guillaume
@ubuntu
:~/
$
./
5
-main.py
Exception
raised
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-exceptions
File:
5-raise_exception.py
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
Select a repositoryâ€¦
Folder (optional)
Run the correction
Get a sandbox
QA Review
Ã—
5. Raise exception
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
Students who are done with "5. Raise exception"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>6. Raise a message</summary>

**Files:**

- [`6-raise_exception_msg.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-exceptions/6-raise_exception_msg.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-exceptions`

**Task details:**

```text
6. Raise a message
Write a function that raises a name exception with a message.
Prototype:
def raise_exception_msg(message=""):
You are not allowed to import any module
guillaume
@ubuntu
:~/
$
cat
6
-main.py
#!/usr/bin/python3
raise_exception_msg = __import__(
'6-raise_exception_msg'
).raise_exception_msg
try:
raise_exception_msg(
"C is fun"
)
except
NameError
as
ne:
print(ne)

guillaume
@ubuntu
:~/
$
./
6
-main.py
C is fun
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-exceptions
File:
6-raise_exception_msg.py
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
Select a repositoryâ€¦
Folder (optional)
Run the correction
Get a sandbox
QA Review
Ã—
6. Raise a message
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
Students who are done with "6. Raise a message"
Ã—
Recommended Sandboxes
Loading...
```

</details>


---

## ðŸ§ª Testing

Use the provided task examples and Holberton checker to validate the project.

---

## ðŸ‘¤ Author

Project from Holberton School.

README generated with Antoine's README Factory workflow.
