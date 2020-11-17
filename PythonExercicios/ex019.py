#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
nome1=(input('digite o nome do primeiro aluno: '))
nome2=(input('digite o nome do segundo aluno: '))
nome3=(input('digite o nome do terceiro aluno: '))
nome4=(input('digite o nome do quarto aluno: '))
lista=[nome1,nome2,nome3,nome4]
escolhido=choice(lista)
print('o aluno escolhido foi: {}'.format(escolhido))

