soma = 0
count = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número inteiro: '.format(c)))
    if n % 2 == 0:
        soma += n
        count += 1
print('Você informou {} números pares e a soma deles é {}.'.format(count, soma))
