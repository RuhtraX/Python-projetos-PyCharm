from math import sqrt,floor
num = input('digite um numero: ')
while not num.isnumeric():
	print(f'{num} não é um número. Tente novamente.')
	num = input('digite um numero: ')
num = int(num)
raiz = sqrt(num)
print('a raiz quadrada de {} é igual a {}'.format(num,floor(raiz)))
