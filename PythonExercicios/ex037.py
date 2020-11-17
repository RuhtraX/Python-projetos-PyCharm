#Escreva um programa em Python que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
from time import sleep
print('CONVERSOR DE NÚMEROS')
num = int(input('Digite um número inteiro: '))
print('''Escolha a base para conversão: 
[1] - para BINÁRIO
[2] - para OCTAL
[3] - para HEXADECINAL''')
escolha = int(input())
if escolha == 1:
    print('{} em BINÁRIO é igual a {}'.format(num,bin(num)[2:])) # a expressão [2:] significa que ele vai fatiar a string  e mostrar o valor apenas do terceiro caracter em diante começando pelo 0
elif escolha == 2:
    print('{} em OCTAL é igual a {}'.format(num,oct(num)[2:]))
elif escolha == 3:
    print('{} em HEXADECIMAL é igual a {}'.format(num,hex(num)[2:]))
else:
    sleep(1)
    print('Opção inválida. Tente novamente!')