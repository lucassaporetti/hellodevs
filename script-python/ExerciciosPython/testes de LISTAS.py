# num = [8, 5, 4, 3, 9]
# num[2] = 8
# num.sort(reverse=True)
# del num[4]
# num.pop(1)
# num.pop()
# num.remove(9)
# num.append(7)
# num.insert(0, 4)
# if 4 in num:
#     num.remove(4)
# else:
#     num.insert(1, 77)
#
# print(num)
#
# print(f'Essa lista tem {len(num)} elementos.')


# valores = list()
# valores.append(5)
# valores.append(6)
# valores.append(3)
#
# for p, v in enumerate(valores):
#     print(f'Na posição {p} encontrei o valor {v}.')


valores = list()
for cont in range(0, 5):
    valores.append(input('Digite um valor: '))

for p, v in enumerate(valores):
    print(f'Na posição {p} encontrei o valor {v}.')


