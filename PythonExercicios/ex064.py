# ler vários números inteiros e só parar qdo o usuário digitar 999. Ao final mostrar qtos numeros
# foram digitados e mostrar a soma entre eles desconsiderando o 999 que é a condição de parada.
n = int(input('Digite um número inteiro: '))
cont = 1
total = n
while n != 999:
    n = int(input('Digite outro número inteiro: '))
    cont = cont + 1
    total = total + n
print('Foram declarados {} números e a soma entre eles é igual a {}.'.format(cont-1,total-999))
