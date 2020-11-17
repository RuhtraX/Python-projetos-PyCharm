#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
vlprod=float(input('qual o valor do produto? R$ '))
desc=(vlprod*5)/100
pcofinal=vlprod-desc
print('o valor do produto com desconto de 5% é igual a R$ {:.2f}'.format(pcofinal))