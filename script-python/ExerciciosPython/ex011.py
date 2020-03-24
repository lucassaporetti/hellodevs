la = float(input('Informe a largura da parede: '))
al = float(input('Informe a altura da parede: '))
ar = la * al
qt = ar / 2
print('A área da parede é de {:.2f}m² e a quantidade de'
      ' tinta necessária para pintá-la será {:.2f} litros.'.format(ar, qt))
