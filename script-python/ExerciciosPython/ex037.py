while True:

    try:

        num = int(input('\nDigite um número inteiro: '))

        if num != str() or num != float():

            print("""\nEscolha uma das bases para conversão:\n
            [ 1 ] converter para BINÁRIO
            [ 2 ] converter para OCTAL
            [ 3 ] converter para HEXADECIMAL""")

    except ValueError as err:

        print('\nVocê não digitou um número inteiro! Tente novamente!')
        input('\nAperte enter para continuar...')
        continue

    option = int(input('\nSua opção: '))

    if option == 1:
        print('\n{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
    elif option == 2:
        print('\n{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
    elif option == 3:
        print('\n{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
    else:
        print('\n{} não é uma opção válida!'.format(option))

    input('\nAperte enter para continuar...')
