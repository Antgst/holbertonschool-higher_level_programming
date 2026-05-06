# ðŸ“˜ Python - Everything is object

## ðŸ“Œ Description

<br />

---

## ðŸ“š Resources

**Read or watch**:



- [9.10. Objects and values](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#objects-and-values)

- [9.11. Aliasing](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#aliasing)

- [Immutable vs mutable types](https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types)

- [Mutation](http://www.composingprograms.com/pages/24-mutable-data.html#sequence-objects) (*Only this chapter*)

- [9.12. Cloning lists](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#cloning-lists)

- [Python tuples: immutable but potentially changing](https://www.oreilly.com/radar/)

---

## ðŸŽ¯ Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), __without the help of Google__:



### General



- What is an object

- What is the difference between a class and an object or instance

- What is the difference between immutable object and mutable object

- What is a reference

- What is an assignment

- What is an alias

- How to know if two variables are identical

- How to know if two variables are linked to the same object

- How to display the variable identifier (which is the memory address in the CPython implementation)

- What is mutable and immutable

- What are the built-in mutable types

- What are the built-in immutable types

- How does Python pass variables to functions

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





### `.txt` Answer Files



- Only one line

- No Shebang on the first line (i.e. "#!/usr/bin/python3")

- All your files should end with a new line

---

## âš™ï¸ Setup

_No specific setup detected._

---

## ðŸ§  Quiz

_No quiz detected in the exported HTML._


---

## ðŸ§© Tasks

<details>
<summary>0. Who am I?</summary>

**Files:**

- [`0-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/0-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
0. Who am I?
What function would you use to print the type of an object?
Write the name of the function in the file, without
()
.
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
0-answer.txt
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
Get a sandbox
QA Review
Ã—
0. Who am I?
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
Students who are done with "0. Who am I?"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>1. Where are you?</summary>

**Files:**

- [`1-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/1-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
1. Where are you?
How do you get the variable identifier (which is the memory address in the CPython implementation)?
Write the name of the function in the file, without
()
.
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
1-answer.txt
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
Get a sandbox
QA Review
Ã—
1. Where are you?
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
Students who are done with "1. Where are you?"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>2. Right count</summary>

**Files:**

- [`2-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/2-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
2. Right count
In the following code, do
a
and
b
point to the same object?
Answer with
Yes
or
No
.
>>>
a =
89
>>>
b =
100
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
2-answer.txt
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
Get a sandbox
QA Review
Ã—
2. Right count
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
Students who are done with "2. Right count"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>3. Right count =</summary>

**Files:**

- [`3-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/3-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
3. Right count =
In the following code, do
a
and
b
point to the same object?
Answer with
Yes
or
No
.
>>>
a =
89
>>>
b =
89
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
3-answer.txt
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
Get a sandbox
QA Review
Ã—
3. Right count =
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
Students who are done with "3. Right count ="
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>4. Right count =</summary>

**Files:**

- [`4-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/4-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
4. Right count =
In the following code, do
a
and
b
point to the same object?
Answer with
Yes
or
No
.
>>>
a =
89
>>>
b = a
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
4-answer.txt
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
Get a sandbox
QA Review
Ã—
4. Right count =
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
Students who are done with "4. Right count ="
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>5. Right count =+</summary>

**Files:**

- [`5-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/5-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
5. Right count =+
In the following code, do
a
and
b
point to the same object?
Answer with
Yes
or
No
.
>>>
a =
89
>>>
b = a +
1
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
5-answer.txt
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
Get a sandbox
QA Review
Ã—
5. Right count =+
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
Students who are done with "5. Right count =+"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>6. Is equal</summary>

**Files:**

- [`6-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/6-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
6. Is equal
What do these 3 lines print?
>>>
s1 =
"Best School"
>>>
s2 = s1
>>>
print
(s1 == s2)
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
6-answer.txt
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
Get a sandbox
QA Review
Ã—
6. Is equal
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
Students who are done with "6. Is equal"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>7. Is the same</summary>

**Files:**

- [`7-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/7-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
7. Is the same
What do these 3 lines print?
>>>
s1 =
"Best"
>>>
s2 = s1
>>>
print
(s1
is
s2)
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
7-answer.txt
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
Get a sandbox
QA Review
Ã—
7. Is the same
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
Students who are done with "7. Is the same"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>8. Is really equal</summary>

**Files:**

- [`8-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/8-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
8. Is really equal
What do these 3 lines print?
>>>
s1 =
"Best School"
>>>
s2 =
"Best School"
>>>
print
(s1 == s2)
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
8-answer.txt
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
Get a sandbox
QA Review
Ã—
8. Is really equal
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
Students who are done with "8. Is really equal"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>9. Is really the same</summary>

**Files:**

- [`9-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/9-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
9. Is really the same
What do these 3 lines print?
>>>
s1 =
"Best School"
>>>
s2 =
"Best School"
>>>
print
(s1
is
s2)
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
9-answer.txt
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
Get a sandbox
QA Review
Ã—
9. Is really the same
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
Students who are done with "9. Is really the same"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>10. And with a list, is it equal</summary>

**Files:**

- [`10-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/10-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
10. And with a list, is it equal
What do these 3 lines print?
>>>
l1 = [
1
,
2
,
3
]
>>>
l2 = [
1
,
2
,
3
]
>>>
print
(l1 == l2)
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
10-answer.txt
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
Get a sandbox
QA Review
Ã—
10. And with a list, is it equal
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
Students who are done with "10. And with a list, is it equal"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>11. And with a list, is it the same</summary>

**Files:**

- [`11-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/11-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
11. And with a list, is it the same
What do these 3 lines print?
>>>
l1 = [
1
,
2
,
3
]
>>>
l2 = [
1
,
2
,
3
]
>>>
print
(l1
is
l2)
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
11-answer.txt
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
Get a sandbox
QA Review
Ã—
11. And with a list, is it the same
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
Students who are done with "11. And with a list, is it the same"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>12. And with a list, is it really equal</summary>

**Files:**

- [`12-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/12-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
12. And with a list, is it really equal
What do these 3 lines print?
>>>
l1 = [
1
,
2
,
3
]
>>>
l2 = l1
>>>
print
(l1 == l2)
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
12-answer.txt
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
Get a sandbox
QA Review
Ã—
12. And with a list, is it really equal
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
Students who are done with "12. And with a list, is it really equal"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>13. And with a list, is it really the same</summary>

**Files:**

- [`13-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/13-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
13. And with a list, is it really the same
What do these 3 lines print?
>>>
l1 = [
1
,
2
,
3
]
>>>
l2 = l1
>>>
print
(l1
is
l2)
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
13-answer.txt
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
Get a sandbox
QA Review
Ã—
13. And with a list, is it really the same
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
Students who are done with "13. And with a list, is it really the same"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>14. List append</summary>

**Files:**

- [`14-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/14-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
14. List append
What does this script print?
l1 = [
1
,
2
,
3
]
l2 = l1
l1.
append
(
4
)
print
(l2)
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
14-answer.txt
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
Get a sandbox
QA Review
Ã—
14. List append
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
Students who are done with "14. List append"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>15. List add</summary>

**Files:**

- [`15-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/15-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
15. List add
What does this script print?
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
15-answer.txt
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
Get a sandbox
QA Review
Ã—
15. List add
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
Students who are done with "15. List add"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>16. Integer incrementation</summary>

**Files:**

- [`16-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/16-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
16. Integer incrementation
What does this script print?
def
increment
(n):
    n +=
1
a =
1
increment
(a)
print
(a)
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
16-answer.txt
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
Get a sandbox
QA Review
Ã—
16. Integer incrementation
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
Students who are done with "16. Integer incrementation"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>17. List incrementation</summary>

**Files:**

- [`17-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/17-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
17. List incrementation
What does this script print?
def
increment
(n):
    n.
append
(
4
)

l = [
1
,
2
,
3
]
increment
(l)
print
(l)
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
17-answer.txt
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
Get a sandbox
QA Review
Ã—
17. List incrementation
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
Students who are done with "17. List incrementation"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>18. List assignation</summary>

**Files:**

- [`18-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/18-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
18. List assignation
What does this script print?
def
assign_value
(n, v):
    n = v

l1 = [
1
,
2
,
3
]
l2 = [
4
,
5
,
6
]
assign_value
(l1, l2)
print
(l1)
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
18-answer.txt
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
Get a sandbox
QA Review
Ã—
18. List assignation
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
Students who are done with "18. List assignation"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>19. Copy a list object</summary>

**Files:**

- [`19-copy_list.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/19-copy_list.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
19. Copy a list object
Write a function
def copy_list(a_list):
that returns a
copy
of a list.
The input list can contain any type of objects
Your file should be maximum 3-line long (no documentation needed)
You are not allowed to import any module
guillaume
@ubuntu
:~/
$
cat
19
-main.py
#!/usr/bin/python3
copy_list = __import__(
'19-copy_list'
).copy_list

my_list = [
1
,
2
,
3
]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

guillaume
@ubuntu
:~/
$
./
19
-main.py
[
1
,
2
,
3
]
[
1
,
2
,
3
]
[
1
,
2
,
3
]
True
False
guillaume
@ubuntu
:~/
$
wc -l
19
-copy_list.py
3
19
-copy_list.py
guillaume
@ubuntu
:~/
$
No test cases needed
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
19-copy_list.py
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
19. Copy a list object
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
Students who are done with "19. Copy a list object"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>20. Tuple or not?</summary>

**Files:**

- [`20-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/20-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
20. Tuple or not?
a
= ()
Is
a
a tuple? Answer with
Yes
or
No
.
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
20-answer.txt
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
Get a sandbox
QA Review
Ã—
20. Tuple or not?
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
Students who are done with "20. Tuple or not?"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>21. Tuple or not?</summary>

**Files:**

- [`21-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/21-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
21. Tuple or not?
a
= (
1
,
2
)
Is
a
a tuple? Answer with
Yes
or
No
.
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
21-answer.txt
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
Get a sandbox
QA Review
Ã—
21. Tuple or not?
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
Students who are done with "21. Tuple or not?"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>22. Tuple or not?</summary>

**Files:**

- [`22-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/22-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
22. Tuple or not?
a
= (
1
)
Is
a
a tuple? Answer with
Yes
or
No
.
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
22-answer.txt
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
Get a sandbox
QA Review
Ã—
22. Tuple or not?
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
Students who are done with "22. Tuple or not?"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>23. Tuple or not?</summary>

**Files:**

- [`23-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/23-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
23. Tuple or not?
a
= (
1
, )
Is
a
a tuple? Answer with
Yes
or
No
.
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
23-answer.txt
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
Get a sandbox
QA Review
Ã—
23. Tuple or not?
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
Students who are done with "23. Tuple or not?"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>24. Who I am?</summary>

**Files:**

- [`24-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/24-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
24. Who I am?
What does this script print?
a = (1)
b = (1)
a is b
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
24-answer.txt
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
Get a sandbox
QA Review
Ã—
24. Who I am?
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
Students who are done with "24. Who I am?"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>25. Tuple or not</summary>

**Files:**

- [`25-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/25-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
25. Tuple or not
What does this script print?
a = (1, 2)
b = (1, 2)
a is b
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
25-answer.txt
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
Get a sandbox
QA Review
Ã—
25. Tuple or not
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
Students who are done with "25. Tuple or not"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>26. Empty is not empty</summary>

**Files:**

- [`26-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/26-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
26. Empty is not empty
What does this script print?
a = ()
b = ()
a is b
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
26-answer.txt
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
Get a sandbox
QA Review
Ã—
26. Empty is not empty
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
Students who are done with "26. Empty is not empty"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>27. Still the same?</summary>

**Files:**

- [`27-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/27-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
27. Still the same?
>>>
id
(a)
139926795932424
>>>
a
[1, 2, 3, 4]
>>>
a = a + [
5
]
>>>
id
(a)
Will the last line of this script print
139926795932424
? Answer with
Yes
or
No
.
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
27-answer.txt
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
Get a sandbox
QA Review
Ã—
27. Still the same?
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
Students who are done with "27. Still the same?"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>28. Same or not?</summary>

**Files:**

- [`28-answer.txt`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/28-answer.txt)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-everything_is_object`

**Task details:**

```text
28. Same or not?
>>>
a
[1, 2, 3]
>>>
id
(a)
139926795932424
>>>
a += [
4
]
>>>
id
(a)
Will the last line of this script print
139926795932424
? Answer with
Yes
or
No
.
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-everything_is_object
File:
28-answer.txt
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
Get a sandbox
QA Review
Ã—
28. Same or not?
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
Students who are done with "28. Same or not?"
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
