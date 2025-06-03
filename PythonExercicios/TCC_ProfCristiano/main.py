from tkinter import *
from tkinter import messagebox

cadastroPecas = []
pecasCadastradas = []

def CadastrarPeca():
	def cadastro():
		cadastroPecas.append(str(caixadesc.get()).strip().upper())
		cadastroPecas.append(str(caixaqtd.get()).strip().upper())
		pecasCadastradas.append(cadastroPecas[:])
		cadastroPecas.clear()
		messagebox.showinfo("Cadastrar", "Peça cadastrada com sucesso!")
		janela_cadastrar.destroy()
	janela_cadastrar = Toplevel(root) # cria nova janela filha através da janela principal(janela_menu)
	janela_cadastrar.geometry("600x425")
	janela_cadastrar.resizable(0, 0)
	janela_cadastrar.title("Cadastrar Peça")
	janela_cadastrar.configure(background='grey')
	text = Label(janela_cadastrar, text="Digite a descrição da peça: ", font=("Quentine", 12,), fg="black",
	background="#E6E6FA")
	text.place(x=30, y=50)
	caixadesc = StringVar()
	caixadescBox = Entry(janela_cadastrar, textvariable=caixadesc, font=("Quentine", 12,), fg="black")
	caixadescBox.place(x=30, y=100, width=205, height=30)
	text = Label(janela_cadastrar, text="Digite a quantidade da peça: ", font=("Quentine", 12,), fg="black",
	background="#E6E6FA")
	text.place(x=30, y=200)
	caixaqtd = StringVar()
	caixaqtdBox = Entry(janela_cadastrar, textvariable=caixaqtd, font=("Quentine", 12,), fg="black")
	caixaqtdBox.place(x=30, y=250, width=215, height=30)
	enterButton1 = Button(janela_cadastrar, text="OK", command=cadastro)
	enterButton1.config(height=2, width=10)
	enterButton1.place(x=500, y=350)

def ProcurarPeca():
	def procurar():
		item = str(caixaqtd.get()).strip().upper()
		pecaEncontrada = False
		o = -1
		for pc in pecasCadastradas:
			o = o + 1
			if pc[0] == item:
				messagebox.showinfo("Procurar", ("Peça encontrada: {}".format(pecasCadastradas[o])))
				pecaEncontrada = True
				break
		if pecaEncontrada == False:
			messagebox.showinfo("Procurar", "Item não encontrado! Favor verificar se a peça esta cadastrada e tente novamente.")
		janela_procura.destroy()
	janela_procura = Toplevel(root)
	janela_procura.geometry("600x425")
	janela_procura.title("Procurar Peça")
	janela_procura.configure(background='grey')
	text = Label(janela_procura, text="Digite a descrição da peça: ", font=("Quentine", 12,), fg="black",
				 background="#E6E6FA")
	text.place(x=30, y=50)
	caixaqtd = StringVar()
	caixaqtdBox = Entry(janela_procura, textvariable=caixaqtd, font=("Quentine", 12,), fg="black")
	caixaqtdBox.place(x=30, y=100, width=205, height=30)
	enterButton1 = Button(janela_procura, text="OK", command=procurar)
	enterButton1.config(height=2, width=10)
	enterButton1.place(x=500, y=350)

def AlterarPeca():
	def procurar():
		item = str(caixaqtd5.get()).strip().upper()
		pecaEncontrada = False
		o = -1
		for pc in pecasCadastradas:
			o = o + 1
			if pc[0] == item:
				messagebox.showinfo("Procurar", ("Peça encontrada: {}!".format(pecasCadastradas[o])))
				pecaEncontrada = True
				def troca():
					if messagebox.askokcancel("Alterar", "Tem certeza que deseja alterar a peça?"):
						novaDescricao = str(caixaNovoNome.get()).strip().upper()
						pecasCadastradas[o][0] = novaDescricao[:]
						messagebox.showinfo("Alterar", "Peça alterada com sucesso!")
						novaJanelaAlterar.destroy()
						janela_procura.destroy()

				novaJanelaAlterar = Toplevel(root)
				novaJanelaAlterar.geometry("600x425")
				novaJanelaAlterar.title("Alterar Peça")
				novaJanelaAlterar.configure(background='yellow')
				text = Label(novaJanelaAlterar, text="Digite a NOVA descrição da peça: ", font=("Quentine", 12,), fg="black",
							 background="#E6E6FA")
				text.place(x=30, y=50)
				caixaNovoNome = StringVar()
				caixaNovoNomeBox = Entry(novaJanelaAlterar, textvariable=caixaNovoNome, font=("Quentine", 12,), fg="black")
				caixaNovoNomeBox.place(x=30, y=100, width=205, height=30)
				enterButton1 = Button(novaJanelaAlterar, text="OK", command=troca)
				enterButton1.config(height=2, width=10)
				enterButton1.place(x=500, y=350)
				break
		if pecaEncontrada == False:
			messagebox.showinfo("Procurar", "Item não encontrado! Favor verificar se a peça esta cadastrada e tente novamente.")

	janela_procura = Toplevel(root)
	janela_procura.geometry("600x425")
	janela_procura.title("Alterar Peça")
	janela_procura.configure(background='grey')
	text = Label(janela_procura, text="Digite a descrição da peça: ", font=("Quentine", 12,), fg="black",
				 background="#E6E6FA")

	text.place(x=30, y=60)
	caixaqtd5 = StringVar()
	caixaqtd5Box = Entry(janela_procura, textvariable=caixaqtd5, font=("Quentine", 12,), fg="black")
	caixaqtd5Box.place(x=30, y=100, width=205, height=30)
	enterButton1 = Button(janela_procura, text="Procurar Peça", command=procurar)
	enterButton1.config(height=2, width=12)
	enterButton1.place(x=500, y=350)

def DeletarPeca():
	def procurar():
		item = str(caixadelete.get()).strip().upper()
		pecaEncontrada = False
		j = -1
		for pc in pecasCadastradas:
			j = j + 1
			if pc[0] == item:
				messagebox.showinfo("Procurar", ("Peça encontrada: {}!".format(pecasCadastradas[j])))
				pecaEncontrada = True

				def deletar():
					if messagebox.askokcancel("Deletar", "Tem certeza que deseja deletar a peça?"):
						pecasCadastradas[j] = "0"
						messagebox.showinfo("Deletar", "Peça deletada com sucesso!")
						novaJanelaDeletar.destroy()
						janela_procura.destroy()

				novaJanelaDeletar = Toplevel(root)
				novaJanelaDeletar.geometry("600x425")
				novaJanelaDeletar.title("Deletar Peça")
				novaJanelaDeletar.configure(background='red')
				text = Label(novaJanelaDeletar, text="Digite a peça a ser deletada: ", font=("Quentine", 12,), fg="black",
							 background="#E6E6FA")
				text.place(x=30, y=50)
				caixaDeletar = StringVar()
				caixaDeletarBox = Entry(novaJanelaDeletar, textvariable=caixaDeletar, font=("Quentine", 12,), fg="black")
				caixaDeletarBox.place(x=30, y=100, width=205, height=30)
				enterButton1 = Button(novaJanelaDeletar, text="OK", command=deletar)
				enterButton1.config(height=2, width=10)
				enterButton1.place(x=500, y=350)
				break
		if pecaEncontrada == False:
			messagebox.showinfo("Deletar", f'Item {item} não encontrado!')

	janela_procura = Toplevel(root)
	janela_procura.geometry("600x425")
	janela_procura.title("Deletar Peça")
	janela_procura.configure(background='grey')
	text = Label(janela_procura, text="Digite a descrição da peça: ", font=("Quentine", 12,), fg="black",
				 background="#E6E6FA")

	text.place(x=30, y=60)
	caixadelete = StringVar()
	caixadeleteBox = Entry(janela_procura, textvariable=caixadelete, font=("Quentine", 12,), fg="black")
	caixadeleteBox.place(x=30, y=100, width=205, height=30)
	enterButton1 = Button(janela_procura, text="Procurar Peça", command=procurar)
	enterButton1.config(height=2, width=12)
	enterButton1.place(x=500, y=350)

def ComprarPeca():
	def procurar():
		item = str(caixaComprar2.get()).strip().upper()
		pecaEncontrada = False
		j = -1
		for pc in pecasCadastradas:
			j = j + 1
			if pc[0] == item:
				messagebox.showinfo("Procurar", ("Peça encontrada: {}!".format(pecasCadastradas[j])))
				pecaEncontrada = True

				def comprar():
					if messagebox.askokcancel("Comprar", "Tem certeza que deseja comprar a peça?"):
						novaqtd = int(caixaComprarqtd.get())
						qtdpeca = pecasCadastradas[j][1]
						qtdpeca = int(qtdpeca)
						novovalor = novaqtd + qtdpeca
						novovalor = str(novovalor)

						pecasCadastradas[j][1] = novovalor[:]

						messagebox.showinfo("Comprar", "Peça comprada com sucesso!")
						novaJanelaComprar.destroy()
						janela_procura.destroy()

				novaJanelaComprar = Toplevel(root)
				novaJanelaComprar.geometry("600x425")
				novaJanelaComprar.title("Comprar Peça")
				novaJanelaComprar.configure(background='green')

				text = Label(novaJanelaComprar, text="Digite a quantidade da peça: ", font=("Quentine", 12,),
							 fg="black",
							 background="#E6E6FA")
				text.place(x=30, y=50)
				caixaComprarqtd = StringVar()
				caixaComprarqtdBox = Entry(novaJanelaComprar, textvariable=caixaComprarqtd, font=("Quentine", 12,),
										fg="black")
				caixaComprarqtdBox.place(x=30, y=100, width=205, height=30)

				enterButton1 = Button(novaJanelaComprar, text="OK", command=comprar)
				enterButton1.config(height=2, width=10)
				enterButton1.place(x=500, y=350)
				break

		if pecaEncontrada == False:
			messagebox.showinfo("Comprar", "Item não encontrado! Favor verificar se a peça esta cadastrada e tente novamente.")

	janela_procura = Toplevel(root)
	janela_procura.geometry("600x425")
	janela_procura.title("Comprar Peça")
	janela_procura.configure(background='grey')
	text = Label(janela_procura, text="Digite a descrição da peça: ", font=("Quentine", 12,), fg="black",
				 background="#E6E6FA")

	text.place(x=30, y=60)
	caixaComprar2 = StringVar()
	caixaComprar2Box = Entry(janela_procura, textvariable=caixaComprar2, font=("Quentine", 12,), fg="black")
	caixaComprar2Box.place(x=30, y=100, width=205, height=30)
	enterButton1 = Button(janela_procura, text="Procurar Peça", command=procurar)
	enterButton1.config(height=2, width=12)
	enterButton1.place(x=500, y=350)

def VenderPeca():
	def procurar():
		item = str(caixaVender2.get()).strip().upper()
		pecaEncontrada = False
		m = -1
		for pc in pecasCadastradas:
			m = m + 1
			if pc[0] == item:
				messagebox.showinfo("Procurar", ("Peça encontrada: {}!".format(pecasCadastradas[m])))
				pecaEncontrada = True

				def vender():
					if messagebox.askokcancel("Vender", "Tem certeza que deseja vender a peça?"):
						novaqtd = int(caixaVenderqtd.get())
						qtdpeca = int(pecasCadastradas[m][1])
						if novaqtd > qtdpeca:
							messagebox.showinfo("Vender", "Estoque insuficiente!")
						else:
							novovalor = qtdpeca - novaqtd
							novovalor = str(novovalor)
							pecasCadastradas[m][1] = novovalor[:]
							messagebox.showinfo("Vender", "Peça vendida com sucesso!")
							novaJanelaVender.destroy()
							janela_procura.destroy()

				novaJanelaVender = Toplevel(root)
				novaJanelaVender.geometry("600x425")
				novaJanelaVender.title("Vender Peça")
				novaJanelaVender.configure(background='black')

				text = Label(novaJanelaVender, text="Digite a quantidade da peça: ", font=("Quentine", 12,),
							 fg="black",
							 background="#E6E6FA")
				text.place(x=30, y=50)
				caixaVenderqtd = StringVar()
				caixaVenderqtdBox = Entry(novaJanelaVender, textvariable=caixaVenderqtd, font=("Quentine", 12,),
										   fg="black")
				caixaVenderqtdBox.place(x=30, y=100, width=205, height=30)

				enterButton1 = Button(novaJanelaVender, text="OK", command=vender)
				enterButton1.config(height=2, width=10)
				enterButton1.place(x=500, y=350)

				break
		if pecaEncontrada == False:
			pecaEncontrada = True
			messagebox.showinfo("Vender",
								"Item não encontrado! Favor verificar se a peça esta cadastrada e tente novamente.")

	janela_procura = Toplevel(root)
	janela_procura.geometry("600x425")
	janela_procura.title("Vender Peça")
	janela_procura.configure(background='grey')
	text = Label(janela_procura, text="Digite a descrição da peça: ", font=("Quentine", 12,), fg="black",
				 background="#E6E6FA")

	text.place(x=30, y=60)
	caixaVender2 = StringVar()
	caixaVender2Box = Entry(janela_procura, textvariable=caixaVender2, font=("Quentine", 12,), fg="black")
	caixaVender2Box.place(x=30, y=100, width=205, height=30)
	enterButton1 = Button(janela_procura, text="Procurar Peça", command=procurar)
	enterButton1.config(height=2, width=12)
	enterButton1.place(x=500, y=350)

def VisualizarEstq():
	janela_visualizaEstoque= Toplevel(root)
	janela_visualizaEstoque.geometry("600x425")
	janela_visualizaEstoque.title("Visualizar Estoque")
	janela_visualizaEstoque.configure(background='purple')

	text = Label(janela_visualizaEstoque, text=(pecasCadastradas), font=("Quentine", 12,), fg="black",
					background="#E6E6FA")
	text.place(x=30, y=60)

def Sair():
	root.destroy()

if __name__ == "__main__":
	root = Tk()
	menubar = Menu(root)
	#Configurações da janela (tamanho, ícone, título)
	root.geometry("600x425")
	root.resizable(0, 0)
	root.title("Estoque Car")
	root.configure(background='blue')

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
