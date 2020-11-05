from time import sleep
valores = []
while True:
    numero = int(input('Digite um número: '))
    if numero not in valores:
        valores.append(numero)
        sleep(0.5)
        print('\033[33mValor adicionado com sucesso.\033[m')
    else:
        print('\033[7mValor já cadastrado.\033[m')
    resposta = str(input('Quer continuar [S/N]? '))[0]
    if resposta not in 'SsNn':
        print('\033[31mOpção inválida!\033[m')
    if resposta in 'Nn':
        break
print('-='*20)
print('Os valores digitados foram: ', end='')
print(sorted(valores))

