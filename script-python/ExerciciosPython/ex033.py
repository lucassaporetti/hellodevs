number1 = int(input('Digite um número: '))
number2 = int(input('Digite o segundo número: '))
number3 = int(input('Digite o terceiro número: '))
menor = number1
maior = number1
if number2 < number1 and number2 < number3:
    menor = number2
if number3 < number1 and number3 < number2:
    menor = number3
if number2 > number1 and number2 > number3:
    maior = number2
if number3 > number1 and number3 > number2:
    maior = number3
print('O número menor é {} e o maior é {}.'.format(menor, maior))
