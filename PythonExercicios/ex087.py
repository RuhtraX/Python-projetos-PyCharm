#Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = somaterceiracoluna = maior = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input('Digite um valor para a {} e {}: '.format(linha, coluna)))
print('-='*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somapares += matriz[linha][coluna]
    print()
print('A soma de todos os valores pares digitados é igual a {}'.format(somapares))
for linha in range(0, 3):
    somaterceiracoluna += matriz[linha][2]
print('A soma dos valores da terceira coluna é igual a {}'.format(somaterceiracoluna))
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print('O maior valor da segunda linha é igual a {}'.format(maior))
