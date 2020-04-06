lista = []

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    continua = str(input('Quer contiuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break

print(f'Você digitou {len(lista)} elementos;')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5  não foi encontrado na lista!')
