class Car:
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

    def __str__(self):

        color = {'clean': '\033[m', 'white': '\033[30m', 'red': '\033[31m',
                 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
                 'purple': '\033[35m', 'cyan': '\033[36m'}

        return f'{color["blue"]}{"-=" * 30}{color["clean"]}\n' \
               f'{color["cyan"]}Name: {color["clean"]}{self.name}\n' \
               f'{color["cyan"]}Year: {color["clean"]}{self.year}\n' \
               f'{color["cyan"]}Category: {color["clean"]}{self.category}\n' \
               f'{color["cyan"]}Color: {color["clean"]}{self.color}\n' \
               f'{color["cyan"]}A/C: {color["clean"]}{self.a_c}\n' \
               f'{color["cyan"]}Gear Box: {color["clean"]}{self.gear_box}\n' \
               f'{color["cyan"]}Fuel: {color["clean"]}{self.fuel}\n' \
               f'{color["cyan"]}Doors: {color["clean"]}{self.doors}\n' \
               f'{color["cyan"]}Passengers: {color["clean"]}{self.passengers}\n' \
               f'{color["cyan"]}Suitcase: {color["clean"]}{self.suitcase}\n' \
               f'{color["cyan"]}Price: {color["clean"]}{self.price}\n' \
               f'{color["cyan"]}Plate: {color["clean"]}{self.plate}\n' \
               f'{color["cyan"]}Chassis: {color["clean"]}{self.chassis}\n' \
               f'{color["blue"]}{"-=" * 30}{color["clean"]}'

    def add_new_car(self):
        color = {'clean': '\033[m', 'white': '\033[30m', 'red': '\033[31m',
                 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
                 'purple': '\033[35m', 'cyan': '\033[36m'}
        car_stock = 'car_stock.txt'
        # new_car = {'Name': self.name, 'Year': self.year}
        try:
            a = open(car_stock, 'at')
        except:
            print('There was an error opening the file!')
        else:
            try:
                a.write(str(self.__dict__))
            except:
                print('There was an error when writing the data!')
            else:
                print(f'\n{color["yellow"]}New car {color["clean"]}'
                      f'< {color["purple"]}{self.name}{color["clean"]} > '
                      f'{color["yellow"]}successfully added!{color["clean"]}')
                a.close()
