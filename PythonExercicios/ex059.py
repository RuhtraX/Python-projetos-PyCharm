# programa que lê dois valores e mostra um menu na tela.
# o programa deverá realizar a operação em cada caso.
from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    sleep(1)
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair''')
    opcao = int(input('>>>>>Qual a sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('\033[31m{} + {} =\033[m \033[32m{}\033[m'.format(n1, n2, soma))
    elif opcao == 2:
        multiplicacao = n1 * n2
        print('\033[31m{} x {} =\033[m \033[32m{}\033[m'.format(n1, n2, multiplicacao))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('O maior número é \033[32m{}\033[m.'.format(maior))
        elif n2 > n1:
            maior = n2
            print('O maior número é \033[32m{}\033[m.'.format(maior))
        elif n1 == n2:
            print('\033[7mNão há maior entre eles porque os números são iguais.\033[m')
    elif opcao == 4:
        print('Informe os novos números.')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção inválida. Tente novamente.')
print('Fim do programa.')
