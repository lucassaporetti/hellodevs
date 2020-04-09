from random import randint
from operator import itemgetter

print('Valores sorteados:')

ranking = list()

jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}

for key, value in jogo.items():
    print(f'O {key} tirou {value} no dado.')

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('=-' * 15)

print('== RANKING DOS JOGADORES ==')

for indice, valor in enumerate(ranking):
    print(f'{indice + 1}º lugar: {valor[0]} com {valor[1]}.')
