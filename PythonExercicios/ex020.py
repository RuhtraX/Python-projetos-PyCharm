#O mesmo professor do desafio 019 quer sortear a ordem de apresentação
#de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
n1=(input('primeiro aluno: '))
n2=(input('segundo aluno: '))
n3=(input('terceiro aluno: '))
n4=(input('quarto aluno: '))
lista=[n1,n2,n3,n4]
shuffle(lista)
print('A ordem de apresentação é {}'.format(lista))