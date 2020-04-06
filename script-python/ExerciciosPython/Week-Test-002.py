#!/usr/bin/env python

"""
   @script: Bookstore
  @purpose: Provide a bookstore app
  @created: Mar 03, 2020
   @author: Lucas Saporetti
   @mailto: lucassaporetti@gmail.com
"""

import sys
import os
import datetime
import ast

BOOKSTORE = os.path.basename(__file__)

USAGE = f"""
Usage: python {BOOKSTORE}
"""

MAIN_MENU = f"""\033[1J\033[H
@ Lucas Bookstore v0.9.0
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
** Changes are automatically saved
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
[0] Exit
[1] Add Book
[2] Remove Book
[3] Edit Book
[4] List Books
[5] Search Book"""

MENU_OPTIONS = ['0', '1', '2', '3', '4', '5']

BOOKSTORE = 'bookstore.dat'

BOOKS = []

op = None

if os.path.exists(BOOKSTORE):
    with open(BOOKSTORE, 'r') as f_bookstore:
        data = f_bookstore.read()
        BOOKS = ast.literal_eval(data)
        print(f'{len(BOOKS)} books loaded !')

while op != '0':

    os.system("cls")
    new_book = {"index": None, "book_name": None, "author": None, "published": None, "pages": None}
    print(MAIN_MENU)
    op = input('\n$ ')

    if op == '1':
        while True:
            try:
                new_book['index'] = int(input('Index: '))
            except ValueError as err:
                print('Index must be a number, please try again!')
                continue
            found = [book for book in BOOKS if new_book['index'] == book['index']]
            if len(found) > 0 and len(BOOKS) >= 1:
                print('This index number already exists. Please try again...')
            elif new_book['index'] > 9999:
                print('Index number must be up to 4 digits, please try again...')
            elif new_book['index'] == 0:
                print('Index number can\'t be [0]. Please try again...')
            else:
                break

        while True:
            new_book['book_name'] = input('Book name: ')

            if len(new_book['book_name']) > 31:
                print('Book name must be up to 30 characters, please try again...')
            else:
                break

        while True:
            new_book['author'] = input('Author: ')

            if len(new_book['author']) > 61:
                print('Author name must be up to 60 characters, please try again...')
            else:
                break

        while True:
            try:
                new_book['published'] = input('Published: [dd/mm/yyyy] ')
                date_format = '%d/%m/%Y'
                date_obj = datetime.datetime.strptime(new_book['published'], date_format)
            except ValueError:
                print("Incorrect data format, should be dd/mm/yyyy")
                continue
            else:
                break

        while True:
            try:
                new_book['pages'] = int(input('Pages: '))
            except ValueError as err:
                print('Pages must be a number, please try again...')
                continue
            if new_book['pages'] < 1 or new_book['pages'] > 1000:
                print('Number of pages must be between 1 and 1000, please try again...')
            else:
                break

        BOOKS.append(new_book.copy())

        print(f'\nBook {new_book} successfully added!')

    elif op == '2':
        if len(BOOKS) == 0:
            print('-=- There are no books stored yet -=-')
        else:
            index = 1
            while index != 0:
                try:
                    index = int(input('Enter a book index to remove: ["0" return to menu]  '))
                except ValueError as err:
                    print('Index must be a number, please try again...')
                    continue

                found = [book for book in BOOKS if index != book['index']]

                if len(found) != len(BOOKS):
                    confirm = input(f'Confirm removal of book {index}? [Y/N]? ').strip().upper()[0]
                    while confirm not in ['Y', 'N']:
                        confirm = input('Invalid character! Confirm removal of book {index} (y/[n])? ').strip().upper()[0]
                    if confirm == 'Y':
                        BOOKS = found
                        print(f'\nBook {index} successfully removed!\n')
                    if confirm == 'N':
                        continue
                else:
                    print(f'Book {index} not found')

    elif op == '3':
        if len(BOOKS) == 0:
            print('-=- There are no books stored yet -=-')
        else:
            index = 1
            while index != 0:
                try:
                    index = int(input('Enter a book index to edit: ["0" return to menu]  '))
                except ValueError as err:
                    print('Index must be a number, please try again...')
                    continue

                found = [book for book in BOOKS if index == book['index']]

                if len(found) > 0:
                    new_book = found[0]

                    # while True:
                    #     try:
                    #         new_book['index'] = int(input('New index: '))
                    #     except ValueError as err:
                    #         print('Index must be a number, please try again!')
                    #         continue
                    #
                    #     if new_book['index'] > 9999 or new_book['index'] == 0:
                    #         print('Index number can\'t be [0] and must be up to 4 digits, please try again...')
                    #     else:
                    #         break

                    while True:
                        new_book['book_name'] = input('New book name: ')

                        if len(new_book['book_name']) > 31:
                            print('Book name must be up to 30 characters, please try again...')
                        else:
                            break

                    while True:
                        new_book['author'] = input('New author: ')

                        if len(new_book['author']) > 61:
                            print('Author name must be up to 60 characters, please try again...')
                        else:
                            break

                    while True:
                        try:
                            new_book['published'] = input('New published: [dd/mm/yyyy] ')
                            date_format = '%d/%m/%Y'
                            date_obj = datetime.datetime.strptime(new_book['published'], date_format)
                        except ValueError:
                            print("Incorrect data format, should be dd/mm/yyyy")
                            continue
                        else:
                            break

                    while True:
                        try:
                            new_book['pages'] = int(input('New pages: '))
                        except ValueError as err:
                            print('Pages must be a number, please try again...')
                            continue
                        if new_book['pages'] < 1 or new_book['pages'] > 1000:
                            print('Number of pages must be between 1 and 1000, please try again...')
                        else:
                            break

                    print('\nBook updated! ' + str(new_book))
                else:
                    print(f'Book {index} not found')

    elif op == '4':

        if len(BOOKS) == 0:
            print('-=- There are no books stored yet -=-')

        else:
            print('-=' * 60)
            for book in BOOKS:
                print(f'00{BOOKS.index(book) + 1}       {book}')
            print('-=' * 60)

    elif op == '5':

        if len(BOOKS) == 0:
            print('-=- There are no books stored yet -=-')
        else:
            index = 1
            while index != 0:
                try:
                    index = int(input('Enter a book index to search: ["0" return to menu]  '))
                except ValueError as err:
                    print('Index must be a number, please try again...')
                    continue

                found = [book for book in BOOKS if index == book['index']]

                if len(found) > 0:
                    print(f'{len(found)} books found!\n')
                    print('-=' * 60)
                    for book in found:
                        print(f'00{found.index(book) + 1}       {found}')
                    print('-=' * 60)
                else:
                    print(f'Book {index} not found')

    elif op == '0':
        with open(BOOKSTORE, 'w') as f_bookstore:
            f_bookstore.write(str(BOOKS))
            print(f'{len(BOOKS)} books saved !')
        sys.exit(0)
    else:
        print('# Invalid option ' + op)

    input('\nPress enter to continue\n')

sys.exit(0)
