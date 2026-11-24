n1 = input('Digite um número: ')
while not n1.isnumeric():
	print(f'{n1} não é um número. Tente novamente.')
	n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')
while not n2.isnumeric():
	print(f'{n2} não é um número. Tente novamente.')
	n2 = input('Digite outro número: ')
n1 = int(n1)
n2 = int(n2)
s = n1 + n2
print(f'A soma entre {n1} e {n2} vale {s}')
