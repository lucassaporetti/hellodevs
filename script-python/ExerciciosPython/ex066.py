count = 0
soma = 0
while True:
    num = int(input('Digite um número: [999 p/ sair]  '))
    if num == 999:
        break
    count = count + 1
    soma = soma + num
print(f'A soma dos {count} valores foi {soma}.')
