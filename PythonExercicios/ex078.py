#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual
# foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valores = []
maior = 0
menor = 0
for c in range(0, 5):
    valores.append(int(input('Digite um número: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('Os valores digitados foram: ', end='')
print(valores)
for index, v in enumerate(valores):
    if v == maior:
        print('O MAIOR número encontrado foi {} e ele está na {}ª posição'.format(maior, index))
    if v == menor:
        print('O MENOR número encontrado foi {} e ele está na {}ª posição'.format(menor, index))







