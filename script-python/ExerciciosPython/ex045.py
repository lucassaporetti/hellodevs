import emoji
import random
from time import sleep

while True:

    pedra = emoji.emojize(':punch:', use_aliases=True) + ' [ PEDRA ]'
    papel = emoji.emojize(':wave:', use_aliases=True) + ' [ PAPEL ]'
    tesoura = emoji.emojize(':v:', use_aliases=True) + '  [ TESOURA ]'

    options_list = [1, 2, 3]

    pc = random.choice(options_list)

    print('\n' + '-=' * 5 + '-', '\n  JOKENPO\n' + '-=' * 5 + '-')

    print('''\nESCOLHA SUA MÃO:\n\n1 - {}\n2 - {}\n3 - {}  '''.format(pedra, papel, tesoura))

    try:
        op = int(input('\nDigite o número da sua opção: '))
        if op not in options_list:
            print('\nVocê escolheu uma OPÇÃO INVÁLIDA!')
            input('\nFim de jogo! Aperte ENTER para jogar novamente...\n')
            continue

    except ValueError as err:
        print('\nOpção inválida!')
        input('\nFim de jogo! Aperte ENTER para jogar novamente...\n')
        continue

    print('\nJO\n')
    sleep(0.5)
    print('KEN\n')
    sleep(0.5)
    print('PO!!!\n')
    sleep(0.5)

    print('-=' * 17)

    if op == 1:
        print('Você escolheu {}!'. format(pedra))
    elif op == 2:
        print('Você esolheu {}!'.format(papel))
    elif op == 3:
        print('Você escolheu {}!'.format(tesoura))

    if pc == 1:
        print('\nEu escolhi {}!'. format(pedra))
    elif pc == 2:
        print('\nEu escolhi {}!'.format(papel))
    elif pc == 3:
        print('\nEu escolhi {}!'.format(tesoura))

    print('-=' * 17)

    if op == pc:
        print('\nEMPATE!!!')
    elif op == 1 and pc == 2:
        print('\nPAPEL embrulha PEDRA!\n\nVocê PERDEU!!!')
    elif op == 1 and pc == 3:
        print('\nPEDRA quebra TESOURA\n\nVocê VENCEU!!!')
    elif op == 2 and pc == 1:
        print('\nPAPEL embrulha PEDRA!\n\nVocê VENCEU!!!')
    elif op == 2 and pc == 3:
        print('\nTESOURA corta PAPEL!\n\nVocê PERDEU!!!')
    elif op == 3 and pc == 1:
        print('\nPEDRA quebra TESOURA!\n\nVocê PERDEU!!!')
    elif op == 3 and pc == 2:
        print('\nTESOURA corta PAPEL!\n\nVocê VENCEU!!!')

    input('\nFim de jogo! Aperte ENTER para jogar novamente...')
