print('{:=^40}'.format(' RAFOLI STORE '))
produto = float(input('Qual o valor do produto: R$ '))
print('''Digite a forma de pagamento: 
[1]-À vista dinheiro/cheque 
[2]-À vista cartão 
[3]-Até 2x no cartão 
[4]-3x ou mais no cartão''')
fpgto = int(input())
if fpgto == 1:
    print('O valor total é igual a R$ {:.2f}.'.format(produto-(produto*0.10)))
elif fpgto == 2:
    print('O valor total é igual a R$ {:.2f}.'.format(produto-(produto*0.05)))
elif fpgto == 3:
    print('Em quantas parcelas? ')
    opção = int(input())
    if opção == 1:
        print('O valor total é igual a R$ \033[33m{:.2f}\033[m.'.format(produto))
    elif opção == 2:
        print('O valor total é igual a R$ \033[33m{:.2f}\033[m sendo em {}x pacelas de R$ {:.2f}.'.format(produto,opção,produto/opção))
    else:
        print('Opção inválida! Tente novamente.')
elif fpgto == 4:
    print('Em quantas parcelas? ')
    opção = int(input())
    if opção < 3:
        print('Opção inválida! Tente novamente.')
    else:
        prodcomj = produto + produto*0.20
        print('O valor total é igual a R$ {:.2f} sendo em {}x parcelas de R$ {:.2f}'.format(prodcomj,opção,prodcomj/opção))
else:
    print('Opção inválida. Tente novamente.')
