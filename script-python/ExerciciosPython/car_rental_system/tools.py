colors_dict = {'clean': '\033[m',
               'white': '\033[30m',
               'red': '\033[31m',
               'green': '\033[32m',
               'yellow': '\033[33m',
               'blue': '\033[34m',
               'purple': '\033[35m',
               'cyan': '\033[36m'}

style_dict = {'none': '\033[0m',
              'bold': '\033[1m',
              'underline': '\033[4m',
              'negative': '\033[7m'}


def print_error(msg: str, end='\n'):
    print(f'{colors_dict["red"]}# ERROR: {msg}{colors_dict["clean"]}' + end)


def colored_line(color, line_len=30, end='\n'):
    return f'{color}{"-=" * line_len}{colors_dict["clean"]}{end}'


def line():
    print('-' + '=-' * 17)


def title(txt):
    line()
    print(f'{colors_dict["white"]}{txt.center(34)}{colors_dict["clean"]}')
    line()


def validate(msg):
    ret_val = None
    while ret_val is None:
        try:
            ret_val = int(input(msg))
            if ret_val not in [0, 1, 2, 3, 4, 5, 6]:
                print_error('Please, choose a valid option.')
                ret_val = None
                continue
        except (ValueError, TypeError):
            print_error('Please, choose a valid option.')
            ret_val = None
            continue
        except KeyboardInterrupt:
            print_error('The user interrupted the program [ctrl+c]')
            break

    return ret_val


def validate_user(msg: str):
    ret_val = None
    while ret_val is None:
        try:
            ret_val = input(msg).strip().upper()
            if ret_val not in ['A', 'B', 'C']:
                print_error('Please, choose a valid option.')
                ret_val = None
                continue
        except KeyboardInterrupt:
            print_error('The user interrupted the program [ctrl+c]')
            break

    return ret_val


def read_int(msg, length):
    ret_val = None
    while ret_val is None:
        try:
            ret_val = int(input(msg))
            if len(str(ret_val)) != length:
                print_error(f'This value must contain {length} digits.')
                ret_val = None
                continue
        except (ValueError, TypeError):
            print_error('Please, enter numbers only.')
            ret_val = None
            continue
        except KeyboardInterrupt:
            print_error('The user interrupted the program [ctrl+c]')
            break

    return ret_val


def read_age(msg, mini=18, maxi=80):
    ret_val = None
    while ret_val is None:
        try:
            ret_val = int(input(msg))
            if ret_val < mini:
                print_error(f'The user must be at least 18 years old.')
                ret_val = None
                continue
            elif ret_val > maxi:
                print_error(f'The user must be at most 80 years old.')
                ret_val = None
                continue
        except (ValueError, TypeError):
            print_error('Please, enter numbers only.')
            ret_val = None
            continue
        except KeyboardInterrupt:
            print_error('The user interrupted the program [ctrl+c]')
            break

    return ret_val


def read_float(msg):
    ret_val = None
    while ret_val is None:
        try:
            ret_val = float(input(msg))
        except (ValueError, TypeError):
            print_error('Please, enter real numbers only.')
            ret_val = None
            continue
        except KeyboardInterrupt:
            print_error('The user interrupted the program [ctrl+c]')
            break

    return f'${ret_val:.2f}'


def read_str(msg: str, min_len=1, max_len=30):
    ret_val = None
    while ret_val is None:
        try:
            ret_val = input(msg).strip()
            if ret_val == '' or len(ret_val) < min_len:
                print_error(f'This field must contain a minimum of {min_len} characters.')
                ret_val = None
                continue
            if len(ret_val) > max_len:
                print_error(f'This field must contain the maximum of {max_len} characters')
                ret_val = None
                continue
        except KeyboardInterrupt:
            print_error('The user interrupted the program [ctrl+c]')
            break

    return ret_val


def read_y_n(msg: str):
    ret_val = None
    while ret_val is None:
        try:
            ret_val = input(msg).strip().upper()
            if ret_val not in ['Y', 'N']:
                print_error('This field only accepts Y or N as a character.')
                ret_val = None
                continue
        except KeyboardInterrupt:
            print_error('The user interrupted the program [ctrl+c]')
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
            print_error('Incorrect date format. Accepted format: YYYY/mm/dd')
            ret_val = None
            continue
        except KeyboardInterrupt:
            print_error('The user interrupted the program [ctrl+c]')
            break

    return ret_val


def load_file(name):
    try:
        f = open(name, 'r+')
    except OSError:
        print('Error reading the files!')
    else:
        title('')
        for line in f:
            data = line.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<30}{data[1]:>3} anos')
    finally:
        f.close()


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
#     tools.print_error('Could not find the following files: {}'.format(missing))
#     continue