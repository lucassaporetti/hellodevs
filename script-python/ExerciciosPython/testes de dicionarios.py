# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# del pessoas['sexo']
# pessoas['nome'] = 'Lucas'
# pessoas['idade'] = 30
# pessoas['peso'] = 70
# for key, value in pessoas.items():
#     print(f'{key} = {value}')

# brasil = []
# estado1 = {'UF': 'Minas Gerais', 'sigla': 'MG'}
# estado2 = {'UF': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
#
# print(brasil[0]['sigla'])

brasil = list()
estado = dict()
for cont in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for key, value in e.items():
        print(f'O campo {key} tem valor {value}.')



