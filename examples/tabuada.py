#!/usr/bin/env python3

qty = int(input("Quantity: "))
num = int(input("Number: "))
num_array = range(int(qty))

print(f"Printing {qty} numbers for factor {num} ...")
print('-'*35)
cols = (
    [str(f'{even} * {num} = {even*num} ') for even in num_array if even % 2 == 0],
    [str(f'{odd} * {num} = {odd*num} ') for odd in num_array if odd % 2 != 0]
)
for i in range(len(cols[0])):
    if len(cols[1]) > i:
        print('{:20}  {}'.format(cols[0][i], cols[1][i]))
    else:
        print('{}'.format(cols[0][i]))
print('-'*35)
