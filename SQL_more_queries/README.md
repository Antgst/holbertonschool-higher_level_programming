# ðŸ“˜ SQL - More queries

## ðŸ“Œ Description

_No description detected._

---

## ðŸ“š Resources

**Read or watch**:



- [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)

- [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://www.mysqltutorial.org/mysql-administration/mysql-grant/)

- [MySQL constraints](https://zetcode.com/mysql/constraints/)

- [Basic query operation: the join](https://github.com/hs-hq/project_resources/blob/main/sql/database_design_join.md)

- [SQL technique: multiple joins and the distinct keyword](https://github.com/hs-hq/project_resources/blob/main/sql/database_design_multiple_joins.md)

- [SQL technique: join types](https://github.com/hs-hq/project_resources/blob/main/sql/database_design_join_types.md)

- [SQL technique: subqueries](https://github.com/hs-hq/project_resources/blob/main/sql/database_design_subqueries.md)

- [SQL technique: union and minus](https://github.com/hs-hq/project_resources/blob/main/sql/database_design_union_minus.md)

- [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)

- [The Seven Types of SQL Joins](https://tableplus.com/blog/2018/09/a-beginners-guide-to-seven-types-of-sql-joins.html)

- [MySQL Tutorial](https://www.youtube.com/watch?v=yPu6qV5byu4)

- [SQL Style Guide](https://www.sqlstyle.guide/)

- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)





Extra resources around relational database model design:



- [Design](https://www.guru99.com/database-design.html)

- [Normalization](https://www.guru99.com/database-normalization.html)

- [ER Modeling](https://www.guru99.com/er-modeling.html)

---

## ðŸŽ¯ Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), __without the help of Google__:



### General



- How to create a new MySQL user

- How to manage privileges for a user to a database or table

- What's a `PRIMARY KEY`

- What's a `FOREIGN KEY`

- How to use `NOT NULL` and `UNIQUE` constraints

- How to retrieve datas from multiple tables in one request

- What are subqueries

- What are `JOIN` and `UNION`

---

## âœ… Requirements

### General



- Allowed editors: `vi`, `vim`, `emacs`

- All your files will be executed on Ubuntu 20.04 LTS using `MySQL 8.0` (version 8.0.25)

- All your files should end with a new line

- All your SQL queries should have a comment just before (i.e. syntax above)

- All your files should start by a comment describing the task

- All SQL keywords should be in uppercase (`SELECT`, `WHERE`...)

- A `README.md` file, at the root of the folder of the project, is mandatory

- The length of your files will be tested using `wc`

---

## âš™ï¸ Setup

_No specific setup detected._

---

## ðŸ§  Quiz

<details>
<summary>Question #0</summary>

**Question:** What DCL means?

**Available answers:**

- `Document Control Language`
- `Data Control Language`
- `Data Concept Language`
- `Document Control Line`

**Answer:** `Data Control Language`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #1</summary>

**Question:** Is it possible to give only read access to a database to a user?

**Available answers:**

- `Yes`
- `No`

**Answer:** `Yes`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #2</summary>

**Question:** Is it possible to give only read access to a table to a user?

**Available answers:**

- `Yes`
- `No`

**Answer:** `Yes`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #3</summary>

**Question:** Is it possible to give only read access to multiple databases and tables to a user?

**Available answers:**

- `Yes`
- `No`

**Answer:** `Yes`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #4</summary>

**Question:** Is it possible to give only delete access to a table to a user?

**Available answers:**

- `Yes`
- `No`

**Answer:** `Yes`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #5</summary>

**Question:** Is it possible to give only insert access to a table to a user?

**Available answers:**

- `Yes`
- `No`

**Answer:** `Yes`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #6</summary>

**Question:** Which JOIN type doesn't exist? (please select all correct answers)

**Available answers:**

- `LEFT`
- `IN LEFT`
- `RIGHT AND LEFT`
- `INNER`
- `TOP`
- `FULL OUTER`
- `FULL INNER`

**Answer:** `FULL INNER`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>


---

## ðŸ§© Tasks

<details>
<summary>0. My privileges!</summary>

**Files:**

- [`0-privileges.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_more_queries/0-privileges.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_more_queries`

**Task details:**

```text
0. My privileges!
Write a script that lists all privileges of the MySQL users
user_0d_1
and
user_0d_2
on your server (in
localhost
).
guillaume
@ubuntu
:~/
$
cat
0
-privileges.sql |
mysql -hlocalhost -uroot -p
Enter password:
ERROR 1141 (42000) at line 3: There is no such grant
defined
for
user 'user_0d_1' on host 'localhost'
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ echo "CREATE USER 'user_0d_1'@'localhost';"
|  mysql -hlocalhost -uroot -p
Enter
password:
guillaume
@ubuntu
:~/
$
echo
"GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';"
|
mysql -hlocalhost -uroot -p
Enter password:
guillaume@ubuntu:~/$ cat 0-privileges.sql
| mysql -hlocalhost -uroot -p
Enter
password:
Grants
for
user_0d_1
@localhost
GRANT
SELECT
,
INSERT
,
UPDA
...,
DROP
ROLE
ON
*.*
TO
`user_0d_1`
@
`localhost`
GRANT
APPLICATION_PASSWORD_ADMIN
,
AUDIT
...,
XA_RECOVER_ADMIN
ON
*.*
TO
`user_0d_1`
@
`localhost`
ERROR
1141
(
42000
) at line
4
:
There
is no such grant
defined
for
user
'user_0d_2'
on host
'localhost'
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_more_queries
File:
0-privileges.sql
Score of the task
8
/8
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
0. My privileges!
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
Students who are done with "0. My privileges!"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>1. Root user</summary>

**Files:**

- [`1-create_user.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_more_queries/1-create_user.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_more_queries`

**Task details:**

```text
1. Root user
Write a script that creates the MySQL server user
user_0d_1
.
user_0d_1
should have all privileges on your MySQL server
The
user_0d_1
password should be set to
user_0d_1_pwd
If the user
user_0d_1
already exists, your script should not fail
guillaume
@ubuntu
:~/
$
cat
1
-create_user.sql |
mysql -hlocalhost -uroot -p
Enter password:
guillaume@ubuntu:~/$ cat 0-privileges.sql
| mysql -hlocalhost -uroot -p
Enter
password:
Grants
for
user_0d_1
@localhost
GRANT
SELECT
,
INSERT
...,
DROP
ROLE
ON
*.*
TO
`user_0d_1`
@
`localhost`
GRANT
APPLICATION_PASSWORD_ADMIN
,...,
XA_RECOVER_ADMIN
ON
*.*
TO
`user_0d_1`
@
`localhost`
ERROR
1141
(
42000
) at line
4
:
There
is no such grant
defined
for
user
'user_0d_2'
on host
'localhost'
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_more_queries
File:
1-create_user.sql
Score of the task
6
/6
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
1. Root user
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
Students who are done with "1. Root user"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>2. Read user</summary>

**Files:**

- [`2-create_read_user.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_more_queries/2-create_read_user.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_more_queries`

**Task details:**

```text
2. Read user
Write a script that creates the database
hbtn_0d_2
and the user
user_0d_2
.
user_0d_2
should have only SELECT privilege in the database
hbtn_0d_2
The
user_0d_2
password should be set to
user_0d_2_pwd
If the database
hbtn_0d_2
already exists, your script should not fail
If the user
user_0d_2
already exists, your script should not fail
guillaume
@ubuntu
:~/
$
cat
2
-create_read_user.sql |
mysql -hlocalhost -uroot -p
Enter password:
guillaume@ubuntu:~/$ cat 0-privileges.sql
| mysql -hlocalhost -uroot -p
Enter
password:
Grants
for
user_0d_1
@localhost
GRANT
SELECT
, ...,
DROP
ROLE
ON
*.*
TO
`user_0d_1`
@
`localhost`
GRANT
APPLICATION_PASSWORD_ADMIN
,...,
XA_RECOVER_ADMIN
ON
*.*
TO
`user_0d_1`
@
`localhost`
Grants
for
user_0d_2
@localhost
GRANT
USAGE
ON
*.*
TO
`user_0d_2`
@
`localhost`
GRANT
SELECT
ON
`hbtn_0d_2`
.*
TO
`user_0d_2`
@
`localhost`
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_more_queries
File:
2-create_read_user.sql
Score of the task
6
/6
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
2. Read user
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
Students who are done with "2. Read user"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>3. Always a name</summary>

**Files:**

- [`3-force_name.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_more_queries/3-force_name.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_more_queries`

**Task details:**

```text
3. Always a name
Write a script that creates the table
force_name
on your MySQL server.
force_name
description:
id
INT
name
VARCHAR(256) can't be null
The database name will be passed as an argument of the
mysql
command
If the table
force_name
already exists, your script should not fail
guillaume
@ubuntu
:~/
$
cat
3
-force_name.sql |
mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
guillaume@ubuntu:~/$ echo 'INSERT INTO force_name (id, name) VALUES (89, "Best School");'
| mysql -hlocalhost -uroot -p hbtn_0d_2
Enter
password:
guillaume
@ubuntu
:~/
$
echo
'SELECT * FROM force_name;'
|
mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
id    name
89    Best School
guillaume@ubuntu:~/$ echo 'INSERT INTO force_name (id) VALUES (333);'
| mysql -hlocalhost -uroot -p hbtn_0d_2
Enter
password:
ERROR
1364
(
HY000
) at line
1
:
Field
'name'
doesn
't have a default value
guillaume@ubuntu:~/$ echo '
SELECT
*
FROM
force_name;
' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
id    name
89    Best School
guillaume@ubuntu:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_more_queries
File:
3-force_name.sql
Score of the task
6
/6
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
3. Always a name
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
Students who are done with "3. Always a name"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>4. ID can't be null</summary>

**Files:**

- [`4-never_empty.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_more_queries/4-never_empty.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_more_queries`

**Task details:**

```text
4. ID can't be null
Write a script that creates the table
id_not_null
on your MySQL server.
id_not_null
description:
id
INT with the default value
1
name
VARCHAR(256)
The database name will be passed as an argument of the
mysql
command
If the table
id_not_null
already exists, your script should not fail
guillaume
@ubuntu
:~/$ cat
4
-never_empty.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter
password
:
guillaume
@ubuntu
:~/$ echo
'INSERT INTO id_not_null (id, name) VALUES (89, "Best School");'
| mysql -hlocalhost -uroot -p hbtn_0d_2
Enter
password
:
guillaume
@ubuntu
:~/$ echo
'SELECT * FROM id_not_null;'
| mysql -hlocalhost -uroot -p hbtn_0d_2
Enter
password
:
id    name
89
Best School
guillaume
@ubuntu
:~/$ echo
'INSERT INTO id_not_null (name) VALUES ("Best");'
| mysql -hlocalhost -uroot -p hbtn_0d_2
Enter
password
:
guillaume
@ubuntu
:~/$ echo
'SELECT * FROM id_not_null;'
| mysql -hlocalhost -uroot -p hbtn_0d_2
Enter
password
:
id    name
89
Best School
1
Best
guillaume
@ubuntu
:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_more_queries
File:
4-never_empty.sql
Score of the task
6
/6
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
4. ID can't be null
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
Students who are done with "4. ID can't be null"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>5. Unique ID</summary>

**Files:**

- [`5-unique_id.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_more_queries/5-unique_id.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_more_queries`

**Task details:**

```text
5. Unique ID
Write a script that creates the table
unique_id
on your MySQL server.
unique_id
description:
id
INT with the default value
1
and must be unique
name
VARCHAR(256)
The database name will be passed as an argument of the
mysql
command
If the table
unique_id
already exists, your script should not fail
guillaume
@ubuntu
:~/$ cat
5
-unique_id.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter
password
:
guillaume
@ubuntu
:~/$ echo
'INSERT INTO unique_id (id, name) VALUES (89, "Best School");'
| mysql -hlocalhost -uroot -p hbtn_0d_2
Enter
password
:
guillaume
@ubuntu
:~/$ echo
'SELECT * FROM unique_id;'
| mysql -hlocalhost -uroot -p hbtn_0d_2
Enter
password
:
id    name
89
Best School
guillaume
@ubuntu
:~/$ echo
'INSERT INTO unique_id (id, name) VALUES (89, "Best");'
| mysql -hlocalhost -uroot -p hbtn_0d_2
Enter
password
:
ERROR
1062
(
23000
) at line
1
: Duplicate entry
'89'
for key
'unique_id.id'
guillaume
@ubuntu
:~/$ echo
'SELECT * FROM unique_id;'
| mysql -hlocalhost -uroot -p hbtn_0d_2
Enter
password
:
id    name
89
Best School
guillaume
@ubuntu
:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_more_queries
File:
5-unique_id.sql
Score of the task
6
/6
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
5. Unique ID
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
Students who are done with "5. Unique ID"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>6. States table</summary>

**Files:**

- [`6-states.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_more_queries/6-states.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_more_queries`

**Task details:**

```text
6. States table
Write a script that creates the database
hbtn_0d_usa
and the table
states
(in the database
hbtn_0d_usa
) on your MySQL server.
states
description:
id
INT unique, auto generated, can't be null and is a primary key
name
VARCHAR(256) can't be null
If the database
hbtn_0d_usa
already exists, your script should not fail
If the table
states
already exists, your script should not fail
guillaume
@ubuntu
:~/
$
cat
6
-states.sql |
mysql -hlocalhost -uroot -p
Enter password:
guillaume@ubuntu:~/$ echo 'INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas");'
| mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter
password:
guillaume
@ubuntu
:~/
$
echo
'SELECT * FROM states;'
|
mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
id    name
1    California
2    Arizona
3    Texas
guillaume@ubuntu:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_more_queries
File:
6-states.sql
Score of the task
6
/6
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
6. States table
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
Students who are done with "6. States table"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>7. Cities table</summary>

**Files:**

- [`7-cities.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_more_queries/7-cities.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_more_queries`

**Task details:**

```text
7. Cities table
Write a script that creates the database
hbtn_0d_usa
and the table
cities
(in the database
hbtn_0d_usa
) on your MySQL server.
cities
description:
id
INT unique, auto generated, can't be null and is a primary key
state_id
INT, can't be null and must be a
FOREIGN KEY
that references to
id
of the
states
table
name
VARCHAR(256) can't be null
If the database
hbtn_0d_usa
already exists, your script should not fail
If the table
cities
already exists, your script should not fail
guillaume
@ubuntu
:~/
$
cat
7
-cities.sql |
mysql -hlocalhost -uroot -p
Enter password:
guillaume@ubuntu:~/$ echo 'INSERT INTO cities (state_id, name) VALUES (1, "San Francisco");'
| mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter
password:
guillaume
@ubuntu
:~/
$
echo
'SELECT * FROM cities;'
|
mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
id    state_id    name
1    1   San Francisco
guillaume@ubuntu:~/$ echo 'INSERT INTO cities (state_id, name) VALUES (10, "Paris");'
| mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter
password:
ERROR
1452
(
23000
) at line
1
:
Cannot
add
or
update a child
row:
a foreign key constraint fails (
`hbtn_0d_usa`
.
`cities`
,
CONSTRAINT
`cities_ibfk_1`
FOREIGN
KEY
(
`state_id`
)
REFERENCES
`states`
(
`id`
))
guillaume
@ubuntu
:~/
$
echo
'SELECT * FROM cities;'
|
mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
id    state_id    name
1    1   San Francisco
guillaume@ubuntu:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_more_queries
File:
7-cities.sql
Score of the task
6
/6
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
7. Cities table
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
Students who are done with "7. Cities table"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>8. Cities of California</summary>

**Files:**

- [`8-cities_of_california_subquery.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_more_queries/8-cities_of_california_subquery.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_more_queries`

**Task details:**

```text
8. Cities of California
Write a script that lists all the cities of California that can be found in the database
hbtn_0d_usa
.
The
states
table contains only one record where
name
=
California
(but the
id
can be different, as per the example)
Results must be sorted in ascending order by
cities.id
You are not allowed to use the
JOIN
keyword
The database name will be passed as an argument of the
mysql
command
guillaume
@ubuntu
:~/
$
echo
'SELECT * FROM states;'
|
mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
id    name
1    California
2    Arizona
3    Texas
4    Utah
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;'
| mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter
password:
id    state_id    name
1
1
San
Francisco
2
1
San
Jose
4
2
Page
6
3
Paris
7
3
Houston
8
3
Dallas
guillaume
@ubuntu
:~/
$
cat
8
-cities_of_california_subquery.sql |
mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
id    name
1    San Francisco
2    San Jose
guillaume@ubuntu:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_more_queries
File:
8-cities_of_california_subquery.sql
Score of the task
6
/6
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
8. Cities of California
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
Students who are done with "8. Cities of California"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>9. Cities by States</summary>

**Files:**

- [`9-cities_by_state_join.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_more_queries/9-cities_by_state_join.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_more_queries`

**Task details:**

```text
9. Cities by States
Write a script that lists all cities contained in the database
hbtn_0d_usa
.
Each record should display:
cities.id
-
cities.name
-
states.name
Results must be sorted in ascending order by
cities.id
You can use only one
SELECT
statement
The database name will be passed as an argument of the
mysql
command
guillaume
@ubuntu
:~/
$
echo
'SELECT * FROM states;'
|
mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
id    name
1    California
2    Arizona
3    Texas
4    Utah
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;'
| mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter
password:
id    state_id    name
1
1
San
Francisco
2
1
San
Jose
4
2
Page
6
3
Paris
7
3
Houston
8
3
Dallas
guillaume
@ubuntu
:~/
$
cat
9
-cities_by_state_join.sql |
mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
id    name    name
1    San Francisco   California
2    San Jose    California
4    Page    Arizona
6    Paris   Texas
7    Houston Texas
8    Dallas  Texas
guillaume@ubuntu:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_more_queries
File:
9-cities_by_state_join.sql
Score of the task
6
/6
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
9. Cities by States
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
Students who are done with "9. Cities by States"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>10. Genre ID by show</summary>

**Files:**

- [`10-genre_id_by_show.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_more_queries/10-genre_id_by_show.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_more_queries`

**Task details:**

```text
10. Genre ID by show
Import the database dump from
hbtn_0d_tvshows
to your MySQL server:
download
Write a script that lists all shows contained in
hbtn_0d_tvshows
that have at least one genre linked.
Each record should display:
tv_shows.title
-
tv_show_genres.genre_id
Results must be sorted in ascending order  by
tv_shows.title
and
tv_show_genres.genre_id
You can use only one
SELECT
statement
The database name will be passed as an argument of the
mysql
command
guillaume
@ubuntu
:
~
/
$ cat
10
-
genre_id_by_show.sql
|
mysql
-
hlocalhost
-
uroot
-
p hbtn_0d_tvshows
Enter password:
title    genre_id
Breaking Bad
1
Breaking Bad
6
Breaking Bad
7
Breaking Bad
8
Dexter
1
Dexter
2
Dexter
6
Dexter
7
Dexter
8
Game
of
Thrones
1
Game
of
Thrones
3
Game
of
Thrones
4
House
1
House
2
New
Girl
5
Silicon Valley
5
The Big Bang Theory
5
The
Last
Man
on
Earth
1
The
Last
Man
on
Earth
5
guillaume
@ubuntu
:
~
/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_more_queries
File:
10-genre_id_by_show.sql
Score of the task
6
/6
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
10. Genre ID by show
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
Students who are done with "10. Genre ID by show"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>11. Genre ID for all shows</summary>

**Files:**

- [`11-genre_id_all_shows.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_more_queries/11-genre_id_all_shows.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_more_queries`

**Task details:**

```text
11. Genre ID for all shows
Import the database dump of
hbtn_0d_tvshows
to your MySQL server:
download
(same as
10-genre_id_by_show.sql
)
Write a script that lists all shows contained in the database
hbtn_0d_tvshows
.
Each record should display:
tv_shows.title
-
tv_show_genres.genre_id
Results must be sorted in ascending order by
tv_shows.title
and
tv_show_genres.genre_id
If a show doesn't have a genre, display
NULL
You can use only one
SELECT
statement
The database name will be passed as an argument of the
mysql
command
guillaume
@ubuntu
:
~
/
$ cat
11
-
genre_id_all_shows.sql
|
mysql
-
hlocalhost
-
uroot
-
p hbtn_0d_tvshows
Enter password:
title    genre_id
Better
Call
Saul
NULL
Breaking Bad
1
Breaking Bad
6
Breaking Bad
7
Breaking Bad
8
Dexter
1
Dexter
2
Dexter
6
Dexter
7
Dexter
8
Game
of
Thrones
1
Game
of
Thrones
3
Game
of
Thrones
4
Homeland
NULL
House
1
House
2
New
Girl
5
Silicon Valley
5
The Big Bang Theory
5
The
Last
Man
on
Earth
1
The
Last
Man
on
Earth
5
guillaume
@ubuntu
:
~
/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_more_queries
File:
11-genre_id_all_shows.sql
Score of the task
6
/6
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
11. Genre ID for all shows
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
Students who are done with "11. Genre ID for all shows"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>12. No genre</summary>

**Files:**

- [`12-no_genre.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_more_queries/12-no_genre.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_more_queries`

**Task details:**

```text
12. No genre
Import the database dump from
hbtn_0d_tvshows
to your MySQL server:
download
(same as
11-genre_id_all_shows.sql
)
Write a script that lists all shows contained in
hbtn_0d_tvshows
without a genre linked.
Each record should display:
tv_shows.title
-
tv_show_genres.genre_id
Results must be sorted in ascending order by
tv_shows.title
and
tv_show_genres.genre_id
You can use only one
SELECT
statement
The database name will be passed as an argument of the
mysql
command
guillaume
@ubuntu
:
~
/
$ cat
12
-
no_genre.sql
|
mysql
-
hlocalhost
-
uroot
-
p hbtn_0d_tvshows
Enter password:
title    genre_id
Better
Call
Saul
NULL
Homeland
NULL
guillaume
@ubuntu
:
~
/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_more_queries
File:
12-no_genre.sql
Score of the task
6
/6
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
12. No genre
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
Students who are done with "12. No genre"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>13. Number of shows by genre</summary>

**Files:**

- [`13-count_shows_by_genre.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_more_queries/13-count_shows_by_genre.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_more_queries`

**Task details:**

```text
13. Number of shows by genre
Import the database dump from
hbtn_0d_tvshows
to your MySQL server:
download
(same as
12-no_genre.sql
)
Write a script that lists all genres from
hbtn_0d_tvshows
and displays the number of shows linked to each.
Each record should display:
<TV Show genre>
-
<Number of shows linked to this genre>
First column must be called
genre
Second column must be called
number_of_shows
Don't display a genre that doesn't have any shows linked
Results must be sorted in descending order by the number of shows linked
You can use only one
SELECT
statement
The database name will be passed as an argument of the
mysql
command
guillaume
@ubuntu
:~/
$
cat
13
-count_shows_by_genre.sql |
mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password:
genre    number_of_shows
Drama    5
Comedy    4
Mystery    2
Crime    2
Suspense    2
Thriller    2
Adventure    1
Fantasy    1
guillaume@ubuntu:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_more_queries
File:
13-count_shows_by_genre.sql
Score of the task
6
/6
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
13. Number of shows by genre
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
Students who are done with "13. Number of shows by genre"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>14. My genres</summary>

**Files:**

- [`14-my_genres.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_more_queries/14-my_genres.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_more_queries`

**Task details:**

```text
14. My genres
Import the database dump from
hbtn_0d_tvshows
to your MySQL server:
download
(same as
13-count_shows_by_genre.sql
)
Write a script that uses the
hbtn_0d_tvshows
database to lists all genres of the show
Dexter
.
The
tv_shows
table contains only one record where
title
=
Dexter
(but the
id
can be different)
Each record should display:
tv_genres.name
Results must be sorted in ascending order by the genre name
You can use only one
SELECT
statement
The database name will be passed as an argument of the
mysql
command
guillaume
@ubuntu
:~/
$
cat
14
-my_genres.sql |
mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password:
name
Crime
Drama
Mystery
Suspense
Thriller
guillaume@ubuntu:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_more_queries
File:
14-my_genres.sql
Score of the task
6
/6
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
14. My genres
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
Students who are done with "14. My genres"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>15. Only Comedy</summary>

**Files:**

- [`15-comedy_only.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_more_queries/15-comedy_only.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_more_queries`

**Task details:**

```text
15. Only Comedy
Import the database dump from
hbtn_0d_tvshows
to your MySQL server:
download
(same as
14-my_genres.sql
)
Write a script that lists all Comedy shows in the database
hbtn_0d_tvshows
.
The
tv_genres
table contains only one record where
name
=
Comedy
(but the
id
can be different)
Each record should display:
tv_shows.title
Results must be sorted in ascending order by the show title
You can use only one
SELECT
statement
The database name will be passed as an argument of the
mysql
command
guillaume
@ubuntu
:~/
$
cat
15
-comedy_only.sql |
mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password:
title
New Girl
Silicon Valley
The Big Bang Theory
The Last Man on Earth
guillaume@ubuntu:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_more_queries
File:
15-comedy_only.sql
Score of the task
6
/6
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
15. Only Comedy
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
Students who are done with "15. Only Comedy"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>16. List shows and genres</summary>

**Files:**

- [`16-shows_by_genre.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_more_queries/16-shows_by_genre.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_more_queries`

**Task details:**

```text
16. List shows and genres
Import the database dump from
hbtn_0d_tvshows
to your MySQL server:
download
(same as
15-comedy_only.sql
)
Write a script that lists all shows, and all genres linked to that show, from the database
hbtn_0d_tvshows
.
If a show doesn't have a genre, display
NULL
in the genre column
Each record should display:
tv_shows.title
-
tv_genres.name
Results must be sorted in ascending order by the show title and genre name
You can use only one
SELECT
statement
The database name will be passed as an argument of the
mysql
command
guillaume
@ubuntu
:
~
/
$ cat
16
-
shows_by_genre.sql
|
mysql
-
hlocalhost
-
uroot
-
p hbtn_0d_tvshows
Enter password:
title    name
Better
Call
Saul
NULL
Breaking Bad    Crime
Breaking Bad    Drama
Breaking Bad    Suspense
Breaking Bad    Thriller
Dexter    Crime
Dexter    Drama
Dexter    Mystery
Dexter    Suspense
Dexter    Thriller
Game
of
Thrones    Adventure
Game
of
Thrones    Drama
Game
of
Thrones    Fantasy
Homeland
NULL
House    Drama
House    Mystery
New
Girl    Comedy
Silicon Valley    Comedy
The Big Bang Theory    Comedy
The
Last
Man
on
Earth    Comedy
The
Last
Man
on
Earth    Drama
guillaume
@ubuntu
:
~
/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_more_queries
File:
16-shows_by_genre.sql
Score of the task
6
/6
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
16. List shows and genres
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
Students who are done with "16. List shows and genres"
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
