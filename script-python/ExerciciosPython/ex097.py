def escreva(txt):
    tamanho_linha = len(txt) + 4
    print('=' * tamanho_linha)
    print(f'{txt: ^{tamanho_linha}}')
    print('=' * tamanho_linha)


escreva('PYTHON WORLD')
escreva('OLÁ MUNDO!')
escreva('Lucas')
escreva('EXERCITANDO FUNÇÕES EM PYTHON!')
