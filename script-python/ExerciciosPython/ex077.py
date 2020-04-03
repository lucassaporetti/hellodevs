palavras = ('APRENDER', 'PROGRAMAR', 'PYTHON', 'GAFANHOTO', 'PADAWAN', 'ESTUDAR', 'LINGUAGEM')

for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra in 'AEIOU':
            print(letra.lower(), end=' ')
