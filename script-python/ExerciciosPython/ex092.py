
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
trabalhador['nascimento'] = int(input('Ano de Nascimento: '))
trabalhador['ctps'] = int(input('Carteira de Trabalho: (0 = não tem) '))

if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de Contratação: '))
    trabalhador['salario'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = trabalhador['contratação'] - trabalhador['nascimento'] + 35

print('=-' * 30)
for key, value in trabalhador.items():
    print(f' - {key} tem o valor {value}')
