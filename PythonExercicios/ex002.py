# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
nome =input('Digite seu nome: ')
print('Olá \033[1;36m{}\033[m, é um prazer te conhecer!'.format(nome))