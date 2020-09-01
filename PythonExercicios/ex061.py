# refazer o exercicio 51. mostrar a progressão aritimética dos
# 10 primeiros termos de um número
primeirotermo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
print('{} > '.format(primeirotermo), end='')
while cont <= 9:
    primeirotermo = primeirotermo + razao
    cont = cont + 1
    print('{} > '.format(primeirotermo), end='')
print('FIM')
