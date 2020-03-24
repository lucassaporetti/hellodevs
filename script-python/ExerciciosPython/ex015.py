km = float(input('Quantos km foram percorridos? '))
d = int(input('Por quantos dias o veículo foi alugado? '))
p = (km * 0.15) + (d * 60)
print('O preço a pagar pelo aluguel do veículo é de R${:.2f}'.format(p))
