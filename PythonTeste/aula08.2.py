from math import sqrt
num=input('digite um número: ')
while not num.isnumeric():
	print(f'{num} não é um número. Tente novamente.')
	num=input('digite um número: ')
num = int(num)
raiz=sqrt(num)
print('a raiz de {} é igual a {:.2f}'.format(num,raiz))

import emoji
print(emoji.emojize('Olá Mundo :earth_americas:', use_aliases=True))

import random
n = random.randint(1,60)
print(n)