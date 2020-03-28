#!/usr/bin/env python

from math import pow

color = {'clear': '\033[m',
         'cyan': '\033[1;36m',
         'red': '\033[1;31m'}

MAIN_MENU = f"""\033[1J\033[H
    Lucas-Calculator v0.9.1
    **to {color['cyan']}exit{color['clear']} press [ctrl + c]
    {'=' * 32}
    Operations: + - / * @ ^
    {'-' * 32}"""

allowed_ops = ['+', '-', '/', '*', '@', '^']

while True:

    print(MAIN_MENU)

    try:
        left_operand = float(input('Left operand [0]:'))
        operation = (input('Operation [+]: '))
        if operation not in allowed_ops:
            print('{}Invalid operation, please try again!{}'.format(color['red'], color['clear']))
            input('\n\nPress enter to continue\n')
            continue
        right_operand = float(input('Right operand [0]: '))
        if right_operand == 0 and operation == '/':
            print('{}You cannot do a division by 0!{}'.format(color['red'], color['clear']))
            input('\n\nPress enter to continue\n')
            continue
    except ValueError as err:
        print('{}Invalid number, please try again!{}'.format(color['red'], color['clear']))
        input('\n\nPress enter to continue\n')
        continue

    if operation == '+':
        result = left_operand + right_operand
        print('= {}'.format(result))
    elif operation == '-':
        result = left_operand - right_operand
        print('= {}'.format(result))
    elif operation == '/':
        result = left_operand / right_operand
        print('= {}'.format(result))
    elif operation == '*':
        result = left_operand * right_operand
        print('= {}'.format(result))
    elif operation == '@':
        result = left_operand ** (1 / (right_operand))
        print('= {:.2f}'.format(result))
    elif operation == '^':
        result = pow(left_operand, right_operand)
        print('= {}'.format(result))

    input('\n\nPress enter to continue\n')
