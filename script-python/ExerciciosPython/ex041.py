from datetime import date

print('CATEGORIZADOR DE ATLETAS\n'+'-'*30)

actual_year = date.today().year
birth_year = int(input('\nDigite o ano de nascimento no atleta: '))
age = actual_year - birth_year

if age <= 9:
    print('O atleta tem {} anos.'
          '\nSua categoria é MIRIM.'.format(age))
elif age <= 14:
    print('O atleta tem {} anos.'
          '\nSua categoria é INFANTIL.'.format(age))
elif age <= 19:
    print('O atleta tem {} anos.'
          '\nSua categoria é JUNIOR.'.format(age))
elif age <= 25:
    print('O atleta tem {} anos.'
          '\nSua categoria é SÊNIOR.'.format(age))
else:
    print('O atleta tem {} anos.'
          '\nSua categoria é MASTER.'.format(age))
