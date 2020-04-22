from car_rental_system.tools import *


class Rental:
    RENTAL_DB_OUTFILE = 'rental_list.dat'

    RENTAL_STR_FMT = '{}\n{}{}'.format(
        PrintUtils.colored_line(Colors.blue),
        '{}',
        PrintUtils.colored_line(Colors.blue, end=''))

    def __init__(self, customer_id, selected_car, check_out_date, attendant_id):
        self.customer_id = customer_id
        self.selected_car = selected_car
        self.check_out_date = check_out_date
        self.attendant = attendant_id

    @staticmethod
    def to_label(key):
        label = str(key).title().replace('_', ' ')
        return label

    def __str__(self):
        str_val = ''
        for key, value in self.__dict__.items():
            str_val += f'{Colors.cyan}{Rental.to_label(key)}{Colors.clean}:{value}\n'
        return Rental.RENTAL_STR_FMT.format(str_val)
