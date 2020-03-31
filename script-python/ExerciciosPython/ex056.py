soma_idade = 0
maior_idade_m = 0
total_menoridade_20_f = 0
media_idades = 0
nome_maioridade_m = ''
for pessoa in range(1, 5):
    print('----- {}ª PESSOA -----'.format(pessoa))
    nome = str(input('Nome: ')).strip().capitalize()
    idade = float(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma_idade += idade
    media_idades = soma_idade / 4
    if pessoa == 1 and sexo == 'M':
        maior_idade_m = idade
        nome_maioridade_m = nome
    if sexo == 'M' and idade > maior_idade_m:
        maior_idade_m = idade
        nome_maioridade_m = nome
    if sexo == 'F' and idade < 20:
        total_menoridade_20_f += 1
print('A média de idade do grupo é de {:.1f} anos.'.format(media_idades))
print('O homem mais velho tem {:.0f} anos e se chama {}.'.format(maior_idade_m, nome_maioridade_m))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(total_menoridade_20_f))
