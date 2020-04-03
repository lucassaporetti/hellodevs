print('=' * 30)
print('{:^30}'.format('BANCO SAPORETTI'))
print('=' * 30)

valorSaque = int(input('Valor do saque: R$ '))
print('-' * 40)

NOTAS = [100, 50, 20, 10, 5, 2]
NOTAS_RET = {"100": 0, "50": 0, "20": 0, "10": 0, "5": 0, "2": 0}
MAX_NOTAS = 5
TOT_NOTAS = 0

while valorSaque > 0:
    for nota in NOTAS:
        quantidade = min(MAX_NOTAS, valorSaque // nota)
        valorSaque -= quantidade * nota
        if quantidade > 0:
            NOTAS_RET[f"{nota}"] += quantidade
        if valorSaque == 0:
            break

for n, q in NOTAS_RET.items():
    TOT_NOTAS += q
    print("{} notas de {}".format(q, n))

print(f'Total de cédulas ao todo: {TOT_NOTAS}')
print('=' * 30)
print('Volte sempre ao BANCO SAPORETTI! Tenha um bom dia!')
