from car_rental_system import user
from car_rental_system.tools import *


class Customer(user.User):
    CUSTOMER_STR_FMT = '{}{}{}'.format(
        PrintUtils.colored_line(Colors.blue),
        '{}',
        PrintUtils.colored_line(Colors.blue, end=''))

    def __init__(self, name, age, address, phone, email, drv_license, id_number):
        super().__init__(name, age, address, phone, email)
        self.drv_license = drv_license
        self.id_number = id_number

    @staticmethod
    def to_label(key):
        label = str(key).title().replace('_', ' ').replace('Drv', 'Driver')
        return label

    def __str__(self):
        str_val = ''

        for key, value in self.__dict__.items():
            str_val += f'{Colors.cyan}{Customer.to_label(key)}{Colors.clean}:{value}\n'
        return Customer.CUSTOMER_STR_FMT.format(str_val)
