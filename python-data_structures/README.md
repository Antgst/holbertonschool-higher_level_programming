# ðŸ“˜ Python - Data Structures: Lists, Tuples

## ðŸ“Œ Description

_No description detected._

---

## ðŸ“š Resources

**Read or watch**:



- [3.1.3. Lists](https://docs.python.org/3/tutorial/introduction.html#lists)

- [Data structures](https://docs.python.org/3/tutorial/datastructures.html) (*until `5.3. Tuples and Sequences` included*)

- [Learn to Program 6 : Lists](https://www.youtube.com/watch?v=A1HUzrvS-Pw)

---

## ðŸŽ¯ Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), __without the help of Google__:



### General



- What are lists and how to use them

- What are the differences and similarities between strings and lists

- What are the most common methods of lists and how to use them

- How to use lists as stacks and queues

- What are list comprehensions and how to use them

- What are tuples and how to use them

- When to use tuples versus lists

- What is a sequence

- What is tuple packing

- What is sequence unpacking

- What is the `del` statement and how to use it

---

## âœ… Requirements

### Python Scripts



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

<details>
<summary>Question #0</summary>

**Question:** What do these lines print?

**Available answers:**

- `1`
- `2`
- `[1]`
- `[1, 2]`
- `[1, 2, 3, 4]`

**Answer:** `1`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #1</summary>

**Question:** What do these lines print?

**Available answers:**

- `-1`
- `2`
- `4`
- `[4, 3, 2, 1]`

**Answer:** `4`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #2</summary>

**Question:** What do these lines print?

**Available answers:**

- `-3`
- `[4, 3]`
- `2`

**Answer:** `2`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #3</summary>

**Question:** What do these lines print?

**Available answers:**

- `2`
- `4`
- `6`
- `8`

**Answer:** `4`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #4</summary>

**Question:** What do these lines print?

**Available answers:**

- `2`
- `5`
- `6`

**Answer:** `5`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #5</summary>

**Question:** What do these lines print?

**Available answers:**

- `[1, 2, 3]`
- `[1, 2]`
- `[2, 3]`

**Answer:** `[2, 3]`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #6</summary>

**Question:** What do these lines print?

**Available answers:**

- `[1, 2, 3, 4]`
- `[1, 10, 3, 4]`
- `[1, 2, 10, 4]`
- `[1, 2, 10, 10]`

**Answer:** `[1, 2, 10, 4]`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #7</summary>

**Question:** What do these lines print?

**Available answers:**

- `[1, 2, 3, 4]`
- `[1]`
- `1`
- `a`

**Answer:** `[1, 2, 3, 4]`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #8</summary>

**Question:** What do these lines print?

**Available answers:**

- `[1]`
- `[1, 2, 10, 4]`
- `[1, 2, 3, 4]`
- `a`
- `b`

**Answer:** `[1, 2, 10, 4]`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #9</summary>

**Question:** What do these lines print?

**Available answers:**

- `[1]`
- `[1, 2, 10, 4]`
- `[1, 2, 3, 4]`
- `a`
- `b`

**Answer:** `[1, 2, 10, 4]`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>


---

## ðŸ§© Tasks

<details>
<summary>0. Print a list of integers</summary>

**Files:**

- [`0-print_list_integer.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-data_structures/0-print_list_integer.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-data_structures`

**Task details:**

```text
0. Print a list of integers
Write a function that prints all integers of a list.
Prototype:
def print_list_integer(my_list=[]):
Format: one integer per line. See example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to print the integers with string format
guillaume
@ubuntu
:~/
$
cat
0
-main.py
#!/usr/bin/python3
print_list_integer = __import__(
'0-print_list_integer'
).print_list_integer

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
print_list_integer(my_list)

guillaume
@ubuntu
:~/
$
./
0
-main.py
1
2
3
4
5
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-data_structures
File:
0-print_list_integer.py
Score of the task
21
/21
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
0. Print a list of integers
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
Students who are done with "0. Print a list of integers"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>1. Secure access to an element in a list</summary>

**Files:**

- [`1-element_at.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-data_structures/1-element_at.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-data_structures`

**Task details:**

```text
1. Secure access to an element in a list
Write a function that retrieves an element from a list.
Prototype:
def element_at(my_list, idx):
If
idx
is negative, the function should return
None
If
idx
is out of range (> of number of element in
my_list
), the function should return
None
You are not allowed to import any module
You are not allowed to use
try/except
guillaume
@ubuntu
:~/
$
cat
1
-main.py
#!/usr/bin/python3
element_at = __import__(
'1-element_at'
).element_at

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
idx =
3
print(
"Element at index {:d} is {}"
.format(idx, element_at(my_list, idx)))

guillaume
@ubuntu
:~/
$
./
1
-main.py
Element
at index
3
is
4
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-data_structures
File:
1-element_at.py
Score of the task
12
/12
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
1. Secure access to an element in a list
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
Students who are done with "1. Secure access to an element in a list"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>2. Replace element</summary>

**Files:**

- [`2-replace_in_list.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-data_structures/2-replace_in_list.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-data_structures`

**Task details:**

```text
2. Replace element
Write a function that replaces an element of a list at a specific position.
Prototype:
def replace_in_list(my_list, idx, element):
If
idx
is negative, the function should not modify anything, and returns the original list
If
idx
is out of range (> of number of element in
my_list
), the function should not modify anything, and returns the original list
You are not allowed to import any module
You are not allowed to use
try/except
guillaume
@ubuntu
:~/
$
cat
2
-main.py
#!/usr/bin/python3
replace_in_list = __import__(
'2-replace_in_list'
).replace_in_list

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
idx =
3
new_element =
9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume
@ubuntu
:~/
$
./
2
-main.py
[
1
,
2
,
3
,
9
,
5
]
[
1
,
2
,
3
,
9
,
5
]
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-data_structures
File:
2-replace_in_list.py
Score of the task
12
/12
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
2. Replace element
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
Students who are done with "2. Replace element"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>3. Print a list of integers... in reverse!</summary>

**Files:**

- [`3-print_reversed_list_integer.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-data_structures/3-print_reversed_list_integer.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-data_structures`

**Task details:**

```text
3. Print a list of integers... in reverse!
Write a function that prints all integers of a list, in reverse order.
Prototype:
def print_reversed_list_integer(my_list=[]):
Format: one integer per line. See example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to print the integers with string format
guillaume
@ubuntu
:~/
$
cat
3
-main.py
#!/usr/bin/python3
print_reversed_list_integer = __import__(
'3-print_reversed_list_integer'
).print_reversed_list_integer

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
print_reversed_list_integer(my_list)

guillaume
@ubuntu
:~/
$
./
3
-main.py
5
4
3
2
1
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-data_structures
File:
3-print_reversed_list_integer.py
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
3. Print a list of integers... in reverse!
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
Students who are done with "3. Print a list of integers... in reverse!"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>4. Replace in a copy</summary>

**Files:**

- [`4-new_in_list.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-data_structures/4-new_in_list.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-data_structures`

**Task details:**

```text
4. Replace in a copy
Write a function that replaces an element in a list at a specific position without modifying the original list.
Prototype:
def new_in_list(my_list, idx, element):
If
idx
is negative, the function should return a copy of the original
list
If
idx
is out of range (> of number of element in
my_list
), the function should return a copy of the original
list
You are not allowed to import any module
You are not allowed to use
try/except
guillaume
@ubuntu
:~/
$
cat
4
-main.py
#!/usr/bin/python3
new_in_list = __import__(
'4-new_in_list'
).new_in_list

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
idx =
3
new_element =
9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume
@ubuntu
:~/
$
./
4
-main.py
[
1
,
2
,
3
,
9
,
5
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
]
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-data_structures
File:
4-new_in_list.py
Score of the task
12
/12
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
4. Replace in a copy
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
Students who are done with "4. Replace in a copy"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>5. Can you C me now?</summary>

**Files:**

- [`5-no_c.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-data_structures/5-no_c.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-data_structures`

**Task details:**

```text
5. Can you C me now?
Write a function that removes all characters
c
and
C
from a string.
Prototype:
def no_c(my_string):
The function should return the new string
You are not allowed to import any module
You are not allowed to use
str.replace()
guillaume
@ubuntu
:~/
$
cat
5
-main.py
#!/usr/bin/python3
no_c = __import__(
'5-no_c'
).no_c

print(no_c(
"Best School"
))
print(no_c(
"Chicago"
))
print(no_c(
"C is fun!"
))

guillaume
@ubuntu
:~/
$
./
5
-main.py
Best
Shool
hiago
 is fun!
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-data_structures
File:
5-no_c.py
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
5. Can you C me now?
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
Students who are done with "5. Can you C me now?"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>6. Lists of lists = Matrix</summary>

**Files:**

- [`6-print_matrix_integer.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-data_structures/6-print_matrix_integer.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-data_structures`

**Task details:**

```text
6. Lists of lists = Matrix
Write a function that prints a matrix of integers.
Prototype:
def print_matrix_integer(matrix=[[]]):
Format: see example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use
str.format()
to print integers
guillaume
@ubuntu
:~/
$
cat
6
-main.py
#!/usr/bin/python3
print_matrix_integer = __import__(
'6-print_matrix_integer'
).print_matrix_integer

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

print_matrix_integer(matrix)
print(
"--"
)
print_matrix_integer()

guillaume
@ubuntu
:~/
$
./
6
-main.py |
cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
guillaume@ubuntu:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-data_structures
File:
6-print_matrix_integer.py
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
6. Lists of lists = Matrix
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
Students who are done with "6. Lists of lists = Matrix"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>7. Tuples addition</summary>

**Files:**

- [`7-add_tuple.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-data_structures/7-add_tuple.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-data_structures`

**Task details:**

```text
7. Tuples addition
Write a function that adds 2 tuples.
Prototype:
def add_tuple(tuple_a=(), tuple_b=()):
Returns a tuple with 2 integers:
The first element should be the addition of the first element of each argument
The second element should be the addition of the second element of each argument
You are not allowed to import any module
You can assume that the two tuples will only contain integers
If a tuple is smaller than 2, use the value
0
for each missing integer
If a tuple is bigger than 2, use only the first 2 integers
guillaume
@ubuntu
:~/
$
cat
7
-main.py
#!/usr/bin/python3
add_tuple = __import__(
'7-add_tuple'
).add_tuple

tuple_a = (
1
,
89
)
tuple_b = (
88
,
11
)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (
1
, )))
print(add_tuple(tuple_a, ()))

guillaume
@ubuntu
:~/
$
./
7
-main.py
(
89
,
100
)
(
2
,
89
)
(
1
,
89
)
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-data_structures
File:
7-add_tuple.py
Score of the task
15
/15
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
7. Tuples addition
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
Students who are done with "7. Tuples addition"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>8. More returns!</summary>

**Files:**

- [`8-multiple_returns.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-data_structures/8-multiple_returns.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-data_structures`

**Task details:**

```text
8. More returns!
Write a function that returns a tuple with the length of a string and its first character.
Prototype:
def multiple_returns(sentence):
If the sentence is empty, the first character should be equal to
None
You are not allowed to import any module
guillaume
@ubuntu
:~/
$
cat
8
-main.py
#!/usr/bin/python3
multiple_returns = __import__(
'8-multiple_returns'
).multiple_returns

sentence =
"At school, I learnt C!"
length, first = multiple_returns(sentence)
print(
"Length: {:d} - First character: {}"
.format(length, first))

guillaume
@ubuntu
:~/
$
./
8
-main.py
Length
:
22
-
First
character:
A
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-data_structures
File:
8-multiple_returns.py
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
8. More returns!
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
Students who are done with "8. More returns!"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>9. Find the max</summary>

**Files:**

- [`9-max_integer.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-data_structures/9-max_integer.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-data_structures`

**Task details:**

```text
9. Find the max
Write a function that finds the biggest integer of a list.
Prototype:
def max_integer(my_list=[]):
If the list is empty, return
None
You can assume that the list only contains integers
You are not allowed to import any module
You are not allowed to use the builtin
max()
guillaume
@ubuntu
:~/
$
cat
9
-main.py
#!/usr/bin/python3
max_integer = __import__(
'9-max_integer'
).max_integer

my_list = [
1
,
90
,
2
,
13
,
34
,
5
, -
13
,
3
]
max_value = max_integer(my_list)
print(
"Max: {}"
.format(max_value))

guillaume
@ubuntu
:~/
$
./
9
-main.py
Max
:
90
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-data_structures
File:
9-max_integer.py
Score of the task
12
/12
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
9. Find the max
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
Students who are done with "9. Find the max"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>10. Only by 2</summary>

**Files:**

- [`10-divisible_by_2.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-data_structures/10-divisible_by_2.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-data_structures`

**Task details:**

```text
10. Only by 2
Write a function that finds all multiples of 2 in a list.
Prototype:
def divisible_by_2(my_list=[]):
Return a new list with
True
or
False
, depending on whether the integer at the same position in the original list is a multiple of 2
The new list should have the same size as the original list
You are not allowed to import any module
guillaume@
ubuntu:~/$ cat
10
-main.py
#!/usr/bin/python3
divisible_by_2 = __import__(
'10-divisible_by_2'
).divisible_by_2

my_list = [
0
,
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
6
]
list_result = divisible_by_2(my_list)

i =
0
while
i < len(list_result):
    print(
"{:d} {:s} divisible by 2"
.format(my_list[i],
"is"
if
list_result[i]
else
"is not"
))
    i +=
1
guillaume@
ubuntu:~/$ ./
10
-main.py
0
is
divisible
by
2
1
is
not divisible
by
2
2
is
divisible
by
2
3
is
not divisible
by
2
4
is
divisible
by
2
5
is
not divisible
by
2
6
is
divisible
by
2
guillaume@
ubuntu:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-data_structures
File:
10-divisible_by_2.py
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
10. Only by 2
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
Students who are done with "10. Only by 2"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>11. Delete at</summary>

**Files:**

- [`11-delete_at.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-data_structures/11-delete_at.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-data_structures`

**Task details:**

```text
11. Delete at
Write a function that deletes the item at a specific position in a list.
Prototype:
def delete_at(my_list=[], idx=0):
If
idx
is negative or out of range, nothing change (returns the same list)
You are not allowed to use
pop()
You are not allowed to import any module
guillaume
@ubuntu
:~/
$
cat
11
-main.py
#!/usr/bin/python3
delete_at = __import__(
'11-delete_at'
).delete_at

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
idx =
3
new_list = delete_at(my_list, idx)
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
1
,
2
,
3
,
5
]
[
1
,
2
,
3
,
5
]
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-data_structures
File:
11-delete_at.py
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
11. Delete at
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
Students who are done with "11. Delete at"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>12. Switch</summary>

**Files:**

- [`12-switch.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-data_structures/12-switch.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-data_structures`

**Task details:**

```text
12. Switch
Complete the source code in order to switch value of
a
and
b
You can find the source code
here
Your code should be inserted where the comment is (line 4)
Your program should be exactly 5 lines long
guillaume
@ubuntu
:~/py/
$
./
12
-switch.py
a=
10
- b=
89
guillaume
@ubuntu
:~/py/
$
wc -l
12
-switch.py
5
12
-switch.py
guillaume
@ubuntu
:~/py/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-data_structures
File:
12-switch.py
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
12. Switch
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
Students who are done with "12. Switch"
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
