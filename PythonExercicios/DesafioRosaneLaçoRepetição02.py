# ler nome e quantidade de notas lançadas por dia de 3 pessoas e dizer quem lança mais notas.
from time import sleep
lancamaisdia = 0
melhoranalista = ''
print('-='*20)
for c in range(1, 4):
    nome = str(input('Digite o nome do {}º analista: '.format(c))).capitalize()
    notasdia = int(input('Quantas notas lança por dia: '))
    if c == 1:
        lancamaisdia = notasdia
        melhoranalista = nome
    if notasdia > lancamaisdia:
        lancamaisdia = notasdia
        melhoranalista = nome
    print('-=' * 20)
print('')
sleep(0.5)
print('ANALISANDO...')
sleep(2)
print('O melhor analista entre eles é \033[31m{}\033[m que lança {} por dia!'. format(melhoranalista, lancamaisdia))

