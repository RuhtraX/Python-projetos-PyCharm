#Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo sem considerar espaços.
#- Quantas letras tem o primeiro nome.
nome=str(input('Digite seu nome completo: ')).strip()
print('Todo nome em maísculas: {}'.format(nome.upper()))
print('Todo seu nome em minúsculas: {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa=nome.split()
print('Seu primeiro nome tem {} letras'.format(len(separa[0])))