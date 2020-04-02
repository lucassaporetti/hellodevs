count = soma = num = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        soma = soma + num
        count = count + 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(count, soma))
