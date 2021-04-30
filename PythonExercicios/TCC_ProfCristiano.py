# coding: utf-8
from time import sleep
from tkinter import *
from playsound import playsound

cadastroPecas = []
pecasCadastradas = []
root = Tk()
menubar = Menu(root)
#Configurações da janela (tamanho, ícone, título)
root.geometry("600x425")
root.resizable(0, 0)
root.title("Stock Car")
root.configure(background='blue')

#1
def CadastrarPeca():
    cadastroPecas.append(str(input('Digite a descrição da peça: ')).strip().upper())
    cadastroPecas.append(int(input('Digite a quantidade desta peça: ')))
    pecasCadastradas.append(cadastroPecas[:])
    cadastroPecas.clear()
    sleep(1)
    print('\n')
#2
def ProcurarPeca():
    item = str(input('Digite a descrição da peça: ')).strip().upper()
    pecaEncontrada = False
    for pc in pecasCadastradas:
        if pc[0] == item:
            print(pc)
            pecaEncontrada = True
            break
    if pecaEncontrada == False:
        print('Item não encontrado! Favor verificar se a peça esta cadastrada e tente novamente.')
    sleep(1)
    print('\n')
#3
def AlterarPeca():
    alterar = str(input('Digite a descrição da peça: ')).strip().upper()
    i = -1
    pecaAlterada = False
    for pc in pecasCadastradas:
        i = i + 1
        if pc[0] == alterar:
            pecaAlterada = True
            print(pc)
            resposta = str(input('Tem certeza que deseja alterar a peça? [S/N] ')).strip().upper()[0]
            if resposta == 'S':
                novaDescricao = (str(input('Digite a nova descrição da peça: '))).strip().upper()
                pecasCadastradas[i][0] = novaDescricao[:]
                print(pecasCadastradas)
                print('Peça cadastrada com sucesso!')
                break
    if pecaAlterada == False:
        print('Item não encontrado! Favor verificar se a peça esta cadastrada e tente novamente.')
    sleep(1)
    print('\n')

#4
def DeletarPeca():
    deletarPeca = str(input('Digite a descrição da peça: ')).strip().upper()
    j = -1
    pecaDeletada = False
    for itemD in pecasCadastradas:
        j = j + 1
        if itemD[0] == deletarPeca:
            pecaDeletada = True
            print(itemD)
            sleep(0.5)
            print('\n')
            print('\033[1;36mAVISO! A peça será deletada juntamente com sua quantidade!\033[m')
            print('\n')
            resposta = str(input('Tem certeza que deseja deletar a peça? [S/N] ')).strip().upper()[0]
            if resposta == "S":
                pecasCadastradas[j] = ''
                #pecasCadastradas.remove(j)
                print('Peça deletada com sucesso!')
                break
    if pecaDeletada == False:
        print('Item não encontrado! Favor verificar se a peça esta cadastrada e tente novamente.')
    sleep(1)
    print('\n')
#5
def ComprarPeca():
    comprarPeca = str(input("Digite a peça a ser comprada: ")).strip().upper()
    k = -1
    pecaComprada = False
    for itemC in pecasCadastradas:
        k = k + 1
        if itemC[0] == comprarPeca:
            pecaComprada = True
            print(itemC)
            sleep(0.5)
            novaCompra = int(input('Quantos itens deseja adicionar?  '))
            nova = pecasCadastradas[k][1] + novaCompra
            nova = str(nova)
            pecasCadastradas[k][1] = nova[:]
            print(pecasCadastradas)
            print('Peça comprada com sucesso!')
            pecasCadastradas[k][1] = int(pecasCadastradas[k][1])
            break
    if pecaComprada == False:
        print('Item não encontrado! Favor verificar se a peça esta cadastrada e tente novamente.')
    sleep(1)
    print('\n')
#6
def VenderPeca():
    venderPeca = str(input("Digite a peça a ser vendida: ")).strip().upper()
    v = -1
    pecaVendida = False
    for itemV in pecasCadastradas:
        v = v + 1
        if itemV[0] == venderPeca:
            pecaVendida = True
            print(itemV)
            sleep(0.5)
            novaVenda = int(input('Quantos itens deseja vender?  '))
            novaV = pecasCadastradas[v][1] - novaVenda
            novaV = str(novaV)
            pecasCadastradas[v][1] = novaV[:]
            print(pecasCadastradas)
            print('Peça vendida com sucesso!')
            pecasCadastradas[v][1] = int(pecasCadastradas[v][1])
            break
    if pecaVendida == False:
        print('Item não encontrado! Favor verificar se a peça esta cadastrada e tente novamente.')
    sleep(1)
    print('\n')
#7
def VisualizarEstq():
    sleep(0.5)
    print('PROCESSANDO...')
    print('\n')
    sleep(1)
    print(pecasCadastradas)
    sleep(1)
    print('\n')
#8
def Sair():
    sleep(1)
    print('SAINDO...')

titulo1 = '\033[1;32mSTOCK CAR\033[m'
titulo2 = '\033[7;30mCONTROLE DE ESTOQUE\033[m'
#playsound('topgear.mp3')
print(titulo1.center(50, '='))
print(titulo2.center(50))
print('1 - Cadastrar peça\n2 - Procurar peça\n3 - Alterar peça\n4 - Deletar peça\n5 - Comprar peça\n6 - Vender peça\n7 - Visualizar estoque\n8 - Sair')
print('\033[1m-\033[m' * 40)
opcao = int(input('Digite a opção desejada: '))
print('\n')
while opcao != 8:
    if opcao == 1:
        CadastrarPeca()
    elif opcao == 2:
        ProcurarPeca()
    elif opcao == 3:
        AlterarPeca()
    elif opcao == 4:
        DeletarPeca()
    elif opcao == 5:
        ComprarPeca()
    elif opcao == 6:
        VenderPeca()
    elif opcao == 7:
        VisualizarEstq()
    elif opcao == 8:
        Sair()
    titulo1 = '\033[1;32mSTOCK CAR\033[m'
    titulo2 = '\033[7;30mCONTROLE DE ESTOQUE\033[m'
    print(titulo1.center(50, '='))
    print(titulo2.center(50))
    print('1 - Cadastrar peça\n2 - Procurar peça\n3 - Alterar peça\n4 - Deletar peça\n5 - Comprar peça\n6 - Vender peça\n7 - Visualizar estoque\n8 - Sair')
    print('\033[1m-\033[m' * 40)
    opcao = int(input('Digite a opção desejada: '))
    print('\n')
#cria botão 1
enterButton1 = Button(root, text="Cadastrar Peça", command=CadastrarPeca)
enterButton1.config(height=2, width=30)
enterButton1.place(x=30, y=50)
#cria botão 2
enterButton1 = Button(root, text="Procurar Peça", command=ProcurarPeca)
enterButton1.config(height=2, width=30)
enterButton1.place(x=30, y=100)
#cria botão 3
enterButton1 = Button(root, text="Alterar Peça", command=AlterarPeca)
enterButton1.config(height=2, width=30)
enterButton1.place(x=30, y=150)
#cria botão 4
enterButton1 = Button(root, text="Deletar Peça", command=DeletarPeca)
enterButton1.config(height=2, width=30)
enterButton1.place(x=30, y=200)
#cria botão 5
enterButton1 = Button(root, text="Comprar Peça", command=ComprarPeca)
enterButton1.config(height=2, width=30)
enterButton1.place(x=30, y=250)
#cria botão 6
enterButton1 = Button(root, text="Vender Peça", command=VenderPeca)
enterButton1.config(height=2, width=30)
enterButton1.place(x=30, y=300)
#cria botão 7
enterButton1 = Button(root, text="Visualizar Estoque", command=VisualizarEstq)
enterButton1.config(height=2, width=30)
enterButton1.place(x=30, y=350)
#cria botão 8
enterButton1 = Button(root, text="Sair", command=Sair)
enterButton1.config(height=2, width=10)
enterButton1.place(x=500, y=350)

root.mainloop()



