num=int(input('Digite um número: '))
n=str(num)
print('Analisando o número {}'.format(num))
print('Unidade igual a {}'.format(n[3]))
print('Dezena igual a {}'.format(n[2]))
print('Centena igual a {}'.format(n[1]))
print('Milhar igual a {}'.format(n[0]))

num=int(input('Digite um número: '))
u=num//1%10
d=num//10%10
c=num//100%10
m=num//1000%10
print('Analisando o número {}'.format(num))
print('Unidade igual a {}'.format(u))
print('Dezena igual a {}'.format(d))
print('Centena igual a {}'.format(c))
print('Milhar igual a {}'.format(m))
