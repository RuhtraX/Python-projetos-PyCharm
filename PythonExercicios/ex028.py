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