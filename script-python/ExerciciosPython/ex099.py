from time import sleep


def maior(lista):
    maior_num = 0
    for num in lista:
        if lista[0] == num:
            maior_num = lista[0]
        if num > maior_num:
            maior_num = num
    print('=-' * 30)
    print('Analisando os valores passados...')
    if len(lista) == 1 and lista[0] == 0:
        print(f'Foram informados 0 valores a todo')
    else:
        print(f'{sleep(0.5)}{lista} Foram informados {len(lista)} valores ao todo.', flush=True)
    print(f'O maior valor informado foi {maior_num}.')


valores = [2, 9, 4, 5, 7, 1]
maior(valores)
valores = [4, 7, 0]
maior(valores)
valores = [1, 2]
maior(valores)
valores = [6]
maior(valores)
valores = [0]
maior(valores)
