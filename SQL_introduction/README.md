# 📘 SQL - Introduction

## 📌 Description

_No description detected._

---

## 📚 Resources

**Read or watch**:


- [What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)

- [Install MySQL (MySQL Server)](https://www.youtube.com/watch?v=9h3ctGFTz9w)

- [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)

- [Basic SQL statements: DDL and DML](https://github.com/hs-hq/project_resources/blob/main/sql/database_design_ddl_dml.md)

- [Basic queries: SQL and RA](https://github.com/hs-hq/project_resources/blob/main/sql/database_design_queries.md)

- [SQL technique: functions](https://github.com/hs-hq/project_resources/blob/main/sql/database_design_functions.md)

- [SQL technique: subqueries](https://github.com/hs-hq/project_resources/blob/main/sql/database_design_subqueries.md)

- [What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)

- [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)

- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

- Duo to a temporary bug to some of the resources aboves, you can find most of the information [here](https://www.w3schools.com/sql/default.asp)

---

## 🎯 Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), __without the help of Google__:


### General


- What's a database

- What's a relational database

- What does SQL stand for

- What's MySQL

- How to create a database in MySQL

- What does `DDL` and `DML` stand for

- How to `CREATE` or `ALTER` a table

- How to `SELECT` data from a table

- How to `INSERT`, `UPDATE` or `DELETE` data

- What are `subqueries`

- How to use MySQL functions

---

## ✅ Requirements

### General


- Allowed editors: `vi`, `vim`, `emacs`

- All your files will be executed on Ubuntu 22.04 LTS using `MySQL 8.0` (version 8.0.25)

- All your files should end with a new line

- All your SQL queries should have a comment just before (i.e. syntax above)

- All your files should start by a comment describing the task

- All SQL keywords should be in uppercase (`SELECT`, `WHERE`...)

- A `README.md` file, at the root of the folder of the project, is mandatory

- The length of your files will be tested using `wc`

---

## ⚙️ Setup

_No specific setup detected._

---

## 🧠 Quiz

<details>
<summary>Question #0</summary>

**Question:** What does SQL stand for?

**Available answers:**

- `Sequences of Query Logic`
- `Structured Query Language`
- `Solid Query Language`
- `Structured Question Language`

**Answer:** `Structured Query Language`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #1</summary>

**Question:** What is a relational database? (please select all correct answers)

**Available answers:**

- `a database`
- `a collection of data`
- `married databases`
- `data are organized by tables, records and columns`
- `data are organized by tables and indexes`
- `a table containing multiple object representation`
- `a table containing only one object representation`

**Answer:** `a table containing only one object representation`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #2</summary>

**Question:** What does DDL stand for?

**Available answers:**

- `Data Definition Language`
- `Database Definition Language`
- `Data Document Language`
- `Document Data Language`

**Answer:** `Data Definition Language`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #3</summary>

**Question:** What does DML stand for?

**Available answers:**

- `Database Manipulation Language`
- `Document Manipulation Language`
- `Data Manipulation Language`
- `Document Model Language`

**Answer:** `Data Manipulation Language`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #4</summary>

**Question:** How do you list all users in this table?

**Available answers:**

- `DELETE * FROM users;`
- `SELECT * FROM users;`
- `SELECT ALL users;`

**Answer:** `SELECT * FROM users;`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #5</summary>

**Question:** How to you add a new record in the table users ?

**Available answers:**

- `INSERT users (id, name, age) VALUES (2, "Betty", 30);`
- `INSERT INTO users (id, name) VALUES (2, "Betty", 30);`
- `INSERT INTO users (id, name, age) VALUES (2, "Betty", 30);`
- `INSERT INTO users (id, name, age) VALUES (2, "Betty");`

**Answer:** `INSERT INTO users (id, name, age) VALUES (2, "Betty", 30);`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #6</summary>

**Question:** How do you delete the users record with id = 89 in this table?

**Available answers:**

- `DELETE users WHERE id = 89;`
- `DELETE FROM users WHERE id = 89;`
- `DELETE FROM users;`
- `DELETE FROM users WHERE id IS EQUAL TO 89;`

**Answer:** `DELETE FROM users WHERE id = 89;`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #7</summary>

**Question:** How do you change the name of the users record with id = 89 to Holberton ?

**Available answers:**

- `UPDATE users SET name = "Holberton" WHERE id = 89;`
- `CHANGE users SET name = "Holberton" WHERE id = 89;`
- `UPDATE users SET name = "Holberton";`

**Answer:** `UPDATE users SET name = "Holberton" WHERE id = 89;`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>

<details>
<summary>Question #8</summary>

**Question:** How do you list all users records with age > 21 in this table?

**Available answers:**

- `SELECT * FROM users WHERE age < 21;`
- `SELECT * FROM users WHERE age IS UP TO 21;`
- `SELECT * FROM users WHERE age > 21;`
- `SELECT * FROM users WHERE age BETWEEN 21 AND 89;`

**Answer:** `SELECT * FROM users WHERE age > 21;`

**Explanation / tip:**

_To be reviewed and completed manually if needed._

</details>


---

## 🧩 Tasks

<details>
<summary>0. List databases</summary>

**Files:**

- [`0-list_databases.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_introduction/0-list_databases.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_introduction`

**Task details:**

```text
0. List databases
Write a script that lists all databases of your MySQL server.
guillaume
@ubuntu
:~/
$
cat
0
-list_databases.sql |
mysql -hlocalhost -uroot -p
Enter password:
Database
information_schema
mysql
performance_schema
sys
guillaume@ubuntu:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_introduction
File:
0-list_databases.sql
0. List databases
---
---
---
---
---
```

</details>

<details>
<summary>1. Create a database</summary>

**Files:**

- [`1-create_database_if_missing.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_introduction/1-create_database_if_missing.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_introduction`

**Task details:**

```text
1. Create a database
Write a script that creates the database
hbtn_0c_0
in your MySQL server.
If the database
hbtn_0c_0
already exists, your script should not fail
You are not allowed to use the
SELECT
or
SHOW
statements
guillaume
@ubuntu
:~/
$
cat
1
-create_database_if_missing.sql |
mysql -hlocalhost -uroot -p
Enter password:
guillaume@ubuntu:~/$ cat 0-list_databases.sql
| mysql -hlocalhost -uroot -p
Enter
password:
Database
information_schema
hbtn_0c_0
mysql
performance_schema
guillaume
@ubuntu
:~/
$
cat
1
-create_database_if_missing.sql |
mysql -hlocalhost -uroot -p
Enter password:
guillaume@ubuntu:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_introduction
File:
1-create_database_if_missing.sql
1. Create a database
---
---
---
---
---
```

</details>

<details>
<summary>2. Delete a database</summary>

**Files:**

- [`2-remove_database.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_introduction/2-remove_database.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_introduction`

**Task details:**

```text
2. Delete a database
Write a script that deletes the database
hbtn_0c_0
in your MySQL server.
If the database
hbtn_0c_0
doesn't exist, your script should not fail
You are not allowed to use the
SELECT
or
SHOW
statements
guillaume
@ubuntu
:~/
$
cat
0
-list_databases.sql |
mysql -hlocalhost -uroot -p
Enter password:
Database
hbtn_0c_0
information_schema
mysql
performance_schema
sys
guillaume@ubuntu:~/$ cat 2-remove_database.sql
| mysql -hlocalhost -uroot -p
Enter
password:
guillaume
@ubuntu
:~/
$
cat
0
-list_databases.sql |
mysql -hlocalhost -uroot -p
Enter password:
Database
information_schema
mysql
performance_schema
sys
guillaume@ubuntu:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_introduction
File:
2-remove_database.sql
2. Delete a database
---
---
---
---
---
```

</details>

<details>
<summary>3. List tables</summary>

**Files:**

- [`3-list_tables.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_introduction/3-list_tables.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_introduction`

**Task details:**

```text
3. List tables
Write a script that lists all the tables of a database in your MySQL server.
The database name will be passed as argument of
mysql
command (in the following example:
mysql
is the name of the database)
guillaume
@ubuntu
:~/
$
cat
3
-list_tables.sql |
mysql -hlocalhost -uroot -p mysql
Enter password:
Tables_in_mysql
columns_priv
component
db
default_roles
engine_cost
func
general_log
global_grants
gtid_executed
help_category
help_keyword
help_relation
help_topic
innodb_index_stats
innodb_table_stats
password_history
plugin
procs_priv
proxies_priv
replication_asynchronous_connection_failover
replication_asynchronous_connection_failover_managed
role_edges
server_cost
servers
slave_master_info
slave_relay_log_info
slave_worker_info
slow_log
tables_priv
time_zone
time_zone_leap_second
time_zone_name
time_zone_transition
time_zone_transition_type
user
guillaume@ubuntu:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_introduction
File:
3-list_tables.sql
3. List tables
---
---
---
---
---
```

</details>

<details>
<summary>4. First table</summary>

**Files:**

- [`4-first_table.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_introduction/4-first_table.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_introduction`

**Task details:**

```text
4. First table
Write a script that creates a table called
first_table
in the current database in your MySQL server.
first_table
description:
id
INT
name
VARCHAR(256)
The database name will be passed as an argument of the
mysql
command
If the table
first_table
already exists, your script should not fail
You are not allowed to use the
SELECT
or
SHOW
statements
guillaume
@ubuntu
:~/
$
cat
4
-first_table.sql |
mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$ cat 3-list_tables.sql
| mysql -hlocalhost -uroot -p hbtn_0c_0
Enter
password:
Tables
_in_hbtn_0c_0
first_table
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_introduction
File:
4-first_table.sql
4. First table
---
---
---
---
---
```

</details>

<details>
<summary>5. Full description</summary>

**Files:**

- [`5-full_table.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_introduction/5-full_table.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_introduction`

**Task details:**

```text
5. Full description
Write a script that prints the following description of the table
first_table
from the database
hbtn_0c_0
in your MySQL server.
The database name will be passed as an argument of the
mysql
command
You are not allowed to use the
DESCRIBE
or
EXPLAIN
statements
guillaume
@ubuntu
:
~
/
$ cat
5
-
full_table.sql
|
mysql
-
hlocalhost
-
uroot
-
p hbtn_0c_0
Enter password:
Table
Create
Table
first_table
CREATE
TABLE
`first_table` (\n  `id`
int
DEFAULT
NULL
,\n  `name`
varchar
(
256
)
DEFAULT
NULL
\n) ENGINE
=
InnoDB
DEFAULT
CHARSET
=
utf8mb4
COLLATE
=
utf8mb4_0900_ai_ci
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
SQL_introduction
File:
5-full_table.sql
5. Full description
---
---
---
---
---
```

</details>

<details>
<summary>6. List all in table</summary>

**Files:**

- [`6-list_values.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_introduction/6-list_values.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_introduction`

**Task details:**

```text
6. List all in table
Write a script that lists all rows of the table
first_table
from the database
hbtn_0c_0
in your MySQL server.
All fields should be printed
The database name will be passed as an argument of the
mysql
command
guillaume
@ubuntu
:~/
$
cat
6
-list_values.sql |
mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_introduction
File:
6-list_values.sql
6. List all in table
---
---
---
---
---
```

</details>

<details>
<summary>7. First add</summary>

**Files:**

- [`7-insert_value.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_introduction/7-insert_value.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_introduction`

**Task details:**

```text
7. First add
Write a script that inserts a new row in the table
first_table
(database
hbtn_0c_0
) in your MySQL server.
New row:
id
=
89
name
=
Best School
The database name will be passed as an argument of the
mysql
command
guillaume
@ubuntu
:~/
$
cat
7
-insert_value.sql |
mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$ cat 6-list_values.sql
| mysql -hlocalhost -uroot -p hbtn_0c_0
Enter
password:
id    name
89
Best
School
guillaume
@ubuntu
:~/
$
cat
7
-insert_value.sql |
mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$ cat 7-insert_value.sql
| mysql -hlocalhost -uroot -p hbtn_0c_0
Enter
password:
guillaume
@ubuntu
:~/
$
cat
6
-list_values.sql |
mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
id    name
89    Best School
89    Best School
89    Best School
guillaume@ubuntu:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_introduction
File:
7-insert_value.sql
7. First add
---
---
---
---
---
```

</details>

<details>
<summary>8. Count 89</summary>

**Files:**

- [`8-count_89.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_introduction/8-count_89.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_introduction`

**Task details:**

```text
8. Count 89
Write a script that displays the number of records with
id = 89
in the table
first_table
of the database
hbtn_0c_0
in your MySQL server.
The database name will be passed as an argument of the
mysql
command
guillaume
@ubuntu
:~/
$
cat
8
-count_89.sql |
mysql -hlocalhost -uroot -p hbtn_0c_0
| tail -
1
Enter
password:
3
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_introduction
File:
8-count_89.sql
8. Count 89
---
---
---
---
---
```

</details>

<details>
<summary>9. Full creation</summary>

**Files:**

- [`9-full_creation.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_introduction/9-full_creation.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_introduction`

**Task details:**

```text
9. Full creation
Write a script that creates a table
second_table
in the database
hbtn_0c_0
in your MySQL server and add multiples rows.
second_table
description:
id
INT
name
VARCHAR(256)
score
INT
The database name will be passed as an argument to the
mysql
command
If the table
second_table
already exists, your script should not fail
You are not allowed to use the
SELECT
and
SHOW
statements
Your script should create these records:
id
= 1,
name
= "John",
score
= 10
id
= 2,
name
= "Alex",
score
= 3
id
= 3,
name
= "Bob",
score
= 14
id
= 4,
name
= "George",
score
= 8
guillaume
@ubuntu
:~/
$
cat
9
-full_creation.sql |
mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_introduction
File:
9-full_creation.sql
9. Full creation
---
---
---
---
---
```

</details>

<details>
<summary>10. List by best</summary>

**Files:**

- [`10-top_score.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_introduction/10-top_score.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_introduction`

**Task details:**

```text
10. List by best
Write a script that lists all records of the table
second_table
of the database
hbtn_0c_0
in your MySQL server.
Results should display both the score and the name (in this order)
Records should be ordered by score (top first)
The database name will be passed as an argument of the
mysql
command
guillaume
@ubuntu
:~/
$
cat
10
-top_score.sql |
mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score    name
14    Bob
10    John
8    George
3    Alex
guillaume@ubuntu:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_introduction
File:
10-top_score.sql
10. List by best
---
---
---
---
---
```

</details>

<details>
<summary>11. Select the best</summary>

**Files:**

- [`11-best_score.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_introduction/11-best_score.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_introduction`

**Task details:**

```text
11. Select the best
Write a script that lists all records with a
score >= 10
in the table
second_table
of the database
hbtn_0c_0
in your MySQL server.
Results should display both the score and the name (in this order)
Records should be ordered by score (top first)
The database name will be passed as an argument of the
mysql
command
guillaume
@ubuntu
:~/
$
cat
11
-best_score.sql |
mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score    name
14    Bob
10    John
guillaume@ubuntu:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_introduction
File:
11-best_score.sql
11. Select the best
---
---
---
---
---
```

</details>

<details>
<summary>12. Cheating is bad</summary>

**Files:**

- [`12-no_cheating.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_introduction/12-no_cheating.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_introduction`

**Task details:**

```text
12. Cheating is bad
Write a script that updates the score of Bob to
10
in the table
second_table
.
You are not allowed to use Bob's id value, only the
name
field
The database name will be passed as an argument of the
mysql
command
guillaume
@ubuntu
:~/
$
cat
12
-no_cheating.sql |
mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$ cat 10-top_score.sql
| mysql -hlocalhost -uroot -p hbtn_0c_0
Enter
password:
score    name
10
John
10
Bob
8
George
3
Alex
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_introduction
File:
12-no_cheating.sql
12. Cheating is bad
---
---
---
---
---
```

</details>

<details>
<summary>13. Score too low</summary>

**Files:**

- [`13-change_class.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_introduction/13-change_class.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_introduction`

**Task details:**

```text
13. Score too low
Write a script that removes all records with a
score <= 5
in the table
second_table
of the database
hbtn_0c_0
in your MySQL server.
The database name will be passed as an argument of the
mysql
command
guillaume
@ubuntu
:~/
$
cat
13
-change_class.sql |
mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$ cat 10-top_score.sql
| mysql -hlocalhost -uroot -p hbtn_0c_0
Enter
password:
score    name
10
John
10
Bob
8
George
guillaume
@ubuntu
:~/
$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_introduction
File:
13-change_class.sql
13. Score too low
---
---
---
---
---
```

</details>

<details>
<summary>14. Average</summary>

**Files:**

- [`14-average.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_introduction/14-average.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_introduction`

**Task details:**

```text
14. Average
Write a script that computes the score average of all records in the table
second_table
of the database
hbtn_0c_0
in your MySQL server.
The result column name should be
average
The database name will be passed as an argument of the
mysql
command
guillaume
@ubuntu
:~/
$
cat
14
-average.sql |
mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
average
9.3333
guillaume@ubuntu:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_introduction
File:
14-average.sql
14. Average
---
---
---
---
---
```

</details>

<details>
<summary>15. Number by score</summary>

**Files:**

- [`15-groups.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_introduction/15-groups.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_introduction`

**Task details:**

```text
15. Number by score
Write a script that lists the number of records with the same score in the table
second_table
of the database
hbtn_0c_0
in your MySQL server.
The result should display:
the
score
the number of records for this
score
with the label
number
The list should be sorted by the number of records (descending)
The database name will be passed as an argument to the
mysql
command
guillaume
@ubuntu
:~/
$
cat
15
-groups.sql |
mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score    number
10    2
8    1
guillaume@ubuntu:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_introduction
File:
15-groups.sql
15. Number by score
---
---
---
---
---
```

</details>

<details>
<summary>16. Say my name</summary>

**Files:**

- [`16-no_link.sql`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/SQL_introduction/16-no_link.sql)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `SQL_introduction`

**Task details:**

```text
16. Say my name
Write a script that lists all records of the table
second_table
of the database
hbtn_0c_0
in your MySQL server.
Don't list rows where the
name
column does not contain a value
Results should display the score and the name (in this order)
Records should be listed by descending score
The database name will be passed as an argument to the
mysql
command
In this example, new data have been added to the table
second_table
.
guillaume
@ubuntu
:~/
$
cat
16
-no_link.sql |
mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score    name
18    Aria
12    Aria
10    John
10    Bob
guillaume@ubuntu:~/$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
SQL_introduction
File:
16-no_link.sql
16. Say my name
---
---
---
---
---
```

</details>


---

## 🧪 Testing

Use the provided task examples and Holberton checker to validate the project.

---

## 👤 Author

Project from Holberton School.

README generated with Antoine's README Factory workflow.
