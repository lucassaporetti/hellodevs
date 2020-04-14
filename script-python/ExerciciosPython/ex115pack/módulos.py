def linha():
    print('=' * 42)


def titulo(txt):
    linha()
    print(f'\033[30m{txt.center(42)}\033[m')
    linha()


def itens(lista):
    cores = {'limpa': '\033[m',
             'azul': '\033[34m',
             'vermelho': '\033[31m',
             'amarelo': '\033[33m'}
    c = 1
    for item in lista:
        print(f'{cores["amarelo"]}{c} - {cores["limpa"]}{cores["azul"]}{item}{cores["limpa"]}')
        c = c + 1


def valida(msg):
    while True:
        try:
            n = int(input(msg))
            if n not in [1, 2, 3]:
                print('\033[31mERRO! Digite uma opção válida!\033[m')
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar nenhum número.\033[m')
            return 3
        else:
            return n


def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar nenhum número.\033[m')
            return 0
        else:
            return n


def file_exist(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def create_file(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def load_file(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        titulo('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(file, nome='desconhecido', idade=0):
    try:
        a = open(file, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()

