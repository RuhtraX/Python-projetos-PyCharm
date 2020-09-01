# ler o peso de cinco pessoas e no final mostrar o maior e o menor peso lidos
maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O menor peso lido foi {}Kg e o maior foi {}Kg.'.format(menor,maior))
