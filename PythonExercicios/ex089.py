#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
# de cada aluno individualmente.

listatotal = []
lista = []
while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    lista.append(nome)
    listatotal.append(lista)
    print('-='*20)
    resp = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while resp not in 'NS':
        print('Opção inválida!')
        resp = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if resp == 'S':
        continue
    else:
        break
print(listatotal)



