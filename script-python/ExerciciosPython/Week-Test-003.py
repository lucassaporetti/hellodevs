#!/usr/bin/env python

"""
   @script: Car Rental
  @purpose: Lucas Car Rental app
  @created: Apr 16, 2020
   @author: Lucas Saporetti
   @mailto: lucassaporetti@gmail.com
"""

import sys
from os import path
from car_rental_system import *
from car_rental_system.tools import *
from time import sleep
from random import randint

USAGE = 'Usage: python '


class LocalDB:
    car_db_file = 'car_stock.dat'
    user_db_file = 'user_list.dat'
    customer_db_file = 'customer_list.dat'
    employee_db_file = 'employee_list.dat'
    id_db_file = 'valid_id_list.dat'
    rent_db_file = 'car_rental.dat'
    pending_db_file = 'pending_list.dat'

    def __init__(self):
        self.cars_list = FileUtils.create(self.car_db_file) \
            if not path.exists(self.car_db_file) else FileUtils.read(self.car_db_file)
        self.users_list = FileUtils.create(self.user_db_file) \
            if not path.exists(self.user_db_file) else FileUtils.read(self.user_db_file)
        self.employees_list = FileUtils.create(self.employee_db_file) \
            if not path.exists(self.employee_db_file) else FileUtils.read(self.employee_db_file)
        self.customers_list = FileUtils.create(self.customer_db_file) \
            if not path.exists(self.customer_db_file) else FileUtils.read(self.customer_db_file)
        self.id_list = FileUtils.create(self.id_db_file) \
            if not os.path.exists(self.id_db_file) else FileUtils.read(self.id_db_file)
        self.rent_list = FileUtils.create(self.rent_db_file) \
            if not path.exists(self.rent_db_file) else FileUtils.read(self.rent_db_file)
        self.pending_list = FileUtils.create(self.pending_db_file) \
            if not path.exists(self.pending_db_file) else FileUtils.read(self.pending_db_file)

    def save_cars(self):
        FileUtils.save(LocalDB.car_db_file, self.cars_list)

    def save_users(self):
        FileUtils.save(LocalDB.user_db_file, self.users_list)

    def save_employees(self):
        FileUtils.save(LocalDB.employee_db_file, self.employees_list)

    def save_customers(self):
        FileUtils.save(LocalDB.customer_db_file, self.customers_list)

    def save_id(self):
        FileUtils.save(LocalDB.id_db_file, self.id_list)

    def save_rent(self):
        FileUtils.save(LocalDB.rent_db_file, self.rent_list)

    def save_pending(self):
        FileUtils.save(LocalDB.pending_db_file, self.pending_list)


def main_menu():
    print(f'\033[1J\033[H\n{Colors.purple}@ Lucas Rent a Car v0.9.0{Colors.clean}')
    PrintUtils.print_title('** Changes are automatically saved')
    menu_options = {'Exit': [0], 'Add Car Model': [1], 'Add User': [2],
                    'Rent a car': [3], 'Return a car': [4], 'Car information': [5], 'Listing': [6]}
    for key, value in menu_options.items():
        print(f'{Colors.blue}{value}{Colors.clean} - '
              f'{Colors.cyan}{key}{Colors.clean}')
    PrintUtils.print_line()


def add_user_menu():
    PrintUtils.print_title('NEW USER REGISTRATION')
    menu_options = {'Employee': '[A]', 'Customer': '[B]', 'Previous Menu': '[C]'}
    for key, value in menu_options.items():
        print(f'{Colors.blue}{value}{Colors.clean} - '
              f'{Colors.cyan}{key}{Colors.clean}')
    PrintUtils.print_line()


def create_random_id(start_num, finish_num):
    ret_val = None
    while ret_val is None:
        ret_val = randint(start_num, finish_num)
        if len(db.id_list) == 0:
            return ret_val
        for next_id in db.id_list:
            if ret_val != next_id:
                return ret_val
        ret_val = None


def find_user_id(class_name, class_list, max_val):
    ret_val = None
    while ret_val is None:
        ret_val = read_int(f'{class_name} ID: ', max_val)
        for item in class_list:
            if ret_val == item['id_number']:
                return ret_val
        ret_val = None
        PrintUtils.print_error(f'{class_name} ID not found!')


def search_name(class_name, class_list):
    results = False
    while results is False:
        name_search = read_str(f'Search a {class_name} by name: ').strip().upper()
        for item in class_list:
            if name_search in item['name'].strip().upper():
                results = True
                print(PrintUtils.colored_line(Colors.blue))
                for key, value in item.items():
                    print(f'{Colors.cyan}{key.title().replace("_", " ")}{Colors.clean}:{value}')
                print(PrintUtils.colored_line(Colors.blue))
        if results is True:
            return results
        else:
            PrintUtils.print_error(f'No {class_name} found.')


def create_pending():
    ret_val = validate_character('Pending Payment: [Y/N] ')
    if ret_val == 'Y':
        db.pending_list.append(new_rent.__dict__)
        db.save_pending()
        for item in db.customers_list:
            if new_rent.__dict__['customer_id'] == item['id_number']:
                item['Pending Payment'] = new_rent.__dict__['price']
        db.save_customers()
        return ret_val


def block_by_pending():
    block = False
    total_pending = ''
    search_customer_id = find_user_id('Customer', db.customers_list, 2)
    for pending in db.pending_list:
        if search_customer_id == pending['customer_id']:
            block = True
            total_pending = pending["price"]
    if block is True:
        print(f'{Colors.red}Attention! This customer has a pending amount of '
              f'{total_pending} in the system{Colors.clean}')
        return block
    if block is False:
        return search_customer_id

#
# def choose_car():
#     results = False
#     while results is False:
#         for item in db.cars_list:
#             if item['situation'] == 'Free':
#
#         car_search = read_str(f'Choose a car from stock: ').strip().upper()
#         for item in class_list:
#             if name_search in item['name'].strip().upper():
#                 results = True
#                 print(PrintUtils.colored_line(Colors.blue))
#                 for key, value in item.items():
#                     print(f'{Colors.cyan}{key.print_title().replace("_", " ")}{Colors.clean}:{value}')
#                 print(PrintUtils.colored_line(Colors.blue))
#         if results is True:
#             return results
#         else:
#             PrintUtils.print_error(f'No {class_name} found.')


db = LocalDB()
done = False
op = None


while not done:
    clear_screen()
    main_menu()
    op = validate_op(f'{Colors.yellow}Your Option: {Colors.clean}')

    if op == 0:
        print('\nShutting down the system', end='')
        sleep(0.5), print('.', end=''), sleep(0.5),
        print('.', end=''), sleep(0.5), print('.', end='')
        sleep(0.5), print(' See you later!')
        done = True

    elif op == 1:
        clear_screen()
        PrintUtils.print_title('NEW CAR REGISTRATION')
        new_car = car.Car(read_str('Name: ', 1, 50), read_int('Year: ', 4),
                          read_str('Category: ', 1, 15), read_str('Color: ', 1, 15),
                          validate_character('A/C: [Y/N] '), read_str('Gear Box: ', 1, 10),
                          read_str('Fuel: ', 1, 10), read_int('Doors: ', 1),
                          read_int('Passengers: ', 1), read_int('Suitcase: ', 1),
                          read_float('Price / Day: $'), read_str('Plate: ', 7, 7),
                          read_str('Chassis: ', 17, 17))
        db.cars_list.append(new_car.__dict__)
        db.save_cars()
        print(new_car)
        proceed = input('\nPress enter to proceed to the main menu...')

    elif op == 2:
        clear_screen()
        add_user_menu()
        user_op = validate_user_op(f'{Colors.yellow}Your Option: {Colors.clean}')

        if user_op == 'A':
            new_user = employee.Employee(read_str('Name: ', 1, 50), read_age('Age: '),
                                         read_str('Address: ', 10, 100), read_int('Phone: ', 11),
                                         read_str('Email: ', 1, 50), read_str('Access Type: ', 1, 30),
                                         read_date('Hired Date: '), read_float('Salary: $'),
                                         create_random_id(1, 9))
            db.users_list.append(new_user.__dict__)
            db.save_users()
            db.employees_list.append(new_user.__dict__)
            db.save_employees()
            db.id_list.append(new_user.__dict__['id_number'])
            db.save_id()
            print(new_user)
            proceed = input('\nPress enter to proceed to the main menu...')

        elif user_op == 'B':
            new_user = customer.Customer(read_str('Name: ', 1, 50), read_age('Age: '),
                                         read_str('Address: ', 10, 100), read_int('Phone: ', 11),
                                         read_str('Email: ', 1, 50), read_str('Driver License: ', 1, 30),
                                         create_random_id(10, 99))
            db.users_list.append(new_user.__dict__)
            db.save_users()
            db.customers_list.append(new_user.__dict__)
            db.save_customers()
            db.id_list.append(new_user.__dict__['id_number'])
            db.save_id()
            print(new_user)
            proceed = input('\nPress enter to proceed to the main menu...')
        else:
            continue

    elif op == 3:
        if len(db.cars_list) == 0:
            PrintUtils.print_error('There are no cars added in stock.')
        if len(db.employees_list) == 0:
            PrintUtils.print_error('There are no employees added to the system.')
        if len(db.customers_list) == 0:
            PrintUtils.print_error('There are no customers added to the system.')
        else:
            clear_screen()
            PrintUtils.print_title('RENT A CAR')
            search_name('Customer', db.customers_list)
            print(PrintUtils.colored_line(Colors.blue))
            print(f'{Colors.white}To start a rental record, please enter with the Customer ID{Colors.clean}')
            print(PrintUtils.colored_line(Colors.blue))
            financial_tester = block_by_pending()

            if financial_tester is True:
                proceed = input('\nPress enter to proceed to the main menu...')
            else:
                new_rent = rental.Rental(financial_tester, read_date('Check Out Date: '),
                                         read_float('Price: $'), find_user_id('Employee', db.employees_list, 1))
                create_pending()
                db.rent_list.append(new_rent.__dict__)
                db.save_rent()
                print(new_rent)
                PrintUtils.print_title(f'{Colors.yellow}New rental successfully completed!{Colors.clean}')
                proceed = input('\nPress enter to proceed to the main menu...')
    #
    # elif op == 4:
