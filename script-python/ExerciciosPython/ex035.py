import emoji
print('Suas linhas retas conseguem formar um triângulo?')
reta1 = float(input('\nDigite o comprimento da reta 1: '))
reta2 = float(input('Digite o comprimento da reta 2: '))
reta3 = float(input('Digite o comprimento da reta 3: '))
if reta2 - reta3 < reta1 < reta2 + reta3\
         and reta1 - reta3 < reta2 < reta1 + reta3 \
         and reta1 - reta2 < reta3 < reta1 + reta2:
    print('\nParabéns! Você formou um triângulo!',
          emoji.emojize(':small_red_triangle:', use_aliases=True))
else:
    print('\nOps! Você não formou um triângulo!',
          emoji.emojize(':-1:', use_aliases=True))
