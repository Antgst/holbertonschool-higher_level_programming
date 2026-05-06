# ðŸ“˜ JavaScript DOM manipulation

## ðŸ“Œ Description

# JavaScript DOM Manipulation

---

## ðŸ“š Resources

### Read or watch:



- [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/What_is_JavaScript)

- [Introduction to the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)

- [Document Interface](https://developer.mozilla.org/en-US/docs/Web/API/Document)

- [Element Class](https://developer.mozilla.org/en-US/docs/Web/API/Element)

- [Locating DOM elements using selectors](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Selection_and_traversal_on_the_DOM_tree)

- [CSS Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)

- [CSS Diner](https://flukeout.github.io/) Play with Selectors

- [DOM Scripting](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/DOM_scripting)

- [Network Requests](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Network_requests)

- [What went wrong? Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/What_went_wrong)

---

## ðŸŽ¯ Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), without the help of Google:



### General

- How to select HTML elements in JavaScript

- What are differences between ID, class and tag name selectors

- How to modify an HTML element style

- How to get and update an HTML element content

- How to modify the DOM

- How to make a request with XmlHTTPRequest

- How to make a request with Fetch API

- How to listen/bind to DOM events

- How to listen/bind to user events

---

## âœ… Requirements

### General

- Allowed editors: All of them.

- All your files will be interpreted on Chrome browser (version 57.0 or later)

- All your files should end with a new line

- A mandatory `README.md` file with meaningful information about the content, should be placed at the root folder of the project.

- Your code should be `semistandard` compliant

- You are not allowed to use var

- HTML should not reload for each action: DOM manipulation, update values, fetch dataâ€¦

---

## âš™ï¸ Setup

_No specific setup detected._

---

## ðŸ§  Quiz

_No quiz detected in the exported HTML._


---

## ðŸ§© Tasks

<details>
<summary>0. Color Me</summary>

**Files:**

- [`0-script.js`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/javascript-dom_manipulation/0-script.js)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `javascript-dom_manipulation`

**Task details:**

```text
0. Color Me
Write a JavaScript script that updates the text color of the
header
element to red (
#FF0000
):
You must use
document.querySelector
to select the HTML tag
Please test with this HTML file in your browser:
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 0-main.html
<!DOCTYPE
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
Holberton School
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
header
>
First HTML page
</
header
>
<
footer
>
Holberton School - 2022
</
footer
>
<
script
type
=
"text/javascript"
src
=
"0-script.js"
>
</
script
>
</
body
>
</
html
>
javiercito@ubuntu:~/javascript-dom_manipulation$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
javascript-dom_manipulation
File:
0-script.js
Score of the task
1
/1
pt
100.0%
0
correction requests
QA Review
Ã—
0. Color Me
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
Students who are done with "0. Color Me"
```

</details>

<details>
<summary>1. Click and turn red</summary>

**Files:**

- [`1-script.js`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/javascript-dom_manipulation/1-script.js)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `javascript-dom_manipulation`

**Task details:**

```text
1. Click and turn red
Write a JavaScript script that updates the text color of the
header
element to red (
#FF0000
) when the user clicks on the tag with id
red_header
:
Please test with this HTML file in your browser:
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 1-main.html
<!DOCTYPE
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
Holberton School
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
header
>
First HTML page
</
header
>
<
div
id
=
"red_header"
>
Red header
</
div
>
<
footer
>
Holberton School - 2022
</
footer
>
<
script
type
=
"text/javascript"
src
=
"1-script.js"
>
</
script
>
</
body
>
</
html
>
javiercito@ubuntu:~/javascript-dom_manipulation$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
javascript-dom_manipulation
File:
1-script.js
Score of the task
5
/5
pts
100.0%
0
correction requests
QA Review
Ã—
1. Click and turn red
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
Students who are done with "1. Click and turn red"
```

</details>

<details>
<summary>2. Add `.red` class</summary>

**Files:**

- [`2-script.js`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/javascript-dom_manipulation/2-script.js)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `javascript-dom_manipulation`

**Task details:**

```text
2. Add `.red` class
Write a JavaScript script that adds the class
red
to the
header
element when the user clicks on the tag with id
red_header
Please test with this HTML file in your browser:
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 2-main.html
<!DOCTYPE
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
Holberton School
</
title
>
<
style
>
.red
{
color
:
#FF0000
;
      }
</
style
>
</
head
>
<
body
>
<
header
>
First HTML page
</
header
>
<
div
id
=
"red_header"
>
Red header
</
div
>
<
footer
>
Holberton School - 2022
</
footer
>
<
script
type
=
"text/javascript"
src
=
"2-script.js"
>
</
script
>
</
body
>
</
html
>
javiercito@ubuntu:~/javascript-dom_manipulation$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
javascript-dom_manipulation
File:
2-script.js
Score of the task
5
/5
pts
100.0%
0
correction requests
QA Review
Ã—
2. Add `.red` class
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
Students who are done with "2. Add `.red` class"
```

</details>

<details>
<summary>3. Toggle classes</summary>

**Files:**

- [`3-script.js`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/javascript-dom_manipulation/3-script.js)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `javascript-dom_manipulation`

**Task details:**

```text
3. Toggle classes
Write a JavaScript script that toggles the class of the
header
element when the user clicks on the tag id
toggle_header
:
The
header
element must always have one class:
red
or
green
, never both in the same time and never empty.
If the current class is
red
, when the user click on id
toggle_header
element, the class must be updated to
green
; and the reverse.
Please test with this HTML file in your browser:
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 3-main.html
<!DOCTYPE
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
Holberton School
</
title
>
<
style
>
.red
{
color
:
#FF0000
;
      }
.green
{
color
:
#00FF00
;
      }
</
style
>
</
head
>
<
body
>
<
header
class
=
"green"
>
First HTML page
</
header
>
<
div
id
=
"toggle_header"
>
Toggle header
</
div
>
<
footer
>
Holberton School - 2022
</
footer
>
<
script
type
=
"text/javascript"
src
=
"3-script.js"
>
</
script
>
</
body
>
</
html
>
javiercito@ubuntu:~/javascript-dom_manipulation$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
javascript-dom_manipulation
File:
3-script.js
Score of the task
5
/5
pts
100.0%
0
correction requests
QA Review
Ã—
3. Toggle classes
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
Students who are done with "3. Toggle classes"
```

</details>

<details>
<summary>4. List of elements</summary>

**Files:**

- [`4-script.js`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/javascript-dom_manipulation/4-script.js)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `javascript-dom_manipulation`

**Task details:**

```text
4. List of elements
Write a JavaScript script that adds a
li
element to a list when the user clicks on the element with id
add_item
:
The new element must be:
<li>Item</li>
The new element must be added to the
ul
element with class
my_list
Please test with this HTML file in your browser:
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 4-main.html
<!DOCTYPE
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
Holberton School
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
header
>
First HTML page
</
header
>
<
br
/>
<
div
id
=
"add_item"
>
Add item
</
div
>
<
br
/>
<
ul
class
=
"my_list"
>
<
li
>
Item
</
li
>
</
ul
>
<
footer
>
Holberton School - 2022
</
footer
>
<
script
type
=
"text/javascript"
src
=
"4-script.js"
>
</
script
>
</
body
>
</
html
>
javiercito@ubuntu:~/javascript-dom_manipulation$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
javascript-dom_manipulation
File:
4-script.js
Score of the task
5
/5
pts
100.0%
0
correction requests
QA Review
Ã—
4. List of elements
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
Students who are done with "4. List of elements"
```

</details>

<details>
<summary>5. Change the text</summary>

**Files:**

- [`5-script.js`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/javascript-dom_manipulation/5-script.js)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `javascript-dom_manipulation`

**Task details:**

```text
5. Change the text
Write a JavaScript script that updates the text of the
header
element to
New Header!!!
when the user clicks on the element with id
update_header
Please test with this HTML file in your browser:
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 5-main.html
<!DOCTYPE
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
Holberton School
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
header
>
First HTML page
</
header
>
<
br
/>
<
div
id
=
"update_header"
>
Update the header
</
div
>
<
br
/>
<
footer
>
Holberton School - 2022
</
footer
>
<
script
type
=
"text/javascript"
src
=
"5-script.js"
>
</
script
>
</
body
>
</
html
>
javiercito@ubuntu:~/javascript-dom_manipulation$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
javascript-dom_manipulation
File:
5-script.js
Score of the task
5
/5
pts
100.0%
0
correction requests
QA Review
Ã—
5. Change the text
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
Students who are done with "5. Change the text"
```

</details>

<details>
<summary>6. Star wars character</summary>

**Files:**

- [`6-script.js`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/javascript-dom_manipulation/6-script.js)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `javascript-dom_manipulation`

**Task details:**

```text
6. Star wars character
Write a JavaScript script that fetches the character
name
from this URL:
https://swapi-api.hbtn.io/api/people/5/?format=json
The name must be displayed in the HTML tag with id
character
.
You must use the
Fetch API
.
You probably should read something about
usign Promises
later.
Please test with this HTML file in your browser:
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 6-main.html
<!DOCTYPE
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
Holberton School
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
header
>
Star Wars character
</
header
>
<
br
/>
<
div
id
=
"character"
>
</
div
>
<
br
/>
<
footer
>
Holberton School - 2022
</
footer
>
<
script
type
=
"text/javascript"
src
=
"6-script.js"
>
</
script
>
</
body
>
</
html
>
javiercito@ubuntu:~/javascript-dom_manipulation$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
javascript-dom_manipulation
File:
6-script.js
Score of the task
5
/5
pts
100.0%
0
correction requests
QA Review
Ã—
6. Star wars character
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
Students who are done with "6. Star wars character"
```

</details>

<details>
<summary>7. Star Wars movies</summary>

**Files:**

- [`7-script.js`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/javascript-dom_manipulation/7-script.js)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `javascript-dom_manipulation`

**Task details:**

```text
7. Star Wars movies
Write a JavaScript script that fetches and lists the
title
for all movies by using this URL:
https://swapi-api.hbtn.io/api/films/?format=json
All movie titles must be list in the HTML
ul
element with id
list_movies
You must use the Fetch API.
Please test with this HTML file in your browser:
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 7-main.html
<!DOCTYPE
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
Holberton School
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
header
>
Star Wars movies
</
header
>
<
br
/>
<
ul
id
=
"list_movies"
>
</
ul
>
<
br
/>
<
footer
>
Holberton School - 2022
</
footer
>
<
script
type
=
"text/javascript"
src
=
"7-script.js"
>
</
script
>
</
body
>
</
html
>
javiercito@ubuntu:~/javascript-dom_manipulation$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
javascript-dom_manipulation
File:
7-script.js
Score of the task
5
/5
pts
100.0%
0
correction requests
QA Review
Ã—
7. Star Wars movies
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
Students who are done with "7. Star Wars movies"
```

</details>

<details>
<summary>8. Say Hello!</summary>

**Files:**

- [`8-script.js`](https://github.com/Antgst/holbertonschool-higher_level_programming/blob/main/javascript-dom_manipulation/8-script.js)

**Repository:** `holbertonschool-higher_level_programming`

**Directory:** `javascript-dom_manipulation`

**Task details:**

```text
8. Say Hello!
Write a JavaScript script that fetches from
https://hellosalut.stefanbohacek.com/?lang=fr
and displays the value of
hello
from that fetch in the HTML element with id
hello
.
The translation of â€œhelloâ€ must be displayed in the HTML element with id
hello
Your script must work when it is imported from the
<head>
tag
Please test with this HTML file in your browser:
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 8-main.html
<!DOCTYPE
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
Holberton School
</
title
>
<
script
type
=
"text/javascript"
src
=
"8-script.js"
>
</
script
>
</
head
>
<
body
>
<
header
>
Say Hello!
</
header
>
<
br
/>
<
div
id
=
"hello"
>
</
div
>
<
br
/>
<
footer
>
Holberton School - 2022
</
footer
>
</
body
>
</
html
>
javiercito@ubuntu:~/javascript-dom_manipulation$
Repo:
GitHub repository:
holbertonschool-higher_level_programming
Directory:
javascript-dom_manipulation
File:
8-script.js
Score of the task
5
/5
pts
100.0%
0
correction requests
QA Review
Ã—
8. Say Hello!
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
Students who are done with "8. Say Hello!"
```

</details>


---

## ðŸ§ª Testing

Use the provided task examples and Holberton checker to validate the project.

---

## ðŸ‘¤ Author

Project from Holberton School.

README generated with Antoine's README Factory workflow.
