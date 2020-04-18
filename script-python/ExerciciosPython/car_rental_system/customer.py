from car_rental_system import user, tools


class Customer(user.User):
    CUSTOMER_DB_OUTFILE = 'customer_list.dat'

    def __init__(self, name, age, address, phone, email, drv_license, rentals, id_number):
        super().__init__(name, age, address, phone, email)
        self.drv_license = drv_license
        self.rentals = rentals
        self.id_number = id_number

    def find_id(self):
        with open("customer_list.dat") as fobj:
            file = fobj.read().strip().split()
            while True:
                try:
                    self.id_number = tools.read_int('Customer ID: ', 3)
                    if self.id_number in file:
                        continue
                except:
                    tools.print_error('This ')
                    break

        # while True:
        #     try:
        #         CUSTOMER_DB_OUTFILE.__dict__['id_number'] = int(input('Customer ID: '))
        #     except ValueError:
        #         tools.print_error('Customer ID must be a number!')
        #         continue
        #     found = [id_number for customer in Customer.__dict__ if Customer.__dict__['id_number'] == Customer.__dict__['id_number']
        #     if len(found) > 0 and len() >= 1:
        #         print('This index number already exists. Please try again...')

    def add_new_customer(self):
        try:
            a = open(Customer.CUSTOMER_DB_OUTFILE, 'a+')
        except OSError:
            tools.print_error(f'There was an error opening the file!')
        else:
            try:
                a.write('{}\n'.format(str(self.__dict__)))
            except OSError:
                tools.print_error(f'There was an error when writing the data!')
            else:
                print(f'\n{tools.colors_dict["yellow"]}New Customer User {tools.colors_dict["clean"]}'
                      f'< {tools.colors_dict["purple"]}{self.name}{tools.colors_dict["clean"]} > '
                      f'{tools.colors_dict["yellow"]}successfully added!{tools.colors_dict["clean"]}')
                a.close()
