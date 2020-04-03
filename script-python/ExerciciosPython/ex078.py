valores = []
maior = 0
menor = 0

for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))

    if cont == 0:
        maior = valores[cont]
        menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]

print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} e ele apareceu nas posições ', end='')
for p, n in enumerate(valores):
    if n == maior:
        print(f'{p}... ', end='')
print()
print(f'O menor valor digitado foi {menor} e ele apareceu nas posições ', end='')
for p, n in enumerate(valores):
    if n == menor:
        print(f'{p}... ', end='')
print()
# n = [int(input(f'\nDigite um valor para a posição {pos}: ')) for pos in range(5)]
# print(f'\nVocê digitou os valores {n}.')
# print(f'\nMaior nº digitado foi {max(n)} nas posições {", ".join(str(i) for i in range(5) if n[i] == max(n))}.')
# print(f'Menor nº digitado foi {min(n)} nas posições {", ".join(str(i) for i in range(5) if n[i] == min(n))}.')
