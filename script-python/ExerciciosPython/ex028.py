import random
import emoji
question = int(input('Estou pensando em um número de 0 a 5...\n'
                     'Que número é esse? '))
randomize = random.randint(0, 5)
print('O número que eu pensei foi {}.'.format(randomize))
if question == randomize:
    print('Parabéns! Você acertou!',
          emoji.emojize(':thumbsup:', use_aliases=True))
else:
    print('Ops! Você errou!',
          emoji.emojize(':-1:', use_aliases=True))
