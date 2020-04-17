def line():
    print('-' + '=-' * 17)


def title(txt):
    line()
    print(f'\033[30m{txt.center(34)}\033[m')
    line()


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


def validate(msg):
    while True:
        try:
            n = int(input(msg))
            if n not in [0, 1, 2, 3, 4, 5, 6]:
                print('\033[31mERROR! Please, choose a valid option.\033[m')
        except (ValueError, TypeError):
            print('\033[31mERROR! The choice in the menu must be a number.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUser preferred not to type anything.\033[m')
            return 0
        else:
            return n


def read_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERROR! Please, enter numbers only.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUser preferred not to type anything.\033[m')
            return 0
        else:
            return n


def read_float(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERROR! Please, enter real numbers only.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUser preferred not to type anything.\033[m')
            return 0
        else:
            return n


def file_exist(name):
    try:
        f = open(name, 'rt')
        f.close()
    except FileNotFoundError:
        return False
    else:
        return True


def create_file(name):
    try:
        f = open(name, 'wt+')
        f.close()
    except:
        print('There was an error creating the file!')
    else:
        print('New registration added successfully')


def load_file(name):
    try:
        f = open(name, 'rt')
    except:
        print('Error reading the files!')
    else:
        title('')
        for line in f:
            data = line.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<30}{data[1]:>3} anos')
    finally:
        f.close()


def registration(file):
    try:
        a = open(file, 'at')
    except:
        print('There was an error opening the file!')
    else:
        try:
            a.write(f'{name}; {idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()
