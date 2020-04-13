def jogador(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))
if gols.isnumeric():#se for numérico:
    gols = int(gols)#recebe o número
else:
    gols = 0
if nome.strip() == '':
    jogador(gols=gols)
else:
    jogador(nome, gols)
