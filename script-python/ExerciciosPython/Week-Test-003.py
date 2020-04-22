#!/usr/bin/env python

"""
   @script: Car Rental
  @purpose: Lucas Car Rental app
  @created: Apr 16, 2020
   @author: Lucas Saporetti
   @mailto: lucassaporetti@gmail.com
"""

from os import path
from car_rental_system import *
from car_rental_system.tools import *
from time import sleep
from random import randint
from datetime import datetime

USAGE = 'Usage: python '


class LocalDB:
    car_db_file = 'car_stock.dat'
    user_db_file = 'user_list.dat'
    customer_db_file = 'customer_list.dat'
    employee_db_file = 'employee_list.dat'
    id_db_file = 'valid_id_list.dat'
    all_rental_history = 'rental_history.dat'
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
        self.all_rentals_list = FileUtils.create(self.all_rental_history) \
            if not path.exists(self.all_rental_history) else FileUtils.read(self.all_rental_history)
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
        FileUtils.save(LocalDB.all_rental_history, self.all_rentals_list)

    def save_pending(self):
        FileUtils.save(LocalDB.pending_db_file, self.pending_list)


def main_menu():
    print(f'\033[1J\033[H\n{Colors.purple}@ Lucas Rent a Car v0.9.0{Colors.clean}')
    PrintUtils.print_title('** Changes are automatically saved')
    menu_options = {'Exit': [0], 'Add Car Model': [1], 'Add User': [2], 'Rent a car': [3],
                    'Return a car': [4], 'Settle pending payments(TO DO...)': [5], 'Listing': [6]}
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


def listing_menu():
    PrintUtils.print_title('LISTING MENU')
    menu_options = {'Employees': '[A]', 'Customers': '[B]', 'Car models': '[C]', 'Rentals': '[D]',
                    'Pending Rents': '[E]', 'Main Menu': '[F]'}
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


def test_availability_cars(situation):
    if len(db.cars_list) != 0:
        result = False
        while result is False:
            for a_car in db.cars_list:
                if a_car['situation'] == situation:
                    result = True
                    return result
            if result is False:
                return result
    else:
        PrintUtils.print_error('There are no cars added in stock.')


def search_item(class_name, class_list, item_search):
    results = False
    while results is False:
        name_search = input(f'Press enter to see all {class_name}s or search a {class_name} by '
                            f'{item_search.replace("_", " ")}: ').strip().upper()
        for item in class_list:
            if name_search in item[item_search].strip().upper():
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
    ret_val = validate_character('Confirm payment? [Y/N] ')
    if ret_val == 'N':
        new_rent.__dict__['pending_payment'] = new_rent.__dict__['total_price']
        for item in db.customers_list:
            if new_rent.__dict__['customer_id'] == item['id_number']:
                item['pending_payment'] = new_rent.__dict__['total_price']
                item['total_rents'] = item['total_rents'] + 1
                new_rent.__dict__['customer_sign'] = item['name']
        db.save_customers()
        return ret_val
    if ret_val == 'Y':
        new_rent.__dict__['pending_payment'] = 0
        for item in db.customers_list:
            if new_rent.__dict__['customer_id'] == item['id_number']:
                item['pending_payment'] = 0
                item['total_rents'] = item['total_rents'] + 1
                new_rent.__dict__['customer_sign'] = item['name']
        db.save_customers()
        return ret_val


def block_by_pending():
    block = False
    total_pending = ''
    search_customer_id = find_user_id('Customer', db.customers_list, 2)
    for a_customer in db.customers_list:
        if search_customer_id == a_customer['id_number']:
            if a_customer['pending_payment'] != 0:
                block = True
                total_pending = a_customer['pending_payment']
    if block is True:
        print(f'{Colors.red}Attention! This customer has a pending amount of '
              f'{total_pending} in the system{Colors.clean}')
        return block
    if block is False:
        return search_customer_id


def choose_car(status):
    for item in db.cars_list:
        if item['situation'] == status:
            print(PrintUtils.colored_line(Colors.blue))
            for key, value in item.items():
                print(f'{Colors.cyan}{key.title().replace("_", " ").replace("A C", "A/C")}{Colors.clean}:{value}')
            print(PrintUtils.colored_line(Colors.blue))
    result = False
    while result is False:
        car_search = read_str(f'Enter a license plate from stock to select the car: ', 7, 7).strip().upper()
        for item in db.cars_list:
            if car_search == item['plate'].upper().strip() and item['situation'] == status:
                return car_search
        if result is False:
            PrintUtils.print_error('The characters entered do not correspond to an available license plate.')


def calc_total_days_price():
    y = int(new_rent.__dict__['check_out_date'][0:4])
    m = int(new_rent.__dict__['check_out_date'][5:7])
    d = int(new_rent.__dict__['check_out_date'][8:10])
    date_result = datetime(y, m, d)
    calc_date = date_result - datetime.now()
    total_days = calc_date.days + 1
    total_price = 0
    for a_car in db.cars_list:
        if new_rent.__dict__['selected_car'] == a_car['plate'].strip().upper():
            total_price = float(a_car['price'].replace('$', '')) * total_days
            new_rent.__dict__['price_per_day'] = a_car['price']
    print(f'\nTotal days: {total_days}\nTotal price: ${total_price:.2f}\n')
    new_rent.__dict__['check_in_date'] = str(datetime.now().isoformat(' ', 'seconds'))
    new_rent.__dict__['total_days'] = total_days
    new_rent.__dict__['total_price'] = f'${total_price:.2f}'


def complete_rent():
    for unit_car in db.cars_list:
        if unit_car['plate'].upper().strip() == new_rent.__dict__['selected_car'].upper().strip():
            unit_car['situation'] = 'Rent'
            unit_car['rented_by'] = new_rent.__dict__['customer_id']


def return_rent():
    result = True
    for rent in db.pending_list:
        if rent['selected_car'] == selected_car.strip().upper():
            PrintUtils.print_title('SELECTED RENTAL REGISTRATION')
            print(PrintUtils.colored_line(Colors.blue))
            for key, value in rent.items():
                print(f'{Colors.cyan}{key.title().replace("_", " ")}{Colors.clean}:{value}')
            print(PrintUtils.colored_line(Colors.blue))
            return_date = read_date('\nEnter the return date: ')
            y = int(return_date[0:4])
            m = int(return_date[5:7])
            d = int(return_date[8:10])
            date_return_result = datetime(y, m, d)
            y2 = int(rent['check_out_date'][0:4])
            m2 = int(rent['check_out_date'][5:7])
            d2 = int(rent['check_out_date'][8:10])
            check_out_result = datetime(y2, m2, d2)
            calc_date = date_return_result - check_out_result
            total_days = calc_date.days
            if rent['pending_payment'] != 0:
                previous_pending = rent['pending_payment'].replace('$', '')
            else:
                previous_pending = 0
            if total_days == 0 and previous_pending == 0:
                for a_car in db.cars_list:
                    if rent['selected_car'] == a_car['plate']:
                        del a_car['rented_by']
                        a_car['situation'] = 'Free'
                        db.save_cars()
                        db.all_rentals_list.append(rent)
                        db.save_rent()
                        db.pending_list.remove(rent)
                        db.save_pending()
                        return result
            elif total_days == 0 and float(previous_pending) > 0:
                print(f'The total value of the return pending is ${previous_pending}')
                ret_val = validate_character('Confirm payment?: [Y/N] ')
                for a_car in db.cars_list:
                    if rent['selected_car'] == a_car['plate']:
                        del a_car['rented_by']
                        a_car['situation'] = 'Free'
                        db.save_cars()
                if ret_val == 'Y':
                    for a_customer in db.customers_list:
                        if rent['customer_id'] == a_customer['id_number']:
                            a_customer['pending_payment'] = 0
                            db.save_customers()
                            db.all_rentals_list.append(rent)
                            db.save_rent()
                            db.pending_list.remove(rent)
                            db.save_pending()
                            return result
                if ret_val == 'N':
                    db.all_rentals_list.append(rent)
                    db.save_rent()
                    return result
            elif total_days < 0:
                if previous_pending == 0:
                    for a_car in db.cars_list:
                        if rent['selected_car'] == a_car['plate']:
                            del a_car['rented_by']
                            a_car['situation'] = 'Free'
                            db.save_cars()
                            db.all_rentals_list.append(rent)
                            db.save_rent()
                            db.pending_list.remove(rent)
                            db.save_pending()
                            return result
                else:
                    print(f'The total value of the return pending is ${previous_pending}')
                ret_val = validate_character('Confirm payment?: [Y/N] ')
                for a_car in db.cars_list:
                    if rent['selected_car'] == a_car['plate']:
                        del a_car['rented_by']
                        a_car['situation'] = 'Free'
                        db.save_cars()
                if ret_val == 'Y':
                    for a_customer in db.customers_list:
                        if rent['customer_id'] == a_customer['id_number']:
                            a_customer['pending_payment'] = 0
                            db.save_customers()
                            db.all_rentals_list.append(rent)
                            db.save_rent()
                            db.pending_list.remove(rent)
                            db.save_pending()
                            return result
                if ret_val == 'N':
                    db.all_rentals_list.append(rent)
                    db.save_rent()
                    return result
            elif total_days > 0:
                price_per_day = rent['price_per_day'].replace('$', '')
                first_total_price = rent['total_price'].replace('$', '')
                total_price = float(previous_pending) + (total_days * float(price_per_day))
                print(f'The total value of the return pending is ${total_price}')
                ret_val = validate_character('Confirm payment?: [Y/N] ')
                for a_car in db.cars_list:
                    if rent['selected_car'] == a_car['plate']:
                        del a_car['rented_by']
                        a_car['situation'] = 'Free'
                        db.save_cars()
                if ret_val == 'Y':
                    for a_customer in db.customers_list:
                        if rent['customer_id'] == a_customer['id_number']:
                            a_customer['pending_payment'] = 0
                            db.save_customers()
                            rent['check_out_date'] = return_date
                            rent['total_days'] = rent['total_days'] + total_days
                            if rent['pending_payment'] != 0:
                                rent['total_price'] = f'${total_price}'
                            elif rent['pending_payment'] == 0:
                                rent['total_price'] = f'${float(first_total_price) + total_price}'
                            rent['pending_payment'] = 0
                            db.all_rentals_list.append(rent)
                            db.save_rent()
                            db.pending_list.remove(rent)
                            db.save_pending()
                            return result
                if ret_val == 'N':
                    rent['check_out_date'] = return_date
                    rent['total_days'] = rent['total_days'] + total_days
                    if rent['pending_payment'] != 0:
                        rent['total_price'] = f'${total_price}'
                    elif rent['pending_payment'] == 0:
                        rent['total_price'] = f'${float(first_total_price) + total_price}'
                    rent['pending_payment'] = f'${total_price}'
                    db.all_rentals_list.append(rent)
                    db.save_rent()
                    db.save_pending()
                    for a_customer in db.customers_list:
                        if rent['customer_id'] == a_customer['id_number']:
                            a_customer['pending_payment'] = f'${total_price}'
                            db.save_customers()
                            return result


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
                          read_float('Price / Day: $'), read_str('Plate: ', 7, 7).upper(),
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
        if test_availability_cars('Free') is False:
            PrintUtils.print_error('No availability. All cars are rented.')
        elif len(db.employees_list) == 0:
            PrintUtils.print_error('There are no employees added to the system.')
        elif len(db.customers_list) == 0:
            PrintUtils.print_error('There are no customers added to the system.')
        else:
            clear_screen()
            PrintUtils.print_title('RENT A CAR')
            search_item('Customer', db.customers_list, 'name')

            print(PrintUtils.colored_line(Colors.blue))
            print(f'{Colors.white}To start a rental record, please enter with the Customer ID{Colors.clean}')
            print(PrintUtils.colored_line(Colors.blue))

            financial_tester = block_by_pending()

            if financial_tester is True:
                proceed = input('\nPress enter to proceed to the main menu...')
            else:
                new_rent = rental.Rental(financial_tester, choose_car('Free'), read_date('Check out date: '),
                                         find_user_id('Employee', db.employees_list, 1))

                print('Calculating total price...')
                sleep(0.3)

                calc_total_days_price()
                create_pending()
                complete_rent()
                db.pending_list.append(new_rent.__dict__)
                db.save_pending()
                db.save_cars()

                print(new_rent)
                PrintUtils.print_title(f'{Colors.yellow}New rental successfully completed!{Colors.clean}')
                proceed = input('\nPress enter to proceed to the main menu...')

    elif op == 4:
        if test_availability_cars('Rent') is False:
            PrintUtils.print_error('No cars are rented')
        elif len(db.employees_list) == 0:
            PrintUtils.print_error('There are no employees added to the system.')
        elif len(db.customers_list) == 0:
            PrintUtils.print_error('There are no customers added to the system.')
        else:
            clear_screen()
            PrintUtils.print_title('RETURN A CAR TO STOCK')

            print(PrintUtils.colored_line(Colors.blue))
            print(f'{Colors.white}Which car do you want to return?{Colors.clean}')
            print(PrintUtils.colored_line(Colors.blue))

            selected_car = choose_car('Rent')

            return_rent()

            PrintUtils.print_title(f'{Colors.yellow}Car return successfully completed!{Colors.clean}')
            proceed = input('\nPress enter to proceed to the main menu...')

    elif op == 5:
        PrintUtils.print_title('TO DO...')

    elif op == 6:
        clear_screen()
        listing_menu()
        user_op = validate_listing_op(f'{Colors.yellow}Your Option: {Colors.clean}')

        if user_op == 'A':
            if len(db.employees_list) == 0:
                PrintUtils.print_error('There are no employees added to the system.')
            else:
                previous_menu = 'Y'
                while previous_menu == 'Y':
                    clear_screen()
                    PrintUtils.print_title('EMPLOYEES LIST')
                    search_item('Employee', db.employees_list, 'name')
                    previous_menu = \
                        validate_character('Type "Y" for new search or "N" to return to Main Menu: ')

        elif user_op == 'B':
            if len(db.customers_list) == 0:
                PrintUtils.print_error('There are no customers added to the system.')
            else:
                previous_menu = 'Y'
                while previous_menu == 'Y':
                    clear_screen()
                    PrintUtils.print_title('CUSTOMERS LIST')
                    search_item('Customer', db.customers_list, 'name')
                    previous_menu = \
                        validate_character('Type "Y" for new search or "N" to return to Main Menu: ')

        elif user_op == 'C':
            if len(db.cars_list) == 0:
                PrintUtils.print_error('There are no cars added in stock.')
            else:
                previous_menu = 'Y'
                while previous_menu == 'Y':
                    clear_screen()
                    PrintUtils.print_title('CARS LIST')
                    search_item('Car', db.cars_list, 'name')
                    previous_menu = \
                        validate_character('Type "Y" for new search or "N" to return to the Main Menu: ')

        elif user_op == 'D':
            if len(db.all_rentals_list) == 0:
                PrintUtils.print_error('There is no rental history in the system.')
            else:
                previous_menu = 'Y'
                while previous_menu == 'Y':
                    clear_screen()
                    PrintUtils.print_title('ALL RENTAL HISTORY LIST')
                    search_item('Rent', db.all_rentals_list, 'customer_sign')
                    previous_menu = \
                        validate_character('Type "Y" for new search or "N" to return to Main Menu: ')

        elif user_op == 'E':
            if len(db.pending_list) == 0:
                PrintUtils.print_error('There is no pending rent in the system.')
            else:
                previous_menu = 'Y'
                while previous_menu == 'Y':
                    clear_screen()
                    PrintUtils.print_title('RENTAL PENDING LIST')
                    search_item('Pending', db.pending_list, 'customer_sign')
                    previous_menu = \
                        validate_character('Type "Y" for new search or "N" to return to Main Menu: ')
        else:
            continue
