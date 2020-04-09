pessoa = {}
galera = []
soma_idade = []
media_idade = 0
acima_media = []
mulheres = []
continua = ''
while continua != 'N':
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    while pessoa['sexo'] not in ('M', 'F'):
        print('ERRO! Por favor, digite apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    soma_idade.append(pessoa['idade'])
    galera.append(pessoa.copy())
    media_idade = sum(soma_idade) / len(soma_idade)
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continua not in ('S', 'N'):
        print('ERRO! Responda apenas S ou N.')
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('=-' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'B) A média de idade é de {media_idade:.1f} anos.')
print(f'C) As mulheres cadastradas foram {mulheres}.')
print(f'D) Lista de pessoas que estão acima da média:')
for p in galera:
    if p['idade'] > media_idade:
        print('     ')
        for key, value in p.items():
            print(f'{key} = {value}; ', end='')
        print()
print('<< ENCERRADO >>')
