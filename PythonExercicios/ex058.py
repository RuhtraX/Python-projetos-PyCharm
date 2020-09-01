from random import choice
lista=[0,1,2,3,4,5,6,7,8,9,10]
n=choice(lista)
cont = 1
adivinha=int(input('Qual foi o número escolhido pelo computador? '))
while adivinha != n:
    if adivinha > n:
        print('Você errou. É MENOS.')
    if adivinha < n:
        print('Você errou. É MAIS.')
    cont = cont + 1
    adivinha = int(input('Qual foi o número escolhido pelo computador? '))
print('Você acertou, porém precisou de {} tentativas para conseguir.'.format(cont))

#from random import randint
#computador = randint(0, 10)
#print('Eu, computador, pensei em um número de 0 a 10. Tente adivinhar.')
#acertou = False
#palpites = 0
#while not acertou:
    #jogador = int(input('Qual seu palpite: '))
    #palpites = palpites + 1
    #if jogador == computador:
        #acertou = True
    #else:
        #if jogador < computador:
            #print('é mais...')
        #elif jogador > computador:
            #print('é menos')
#print('Você acertou, porém precisou de {} tentativas para conseguir.'.format(palpites)')
