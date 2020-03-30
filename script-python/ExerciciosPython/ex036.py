print('CALCULADORA PARA APROVAÇÃO DE EMPRÉSTIMO\n'+'-' * 40)

house_value = float(input('Qual é o valor da casa? R$'))
buyer_salary = float(input('Qual é o salário do comprador? R$'))
years_installment = int(input('Em quantos anos ele irá pagar? '))
portion = house_value / (years_installment * 12)

if portion > (buyer_salary * 30) / 100:
    print('\nCRÉDITO NÃO APROVADO!\n'
          'A PARCELA DE R${:.2f} ESTÁ ACIMA DO LIMITE DE 30% DO SALÁRIO DO COMPRADOR!'.format(portion))
else:
    print('\nCRÉDITO APROVADO!\n'
          'A PARCELA DE R${:.2f} ESTÁ DENTRO DO LIMITE DE 30% DO SALÁRIO DO COMPRADOR!'.format(portion))
