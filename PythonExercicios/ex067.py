#Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
n = 0
resp = ''
while True:
    n = int(input('Digite um número inteiro: '))
    if n < 0:
        break
    else:
        for c in range(1, 11):
            print('{} x {} = \033[34m{}\033[m'.format(n, c, n*c))
    resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resp != 'S':
        break
print('Acabou')