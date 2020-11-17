#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
from time import sleep
vel=int(input('Qual a velocidade do veículo? '))
if vel >=40 and vel <=80:
    print('Sua velocidade está dentro da máxima permitida.')
elif vel <40:
    print('Você está muito devagar.\nAnde um pouco mais rápido.')
else:
    multa=float(vel-80)*7
    sleep(1)
    print('Atenção! Você foi multado!\nTerá de pagar R$ {:.2f}'.format(multa))
print('Dirija com segurança. Boa viagem!')
