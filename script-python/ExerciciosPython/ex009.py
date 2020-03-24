n = int(input('Digite um número para ver sua tabuada: '))
n1 = n * 1
n2 = n * 2
n3 = n * 3
n4 = n * 4
n5 = n * 5
n6 = n * 6
n7 = n * 7
n8 = n * 8
n9 = n * 9
n10 = n * 10
print('Eis a tabuada deste número:')
print('-' * 31)
print('{} x 1 = {}'
      '{:>11} x 6 = {}\n{} x 2 = {}{:>10} x 7 = {}\n{} x 3 = {}'
      '{:>10} x 8 = {}\n{} x 4 = {}{:>10} x 9 = {}\n{} x 5 = {}'
      '{:>10} x 10 = {}'
      .format(n, n1, n, n6, n, n2, n, n7, n, n3, n, n8, n, n4, n, n9, n, n5, n, n10))
print('-' * 31)
