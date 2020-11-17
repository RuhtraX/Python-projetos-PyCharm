# Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

#n = int(input('Digite um número inteiro: '))
n = 0
cont = 0
total = 0
#total = n
while n != 999:
    n = int(input('Digite um número inteiro: '))
    cont = cont + 1
    total = total + n
    if cont == 1:
        maior = n
        menor = n
    else:
        if n != 999 and n > maior:
            maior = n
        if n < menor:
            menor = n
media = (total - 999) / (cont - 1) # esse -1 é referente ao 999 que é ponto de parada
print('''A média entre os valores é igual {}, 
o maior número digitado foi {} e o menor número foi {}.'''.format(media,maior,menor))

