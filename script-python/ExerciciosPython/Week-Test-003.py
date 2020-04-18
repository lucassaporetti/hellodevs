#!/usr/bin/env python

"""
   @script: Car Rental
  @purpose: Lucas Car Rental app
  @created: Apr 16, 2020
   @author: Lucas Saporetti
   @mailto: lucassaporetti@gmail.com
"""

import sys
import os
from car_rental_system import tools, car, user, employee, customer, rental
from time import sleep
from random import randint
import ast

CAR_DB_OUTFILE = 'car_stock.dat'
USER_DB_OUTFILE = 'user_list.dat'
CUSTOMER_DB_OUTFILE = 'customer_list.dat'
EMPLOYEE_DB_OUTFILE = 'employee_list.dat'
CAR_RENTAL = 'car_rental.dat'

USAGE = f'Usage: python {CAR_RENTAL}'

colors_dict = {'clean': '\033[m', 'white': '\033[30m', 'red': '\033[31m',
               'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
               'purple': '\033[35m', 'cyan': '\033[36m'}


def check_db_files():
    car_db_exists = os.path.exists(CAR_DB_OUTFILE)
    open(CAR_DB_OUTFILE, 'w').close() if not car_db_exists else None
    customer_db_exists = os.path.exists(CUSTOMER_DB_OUTFILE)
    open(CUSTOMER_DB_OUTFILE, 'w').close() if not customer_db_exists else None
    employee_db_exists = os.path.exists(EMPLOYEE_DB_OUTFILE)
    open(EMPLOYEE_DB_OUTFILE, 'w').close() if not employee_db_exists else None


def main_menu():
    print(f'\033[1J\033[H\n{colors_dict["purple"]}@ Lucas Rent a Car v0.9.0{colors_dict["clean"]}')
    tools.title('** Changes are automatically saved')
    menu_options = {'Exit': [0], 'Add Car Model': [1], 'Add User': [2],
                    'Rent a car': [3], 'Return a car': [4], 'Car information': [5], 'Listing': [6]}
    for key, value in menu_options.items():
        print(f'{colors_dict["blue"]}{value}{colors_dict["clean"]} - '
              f'{colors_dict["cyan"]}{key}{colors_dict["clean"]}')
    tools.line()


def add_user_menu():
    tools.title('NEW USER REGISTRATION')
    menu_options = {'Employee': '[A]', 'Customer': '[B]', 'Previous Menu': '[C]'}
    for key, value in menu_options.items():
        print(f'{colors_dict["blue"]}{value}{colors_dict["clean"]} - '
              f'{colors_dict["cyan"]}{key}{colors_dict["clean"]}')
    tools.line()


def find_id():
    ret_val = None
    with open("customer_list.dat", "r") as file:
        contents = file.read()
        customers = ast.literal_eval(contents)
    while ret_val is None:
        ret_val = tools.read_int('Customer ID: ', 2)
        for next_customer in customers:
            if ret_val == next_customer['id_number']:
                break
            else:
                ret_val = None
                continue
        if ret_val is None:
            tools.print_error('Customer ID not found!')


CARS = []

op = None
check_db_files()

while True:
    os.system('cls')
    main_menu()
    op = tools.validate(f'{colors_dict["yellow"]}Your Option: {colors_dict["clean"]}')

    if op == 0:
        print('\nShutting down the system', end='')
        sleep(0.5), print('.', end=''), sleep(0.5),
        print('.', end=''), sleep(0.5), print('.', end='')
        sleep(0.5), print(' See you later!')
        break

    elif op == 1:
        os.system('cls')
        print()
        tools.title('NEW CAR REGISTRATION')
        new_car = car.Car(tools.read_str('Name: ', 1, 50), tools.read_int('Year: ', 4),
                          tools.read_str('Category: ', 1, 15), tools.read_str('Color: ', 1, 15),
                          tools.read_y_n('A/C: [Y/N] '), tools.read_str('Gear Box: ', 1, 10),
                          tools.read_str('Fuel: ', 1, 10), tools.read_int('Doors: ', 1),
                          tools.read_int('Passengers: ', 1), tools.read_int('Suitcase: ', 1),
                          tools.read_float('Price / Day: $'), tools.read_str('Plate: ', 7, 7),
                          tools.read_str('Chassis: ', 17, 17))
        car.Car.add_new_car(new_car)

        print(new_car)
        proceed = input('\nPress enter to proceed to the main menu...')

    elif op == 2:
        os.system('cls')
        print()
        add_user_menu()
        user_op = tools.validate_user(f'{colors_dict["yellow"]}Your Option: {colors_dict["clean"]}')

        if user_op == 'A':
            new_user = employee.Employee(tools.read_str('Name: ', 1, 50), tools.read_age('Age: '),
                                         tools.read_str('Address: ', 10, 100), tools.read_int('Phone: ', 11),
                                         tools.read_str('Email: ', 1, 50), tools.read_str('Access Type: ', 1, 30),
                                         tools.read_date('Hired Date: '), tools.read_float('Salary: $'),
                                         randint(1, 100))

            employee.Employee.add_new_employee(new_user)
            user.User.add_new_user(new_user)
            print(new_user)

        elif user_op == 'B':
            new_user = customer.Customer(tools.read_str('Name: ', 1, 50), tools.read_age('Age: '),
                                         tools.read_str('Address: ', 10, 100), tools.read_int('Phone: ', 11),
                                         tools.read_str('Email: ', 1, 50), tools.read_str('Driver License: ', 1, 30),
                                         tools.read_int('Rentals: ', 1), randint(1, 100))
            customer.Customer.add_new_customer(new_user)
            user.User.add_new_user(new_user)
            print(new_user)

        else:
            continue

        proceed = input('\nPress enter to proceed to the main menu...')

    elif op == 3:
        os.system('cls')
        print()
        tools.title('RENT A CAR')
        new_rent = rental.Rental(find_id(), tools.read_date('Check Out Date: '),
                                 tools.read_float('Price: $'), 'Pending Payment: NO',
                                 tools.read_int('Attendant ID: ', 10))
        rental.Rental.add_new_rent(new_rent)

        print(new_rent)
        proceed = input('\nPress enter to proceed to the main menu...')
