#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os
# valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
valores = []
pares = []
impares = []
while True:
    n = int(input('Digite um número: '))
    valores.append(n)
    if n in valores and n %2 == 0:
        pares.append(n)
    if n in valores and n %2 == 1:
        impares.append(n)
    resposta = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if resposta not in 'SN':
        print('Opção inválida!')
    if resposta == 'N':
        break
print('Números digitados: {}.'.format(valores))
print('Números PARES digitados: {}.'.format(pares))
print('Números ÍMPARES digitados: {}.'.format(impares))
