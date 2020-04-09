from random import randint
from time import sleep

print('=-' * 15)
print(f'{"JOGOS DA MEGA SENA": ^30}')
print('=-' * 15)

qtd = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{f" SORTEANDO {qtd} JOGOS ":=^30}')

lista = list()
total = 0
jogo = list()

while total < qtd:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont = cont + 1
        if cont >= 6:
            break
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
    total = total + 1
for i, l in enumerate(jogo):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)

print(f'{" < BOA SORTE! > ":=^30}')
