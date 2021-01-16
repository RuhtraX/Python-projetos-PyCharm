#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos
#jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
numero = int(input('Quantos jogos você quer sortear? '))
sorteio = (randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60))
n = []
for c in range(0, numero):
    if sorteio[0] or sorteio[1] or sorteio[2] or sorteio[3] or sorteio[4] or sorteio[5] not in n:
        #if randint(1, 60) not in n:
            n.append(sorted(sorteio))
print(n)


