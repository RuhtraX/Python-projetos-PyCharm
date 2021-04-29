#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
# de cada aluno individualmente.

listatotal = []
lista = []
while True:
    alunoNotas = (str(input('Digite o nome do aluno: ')), int(input('Digite a primeira nota: ')), int(input('Digite a segunda nota: ')))
    lista.append(alunoNotas)
    listatotal.append(lista[:])
    lista.clear()
    print('-='*20)
    resp = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while resp not in 'NS':
        print('Opção inválida!')
        resp = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if resp == 'S':
        continue
    else:
        break
for c[0] in listatotal:
    print('{} média igual a {}'.format(c, lista[1] / lista[2]))
    



