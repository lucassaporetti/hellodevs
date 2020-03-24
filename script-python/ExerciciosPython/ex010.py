COTACAO_DOLLAR = 5.13
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dollar = real / COTACAO_DOLLAR
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dollar))
