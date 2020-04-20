from car_rental_system import user
from car_rental_system.tools import *


class Employee(user.User):
    EMPLOYEE_STR_FMT = '{}{}{}'.format(
        PrintUtils.colored_line(Colors.blue),
        '{}',
        PrintUtils.colored_line(Colors.blue, end=''))

    def __init__(self, name, age, address, phone, email, access_type, hired_date, salary, id_number):
        super().__init__(name, age, address, phone, email)
        self.access_type = access_type
        self.hired_date = hired_date
        self.salary = salary
        self.id_number = id_number

    @staticmethod
    def to_label(key):
        label = str(key).title().replace('_', ' ')
        return label

    def __str__(self):
        str_val = ''

        for key, value in self.__dict__.items():
            str_val += f'{Colors.cyan}{Employee.to_label(key)}{Colors.clean}:{value}\n'
        return Employee.EMPLOYEE_STR_FMT.format(str_val)
