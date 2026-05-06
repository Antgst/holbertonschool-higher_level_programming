# ðŸ“˜ Python - Object-relational mapping

## ðŸ“Œ Description

_No description detected._

---

## ðŸ“š Resources

**Read or watch**:



- [Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)

- [mysqlclient/MySQLdb documentation](https://mysqlclient.readthedocs.io/) (*please don't pay attention to `_mysql`*)

- [MySQLdb tutorial](https://www.mikusa.com/python-mysql-docs/index.html)

- [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)

- [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)

- [mysqlclient/MySQLdb](https://github.com/PyMySQL/mysqlclient)

- [Introduction to SQLAlchemy](https://www.youtube.com/watch?v=woKYyhLCcnU)

- [Flask SQLAlchemy](https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW)

- [10 common stumbling blocks for SQLAlchemy newbies](http://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html)

- [Python SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/database/python-sqlalchemy.html)

- [SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/) (*__Warning:__ This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL*)

- [SQLAlchemy Tutorial](https://overiq.com/sqlalchemy-101/)

---

## ðŸŽ¯ Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), __without the help of Google__:



### General



- How to connect to a MySQL database from a Python script

- How to `SELECT` rows in a MySQL table from a Python script

- How to `INSERT` rows in a MySQL table from a Python script

- What ORM means

- How to map a Python Class to a MySQL table

---

## âœ… Requirements

### General



- Allowed editors: `vi`, `vim`, `emacs`

- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)

- Your files will be executed with `MySQLdb` version `2.0.x`

- Your files will be executed with `SQLAlchemy` version `1.4.x`

- All your files should end with a new line

- The first line of all your files should be exactly `#!/usr/bin/python3`

- A `README.md` file, at the root of the folder of the project, is mandatory

- Your code should use the pycodestyle (version 2.7.*)

- All your files must be executable

- The length of your files will be tested using `wc`

- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)' `)

- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)' `)

- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)' ` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)' `)

- A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class or method (the length of it will be verified)

- You are not allowed to use `execute` with sqlalchemy

---

## âš™ï¸ Setup

_No specific setup detected._

---

## ðŸ§  Quiz

_No quiz detected in the exported HTML._


---

## ðŸ§© Tasks

<details>
<summary>0. Get all states</summary>

**Files:**

- [`0-select_states.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/0-select_states.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-object_relational_mapping`

**Task details:**

```text
0. Get all states
Write a script that lists all
states
from the database
hbtn_0e_0_usa
:
Your script should take 3 arguments:
mysql username
,
mysql password
and
database name
(no argument validation needed)
You must use the module
MySQLdb
(
import MySQLdb
)
Your script should connect to a MySQL server running on
localhost
at port
3306
Results must be sorted in ascending order by
states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
guillaume
@ubuntu
:
~
/
$ cat
0
-
select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE
DATABASE IF
NOT
EXISTS
hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE
TABLE
IF
NOT
EXISTS
states (
    id
INT
NOT
NULL
AUTO_INCREMENT,
    name
VARCHAR
(
256
)
NOT
NULL
,
PRIMARY
KEY (id)
);
INSERT
INTO
states (name)
VALUES
("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume
@ubuntu
:
~
/
$ cat
0
-
select_states.sql
|
mysql
-
uroot
-
p
Enter password:
guillaume
@ubuntu
:
~
/
$ .
/
0
-
select_states.py root root hbtn_0e_0_usa
(
1
,
'California'
)
(
2
,
'Arizona'
)
(
3
,
'Texas'
)
(
4
,
'New York'
)
(
5
,
'Nevada'
)
guillaume
@ubuntu
:
~
/
$
No test cases needed
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-object_relational_mapping
File:
0-select_states.py
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
0. Get all states
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
Students who are done with "0. Get all states"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>1. Filter states</summary>

**Files:**

- [`1-filter_states.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/1-filter_states.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-object_relational_mapping`

**Task details:**

```text
1. Filter states
Write a script that lists all
states
with a
name
starting with
N
(upper N) from the database
hbtn_0e_0_usa
:
Your script should take 3 arguments:
mysql username
,
mysql password
and
database name
(no argument validation needed)
You must use the module
MySQLdb
(
import MySQLdb
)
Your script should connect to a MySQL server running on
localhost
at port
3306
Results must be sorted in ascending order by
states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
guillaume
@ubuntu
:
~
/
$ cat
0
-
select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE
DATABASE IF
NOT
EXISTS
hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE
TABLE
IF
NOT
EXISTS
states (
    id
INT
NOT
NULL
AUTO_INCREMENT,
    name
VARCHAR
(
256
)
NOT
NULL
,
PRIMARY
KEY (id)
);
INSERT
INTO
states (name)
VALUES
("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume
@ubuntu
:
~
/
$ cat
0
-
select_states.sql
|
mysql
-
uroot
-
p
Enter password:
guillaume
@ubuntu
:
~
/
$ .
/
1
-
filter_states.py root root hbtn_0e_0_usa
(
4
,
'New York'
)
(
5
,
'Nevada'
)
guillaume
@ubuntu
:
~
/
$
No test cases needed
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-object_relational_mapping
File:
1-filter_states.py
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
1. Filter states
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
Students who are done with "1. Filter states"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>2. Filter states by user input</summary>

**Files:**

- [`2-my_filter_states.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/2-my_filter_states.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-object_relational_mapping`

**Task details:**

```text
2. Filter states by user input
Write a script that takes in an argument and displays all values in the
states
table of
hbtn_0e_0_usa
where
name
matches the argument.
Your script should take 4 arguments:
mysql username
,
mysql password
,
database name
and
state name searched
(no argument validation needed)
You must use the module
MySQLdb
(
import MySQLdb
)
Your script should connect to a MySQL server running on
localhost
at port
3306
You must use
format
to create the SQL query with the user input
Results must be sorted in ascending order by
states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
guillaume
@ubuntu
:
~
/
$ cat
0
-
select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE
DATABASE IF
NOT
EXISTS
hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE
TABLE
IF
NOT
EXISTS
states (
    id
INT
NOT
NULL
AUTO_INCREMENT,
    name
VARCHAR
(
256
)
NOT
NULL
,
PRIMARY
KEY (id)
);
INSERT
INTO
states (name)
VALUES
("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume
@ubuntu
:
~
/
$ cat
0
-
select_states.sql
|
mysql
-
uroot
-
p
Enter password:
guillaume
@ubuntu
:
~
/
$ .
/
2
-
my_filter_states.py root root hbtn_0e_0_usa
'Arizona'
(
2
,
'Arizona'
)
guillaume
@ubuntu
:
~
/
$
No test cases needed
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-object_relational_mapping
File:
2-my_filter_states.py
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
2. Filter states by user input
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
Students who are done with "2. Filter states by user input"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>3. SQL Injection...</summary>

**Files:**

- [`3-my_safe_filter_states.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/3-my_safe_filter_states.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-object_relational_mapping`

**Task details:**

```text
3. SQL Injection...
Wait, do you remember the previous task? Did you test
"Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
as an input?
guillaume
@ubuntu
:~/
$
./
2
-my_filter_states.py root root hbtn_0e_0_usa
"Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
(
2
,
'Arizona'
)
guillaume
@ubuntu
:~/
$
./
0
-select_states.py root root hbtn_0e_0_usa
guillaume
@ubuntu
:~/
$
What? Empty?
Yes, it's an
SQL injection
to delete all records of a tableâ€¦
Once again, write a script that takes in arguments and displays all values in the
states
table of
hbtn_0e_0_usa
where
name
matches the argument. But this time, write one that is safe from MySQL injections!
Your script should take 4 arguments:
mysql username
,
mysql password
,
database name
and
state name searched
(safe from MySQL injection)
You must use the module
MySQLdb
(
import MySQLdb
)
Your script should connect to a MySQL server running on
localhost
at port
3306
Results must be sorted in ascending order by
states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
guillaume
@ubuntu
:
~
/
$ cat
0
-
select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE
DATABASE IF
NOT
EXISTS
hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE
TABLE
IF
NOT
EXISTS
states (
    id
INT
NOT
NULL
AUTO_INCREMENT,
    name
VARCHAR
(
256
)
NOT
NULL
,
PRIMARY
KEY (id)
);
INSERT
INTO
states (name)
VALUES
("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume
@ubuntu
:
~
/
$ cat
0
-
select_states.sql
|
mysql
-
uroot
-
p
Enter password:
guillaume
@ubuntu
:
~
/
$ .
/
3
-
my_safe_filter_states.py root root hbtn_0e_0_usa
'Arizona'
(
2
,
'Arizona'
)
guillaume
@ubuntu
:
~
/
$
No test cases needed
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-object_relational_mapping
File:
3-my_safe_filter_states.py
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
3. SQL Injection...
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
Students who are done with "3. SQL Injection..."
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>4. Cities by states</summary>

**Files:**

- [`4-cities_by_state.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/4-cities_by_state.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-object_relational_mapping`

**Task details:**

```text
4. Cities by states
Write a script that lists all
cities
from the database
hbtn_0e_4_usa
Your script should take 3 arguments:
mysql username
,
mysql password
and
database name
You must use the module
MySQLdb
(
import MySQLdb
)
Your script should connect to a MySQL server running on
localhost
at port
3306
Results must be sorted in ascending order by
cities.id
You can use only
execute()
once
Results must be displayed as they are in the example below
Your code should not be executed when imported
guillaume
@ubuntu
:
~
/
$ cat
4
-
cities_by_state.sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE
DATABASE IF
NOT
EXISTS
hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE
TABLE
IF
NOT
EXISTS
states (
    id
INT
NOT
NULL
AUTO_INCREMENT,
    name
VARCHAR
(
256
)
NOT
NULL
,
PRIMARY
KEY (id)
);
INSERT
INTO
states (name)
VALUES
("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
CREATE
TABLE
IF
NOT
EXISTS
cities (
    id
INT
NOT
NULL
AUTO_INCREMENT,
    state_id
INT
NOT
NULL
,
    name
VARCHAR
(
256
)
NOT
NULL
,
PRIMARY
KEY (id),
FOREIGN
KEY(state_id)
REFERENCES
states(id)
);
INSERT
INTO
cities (state_id, name)
VALUES
(
1
, "San Francisco"), (
1
, "San Jose"), (
1
, "Los Angeles"), (
1
, "Fremont"), (
1
, "Livermore");
INSERT
INTO
cities (state_id, name)
VALUES
(
2
, "Page"), (
2
, "Phoenix");
INSERT
INTO
cities (state_id, name)
VALUES
(
3
, "Dallas"), (
3
, "Houston"), (
3
, "Austin");
INSERT
INTO
cities (state_id, name)
VALUES
(
4
, "New York");
INSERT
INTO
cities (state_id, name)
VALUES
(
5
, "Las Vegas"), (
5
, "Reno"), (
5
, "Henderson"), (
5
, "Carson City");

guillaume
@ubuntu
:
~
/
$ cat
4
-
cities_by_state.sql
|
mysql
-
uroot
-
p
Enter password:
guillaume
@ubuntu
:
~
/
$ .
/
4
-
cities_by_state.py root root hbtn_0e_4_usa
(
1
,
'San Francisco'
,
'California'
)
(
2
,
'San Jose'
,
'California'
)
(
3
,
'Los Angeles'
,
'California'
)
(
4
,
'Fremont'
,
'California'
)
(
5
,
'Livermore'
,
'California'
)
(
6
,
'Page'
,
'Arizona'
)
(
7
,
'Phoenix'
,
'Arizona'
)
(
8
,
'Dallas'
,
'Texas'
)
(
9
,
'Houston'
,
'Texas'
)
(
10
,
'Austin'
,
'Texas'
)
(
11
,
'New York'
,
'New York'
)
(
12
,
'Las Vegas'
,
'Nevada'
)
(
13
,
'Reno'
,
'Nevada'
)
(
14
,
'Henderson'
,
'Nevada'
)
(
15
,
'Carson City'
,
'Nevada'
)
guillaume
@ubuntu
:
~
/
$
No test cases needed
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-object_relational_mapping
File:
4-cities_by_state.py
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
4. Cities by states
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
Students who are done with "4. Cities by states"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>5. All cities by state</summary>

**Files:**

- [`5-filter_cities.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/5-filter_cities.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-object_relational_mapping`

**Task details:**

```text
5. All cities by state
Write a script that takes in the name of a state as an argument and lists all
cities
of that state, using the database
hbtn_0e_4_usa
Your script should take 4 arguments:
mysql username
,
mysql password
,
database name
and
state name
(SQL injection free!)
You must use the module
MySQLdb
(
import MySQLdb
)
Your script should connect to a MySQL server running on
localhost
at port
3306
Results must be sorted in ascending order by
cities.id
You can use only
execute()
once
The results must be displayed as they are in the example below
Your code should not be executed when imported
guillaume
@ubuntu
:
~
/
$ cat
4
-
cities_by_state.sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE
DATABASE IF
NOT
EXISTS
hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE
TABLE
IF
NOT
EXISTS
states (
    id
INT
NOT
NULL
AUTO_INCREMENT,
    name
VARCHAR
(
256
)
NOT
NULL
,
PRIMARY
KEY (id)
);
INSERT
INTO
states (name)
VALUES
("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
CREATE
TABLE
IF
NOT
EXISTS
cities (
    id
INT
NOT
NULL
AUTO_INCREMENT,
    state_id
INT
NOT
NULL
,
    name
VARCHAR
(
256
)
NOT
NULL
,
PRIMARY
KEY (id),
FOREIGN
KEY(state_id)
REFERENCES
states(id)
);
INSERT
INTO
cities (state_id, name)
VALUES
(
1
, "San Francisco"), (
1
, "San Jose"), (
1
, "Los Angeles"), (
1
, "Fremont"), (
1
, "Livermore");
INSERT
INTO
cities (state_id, name)
VALUES
(
2
, "Page"), (
2
, "Phoenix");
INSERT
INTO
cities (state_id, name)
VALUES
(
3
, "Dallas"), (
3
, "Houston"), (
3
, "Austin");
INSERT
INTO
cities (state_id, name)
VALUES
(
4
, "New York");
INSERT
INTO
cities (state_id, name)
VALUES
(
5
, "Las Vegas"), (
5
, "Reno"), (
5
, "Henderson"), (
5
, "Carson City");

guillaume
@ubuntu
:
~
/
$ .
/
5
-
filter_cities.py root root hbtn_0e_4_usa Texas

guillaume
@ubuntu
:
~
/
$ cat
4
-
cities_by_state.sql
|
mysql
-
uroot
-
p
Enter password:
guillaume
@ubuntu
:
~
/
$ .
/
5
-
filter_cities.py root root hbtn_0e_4_usa Texas
Dallas, Houston, Austin
guillaume
@ubuntu
:
~
/
$ .
/
5
-
filter_cities.py root root hbtn_0e_4_usa Hawaii

guillaume
@ubuntu
:
~
/
$
No test cases needed
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-object_relational_mapping
File:
5-filter_cities.py
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
5. All cities by state
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
Students who are done with "5. All cities by state"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>6. First state model</summary>

**Files:**

- [`model_state.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/model_state.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-object_relational_mapping`

**Task details:**

```text
6. First state model
Write a python file that contains the class definition of a
State
and an instance
Base = declarative_base()
:
State
class:
inherits from
Base
Tips
links to the MySQL table
states
class attribute
id
that represents a column of an auto-generated, unique integer, can't be null and is a primary key
class attribute
name
that represents a column of a string with maximum 128 characters and can't be null
You must use the module
SQLAlchemy
Your script should connect to a MySQL server running on
localhost
at port
3306
WARNING:
all classes who inherit from
Base
must
be imported before calling
Base.metadata.create_all(engine)
guillaume
@ubuntu
:~/
$
cat
6
-model_state.sql
--
Create
database hbtn_0e_6_usa
CREATE
DATABASE
IF
NOT
EXISTS
hbtn_0e_6_usa;
USE
hbtn_0e_6_usa;
SHOW
CREATE
TABLE
states;

guillaume
@ubuntu
:~/
$
cat
6
-model_state.sql |
mysql -uroot -p
Enter password:
ERROR 1146 (42S02) at line 4: Table 'hbtn_0e_6_usa.states' doesn't exist
guillaume@ubuntu:~/$ cat 6-model_state.py
#!/usr/bin/python3
"""Start link
class
to table
in
database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
if
__name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

guillaume@ubuntu:~/$ ./6-model_state.py root root hbtn_0e_6_usa
guillaume@ubuntu:~/$ cat 6-model_state.sql
| mysql -uroot -p
Enter
password:
Table
Create
Table
states
CREATE
TABLE
`states`
(\n
`id`
int(
11
)
NOT
NULL
AUTO_INCREMENT
,\n
`name`
varchar(
128
)
NOT
NULL
,\n
PRIMARY
KEY
(
`id`
)\n)
ENGINE
=
Inno
DB
DEFAULT
CHARSET
=latin1
guillaume
@ubuntu
:~/
$
No test cases needed
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-object_relational_mapping
File:
model_state.py
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
6. First state model
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
Students who are done with "6. First state model"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>7. All states via SQLAlchemy</summary>

**Files:**

- [`7-model_state_fetch_all.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/7-model_state_fetch_all.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-object_relational_mapping`

**Task details:**

```text
7. All states via SQLAlchemy
Write a script that lists all
State
objects from the database
hbtn_0e_6_usa
Your script should take 3 arguments:
mysql username
,
mysql password
and
database name
You must use the module
SQLAlchemy
You must import
State
and
Base
from
model_state
-
from model_state import Base, State
Your script should connect to a MySQL server running on
localhost
at port
3306
Results must be sorted in ascending order by
states.id
The results must be displayed as they are in the example below
Your code should not be executed when imported
guillaume@ubuntu:~/$ cat 7-model_state_fetch_all.sql
-- Insert states
INSERT INTO states (name) VALUES (
"California"
), (
"Arizona"
), (
"Texas"
), (
"New York"
), (
"Nevada"
);
guillaume@ubuntu:~/$ cat 7-model_state_fetch_all.sql | mysql -uroot -p hbtn_0e_6_usa
Enter password:
guillaume@ubuntu:~/$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
guillaume@ubuntu:~/$
No test cases needed
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-object_relational_mapping
File:
7-model_state_fetch_all.py
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
7. All states via SQLAlchemy
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
Students who are done with "7. All states via SQLAlchemy"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>8. First state</summary>

**Files:**

- [`8-model_state_fetch_first.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/8-model_state_fetch_first.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-object_relational_mapping`

**Task details:**

```text
8. First state
Write a script that prints the first
State
object from the database
hbtn_0e_6_usa
Your script should take 3 arguments:
mysql username
,
mysql password
and
database name
You must use the module
SQLAlchemy
You must import
State
and
Base
from
model_state
-
from model_state import Base, State
Your script should connect to a MySQL server running on
localhost
at port
3306
The state you display must be the first in
states.id
You are not allowed to fetch all states from the database before displaying the result
The results must be displayed as they are in the example below
If the table
states
is empty, print
Nothing
followed by a new line
Your code should not be executed when imported
guillaume
@ubuntu
:~/
$
./
8
-model_state_fetch_first.py root root hbtn_0e_6_usa
1
:
California
guillaume
@ubuntu
:~/
$
No test cases needed
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-object_relational_mapping
File:
8-model_state_fetch_first.py
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
8. First state
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
Students who are done with "8. First state"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>9. Contains `a`</summary>

**Files:**

- [`9-model_state_filter_a.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/9-model_state_filter_a.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-object_relational_mapping`

**Task details:**

```text
9. Contains `a`
Write a script that lists all
State
objects that contain the letter
a
from the database
hbtn_0e_6_usa
Your script should take 3 arguments:
mysql username
,
mysql password
and
database name
You must use the module
SQLAlchemy
You must import
State
and
Base
from
model_state
-
from model_state import Base, State
Your script should connect to a MySQL server running on
localhost
at port
3306
Results must be sorted in ascending order by
states.id
The results must be displayed as they are in the example below
Your code should not be executed when imported
guillaume
@ubuntu
:~/
$
./
9
-model_state_filter_a.py root root hbtn_0e_6_usa
1
:
California
2
:
Arizona
3
:
Texas
5
:
Nevada
guillaume
@ubuntu
:~/
$
No test cases needed
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-object_relational_mapping
File:
9-model_state_filter_a.py
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
9. Contains `a`
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
Students who are done with "9. Contains `a`"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>10. Get a state</summary>

**Files:**

- [`10-model_state_my_get.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/10-model_state_my_get.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-object_relational_mapping`

**Task details:**

```text
10. Get a state
Write a script that prints the
State
object with the
name
passed as argument from the database
hbtn_0e_6_usa
Your script should take 4 arguments:
mysql username
,
mysql password
,
database name
and
state name to search
(SQL injection free)
You must use the module
SQLAlchemy
You must import
State
and
Base
from
model_state
-
from model_state import Base, State
Your script should connect to a MySQL server running on
localhost
at port
3306
You can assume you have one record with the state name to search
Results must display the
states.id
If no state has the name you searched for, display
Not found
Your code should not be executed when imported
guillaume
@ubuntu
:~/
$
./
10
-model_state_my_get.py root root hbtn_0e_6_usa
Texas
3
guillaume
@ubuntu
:~/
$
./
10
-model_state_my_get.py root root hbtn_0e_6_usa
Illinois
Not
found
guillaume
@ubuntu
:~/
$
No test cases needed
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-object_relational_mapping
File:
10-model_state_my_get.py
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
10. Get a state
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
Students who are done with "10. Get a state"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>11. Add a new state</summary>

**Files:**

- [`11-model_state_insert.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/11-model_state_insert.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-object_relational_mapping`

**Task details:**

```text
11. Add a new state
Write a script that adds the
State
object "Louisiana" to the database
hbtn_0e_6_usa
Your script should take 3 arguments:
mysql username
,
mysql password
and
database name
You must use the module
SQLAlchemy
You must import
State
and
Base
from
model_state
-
from model_state import Base, State
Your script should connect to a MySQL server running on
localhost
at port
3306
Print the new
states.id
after creation
Your code should not be executed when imported
guillaume
@ubuntu
:~/
$
./
11
-model_state_insert.py root root hbtn_0e_6_usa
6
guillaume
@ubuntu
:~/
$
./
7
-model_state_fetch_all.py root root hbtn_0e_6_usa
1
:
California
2
:
Arizona
3
:
Texas
4
:
New
York
5
:
Nevada
6
:
Louisiana
guillaume
@ubuntu
:~/
$
No test cases needed
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-object_relational_mapping
File:
11-model_state_insert.py
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
11. Add a new state
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
Students who are done with "11. Add a new state"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>12. Update a state</summary>

**Files:**

- [`12-model_state_update_id_2.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/12-model_state_update_id_2.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-object_relational_mapping`

**Task details:**

```text
12. Update a state
Write a script that changes the name of a
State
object from the database
hbtn_0e_6_usa
Your script should take 3 arguments:
mysql username
,
mysql password
and
database name
You must use the module
SQLAlchemy
You must import
State
and
Base
from
model_state
-
from model_state import Base, State
Your script should connect to a MySQL server running on
localhost
at port
3306
Change the name of the
State
where
id = 2
to
New Mexico
Your code should not be executed when imported
guillaume
@ubuntu
:~/
$
./
12
-model_state_update_id_2.py root root hbtn_0e_6_usa
guillaume
@ubuntu
:~/
$
./
7
-model_state_fetch_all.py root root hbtn_0e_6_usa
1
:
California
2
:
New
Mexico
3
:
Texas
4
:
New
York
5
:
Nevada
6
:
Louisiana
guillaume
@ubuntu
:~/
$
No test cases needed
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-object_relational_mapping
File:
12-model_state_update_id_2.py
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
12. Update a state
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
Students who are done with "12. Update a state"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>13. Delete states</summary>

**Files:**

- [`13-model_state_delete_a.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/13-model_state_delete_a.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-object_relational_mapping`

**Task details:**

```text
13. Delete states
Write a script that deletes all
State
objects with a name containing the letter
a
from the database
hbtn_0e_6_usa
Your script should take 3 arguments:
mysql username
,
mysql password
and
database name
You must use the module
SQLAlchemy
You must import
State
and
Base
from
model_state
-
from model_state import Base, State
Your script should connect to a MySQL server running on
localhost
at port
3306
Your code should not be executed when imported
guillaume
@ubuntu
:~/
$
./
13
-model_state_delete_a.py root root hbtn_0e_6_usa
guillaume
@ubuntu
:~/
$
./
7
-model_state_fetch_all.py root root hbtn_0e_6_usa
2
:
New
Mexico
4
:
New
York
guillaume
@ubuntu
:~/
$
No test cases needed
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-object_relational_mapping
File:
13-model_state_delete_a.py
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
13. Delete states
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
Students who are done with "13. Delete states"
Ã—
Recommended Sandboxes
Loading...
```

</details>

<details>
<summary>14. Cities in state</summary>

**Files:**

- [`model_city.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/model_city.py)
- [`14-model_city_fetch_by_state.py`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/14-model_city_fetch_by_state.py)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-object_relational_mapping`

**Task details:**

```text
14. Cities in state
Write a Python file similar to
model_state.py
named
model_city.py
that contains the class definition of a
City
.
City
class:
inherits from
Base
(imported from
model_state
)
links to the MySQL table
cities
class attribute
id
that represents a column of an auto-generated, unique integer, can't be null and is a primary key
class attribute
name
that represents a column of a string of 128 characters and can't be null
class attribute
state_id
that represents a column of an integer, can't be null and is a foreign key to
states.id
You must use the module
SQLAlchemy
Next, write a script
14-model_city_fetch_by_state.py
that prints all
City
objects from the database
hbtn_0e_14_usa
:
Your script should take 3 arguments:
mysql username
,
mysql password
and
database name
You must use the module
SQLAlchemy
You must import
State
and
Base
from
model_state
-
from model_state import Base, State
Your script should connect to a MySQL server running on
localhost
at port
3306
Results must be sorted in ascending order by
cities.id
Results must be display as they are in the example below (
<state name>: (<city id>) <city name>
)
Your code should not be executed when imported
guillaume
@ubuntu
:
~
/
$ cat
14
-
model_city_fetch_by_state.sql
-- Create database hbtn_0e_14_usa, tables states and cities + some data
CREATE
DATABASE IF
NOT
EXISTS
hbtn_0e_14_usa;
USE hbtn_0e_14_usa;
CREATE
TABLE
IF
NOT
EXISTS
states (
    id
INT
NOT
NULL
AUTO_INCREMENT,
    name
VARCHAR
(
256
)
NOT
NULL
,
PRIMARY
KEY (id)
);
INSERT
INTO
states (name)
VALUES
("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
CREATE
TABLE
IF
NOT
EXISTS
cities (
    id
INT
NOT
NULL
AUTO_INCREMENT,
    state_id
INT
NOT
NULL
,
    name
VARCHAR
(
256
)
NOT
NULL
,
PRIMARY
KEY (id),
FOREIGN
KEY(state_id)
REFERENCES
states(id)
);
INSERT
INTO
cities (state_id, name)
VALUES
(
1
, "San Francisco"), (
1
, "San Jose"), (
1
, "Los Angeles"), (
1
, "Fremont"), (
1
, "Livermore");
INSERT
INTO
cities (state_id, name)
VALUES
(
2
, "Page"), (
2
, "Phoenix");
INSERT
INTO
cities (state_id, name)
VALUES
(
3
, "Dallas"), (
3
, "Houston"), (
3
, "Austin");
INSERT
INTO
cities (state_id, name)
VALUES
(
4
, "New York");
INSERT
INTO
cities (state_id, name)
VALUES
(
5
, "Las Vegas"), (
5
, "Reno"), (
5
, "Henderson"), (
5
, "Carson City");

guillaume
@ubuntu
:
~
/
$ cat
14
-
model_city_fetch_by_state.sql
|
mysql
-
uroot
-
p
Enter password:
guillaume
@ubuntu
:
~
/
$ .
/
14
-
model_city_fetch_by_state.py root root hbtn_0e_14_usa
California: (
1
) San Francisco
California: (
2
) San Jose
California: (
3
) Los Angeles
California: (
4
) Fremont
California: (
5
) Livermore
Arizona: (
6
) Page
Arizona: (
7
) Phoenix
Texas: (
8
) Dallas
Texas: (
9
) Houston
Texas: (
10
) Austin
New
York: (
11
)
New
York
Nevada: (
12
) Las Vegas
Nevada: (
13
) Reno
Nevada: (
14
) Henderson
Nevada: (
15
) Carson City
guillaume
@ubuntu
:
~
/
$
No test cases needed
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
python-object_relational_mapping
File:
model_city.py, 14-model_city_fetch_by_state.py
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
14. Cities in state
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
Students who are done with "14. Cities in state"
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
