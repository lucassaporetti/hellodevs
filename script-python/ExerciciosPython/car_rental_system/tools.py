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


def clear_screen():
    print('\033[2J')


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


def validate_listing_op(msg: str):
    ret_val = None
    while ret_val is None:
        try:
            ret_val = input(msg).strip().upper()
            if ret_val not in ['A', 'B', 'C', 'D', 'E', 'F']:
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
    from datetime import datetime
    ret_val = None
    while ret_val is None:
        try:
            date_format = '%Y/%m/%d'
            ret_val = input(msg)
            datetime.strptime(ret_val, date_format)
            y = int(ret_val[0:4])
            m = int(ret_val[5:7])
            d = int(ret_val[8:10])
            date_result = datetime(y, m, d)
            calc_date = date_result - datetime.now()
            total_days = calc_date.days + 1
            if total_days > 0:
                return ret_val
            else:
                PrintUtils.print_error('The date must be at least one day in the future.')
                ret_val = None
        except ValueError:
            PrintUtils.print_error('Incorrect date format. Accepted format: YYYY/mm/dd')
            ret_val = None
            continue
        except KeyboardInterrupt:
            PrintUtils.print_error('The user interrupted the program [ctrl+c]')
            break


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
