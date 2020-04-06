lista_total = []
lista_pares = []
lista_impares = []

while True:
    num = int(input('Digite um número: '))
    lista_total.append(num)
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break

print(f'A lista completa é {lista_total}')
print(f'A lista de pares é {lista_pares}')
print(f'A lista de ímpares é {lista_impares}')
