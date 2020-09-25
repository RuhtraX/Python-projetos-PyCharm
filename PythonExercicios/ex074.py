from random import randint
numeros = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))
print('Os números sorteados foram: ', end='')
for c in numeros:
    print('{} '.format(c), end='')
print('''\nO maior valor sorteado foi {}
e o menor foi {}.'''.format(max(numeros), min(numeros)))
