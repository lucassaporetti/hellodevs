
print('CALCULADORA DE MÉDIAS:\n'+'-'*22)

n1 = float(input('\nPrimeira nota: '))
n2 = float(input('\nSegunda nota: '))
m = (n1 + n2) / 2

if m < 5:
    print('\nA média do aluno foi {}.'
          '\nEle está REPROVADO!'.format(m))
elif 5 <= m < 7:
    print('\nA média do aluno foi {}.'
          '\nEle está em RECUPERAÇÃO!'.format(m))
else:
    print('\nA média do aluno foi {}.'
          '\nEle está APROVADO!'.format(m))
