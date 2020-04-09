from time import sleep


def linha():
    print('=-' * 30)


def contador(inicio, fim, passo):
    linha()
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    if passo == 0:
        passo = 1
    if inicio > fim and passo < 0:
        passo = passo
        fim = fim +(passo)
    if inicio > fim and passo > 0:
        passo = +(-passo)
        fim = fim + (passo)
    if inicio < fim and passo < 0:
        passo = -1*(passo)
    if inicio < fim and passo > 0:
        fim = fim + passo
    for cont in range(inicio, fim, passo):
        sleep(0.5)
        print(f'{cont} ', end='', flush=True)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, -2)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
