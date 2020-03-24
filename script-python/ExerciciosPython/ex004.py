n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
e = n1 ** n2

print('A soma é {};\nO produto é {};\nA divisão é {:.3f};\n'.format(s, m, d), end='')
print('A divisão inteira é {};\nO resto da divisão é {};\nA potência é {}.'.format(di, r, e))
