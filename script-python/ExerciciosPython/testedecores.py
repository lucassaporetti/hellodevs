#CORES NO TERMINAL USANDO CÓDIGO ANSI - ESCAPE SEQUENCE - CÓDIGO: \033[m

print('\033[1;4;7;30mOlá mundo!\033[m')

azul = '\033[1;34mazul\033[m'
vermelho = '\033[1;31mvermelho\033[m'
print('As cores são {} e {}!'.format(azul, vermelho))

cores = {'limpa': '\033[m',
         'azul': '\033[1;34m',
         'vermelho': '\033[1;31m'}#Painel de cores usando uma coleção / dicionário

print('As cores são {}azul{} e {}vermelho{}!'
      .format(cores['azul'], cores['limpa'],
              cores['vermelho'], cores['limpa']))
