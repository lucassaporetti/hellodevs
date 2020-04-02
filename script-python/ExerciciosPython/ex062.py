print('=' * 30 + '\n     10 TERMOS DE UMA PA\n' + '=' * 30)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, end=' → ')
        termo = termo + razao
        cont += 1
    print('PAUSA!')
    mais = int(input('Gostaria de mais termos? Se não, digite [0]. se sim, digite quantos: '))
print('Progressão finalizada com {} termos.'.format(total))
