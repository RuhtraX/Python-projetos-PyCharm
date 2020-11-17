# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os
# 10 primeiros termos da progressão usando a estrutura while.
primeirotermo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
print('{} > '.format(primeirotermo), end='')
while cont <= 9:
    primeirotermo = primeirotermo + razao
    cont = cont + 1
    print('{} > '.format(primeirotermo), end='')
print('FIM')
