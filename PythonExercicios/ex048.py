#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se
# encontram no intervalo de 1 até 500.
soma = 0
cont = 0
for c in range(1, 501, 2): #contagem de 1 a 500 pulando de 2 em 2 para mostrar apenas os ímpares
    if c % 3 == 0:#condição para mostrar se o número é multiplo de 3
        soma = soma + c
        cont = cont + 1
print('A soma dos {} valores solicitados é igual a {}.'.format(cont, soma))

soma2 = 0
cont2 = 0
for i in range(1989, 3528, 2):
    if i % 19 == 0:
        soma2 = soma2 + i
        cont2 = cont2 + 1
print('A soma dos {} valores solicitados é igual a {}.'.format(cont2,soma2))

for c in range(5, 101, 5):
    print(c)
for c in range(102, 201, 2):
    print(c)