#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
# perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
idade = cont = conth = contm = 0
while True:
    idade = int(input('Digite sua idade: '))
    if idade >= 18:
        cont = cont + 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        conth = conth + 1
    if sexo == 'F' and idade < 20:
        contm = contm + 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if opcao == 'N':
        break
print('''Total de pessoas maiores de 18 é igual a {} pessoas,
{} homens cadastrados e {} mulheres com menos de 20 anos.'''.format(cont, conth, contm))
print('Acabou')