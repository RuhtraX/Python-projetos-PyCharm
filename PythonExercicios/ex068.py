from time import sleep
from random import randint
print('JOGO DO PAR OU ÍMPAR')
cont = 0
jogador = 0
escolha = ''
total = 0
while True:
    print('')
    jogador = int(input('Digite um número de 1 a 10: '))
    while jogador < 0 or jogador > 10:
        print('Valor inválido! Tente novamente.')
        jogador = int(input('Digite um número de 1 a 10: '))
    escolha = str(input('Você quer par[P] ou ímpar[I]? ')).strip().upper()[0]
    while escolha not in 'PpIi':
        print('Valor inválido! Tente novamente.')
        escolha = str(input('Você quer par[P] ou ímpar[I]? ')).strip().upper()[0]
    computador = randint(0, 10)
    total = jogador + computador
    sleep(1)
    print('Computador escolheu {}'.format(computador))
    print('O total é igual a {}.'.format(total))
    if escolha == 'P':
        if total % 2 == 0:
            print('Você ganhou.')
            cont = cont + 1
        else:
            print('Você perdeu! Você ganhou {} vezes consecutivas.'.format(cont))
            break
    if escolha == 'I':
        if total % 2 != 0:
            print('Você ganhou.')
            cont = cont + 1
        else:
            print('Você perdeu! Você ganhou {} vezes consecutivas.'.format(cont))
            break
print('GAME OVER')
