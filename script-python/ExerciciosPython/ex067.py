while True:
    count = 0
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    print('-' * 30)
    while count < 10:
        count = count + 1
        print(f'{num} x {count} = {num * count}')
    print('-' * 30)
print('\nOk! Programa de tabuada encerrado!')
