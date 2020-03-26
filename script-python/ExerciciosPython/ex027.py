n = str(input('Digite seu nome completo: ')).strip().split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))
