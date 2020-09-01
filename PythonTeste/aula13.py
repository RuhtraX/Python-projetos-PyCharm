for c in range(0, 6):
    print('oi')
print('fim')

for c in range(1, 7): # contagem de 1 até 6 pq o último digito o programa ignora, por isso se faz de 1 a 7
    print(c)
print('fim')

for c in range(6, 0, -1):# o "-1" no final é para fazer de trás para frente
    print(c)
print('fim')

for c in range(0, 7, 2): # contagem de 0 a 6 pulando de dois em dois
    print(c)
print('fim')

s = 0
for c in range(0, 5):
    n1 = int(input('Digite um número: '))
    s = s + n1
print('A soma de todos os números é igual a {}'.format(s))