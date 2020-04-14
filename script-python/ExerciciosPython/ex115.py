from ex115pack import módulos

file = 'ex115.txt'

if not módulos.file_exist(file):
    print('Arquivo encontrado com sucesso!')
    módulos.create_file(file)

op = None

while True:
    módulos.titulo('MENU PRINCIPAL')
    módulos.itens(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    módulos.linha()
    op = módulos.valida('\033[33mSua Opção: \033[m')
    if op == 1:
        módulos.load_file(file)
    elif op == 2:
        módulos.titulo('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = módulos.leia_int('Idade: ')
        módulos.cadastrar(file, nome, idade)
    elif op == 3:
        módulos.titulo('Saindo do sistema... Até logo!')
        break
