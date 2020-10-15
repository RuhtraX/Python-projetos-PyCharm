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
    if v == maior:                                                     ###### ARRUMAR ########3
        print('{}...'.format(index))
    if v == menor:
        print('{}...'.format(index))
print('O MAIOR número encontrado foi {} e ele está na {}ª posição'.format(maior, index))
print('O MENOR número encontrado foi {} e ele está na {}ª posição'.format(menor, index)



