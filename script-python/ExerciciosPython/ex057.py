sexo = str(input('Qual é o seu sexo [M/F]? ')).strip().upper()[0]
while sexo not in ['M', 'F']:
    sexo = str(input('Caractere inválido! Por favor, digite o seu sexo [M/F]: ')).strip().upper()[0]
print('Seu sexo é {}.'.format(sexo))
