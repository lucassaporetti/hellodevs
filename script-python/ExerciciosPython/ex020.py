from random import shuffle
print('Vamos escolher a ordem dos alunos para a apresentação do trabalho?\n')
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
list = [a1, a2, a3, a4]
s = shuffle(list)
print('A ordem de apresentação do trabalho será: {}'.format(list))