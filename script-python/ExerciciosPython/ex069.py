pessoas_maior = 0
homens = 0
mulher_menor20 = 0

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)

    idade = (input('Idade: '))
    idade = int(idade) if idade.isdigit() else None
    if idade is None:
        print('Número inválido! Tente novamente!')
        input('\nAperte enter para continuar...')
        continue

    sexo = (input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in ['M', 'F']:
        sexo = (input('Caractere inválido! Sexo: [M/F] ')).strip().upper()[0]

    if idade > 18:
        pessoas_maior += 1

    if sexo == 'M':
        homens += 1

    if idade < 20 and sexo == 'F':
        mulher_menor20 += 1

    continuar = (input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in ['S', 'N']:
        continuar = (input('Carcatere inválido! Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas com mais de 18 anos: {pessoas_maior}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulher_menor20} mulheres com menos de 20 anos.')