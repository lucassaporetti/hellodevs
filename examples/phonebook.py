#!/usr/bin/env python

import sys
import os
import ast

PROGRAM = os.path.basename(__file__).upper()

MAIN_MENU = f"""
{PROGRAM} LUCAS PERSONAL CONTACTS

(1) ADD
(2) REMOVE
(3) EDIT
(4) LIST
(5) SAVE
(6) LOAD
(7) EXPORT JSON
(8) IMPORT JSON
(0) EXIT
"""

PHONEBOOK = 'phonebook.txt'
CONTACTS = []
op = None

while op != '0':

    os.system('cls')
    new_contact = {"name": None, "age": None, "address": None, "phone": None}
    print(MAIN_MENU)
    op = input('Your Option$ ')

    if op == '1':
        new_contact['name'] = input('What\'s your name? ')
        new_contact['age'] = input('What\'s your age? ')
        new_contact['address'] = input('What\'s your address? ')
        new_contact['phone'] = input('What\'s your phone? ')
        CONTACTS.append(new_contact.copy())
        print('Contact added ' + str(new_contact))
    elif op == '2':
        name = input('Remove who? ')
        found = [c for c in CONTACTS if name != c['name']]
        if len(found) != len(CONTACTS):
            CONTACTS = found
            print('Contact removed ' + name)
        else:
            print(f'Contact {name} not found')
    elif op == '3':
        name = input('Edit who? ')
        found = [c for c in CONTACTS if name == c['name']]
        if len(found) > 0:
            new_contact = found[0]
            new_contact['name'] = input('New name? ')
            new_contact['age'] = input('New age? ')
            new_contact['address'] = input('New address? ')
            new_contact['phone'] = input('New phone? ')
            print('Contact updated ' + str(new_contact))
        else:
            print(f'Contact {name} not found')
    elif op == '4':
        print(CONTACTS)
    elif op == '5':
        with open(PHONEBOOK, 'w') as f_phonebook:
            f_phonebook.write(str(CONTACTS))
            print(f'{len(CONTACTS)} contacts saved !')
    elif op == '6':
        if os.path.exists(PHONEBOOK):
            with open(PHONEBOOK, 'r') as f_phonebook:
                data = f_phonebook.read()
                CONTACTS = ast.literal_eval(data)
                print(f'{len(CONTACTS)} contacts loaded !')

    elif op == '0':
        sys.exit(0)
    else:
        print('# Invalid option ' + op)

    input('\n\nPress enter to continue\n')
    os.system('cls')
    op = None

input('\n\nPress enter to continue\n')
