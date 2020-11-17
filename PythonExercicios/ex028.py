#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
# venceu ou perdeu.
from random import choice
from time import sleep
lista=[0,1,2,3,4,5]
n=choice(lista)
adivinha=int(input('Qual foi o número escolhido pelo computador? '))
print('PROCESSANDO...')
sleep(2)
if n==adivinha:
    print('PARABÉNS, vc acertou!')
else:
    print('O Computador ganhou.')
print('O computador escolheu {}'.format(n))