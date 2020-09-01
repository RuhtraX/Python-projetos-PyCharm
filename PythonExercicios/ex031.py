km = int(input('Qual a distância da viagem? '))
if km <=200:
    print('Sua passagem custará R$', km*0.50)
elif km >=201:
    print('Sua passagem custará R$', km*0.45)
print('Boa viagem!')