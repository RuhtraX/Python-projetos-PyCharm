#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario=float(input('qual o valor do salário? '))
aumento=(salario*15)/100
salfinal=salario+aumento
print('o valor final do salário com aumento\nde 15% é igual a {} reais'.format(salfinal))
