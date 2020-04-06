expression = str(input('Digite uma expressão matemática: '))
lista_parenteses = []

for simb in expression:
    if simb == '(':
        lista_parenteses.append('(')
    if simb == ')':
        if len(lista_parenteses) > 0:
            lista_parenteses.pop()
        else:
            lista_parenteses.append(')')

if len(lista_parenteses) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')
