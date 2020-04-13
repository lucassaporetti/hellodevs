def leiaInt(msg):
    ok = False
    n = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            n = int(n)
            ok = True
        else:
            print('\033[1;31mERRO! Digite um número válido.\033[m')
        if ok:
            break
    return n


num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}')
