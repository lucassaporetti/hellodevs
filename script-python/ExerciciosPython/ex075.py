num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
num4 = int(input('Digite o último número: '))
tup = (num1, num2, num3, num4)
count = 0
for n in tup:
    if n != 0 and n % 2 == 0:
        count += 1
print(f'Você digitou os valores {tup}')
if 9 in tup:
    print(f'O valor 9 apareceu {tup.count(9)} vezes')
else:
    print('O valor 9 não foi encontrado nenhuma vez.')
if 3 in tup:
    print(f'O valor 3 apareceu na {tup.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi encontrado em nenhuma posição.')
print(f'Os valores pares digitados foram {count}')
