def notas(*grades, sit=False):
    """
    Função para analisar notas e situações de vários alunos
    :param grades:lista com todas as notas do aluno
    :param sit:valor opcional: situação do aluno
    :return:dicionário com várias informações sobre a situação do aluno
    """
    soma = sum(grades)
    maior = max(grades)
    menor = min(grades)
    media = round(soma / len(grades), 1)
    dic = {'total': soma, 'maior': maior, 'menor': menor, 'media': media}
    if sit:
        if media < 5:
            dic['situação'] = 'RUIM'
        elif 5 <= media < 7:
            dic['situação'] = 'RAZOÁVEL'
        else:
            dic['situação'] = 'BOA'
    return dic


resp = notas(5.5, 2, 5.3, 2, 6.5, sit=True)
print(resp)
