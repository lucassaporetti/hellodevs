print('CALCULADORA DE IMC\n' + '-' * 18)

peso = float(input('Digite seu peso: (kg) '))
altura = float(input('\nDigite a sua altura: (m) '))
imc = peso / (altura ** 2)

print('\nSeu imc é de {:.1f}.'.format(imc))

if imc < 18.5:
    print('\nCuidado! Você está abaixo do peso!')
elif imc < 25:
    print('\nParabéns! Você está no peso ideal!')
elif imc < 30:
    print('\nAtenção! Você está com sobrepeso!')
elif imc < 40:
    print('\nMuita atenção! Você está com obesidade!')
else:
    print('Cuidado! Você está com obesidade mórbida!')
