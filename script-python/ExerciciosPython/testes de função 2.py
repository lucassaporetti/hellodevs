#função help para procurar documentação a respeito de determinada função:
# help(print)
#ou:
# print(print.__doc__)

#criando uma docstring de uma nova função:
# def contador(i, f, p):
#     """
#     Faz uma montagem e mostra na tela.
#     :param i: início da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     Função criada por Lucas saporetti
#     """


# def funcao(b):
#     b = b + 4# vai pegar a variavel de fora para somar
#     global a# agora só vale o a de dentro. Isso afeta lá fora.
#     a = 4
#     print(f'N1 local vale {a}')
#     print(b)
#
#
# a = 2# soma com b lá em cima
# funcao(a)# variável local não afeta a de fora.
# print(f'N1 global vale {a}')


# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     return s   #chama o s novamente e o linka a uma nova variável
#
#
# r1 = somar(3, 2, 5)
# r2 = somar(2, 2)
# r3 = somar(6)
#
# print(f'Os resultados foram {r1}, {r2} e {r3}')


# def fatorial(num=1):
#     f = 1
#     for cont in range(num, 0, -1):
#         f = f * cont
#     return f
#
#
# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial(1)
#
# print(f'Os resultados são {f1}, {f2} e {f3}')


# def par(n=0):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#
#
# num = int(input('Digite um número: '))
# if par(num):
#     print(f'{num} é par!')
# else:
#     print(f'{num} não é par!')
