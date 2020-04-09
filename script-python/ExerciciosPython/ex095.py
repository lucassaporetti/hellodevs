jogador = {}
lista_gols = []
lista_jogador = []
continua = ''
soma = 0
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    qtd_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    lista_gols.clear()
    for cont in range(1, qtd_partidas + 1):
        lista_gols.append(int(input(f'Quantos gols na partida {cont}? ')))
    jogador['gols'] = lista_gols[:]
    jogador['total'] = sum(lista_gols)
    lista_jogador.append(jogador.copy())
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continua not in ['S', 'N']:
        print('ERRO! Por favor, digite apenas "S" ou "N".')
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print('=-' * 30)
print(f'{"cod":<4}{"nome":>10}{"gols":>10}{"total":>20}')
print('-' * 50)
cont = 0
for p in lista_jogador:
    cont = cont + 1
    print(f'{cont:<4}{p["nome"]:>10}{"":>6}{lista_jogador[cont - 1]["gols"]}{lista_jogador[cont - 1]["total"]:>14}')
print('-' * 50)
busca = 0
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para sair] '))
    if busca == 999:
        break
    if busca > len(lista_jogador):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {lista_jogador[busca - 1]["nome"]}')
        for indice, gol in enumerate(lista_jogador[busca - 1]['gols']):
            print(f'    No jogo {indice + 1} fez {gol} gols.')
    print('-' * 30)
