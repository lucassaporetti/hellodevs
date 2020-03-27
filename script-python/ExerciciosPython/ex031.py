distance = int(input('Qual será a distância percorrida durante a sua viagem? '))
if distance <= 200:
    print('Para a distância de {}km sua passagem custará R${:.2f}'
          .format(distance, 0.5 * distance))
else:
    print('Para a distância de {}km sua passagem custará R${:.2f}'
          .format(distance, 0.45 * distance))
