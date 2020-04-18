from car_rental_system import user, tools


class Employee(user.User):
    EMPLOYEE_DB_OUTFILE = 'employee_list.dat'

    def __init__(self, name, age, address, phone, email, access_type, hired_date, salary, id_number):
        super().__init__(name, age, address, phone, email)
        self.access_type = access_type
        self.hired_date = hired_date
        self.salary = salary
        self.id_number = id_number

    def add_new_employee(self):
        try:
            a = open(Employee.EMPLOYEE_DB_OUTFILE, 'a+')
        except OSError:
            tools.print_error(f'There was an error opening the file!')
        else:
            try:
                a.write('{}\n'.format(str(self.__dict__)))
            except OSError:
                tools.print_error(f'There was an error when writing the data!')
            else:
                print(f'\n{tools.colors_dict["yellow"]}New Employee User {tools.colors_dict["clean"]}'
                      f'< {tools.colors_dict["purple"]}{self.name}{tools.colors_dict["clean"]} > '
                      f'{tools.colors_dict["yellow"]}successfully added!{tools.colors_dict["clean"]}')
                a.close()
