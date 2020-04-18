from car_rental_system import tools


class Car:
    CAR_DB_OUTFILE = 'car_stock.dat'

    CAR_STR_FMT = '{}{}{}'.format(
        tools.colored_line(tools.colors_dict['blue']),
        '{}',
        tools.colored_line(tools.colors_dict['blue'], end='')
    )

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

    @staticmethod
    def to_label(key):
        label = str(key).title().replace('_', ' ').replace('A C', 'A/C')
        return label

    def __str__(self):
        str_val = ''

        for key, value in self.__dict__.items():
            str_val += f'{tools.colors_dict["cyan"]}{Car.to_label(key)}{tools.colors_dict["clean"]}:{value}\n'
        return Car.CAR_STR_FMT.format(str_val)

    def add_new_car(self):
        try:
            a = open(Car.CAR_DB_OUTFILE, 'a+')
        except OSError:
            tools.print_error(f'There was an error opening the file!')
        else:
            try:
                a.write('{}\n'.format(str(self.__dict__)))
            except OSError:
                tools.print_error(f'There was an error when writing the data!')
            else:
                print(f'\n{tools.colors_dict["yellow"]}New car {tools.colors_dict["clean"]}'
                      f'< {tools.colors_dict["purple"]}{self.name}{tools.colors_dict["clean"]} > '
                      f'{tools.colors_dict["yellow"]}successfully added!{tools.colors_dict["clean"]}')
                a.close()
