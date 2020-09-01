#comida = str(input('Qual é a minha comida favorita? ')).upper()
#cont = 1
#opcao = 'COMIDA JAPONESA'
#if cont == 1 and comida == opcao:
    #print('Parabéns! Vc me conhece mesmo. Precisou apenas de {} tentativa!'.format(cont))
#while comida != opcao:
    #cont = cont + 1
    #print('Você errou. Tente novamente.')
    #comida = str(input('Qual é a minha comida favorita? ')).upper()
    #if cont <= 3 and comida == opcao:
        #print('Eita, ja tava achando que não me conhecia. Vc precisou de {} tentativas.'.format(cont))
    #if cont > 4 and comida == opcao:
        #print('Vc não me conhece mesmo. Vc precisou de {} tentativas.'.format(cont))
from time import sleep
n = int(input('Digite um número: '))
    
opcao = 0
while opcao != 4:
    sleep(1)
    print('''    1 - somar
    2 - dividir total da soma
    3 - novos números
    4 - sair''')
    opcao = int(input('Qual a sua escolha: '))
    if opcao == 1:
        print('A soma de todos os números é igual a {}'.format(soma))
    elif opcao == 2:
        ndivisor = int(input('Por qual número vc quer dividir: '))
        resultado = soma / ndivisor
        print('{} divididos por {} é igual a {}'.format(soma, ndivisor, resultado))
    elif opcao == 3:
        print('Digite os novos números abaixo')
        for c in range(1, 6):
            n = int(input('Digite um número: '))
            soma = soma + n
    elif opcao == 4:
        sleep(1)
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida. Tente novamente')
    print('-='*16)