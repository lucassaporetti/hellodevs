dados = dict()

dados['nome'] = str(input('Nome: '))
dados['media'] = float(input('Média: '))

if dados['media'] < 5:
    dados['sit'] = 'REPROVADO'
elif dados['media'] < 7:
    dados['sit'] = 'RECUPERAÇÃO'
elif dados['media'] >= 7:
    dados['sit'] = 'APROVADO'

print('=-' * 30)
for key, value in dados.items():
    print(f'  -  {key} é igual a {value}')
