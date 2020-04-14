from uteis import moeda


num = float(input('Digite o preço: R$'))
print(f'Metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(num, 10))}')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(num, 13))}')
