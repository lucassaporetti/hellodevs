from random import choice
print('Vamos sortear um aluno?\n')
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
list = [a1, a2, a3, a4]
s = choice(list)
print('O aluno sorteado foi: {}'.format(s))

