from datetime import date

genere = str(input('Digite (m) caso seu sexo seja masculino e (f) caso seja feminino: ')).strip().upper()

if genere == 'F':
    print('\nVocê não precisa se alistar obrigatoriamente nas Forças Armadas.')

if genere != 'F' and genere != 'M':
    print('\nVocê não digitou seu gênero corretamente! Tente novamente!')

if genere == 'M':

    actual_year = date.today().year
    birth_year = int(input('Ano de nascimento? '))
    age = actual_year - birth_year

    print('\nQuem nasceu em {} completa {} anos em {}.'.format(birth_year, age, actual_year))

    if age == 18:
        print('\nVocê tem que se alistar IMEDIATAMENTE!')
    elif age < 18:
        print('\nVocê ainda não fez 18 anos. Faltam {} anos para o seu alistamento!'
              '\n\nSeu alistamento será em {}!'.format(18 - age, actual_year + (18 - age)))
    else:
        print('\nVocê já deveria ter se alistado há {} anos!'
              '\n\nSeu alistamento foi em {}!'.format(age - 18, actual_year - (age - 18)))
