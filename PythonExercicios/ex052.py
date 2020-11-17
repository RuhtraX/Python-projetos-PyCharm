#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um número inteiro: '))
tot = 0 #contabiliza quantas vezes o número foi divisível por um contador(c)
for c in range(1, num+1): #faz uma contagem de 1 até o numero escolhido
    if num % c == 0: #verifica se o numero é divisível pelo contador
        print('\033[32m', end=' ')
        tot += 1 #igual a tot = tot + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('Por isso é um número PRIMO!')
else:
    print('Por isso NÃO é um número PRIMO!')

#MINHA SOLUÇÃO....EM CIMA É DO PROFESSOR GUSTAVO GUANABARA
n = int(input('Digite um número: '))
cont = 0
for c in range(1, n+1):
    print(c, end=' ')
    if n % c == 0:
        cont = cont + 1
if cont == 2:
    print('\né primo')
else:
    print('\nNÃO é primo')

