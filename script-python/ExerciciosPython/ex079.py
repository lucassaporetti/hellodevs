lista_valores = []

while True:

    valor = int(input('Digite um valor: '))

    if valor in lista_valores:
        print('Valor duplicado! Não vou adicionar!')
    else:
        lista_valores.append(valor)
        print('Valor adicionado com sucesso!')

    question = input('Quer continuar? [S/N] ').strip().upper()[0]
    while question not in ['S', 'N']:
        question = str(input('Caractere inválido! Quer continuar? [S/N] ')).strip().upper()[0]
    if question == 'N':
        break

lista_valores.sort()
print(lista_valores)
