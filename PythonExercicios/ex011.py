largura=float(input('qual a largura da parede? '))
altura=float(input('qual a altura da parede? '))
area=largura*altura
tinta=area/2
print('será preciso {:.3f} litros de tinta\npara pintar uma área de {:.2f} metros quadrados'.format(tinta,area))