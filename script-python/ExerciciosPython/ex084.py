dado = []
lista = []
maior_peso = 0
menor_peso = 0
pessoas_pesadas = []
pessoas_leves = []

while True:
    dado.append(str(input('Qual é o seu nome? ')))
    dado.append(float(input('Qual é o seu peso? ')))
    if len(lista) == 0:
        maior_peso = dado[1]
        menor_peso = dado[1]
    else:
        if dado[1] > maior_peso:
            maior_peso = dado[1]
        if dado[1] < menor_peso:
            menor_peso = dado[1]
    lista.append(dado[:])
    dado.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

for pessoas in lista:
    if pessoas[1] >= 100:
        pessoas_pesadas.append(pessoas[0])
    if pessoas[1] <= 70:
        pessoas_leves.append(pessoas[0])

print('-=' * 30)
print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'O maior peso foi de {maior_peso:.1f}kg. As pesoas mais pesadas são {pessoas_pesadas}')
print(f'O menor peso foi de {menor_peso:.1f}kg. As pessoas mais leves são {pessoas_leves}')
