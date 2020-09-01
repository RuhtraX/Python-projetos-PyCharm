nome=input('qual seu nome? ')
print('prazer em te conhecer {:=^20}!'.format(nome))

n1=int(input('digite um valor: '))
n2=int(input('digite outro valor: '))
s=n1+n2
sub=n1-n2
d=n1/n2
m=n1*n2
pt=n1**n2
di=n1//n2
restdiv=n1%n2
print('soma é igual a {}, subtração é igual a {},'.format(s,sub))
print('divisão é igual a {:.2f},\n multiplicação é igual a {},'.format(d,m))
print('potência é igual a {},\n divisão inteira é igual a {}'.format(pt,di), end=' ')
print('e resto da divisão é igual a {}'.format(restdiv))
