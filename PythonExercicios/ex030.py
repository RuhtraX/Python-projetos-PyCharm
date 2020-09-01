from time import sleep
numero = int(input('Digite um número inteiro: '))
resultado = numero % 2
print('PROCESSANDO...')
if resultado == 0:
    sleep(1)
    print('{} é um número PAR.'.format(numero))
else:
    sleep(1)
    print('{} é um número ÍMPAR.'.format(numero))