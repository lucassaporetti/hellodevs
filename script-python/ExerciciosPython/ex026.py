f = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase.'.format(f.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(f.find('A')+1))
print('A última letra A apareceu na posição {}.'.format(f.rfind('A')+1))
