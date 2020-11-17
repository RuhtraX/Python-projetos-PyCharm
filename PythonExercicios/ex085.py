#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
numeros = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input('Digite o {}º valor: '.format(c)))
    if valor %2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('Os números digitados foram: {}'.format(numeros))
print('Os números pares em ordem foram {}'.format(sorted(numeros[0])))
print('Os números ímpares em ordem foram {}'.format(sorted(numeros[1])))





