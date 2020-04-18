from car_rental_system import tools


class User:
    USER_DB_OUTFILE = 'user_list.dat'

    USER_STR_FMT = '{}{}{}'.format(
        tools.colored_line(tools.colors_dict['blue']),
        '{}',
        tools.colored_line(tools.colors_dict['blue'], end='')
    )

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
            str_val += f'{tools.colors_dict["cyan"]}{User.to_label(key)}{tools.colors_dict["clean"]}:{value}\n'
        return User.USER_STR_FMT.format(str_val)

    def add_new_user(self):
        try:
            a = open(User.USER_DB_OUTFILE, 'a+')
        except OSError:
            tools.print_error(f'There was an error opening the file!')
        else:
            try:
                a.write('{}\n'.format(str(self.__dict__)))
            except OSError:
                tools.print_error(f'There was an error when writing the data!')
            else:
                a.close()
