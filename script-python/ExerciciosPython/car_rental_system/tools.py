import ast
import os


class Colors:
    clean = '\033[m'
    white = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'


class Style:
    none = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
    negative = '\033[7m'


class PrintUtils:
    
    @staticmethod
    def print_error(msg: str, end='\n'):
        print(f'{Colors.red}# ERROR: {msg}{Colors.clean}' + end)
    
    @staticmethod
    def colored_line(color, line_len=30, end=''):
        return f'{color}{"-=" * line_len}{Colors.clean}{end}'
    
    @staticmethod
    def print_line():
        print('-' + '=-' * 17)
        
    @staticmethod
    def print_title(txt):
        PrintUtils.print_line()
        print(f'{Colors.white}{txt.center(34)}{Colors.clean}')
        PrintUtils.print_line()


def validate_op(msg):
    ret_val = None
    while ret_val is None:
        try:
            ret_val = int(input(msg))
            if ret_val not in [0, 1, 2, 3, 4, 5, 6]:
                PrintUtils.print_error('Please, choose a valid option.')
                ret_val = None
                continue
        except (ValueError, TypeError):
            PrintUtils.print_error('Please, choose a valid option.')
            ret_val = None
            continue
        except KeyboardInterrupt:
            PrintUtils.print_error('The user interrupted the program [ctrl+c]')
            break
    return ret_val


def validate_user_op(msg: str):
    ret_val = None
    while ret_val is None:
        try:
            ret_val = input(msg).strip().upper()
            if ret_val not in ['A', 'B', 'C']:
                PrintUtils.print_error('Please, choose a valid option.')
                ret_val = None
                continue
        except KeyboardInterrupt:
            PrintUtils.print_error('The user interrupted the program [ctrl+c]')
            break
    return ret_val


def validate_character(msg: str):
    ret_val = None
    while ret_val is None:
        try:
            ret_val = input(msg).strip().upper()
            if ret_val not in ['Y', 'N']:
                PrintUtils.print_error('This field only accepts Y or N as a character.')
                ret_val = None
                continue
        except KeyboardInterrupt:
            PrintUtils.print_error('The user interrupted the program [ctrl+c]')
            break
    return ret_val


def read_int(msg, length):
    ret_val = None
    while ret_val is None:
        try:
            ret_val = int(input(msg))
            if len(str(ret_val)) != length:
                PrintUtils.print_error(f'This value must contain {length} digits.')
                ret_val = None
                continue
        except (ValueError, TypeError):
            PrintUtils.print_error('Please, enter numbers only.')
            ret_val = None
            continue
        except KeyboardInterrupt:
            PrintUtils.print_error('The user interrupted the program [ctrl+c]')
            break
    return ret_val


def read_float(msg):
    ret_val = None
    while ret_val is None:
        try:
            ret_val = float(input(msg))
        except (ValueError, TypeError):
            PrintUtils.print_error('Please, enter real numbers only.')
            ret_val = None
            continue
        except KeyboardInterrupt:
            PrintUtils.print_error('The user interrupted the program [ctrl+c]')
            break
    return f'${ret_val:.2f}'


def read_str(msg: str, min_len=1, max_len=30):
    ret_val = None
    while ret_val is None:
        try:
            ret_val = input(msg).strip()
            if ret_val == '' or len(ret_val) < min_len:
                PrintUtils.print_error(f'This field must contain a minimum of {min_len} characters.')
                ret_val = None
                continue
            if len(ret_val) > max_len:
                PrintUtils.print_error(f'This field must contain the maximum of {max_len} characters')
                ret_val = None
                continue
        except KeyboardInterrupt:
            PrintUtils.print_error('The user interrupted the program [ctrl+c]')
            break
    return ret_val


def read_age(msg, mini=18, maxi=80):
    ret_val = None
    while ret_val is None:
        try:
            ret_val = int(input(msg))
            if ret_val < mini:
                PrintUtils.print_error(f'The user must be at least 18 years old.')
                ret_val = None
                continue
            elif ret_val > maxi:
                PrintUtils.print_error(f'The user must be at most 80 years old.')
                ret_val = None
                continue
        except (ValueError, TypeError):
            PrintUtils.print_error('Please, enter numbers only.')
            ret_val = None
            continue
        except KeyboardInterrupt:
            PrintUtils.print_error('The user interrupted the program [ctrl+c]')
            break
    return ret_val


def read_date(msg: str):
    import datetime
    ret_val = None
    while ret_val is None:
        try:
            date_format = '%Y/%m/%d'
            ret_val = input(msg)
            datetime.datetime.strptime(ret_val, date_format)
            continue
        except ValueError:
            PrintUtils.print_error('Incorrect date format. Accepted format: YYYY/mm/dd')
            ret_val = None
            continue
        except KeyboardInterrupt:
            PrintUtils.print_error('The user interrupted the program [ctrl+c]')
            break
    return ret_val


class FileUtils:
    @staticmethod
    def create(filename: str):
        if not os.path.exists(filename):
            open(filename, "w").close()
        return []

    @staticmethod
    def read(filename: str):
        with open(filename, 'r') as f_data:
            contents = f_data.read()
            data = ast.literal_eval(contents) if contents else []
            return data

    @staticmethod
    def save(filename: str, contents: list):
        with open(filename, 'w') as f_data:
            f_data.write(str(contents))
            f_data.flush()


def clear_screen():
    print('\033[2J')


# def registration(file):
#     try:
#         a = open(file, 'at')
#     except:
#         print('There was an error opening the file!')
#     else:
#         try:
#             a.write(f'{name}; {idade}\n')
#         except:
#             print('Houve um erro na hora de escrever os dados!')
#         else:
#             print(f'Novo registro de {nome} adicionado')
#             a.close()

# car_db_exists = os.path.exists(CAR_DB_OUTFILE)
# customer_db_exists = os.path.exists(CUSTOMER_DB_OUTFILE)
# employee_db_exists = os.path.exists(EMPLOYEE_DB_OUTFILE)
#
# if not car_db_exists or not customer_db_exists or not employee_db_exists:
#     missing = [
#         None if car_db_exists else CAR_DB_OUTFILE,
#         None if customer_db_exists else CUSTOMER_DB_OUTFILE,
#         None if employee_db_exists else EMPLOYEE_DB_OUTFILE
#     ]
#     tools.PrintUtils.print_error('Could not find the following files: {}'.format(missing))
#     continue
