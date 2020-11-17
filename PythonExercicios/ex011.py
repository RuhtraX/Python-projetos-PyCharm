#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura=float(input('qual a largura da parede? '))
altura=float(input('qual a altura da parede? '))
area=largura*altura
tinta=area/2
print('será preciso {:.3f} litros de tinta\npara pintar uma área de {:.2f} metros quadrados'.format(tinta,area))