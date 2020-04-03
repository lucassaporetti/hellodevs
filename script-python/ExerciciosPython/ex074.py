from random import randint

numbers = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))

for c in numbers:
    print(f'{c} ', end='')

print(f'\nO maior valor sorteado foi {max(numbers)}')
print(f'O menor valor sorteado foi {min(numbers)}')
