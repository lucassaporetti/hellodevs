from random import randint
import emoji
from time import sleep

print('=' * 36, '\nVou pensar em um número de 0 a 10...\n' + '=' * 36)

pc_choice = randint(0, 10)
player = int(input('Em que número pensei? '))
palpites = 1

print('Processando...')
sleep(1)

while player != pc_choice:
    if player < pc_choice:
        player = int(input(emoji.emojize(':-1:', use_aliases=True) + ' Mais...Tente mais um: '))
    if player > pc_choice:
        player = int(input(emoji.emojize(':-1:', use_aliases=True) + ' Menos...Tente mais um: '))
    palpites += 1

print('\nParabéns! Você acertou! ' +
      emoji.emojize(':thumbsup:', use_aliases=True) +
      '\nO número que eu pensei foi {}!'
      '\nVocê precisou de {} tentativas para acertar!.'.format(pc_choice, palpites))
