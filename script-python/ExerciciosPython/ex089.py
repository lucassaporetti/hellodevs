from math import ceil
dados = {}
alunos = []
sit = ''

while True:
    dados['nome'] = str(input('Nome: '))
    dados['nota1'] = float(input('Nota 1: '))
    dados['nota2'] = float(input('Nota 2: '))
    dados['media'] = (dados['nota1'] + dados['nota2']) / 2
    dados['media'] = ceil(dados['media'])
    alunos.append(dados.copy())
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break

print('=-' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)

for aluno in alunos:
    print(f'{alunos.index(aluno):<4}{aluno["nome"]:<10}{aluno["media"]:>8.1f}')
print('-' * 30)

while True:
    choice = int(input('Mostrar notas de qual aluno? [999 interrompe] '))
    if choice == 999:
        break
    if choice <= len(alunos) - 1:
        print(f'Notas de {alunos[choice]["nome"]} são [{alunos[choice]["nota1"]}, {alunos[choice]["nota2"]}]')
        print('-' * 30)
