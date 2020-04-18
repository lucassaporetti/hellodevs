from car_rental_system import tools, user, customer, employee


class Rental:
    RENTAL_DB_OUTFILE = 'rental_list.dat'

    RENTAL_STR_FMT = '{}{}{}'.format(
        tools.colored_line(tools.colors_dict['blue']),
        '{}',
        tools.colored_line(tools.colors_dict['blue'], end='')
    )

    def __init__(self, customer_id, check_out_date, price, pending_payment, attendant_id):
        self.customer_id = customer_id
        self.check_out_date = check_out_date
        self.price = price
        self.pending_payment = pending_payment
        self.attendant = attendant_id

    @staticmethod
    def to_label(key):
        label = str(key).title().replace('_', ' ')
        return label

    def __str__(self):
        str_val = ''
        for key, value in self.__dict__.items():
            str_val += f'{tools.colors_dict["cyan"]}{Rental.to_label(key)}{tools.colors_dict["clean"]}:{value}\n'
        return Rental.RENTAL_STR_FMT.format(str_val)

    def add_new_rent(self):
        try:
            a = open(Rental.RENTAL_DB_OUTFILE, 'a+')
        except OSError:
            tools.print_error(f'There was an error opening the file!')
        else:
            try:
                a.write('{}\n'.format(str(self.__dict__)))
            except OSError:
                tools.print_error(f'There was an error when writing the data!')
            else:
                print(f'\n{tools.colors_dict["yellow"]}New rental made successfully!{tools.colors_dict["clean"]}')
                a.close()
