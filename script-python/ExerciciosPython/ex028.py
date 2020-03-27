from random import randint
import emoji
from time import sleep
print('-=-' * 13)
print('Vou pensar em um número de 0 a 5...')
print('-=-' * 13)
question = int(input('Em que número pensei? '))
randomize = randint(0, 5)
print('Processando...')
sleep(2)
print('O número que eu pensei foi {}.'.format(randomize))
if question == randomize:
    print('Parabéns! Você acertou!',
          emoji.emojize(':thumbsup:', use_aliases=True))
else:
    print('Ops! Você errou!',
          emoji.emojize(':-1:', use_aliases=True))
