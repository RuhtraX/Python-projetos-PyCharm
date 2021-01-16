#Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
lista1 = [[], [], []]
n = int(input('Digite um numero: '))
lista1[0].append(n)
n = int(input('Digite um numero: '))
lista1[1].append(n)
n = int(input('Digite um numero: '))
lista1[2].append(n)

lista2 = [[], [], []]
n = int(input('Digite um numero: '))
lista2[0].append(n)
n = int(input('Digite um numero: '))
lista2[1].append(n)
n = int(input('Digite um numero: '))
lista2[2].append(n)

lista3 = [[], [], []]
n = int(input('Digite um numero: '))
lista3[0].append(n)
n = int(input('Digite um numero: '))
lista3[1].append(n)
n = int(input('Digite um numero: '))
lista3[2].append(n)

print(lista1)
print(lista2)
print(lista3)

###SUGESTÃO PROFESSOR
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input('Digite um valor para a {} e {}: '.format(linha, coluna)))
print('-='*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
