#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
from time import sleep
print('==+' * 10)
print('\033[31mSIMULADOR DE EMPRÉSTIMO\033[m')
print('==+' * 10)
imovel = float(input('Qual o valor da imóvel? '))
salario = float(input('Qual o salário do comprador? '))
anos = int(input('Por quantos anos pretende pagar o imóvel? '))
meses = anos * 12
parcela = imovel / meses
print('O valor da parcela será de R$ \033[4m{:.2f}\033[m.'.format(parcela))
trinta = salario * 0.30
sleep(1)
print('PROCESSANDO...')
sleep(3)
if parcela > trinta:
    print('Sinto muito mas seu empréstimo foi \033[7mNEGADO\033[m.')
else:
    print('Parabéns!!! Seu empréstimo foi \033[32mAPROVADO\033[m.')