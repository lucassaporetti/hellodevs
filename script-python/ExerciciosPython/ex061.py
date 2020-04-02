print('=' * 30 + '\n     10 TERMOS DE UMA PA\n' + '=' * 30)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
while cont <= 10:
    print(termo, end=' → ')
    termo = termo + razao
    cont += 1
print('ACABOU!')
