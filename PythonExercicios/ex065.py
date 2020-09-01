# ler vários números inteiros e só parar qdo o usuário digitar 999. Ao final mostrar a média
# entre todos os números que foram digitados e mostrar o maior e menor valor digitados.
n = int(input('Digite um número inteiro: '))
cont = 0
total = n
while n != 999:
    n = int(input('Digite outro número inteiro: '))
    cont = cont + 1
    total = total + n
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = (total - 999) / (cont - 1) # esse -1 é referente ao 999 que é ponto de parada
print('''A média entre os valores é igual {}, 
o maior número digitado foi {} e o menor número foi {}.'''.format(media,maior,menor)
