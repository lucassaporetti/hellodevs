matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = []
soma_pares = 0
soma_coluna2 = 0
maior = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            pares.append(matriz[linha][coluna])

for linha in range(0, 3):
    soma_coluna2 = soma_coluna2 + matriz[linha][2]
# matriz[0][2] + matriz[1][2] + matriz[2][2]

for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    if matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
# maior = max(matriz[1])

for num in pares:
    soma_pares = soma_pares + num

print('=-' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'{matriz[linha][coluna]: ^5}', end='')
    print()

print('=-' * 30)
print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_coluna2}')
print(f'O maior valor da segunda linha é {maior}')
