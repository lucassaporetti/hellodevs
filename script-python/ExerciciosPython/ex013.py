s = float(input('Informe o salário do funcionário: R$'))
a = float(input('Informe a porcentagem de aumento: '))
sa = s + (s * a) / 100
print('O salário corrigido com {:.2f}% de aumento é de: R${:.2f}'.format(a, sa))
