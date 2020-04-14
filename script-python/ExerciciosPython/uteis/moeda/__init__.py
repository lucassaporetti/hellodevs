def moeda(n):
    n = f'R${n:.2f}'.replace('.', ',')
    return n


def metade(n, cifra=False):
    pm = n / 2
    if cifra:
        pm = moeda(pm)
    return pm


def dobro(n, cifra=False):
    pd = n * 2
    if cifra:
        pd = moeda(pd)
    return pd


def aumentar(n, p, cifra=False):
    pn = n + (n * p) / 100
    if cifra:
        pn = moeda(pn)
    return pn


def diminuir(n, p, cifra=False):
    pn = n - (n * p) / 100
    if cifra:
        pn = moeda(pn)
    return pn


def resumo(n=0, pa=10, pd=5):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR".center(30)}')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{pa}% de aumento: \t{aumentar(n, pa, True)}')
    print(f'{pd}% de redução: \t{diminuir(n, pd, True)}')
    print('-' * 30)
