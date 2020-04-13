def voto(a):
    from datetime import date#escopo de importação
    ano_atual = date.today().year
    idade = ano_atual - a
    if idade < 16:
        return f'Com {idade} anos: Voto NEGADO.'
    if 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: Voto OPCIONAL.'
    if 65 > idade >= 18:
        return f'Com {idade} anos: Voto OBRIGATÓRIO.'


print('-' * 32)
ano_nascimento = int(input('Informe o ano de seu nascimento: '))
print(voto(ano_nascimento))
