print('=' * 30 + '\n     10 TERMOS DE UMA PA\n' + '=' * 30)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro_termo + (10 * razao)
for c in range(primeiro_termo, decimo, razao):
    print(c, end=' → ')
print('ACABOU!')
