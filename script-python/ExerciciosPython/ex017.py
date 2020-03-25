from math import hypot
print('Vamos calcular a hipotenusa de um triângulo retângulo?\n')
co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('\nA hipotenusa deste triângulo tem o comprimento de {:.2f}.'.format(hi))
