from random import randint
from time import sleep


def sorteia(lista):
    for cont in range(1, 6):
        lista.append(randint(1, 10))
    print(f'Sorteando 5 valores da lista: ', end='')
    for num in lista:
        sleep(0.3)
        print(f'{num} ', end='', flush=True)
    print('PRONTO!')


def soma_par(lista):
    soma_par = 0
    for num in lista:
        if num % 2 == 0:
            soma_par = soma_par + num
    print(f'Somando os valores pares de {lista}, temos {soma_par}')


numeros = []
sorteia(numeros)
soma_par(numeros)
