# ler nome e quantidade de notas lançadas por dia de 3 pessoas e dizer quanto cada uma lança em
# média em uma semana, em um mês e quem lança mais notas.
from time import sleep
notassemana = 0
notasmes = 0
notassemana1 = 0
notasmes1 = 0
notassemana2 = 0
notasmes2 = 0
notassemana3 = 0
notasmes3 = 0
lancamais = 0
melhoranalista = ''
print('-='*20)
for c in range(1, 4):
    nome = str(input('Digite o nome do {}º analista: '.format(c))).capitalize()
    notasdia = int(input('Quantas notas lança por dia: '))
    notassemana = notasdia * 5
    notasmes = notassemana * 4
    if c == 1:
        notassemana1 = notassemana
        notasmes1 = notasmes
        lancamais = notasmes
        melhoranalista = nome
    if c == 2:
        notassemana2 = notassemana
        notasmes2 = notasmes
        if notasmes > lancamais:
            lancamais = notasmes
            melhoranalista = nome
    if c == 3:
        notassemana3 = notassemana
        notasmes3 = notasmes
        if notasmes > lancamais:
            lancamais = notasmes
            melhoranalista = nome
    print('-=' * 20)
print('')
sleep(0.5)
print('O primeiro analista lança em média {} notas por semana e {} notas por mês.'.format(notassemana1, notasmes1))
sleep(0.5)
print('O segundo analista lança em média {} notas por semana e {} notas por mês.'.format(notassemana2, notasmes2))
sleep(0.5)
print('O terceiro analista lança em média {} notas por semana e {} notas por mês.'.format(notassemana3, notasmes3))
print('')
print('ANALISANDO...')
sleep(2)
print('O melhor analista entre eles é \033[31m{}\033[m que lança {} por mês e é mais PRODUTIVO!'. format(melhoranalista, lancamais))
