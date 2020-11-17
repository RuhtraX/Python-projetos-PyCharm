#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
# você deve mostrar, para cada palavra, quais são as suas vogais.

#palavras = ('Ramo', 'Ralador', 'Bola', 'Escorregador', 'Rinoceronte', 'Rim', 'Helicóptero', 'Branco', 'Elefante', 'Facebook')
#for c in palavras:
#    print('\nNa palavra {} tem as vogais '.format(c.upper()), end='')
#    for vogal in c:
#        if vogal in 'aeiou':
#            print(vogal, end=' ')

from random import randint
lista = (randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60))
print(sorted(lista))
#print(min(lista), max(lista))