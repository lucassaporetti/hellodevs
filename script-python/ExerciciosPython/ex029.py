velocity = float(input('Qual a velocidade do carro? '))
if velocity > 80:
    print('Você ultrapassou a velocidade de 80km/h e foi multado!\n'
          'Por ter ultrapassado {}km/h acima do limite,\n'
          'sua multa será de: R${:.2f}'.format(velocity - 80, (velocity - 80)*7))
else:
    print('Parabéns! Sua velocidade está dentro do limite de 80km/h!')
