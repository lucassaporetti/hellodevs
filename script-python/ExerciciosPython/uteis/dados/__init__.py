def leiaDinheiro(msg):
    ok = False
    while not ok:
        num = str(input(msg)).replace(',', '.').strip()
        if num.isalpha() or num == '':
            print(f'ERRO: {num} é um preço inválido!')
        else:
            ok = True
            return float(num)
