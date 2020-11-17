#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.
valores = []
while True:
    valores.append(int(input('Digite um número: ')))
    resposta = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if resposta not in 'SN':
        print('Opção inválida!')
    if resposta == 'N':
        break
print('-='*25)
print('Os valores digitados foram: {}.'.format(valores))
print('-='*25)
print('Foram digitados {} números'.format(len(valores)))
valores.sort(reverse=True)
print('Os números digitados na ordem inversa: {}'.format(valores))
if 5 in valores:
    print('O valor 5 foi encontrado.')
else:
    print('O valor 5 não foi digitado.')
