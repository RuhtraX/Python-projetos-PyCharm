n=int(input('\033[1;30;42mdigite um número inteiro: \033[m'))
suc=n+1
ant=n-1
print('\033[31mo antecessor de\033[m \033[32m{}\033[m é \033[33m{}\033[m e o sucessor é \033[34m{}\033[m'.format(n,ant,suc))

n=int(input('digite um número inteiro: '))
print('o antecessor de {} é {} e o sucessor é {}'.format(n,(n-1),(n+1)))