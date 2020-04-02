flag = ''
num = count = soma = media = maior = menor = 0

while flag != 'N':
    num = input('Digite um número: ')
    num = int(num) if num.isdigit() else None
    if num is None:
        print('Número inválido! Tente novamente!')
        input('\n\nAperte enter para continuar...\n')
        continue
    count = count + 1
    soma = soma + num
    media = soma / count
    if count == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    flag = str(input('Quer continuar? [s/n] ')).strip().upper()
    while flag not in ['S', 'N']:
        flag = str(input('Caractere inválido! Quer continuar? [s/n] ')).strip().upper()
print('Você digitou {} números e a média foi {:.1f}.'.format(count, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
