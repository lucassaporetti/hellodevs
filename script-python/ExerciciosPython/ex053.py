print('=' * 23 + '\nDETECTOR DE PALÍNDROMOS\n' + '=' * 23)
frase = str(input('Digite uma frase: ')).strip().replace(' ', '').upper()
print('O inverso de {} é {}'.format(frase, frase[::-1]))
if frase == frase[::-1]:
    print('A frase digitada É UM PALÍNDROMO!!!')
else:
    print('A frase digitada NÃO É um palíndromo!')
