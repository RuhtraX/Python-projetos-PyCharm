#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input('quanto de dinheiro você tem em reais? R$ '))
dolar = real / 4.32
euro = real / 4.69
pesoarg = real / 0.070
pesocol = real / 0.0013
print('{:.2f} reais equivale a {:.2f} em dólares'.format(real, dolar))
print('{:.2f} reais equivale a {:.2f} em euros'.format(real, euro))
print('{:.2f} reais equivale a {:.2f} em pesos argentinos'.format(real, pesoarg))
print('{:.2f} reais equivale a {:.2f} em pesos colombianos'.format(real, pesocol))
