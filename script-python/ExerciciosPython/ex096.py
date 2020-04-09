def area(a, b):
    tot = a * b
    print(f'A área de um terreno {a}x{b} é de {tot:.1f}m²')


print('CONTROLE DE TERRENOS')
print('-' * 20)

l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))

area(l, c)
