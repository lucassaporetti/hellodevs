from uteis import moeda


num = float(input('Digite o preço: R$'))
print(f'Metade de {num} é {moeda.metade(num)}')
print(f'O dobro de {num} é {moeda.dobro(num)}')
print(f'Aumentando 10%, temos {moeda.aumentar(num, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(num, 13)}')
