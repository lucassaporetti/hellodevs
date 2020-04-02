print('=' * 20)
print('  BANCO SAPORETTI')
print('=' * 20)

valor = int(input('Que valor você quer sacar? R$ '))

unidades = valor // 1 % 10
dezenas = valor // 10 % 10
centenas = valor // 100 % 10
milhares = valor // 1000 % 10

total_unidades = 0
total_dezenas_10 = 0
total_dezenas_20 = 0
total_dezenas_50 = 0

total_cedulas = 0

while True:

    if unidades <= 9 and unidades != 0:
        total_unidades = unidades
    if dezenas == 1 or dezenas == 3 or dezenas == 6 or dezenas == 8:
        total_dezenas_10 += 1
    if dezenas == 2 or dezenas == 3 or dezenas == 7 or dezenas == 8:
        total_dezenas_20 += 1
    if dezenas == 4 or dezenas == 9:
        total_dezenas_20 += 2
    if dezenas == 5:
        total_dezenas_50 += 1
    if centenas >= 1:
        total_dezenas_50 = total_dezenas_50 + (centenas * 2)
    if milhares >= 1:
        total_dezenas_50 = total_dezenas_50 + (milhares * 20)

    if total_dezenas_50 > 0:
        print(f'Total de {total_dezenas_50} cédulas de R$50')
    if total_dezenas_20 > 0:
        print(f'Total de {total_dezenas_20} cédulas de R$20')
    if total_dezenas_10 > 0:
        print(f'Total de {total_dezenas_10} cédulas de R$10')
    if total_unidades > 0:
        print(f'Total de {total_unidades} cédulas de R$1')
    if valor >= 0:
        break

total_cedulas = total_cedulas + total_unidades + total_dezenas_10 + total_dezenas_20 + total_dezenas_50
print(f'Total de {total_cedulas} cédulas ao todo')
print('=' * 30)
print('Volte sempre ao BANCO SAPORETTI! Tenha um bom dia!')
