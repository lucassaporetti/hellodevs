num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
choice = 0
result = 0
maior = 0
menor = 0

print('''\n[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR\n[ 4 ] NOVOS NÚMEROS\n[ 5 ] SAIR DO PROGRAMA''')

while choice != 5:
    choice = int(input('\nO que deseja fazer? '))
    if choice == 1:
        result = num1 + num2
        print('A soma do número {} com o número {} é igual a {}'.format(num1, num2, result))
    if choice == 2:
        result = num1 * num2
        print('A multiplicação do número {} com o número {} é igual a {}'.format(num1, num2, result))
    if choice == 3 and num1 > num2:
        maior = num1
        menor = num2
        print('O número {} é maior que o número {}'.format(maior, menor))
    if choice == 3 and num2 > num1:
        maior = num2
        menor = num1
        print('O número {} é maior que o número {}'.format(maior, menor))
    if choice == 4:
        num1 = float(input('\nDigite um número: '))
        num2 = float(input('Digite outro número: '))
        print('''\n[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR\n[ 4 ] NOVOS NÚMEROS\n[ 5 ] SAIR DO PROGRAMA''')

print('Bye bye!')
