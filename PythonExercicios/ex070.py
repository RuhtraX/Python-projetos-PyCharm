#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário
# vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
preco = total = contproduto = 0
while True:
    produto = str(input('Digite o nome do produto: '))
    nomeproduto = produto
    preco = float(input('Digite o valor do prduto: R$ '))
    total = total + preco
    if preco > 1000.00:
        contproduto = contproduto + 1
    maisbarato = preco
    if preco < maisbarato:
        maisbarato = nomeproduto
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if opcao == 'N':
        break
print('''Total da compra igual a R$ {:.2f}.
{} produtos custam mais de R$ 1.000,00.
O produto mais barato é {}.'''.format(total, contproduto, nomeproduto))