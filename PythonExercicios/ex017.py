#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.
from math import hypot
co=float(input('qual o comprimento do cateto oposto? '))
ca=float(input('qual o comprimento do cateto adjacente? '))
hi=(co**2 + ca**2)**(1/2)
print('o comprimento da hipotenusa é igual a {:.2f}'.format(hi))

co=float(input('qual o comprimento do cateto oposto? '))
ca=float(input('qual o comprimento do cateto adjacente? '))
hi=hypot(co,ca)
print('o comprimento da hipotenusa é igual a {:.2f}'.format(hi))

