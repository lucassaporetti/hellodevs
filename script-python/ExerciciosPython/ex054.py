from datetime import date
actual_year = date.today().year
maiores = 0
menores = 0

for people in range(1, 8):
    birth_year = int(input('Em que ano a {}ª pessoa nasceu? '.format(people)))
#    maiores += 1 if actual_year - birth_year >= 18 else 0
#    menores += 1 if actual_year - birth_year < 18 else 0
    age = actual_year - birth_year
    if age >= 18:
        maiores += 1
    else:
        menores += 1

print('\nAo todo tivemos {} pessoas maiores de idade'.format(maiores))
print('E também tivemos {} pessoas menores de idade'.format(menores))
