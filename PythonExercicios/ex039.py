#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
# do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
anonasc = int(input('Em que ano você nasceu? '))
ano = date.today().year # comando "date" da biblioteca "datetime" para mostrar o ano atual
idade = ano - anonasc
if idade < 18:
    print('''Você tem {} anos e ainda vai se alistar ao Serviço Militar.
Faltam {} ano(os).'''.format(idade,18-idade))
elif idade == 18:
    print('Você tem {} anos. Está na hora de você se alistar ao Serviço Militar.'.format(idade))
else:
    idade > 18
    print('''Você tem {} anos e já passou do tempo de se alistar ao Serviço Militar.
Tempo excedido em {} ano(os).'''.format(idade,idade-18))

