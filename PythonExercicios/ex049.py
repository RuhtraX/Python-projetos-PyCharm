#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('digite um número inteiro: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n*c))
