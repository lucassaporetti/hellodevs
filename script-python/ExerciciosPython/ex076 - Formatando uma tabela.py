lista = ('Lápis', 1.50, 'Caderno', 15.50, 'Borracha', 2.00, 'Estojo', 20.00)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-' * 40)
