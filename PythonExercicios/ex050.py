#lendo seis números inteiros e fazendo a soma apenas dos números pares
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um numero inteiro: '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Você informou {} números PARES e a soma total deles é igual a {}.'.format(cont,soma))