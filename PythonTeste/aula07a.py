nome=input('qual seu nome? ')
print('prazer em te conhecer {:=^20}!'.format(nome))

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
s=n1+n2
sub=n1-n2
d=n1/n2
m=n1*n2
pt=n1**n2
di=n1//n2
restdiv=n1%n2
print(f'\n soma é igual a {s},\n subtração é igual a {sub},')
print(' divisão é igual a {:.2f},\n multiplicação é igual a {},'.format(d,m))
print(f' potência é igual a {pt},\n divisão inteira é igual a {di}',end=' ')
print(f'e resto da divisão é igual a {restdiv}')
