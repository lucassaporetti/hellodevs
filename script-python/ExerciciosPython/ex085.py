numeros = [[], []]
valor = 0

for n in range(1, 8):
    valor = int(input(f'digite o {n}º valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    if valor % 2 != 0:
        numeros[1].append(valor)

numeros[0].sort()
numeros[1].sort()

print('=-' * 30)
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores ímpares digitados foram: {numeros[1]}')
