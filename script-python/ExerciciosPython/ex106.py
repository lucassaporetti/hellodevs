# remedios = {'febre': 'paracetamol', 'dor de cabeça': 'dorflex', 'colica': 'ibuprofeno',
#             'dor de estômago': 'eno', 'corte no dedo': 'bandaid'}
#
# sintoma = ''
#
# while sintoma != 'E':
#     sintoma = str(input('O que você está sentindo? ["E" para sair] ')).strip().upper()
#     for key, value in remedios.items():
#         if sintoma == key.upper().strip():
#             print(f'Para {key} você precisa usar {value}.')
#     if sintoma == 0:
#         break
# print('Ok, programa encerrado. Viva com saúde!')

# from time import sleep
#
# tempo = int(input('Digite um valor para iniciar o cronômetro: [segundos] '))
# for t in range(tempo, -1, -1):
#     sleep(1)
#
#     print(f'\b\b{t} ', end='')
#
# print('Tanam!!!')

# qtd_biscoitos = int(input('Quantos biscoitos há no pote? '))
# cont = 0
# while qtd_biscoitos != 0:
#     qtd_biscoitos = qtd_biscoitos - 4
#     cont = cont + 1
# print(f'Para 4 pessoas, pegando um biscoito a cada hora, o pote ficará vazio em {cont} hora(s).')
