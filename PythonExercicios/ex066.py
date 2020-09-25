n = 0
cont = 0
soma = 0
while True:
    n = int(input('Digite um número inteiro [999 para parar]: '))
    if n == 999:
        break
    cont = cont + 1
    soma = soma + n
print('Você digitou {} números e o valor da soma entre eles é igual a {}'.format(cont,soma))

