from random import randint

soma = 0
count = 0
result = ''

print('=-' * 13)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 13)

while True:
    pc_number = randint(1, 10)
    player_number = (input('Diga um valor: '))
    player_number = int(player_number) if player_number.isdigit() else None
    if player_number is None:
        print('Número inválido! Tente novamente!')
        input('\n\nAperte enter para continuar...\n')
        continue
    soma = pc_number + player_number
    player_choice = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    while player_choice not in ['P', 'I']:
        player_choice = str(input('Caractere inválido! Par ou Ímpar? [P/I] ')).strip().upper()[0]
    if soma % 2 == 0:
        result = 'PAR'
    else:
        result = 'ÍMPAR'
    if player_choice == 'P' and result == 'PAR' \
            or player_choice == 'I' and result == 'ÍMPAR':
        count = count + 1
        print('-' * 50)
        print(f'Você jogou {player_number} '
              f'e o computador {pc_number}. Total de {soma} deu {result}')
        print('-' * 50)
        print('Você VENCEU!\nVamos jogar novamente...')
        print('=-' * 13)
    else:
        print('-' * 50)
        print(f'Você jogou {player_number} '
              f'e o computador {pc_number}. Total de {soma} deu {result}')
        print('-' * 50)
        break
print('Você PERDEU!')
print('=-' * 16)
print(f'GAME OVER! Você venceu {count} vezes.')
