times = ('Flamengo', 'Palmeiras', 'Santos', 'Grêmio', 'Internacional',
         'Corinthians', 'São Paulo', 'Vasco', 'Cruzeiro', 'Fluminense')

print('-=' * 50)
print('LISTA DE TIMES DO BRASILEIRÃO: ', times)
print('-=' * 50)
print('OS 5 PRIMEIROS SÃO: ', times[0:5])
print('-=' * 50)
print('OS 4 ÚLTIMOS SÃO: ', times[-4:])
print('-=' * 50)
print('Times em ordem alfabética: ', sorted(times))
print('-=' * 50)
print(f'O Corinthians está na {times.index("Corinthians") + 1}ª posição')
