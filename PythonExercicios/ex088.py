#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos
#jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

#MINHA TENTATIVA FRUSTRADA
#from random import randint
#numero = int(input('Quantos jogos você quer sortear? '))
#n = []
#for c in range(0, numero):
#    sorteio = (randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60))
#    if sorteio[0] and sorteio[1] and sorteio[2] and sorteio[3] and sorteio[4] and sorteio[5] not in n:
#        n.append((sorteio))
#    else:
#        sorteio = (randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60))
#print(n)

#SUGESTÃO DO PROFESSOR
from random import randint
from time import sleep
lista = list()
jogos = list()
print('------Jogo da MegaSena------')
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('------SORTEANDO {} JOGOS------'.format(quant))
for i, l in enumerate(jogos):
    print('Jogo {} : {}'.format(i+1, l))
    sleep(1)
print('========BOA SORTE!========')



