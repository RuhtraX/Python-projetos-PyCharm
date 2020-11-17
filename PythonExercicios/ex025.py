#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome=str(input('Qual o seu nome completo? ')).strip()
print('silva' in nome.lower())