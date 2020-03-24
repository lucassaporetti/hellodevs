pa = float(input('Informe o preço do produto: R$'))
pd = pa - (pa * 5) / 100
print('Com 5% de desconto, o novo preço será: R${:.2f}'.format(pd))
print(f'Com 5% de desconto, o novo preço será: R${pd}')

