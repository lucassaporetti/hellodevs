from datetime import date

year = int(input('Que ano quer analisar? Para o ano atual, digite 0: '))

if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('O ano de {} É bissexto!'.format(year))
else:
    print('O ano de {} NÃO é bissexto!'.format(year))
