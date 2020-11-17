#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print('-'*35)
print('Os números digitados foram ', end='')
for c in numeros:
    print('{} '.format(c), end='')
print('')
print('-'*35)
print('\nO número 9 apareceu {} vezes'.format(numeros.count(9))) #comando para contar a qtde de vezes que algo apareceu
if 3 in numeros:
    print('O número 3 apareceu pela primeira vez na posição {}'.format(numeros.index(3)+1))#comando verifica a posição em que algo apareceu
else:
    print('O valor 3 não foi digitado')
print('Os números pares digitados foram ', end='')
for c in numeros:
    if c % 2 == 0:
        print('{} '.format(c), end='')