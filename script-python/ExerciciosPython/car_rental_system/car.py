from car_rental_system.tools import *


class Car:
    CAR_STR_FMT = '{}\n{}{}'.format(
        PrintUtils.colored_line(Colors.blue),
        '{}',
        PrintUtils.colored_line(Colors.blue, end=''))

    def __init__(self, name, year, category, color, a_c, gear_box, fuel, doors,
                 passengers, suitcase, price, plate, chassis):
        self.name = name
        self.year = year
        self.category = category
        self.color = color
        self.a_c = a_c
        self.gear_box = gear_box
        self.fuel = fuel
        self.doors = doors
        self.passengers = passengers
        self.suitcase = suitcase
        self.price = price
        self.plate = plate
        self.chassis = chassis
        self.situation = 'Free'

    @staticmethod
    def to_label(key):
        label = str(key).title().replace('_', ' ').replace('A C', 'A/C')
        return label

    def __str__(self):
        str_val = ''

        for key, value in self.__dict__.items():
            str_val += f'{Colors.cyan}{Car.to_label(key)}{Colors.clean}:{value}\n'
        return Car.CAR_STR_FMT.format(str_val)
