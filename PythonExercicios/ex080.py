#Crie um programa onde o usuário possa digitar cinco valores
# numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.
valores = []
for c in range(0,5):
    n = int(input('Digite um número: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                break
            pos += 1
print('Os valores digitados foram: {}'.format(valores))
