def fatorial(n, show=False):
    """Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: Mostrar ou não a conta.
    :return: O retorno do Fatorial de um número n."""

    f = 1
    while n > 0:
        if show:
            print('{}'.format(n), end='')
            print(' x ' if n > 1 else ' = ', end='')
        f = f * n
        n = n - 1
    return f


print('-' * 30)
print(fatorial(5, False))
