salary = float(input('Qual é o salário do funcionário? R$'))
if salary >= 1250.00:
    print("Seu aumento será de 10%."
          " Novo salário: R${:.2f}".format(salary * 10 / 100 + salary))
else:
    print("Seu aumento será de 15%. "
          "Novo salário: R${:.2f}".format(salary * 15 / 100 + salary))
