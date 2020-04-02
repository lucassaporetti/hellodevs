print('-' * 20)
print('  LOJAS SAPORETTI')
print('-' * 20)

soma_total = 0
qtd_produtos1000 = 0
produto_barato = ''
price_barato = 0
count = 0

while True:

    nome_produto = (input('Nome do produto: '))

    price = input('Preço: R$')
    price = float(price) if price.isdigit() else None
    if price is None:
        print('Valor inválido! Tente novamente!')
        input('\nAperte enter para continuar...')
        continue

    count += 1

    soma_total += price

    if price > 1000:
        qtd_produtos1000 += 1

    if count == 1:
        price_barato = price
        produto_barato = nome_produto

    if price < price_barato:
        price_barato = price
        produto_barato = nome_produto

    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    while continuar not in ['S', 'N']:
        continuar = input('Caractere inválido! Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

print('------ FIM DO PROGRAMA ------')
print(f'O total da compra foi R${soma_total:.2f}')
print(f'Temos {qtd_produtos1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {produto_barato} que custa R${price_barato:.2f}')
