cont = int(input('Digite um número para calcular seu fatorial: '))
fac = 1

print('Calculando {}! = '.format(cont), end='')

while cont > 0:

    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fac = fac * cont
    cont = cont - 1
print(fac)
