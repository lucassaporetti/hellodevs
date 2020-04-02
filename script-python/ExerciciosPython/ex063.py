print('=' * 30 + '\n     SEQUÊNCIA DE FIBONACCI\n' + '=' * 30)

qtd_termos = int(input('Quantos termos você quer mostrar? '))
termo1 = 0
termo2 = 1
termo3 = termo1 + termo2
count = 3

if qtd_termos == 1:
    print('{} → '.format(termo1), end='')
if qtd_termos > 1:
    print('{} → {} → '.format(termo1, termo2), end='')

while count <= qtd_termos:

    print('{} → '.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    termo3 = termo1 + termo2
    count += 1
print('FIM!')
