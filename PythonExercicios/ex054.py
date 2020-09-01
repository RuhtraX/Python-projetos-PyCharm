#faz a leitura de 7 datas de nascimento e verifica quantos já atingiram a maioridade e
#quantos ainda não atingiram
from datetime import date
anoatual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    anonasc = int(input('Digite o ano do seu nascimento: '))
    idade = anoatual - anonasc
    if idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print('''O total de pessoas com idade superior ou igual a 18 anos é {}.
E o total de pessoas menores de 18 anos é igual a {}.'''.format(maior, menor))
