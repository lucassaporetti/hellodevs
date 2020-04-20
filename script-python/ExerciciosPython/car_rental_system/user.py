from car_rental_system.tools import *


class User:
    USER_DB_OUTFILE = 'user_list.dat'

    USER_STR_FMT = '{}{}{}'.format(
        PrintUtils.colored_line(Colors.blue),
        '{}',
        PrintUtils.colored_line(Colors.blue, end=''))

    def __init__(self, name, age, address, phone, email):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.email = email

    @staticmethod
    def to_label(key):
        label = str(key).title().replace('_', ' ').replace('Drv', 'Driver')
        return label

    def __str__(self):
        str_val = ''

        for key, value in self.__dict__.items():
            str_val += f'{Colors.cyan}{User.to_label(key)}{Colors.clean}:{value}\n'
        return User.USER_STR_FMT.format(str_val)
