
escala = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
          'seis', 'sete', 'oito', 'nove', 'dez',
          'onze', 'doze', 'treze', 'quatorze', 'quinze',
          'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um número entre 0 e 20: '))

while True:
    while num not in range(0, len(escala)):
        num = int(input('Tente novamente! Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {escala[num]}')
    question = str(input('\nQuer tentar de novo? [S/N] ')).strip().upper()[0]
    if question == 'S':
        num = int(input('Digite um número entre 0 e 20: '))
    if question == 'N':
        break

print('Ok, bye bye!')
