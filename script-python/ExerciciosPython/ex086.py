lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for lis in range(0, 3):
    for pos in range(0, 3):
        lista[lis][pos] = int(input(f'Digite um valor para [{lis}, {pos}]: '))

print('=-' * 30)
for lis in range(0, 3):
    for pos in range(0, 3):
        print(f'[{lista[lis][pos]: ^5}]', end='')
    print()
