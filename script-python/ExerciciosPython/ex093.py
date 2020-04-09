dados = dict()
lista = list()
dados['nome'] = str(input('Nome do jogador: '))
qtd_partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

soma = 0

for cont in range(1, qtd_partidas + 1):
    lista.append(int(input(f'Quantos gols na partida {cont}? ')))
    dados['gols'] = lista[:]

dados['total'] = sum(lista)
# for gol in dados['gols']:
#     soma = soma + gol
#     dados['total'] = soma

print('=-' * 30)
print(dados)
print('=-' * 30)

for key, value in dados.items():
    print(f'O campo {key} tem o valor {value}')
print('=-' * 30)

print(f'O jogador {dados["nome"]} jogou {qtd_partidas} partidas.')
for indice, gol in enumerate(lista):
    print(f'    => Na partida {indice + 1}, fez {gol} gols.')
print(f'Foi um total de {dados["total"]} gols.')
