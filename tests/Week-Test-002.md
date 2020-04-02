# Friday 03/04/2020 HomeWork

## Bookstore

### Description

Create a bookstore app following the requirements below:

##### General

- EnglishOnly: The program must not contain any non english words for any purposes.
- Pylint: Follow all pylint rules.

#### Allowed operations

* [0] Exit.
* [1] Add Book.
* [2] Remove Book.
* [3] Edit Book.
* [4] List Books.
* [5] Search Book.

#### Visualisation

There must have a menu like the following:

##### Main Menu

```
@ Lucas Bookstore v0.9.0
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
** Changes are automatically saved
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
[0] Exit.
[1] Add Book.
[2] Remove Book.
[3] List Books.
[4] Search Book.

$ <op>
```

##### Add Book

```
    Index: <Unique index on the bookshelf up to 4-digits>
Book Name: <up to 30 letters or numbers>
   Author: <up to 60 letters or numbers>
Published: <publication date with the format `dd/mm/YYYY'>
    Pages: <integer from 1..1000>
```

##### Remove Book

```
Book index: <Unique index on the bookshelf up to 4-digits>

Confirm removal of book <Index> (y/[n])?
```

##### List Books

```
Listing all (<number_of_books>) available book(s):

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
001 <TAB><TAB> { index: <book_index>, name: <book_name>, author: <author>, published: <date>, pages: <num_of_pages> }
002 <TAB><TAB> { index: <book_index>, name: <book_name>, author: <author>, published: <date>, pages: <num_of_pages> }
...
...
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
```

If there are no books yet stored, the following message should be displayed:

`
-=- There are no books stored yet -=-
`

##### Search Books

This menu item is optional. That's my challenge for you.

If there are no books that matches the criteria, the following message should be displayed:

```
Author: <up to 60 letters or numbers>

-=- Did not find any books for that search -=-
```

Otherwise``

```
Name or Author: <up to 60 letters or numbers>

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
001 <TAB><TAB> { index: <book_index>, name: <book_name>, author: <author>, published: <date>, pages: <num_of_pages> }
002 <TAB><TAB> { index: <book_index>, name: <book_name>, author: <author>, published: <date>, pages: <num_of_pages> }
...
...
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
```

##### PLUS-Extra-Challenge:

1. All Add/Remove/Edit data would be persisted.
1. After every time the program exists (0 pressed), the data is saved automatically.
2. When the program starts, old file data is loaded if the file exists.

#### Non-Functional requirements:

    1. There should be a loop clearing the screen every time before displaying the menu.
    2. The app should handle pressing letters instead of numbers.
    3. The app should handle invalid operations **NOT IN** the menu options.
    4. The app should handle invalid the limits of digits/characters specified.
    5. The app should handle invalid indexes using the messages (index <XX> not found).
    6. The app should handle other errors that you find out.
    7. You must use the application template specified below


#### Application template:

```python
#!/usr/bin/env python

"""
   @script: <script name>
  @purpose: Provide a bookstore app
  @created: Mon DD, YYYY
   @author: <author>
   @mailto: <email>
"""

import sys
import os

# This application name.
APP_NAME = os.path.basename(__file__)

# Current application version; tuple: (major, minor, build).
VERSION = (0, 9, 0)

# Help message to be displayed by the application.
USAGE = f"""
Usage: python {APP_NAME}
"""

# The main menu.
MAIN_MENU = f"""\033[1J\033[H
@ Lucas Bookstore v{'.'.join(VERSION)}
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
** Changes are automatically saved
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
[0] Exit
[1] Add Book
[2] Remove Book
[3] Edit Book
[4] List Books
[5] Search Book

[Add]"""

# Allowed menu options.
MENU_OPTIONS = ['0', '1', '2', '3', '4', '5']

# The file name of the bookstore.
BOOKSTORE = 'bookstore.dat'

# Hold all the stored books.
BOOKS = []

# The menu option selected by the user.
op = None

# New book is a dictionary object and must have the following fields:
#   new_contact = { "index": None, "name": None, "author": None, "published": None, "pages": None }

# ...Your code goes here...

sys.exit(0)
```
