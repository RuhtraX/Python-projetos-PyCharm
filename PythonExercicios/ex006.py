n=int(input('digite um número: '))
dob=n*2
tri=n*3
raiz=n**(1/2)
print('dobro de {} é igual a {}, o triplo é igual a {}'.format(n,dob,tri), end=' ')
print('e a raiz quadrada é igual a {:.2f}'.format(raiz))

print('dobro de {} é igual a {},\no triplo é igual a {},\ne a raiz quadrada é igual a {:.2f}'.format(n,dob,tri,raiz))



n=int(input('digite um número: '))
print('dobro de {} é igual a {}, o triplo é igual a {}'.format(n,(n*2),(n*3)), end=' ')
print('e a raiz quadrada é igual a {:.2f}'.format((n**(1/2))))