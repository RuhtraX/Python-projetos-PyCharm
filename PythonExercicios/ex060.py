# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex.: 5  - fatorial de 5 é: 5*4*3*2*1=120

#num = int(input('Digite um número inteiro para saber o seu fatorial: '))
#c = num
#fat = 1
#print('Calculando {}! = '.format(num), end='')
#while c > 0:
    #print('{}'.format(c), end='')
    #print(' x ' if c > 1 else ' = ', end='')
    #fat *= c
    #c -= 1
#print('{}'.format(fat))


#from math import factorial
#num = int(input('Digite um número inteiro para saber o seu fatorial: '))
#print(factorial(num))

from math import factorial
num = int(input('Digite um número inteiro para saber o seu fatorial: '))
for c in range(num,0,-1):
    print('{} '.format(c), end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
print(factorial(num))
