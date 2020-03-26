nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome contém {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome contém {} letras'.format(nome.find(' ')))
separa = nome.split() #another way
print('Seu primeiro nome contém {} letras'.format(len(separa[0])))














