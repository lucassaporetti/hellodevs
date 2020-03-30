print('LOJAS SAPORETTI\n'+'=' * 15)

while True:

    try:
        price = float(input('\nDigite o valor da compra: R$ '))
    except ValueError as err:
        print('\nDigite um valor numérico.')
        input('\n\nAperte enter para continuar...\n')
        continue

    vista_cash = price - (price * 10 / 100)
    vista_card = price - (price * 5 / 100)
    three_more_x = price + (price * 20 / 100)

    print('''\nFORMAS DE PAGAMENTO
    [ 1 ] à vista dinheiro/cheque
    [ 2 ] à vista cartão
    [ 3 ] 2x no cartão
    [ 4 ] 3x ou mais no cartão''')

    try:
        op = int(input('\nDigite a opção: '))
    except ValueError as err:
        print('\nOpção inválida! Tente novamente.')
        input('\nAperte enter para continuar...\n')
        continue

    if op == 1:
        print('\nSua compra de R${:.2f} vai custar R${:.2f} no final.'.format(price, vista_cash))
    elif op == 2:
        print('\nSua compra de R${:.2f} vai custar R${:.2f} no final.'.format(price, vista_card))
    elif op == 3:
        print('\nSua compra de R${:.2f} será parcelada em 2x de R${:.2f} SEM JUROS'.format(price, price / 2))
    elif op == 4:

        try:
            pa = int(input('\nQuantas parcelas? '))
        except ValueError as err:
            print('\nDigite um valor numérico.')
            input('\nAperte enter para continuar...\n')
            continue

        print('\nSua compra de R${:.2f} será parcelada em {}x de R${:.2f} COM JUROS de 20% incluso.'
                '\n\nPreço final do produto: R${:.2f}'.format(price, pa, three_more_x / pa, three_more_x))
    else:
        print('\nOpção inválida! Tente novamente.')
