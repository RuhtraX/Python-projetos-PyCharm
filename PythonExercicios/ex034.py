salario = float(input('Qual o valor do salário do funcionário? '))
if salario > 1250.00:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
print('O novo valor do salário com reajuste é de {}'.format(salario+aumento))