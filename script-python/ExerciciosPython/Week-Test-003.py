#!/usr/bin/env python

"""
   @script: Bookstore
  @purpose: Lucas Car Rental app
  @created: Apr 16, 2020
   @author: Lucas Saporetti
   @mailto: lucassaporetti@gmail.com
"""

import sys
import os
from car_rental_system import tools
from car_rental_system import car
from time import sleep

CAR_RENTAL = 'car_rental.txt'
CAR_STOCK = 'car_stock.txt'

USAGE = f'Usage: python {CAR_RENTAL}'

colors_dict = {'clean': '\033[m', 'white': '\033[30m', 'red': '\033[31m',
               'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
               'purple': '\033[35m', 'cyan': '\033[36m'}


def main_menu():
    print(f'\033[1J\033[H\n{colors_dict["purple"]}@ Lucas Rent a Car v0.9.0{colors_dict["clean"]}')
    tools.title('** Changes are automatically saved')
    menu_options = {'Exit': [0], 'Add Car Model': [1], 'Add User': [2],
                    'Rent a car': [3], 'Return a car': [4], 'Car information': [5], 'Listing': [6]}
    for key, value in menu_options.items():
        print(f'{colors_dict["blue"]}{value}{colors_dict["clean"]} - '
              f'{colors_dict["cyan"]}{key}{colors_dict["clean"]}')
    tools.line()


CARS = []

op = None

while True:
    main_menu()
    op = tools.validate('\033[33mYour Option: \033[m')

    if op == 0:
        print('\nShutting down the system', end='')
        sleep(0.5), print('.', end=''), sleep(0.5),
        print('.', end=''), sleep(0.5), print('.', end='')
        sleep(0.5), print(' See you later!')
        break

    elif op == 1:
        tools.title('NEW CAR REGISTRATION')
        new_car = car.Car(str(input('Name: ')), tools.read_int('Year: '),
                          str(input('Category: ')), str(input('Color: ')),
                          str(input('A/C: [Y/N] ')), str(input('Gear Box: ')),
                          str(input('Fuel: ')), tools.read_int('Doors: '),
                          tools.read_int('Passangers: '), tools.read_int('Suitcase: '),
                          tools.read_float('Price / Day: $'), str(input('Plate: ')),
                          str(input('Chassis: ')))
        car.Car.add_new_car(new_car)

        print(new_car)
