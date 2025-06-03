def listarOpcoes(opcoes):
	for opcao in opcoes:
		print(f'{opcao} - {opcoes[opcao][0]} ' + 'R${:.2f}'.format(opcoes[opcao][1]))
	print()

def escolherOpcao(opcoes):
	while True:
		try:
			o = int(input('Escolha um item no Menu: '))
			if o > 0 and o <= len(opcoes):
				return o
			else:
				print(f'Opção [{o}] inválida.')
		except Exception as e:
			print(f'Erro: {e}')

if __name__ == '__main__':
	print('Prova Sérgio\n')
	opcoes = {
		1: ['X-salada', 7],
		2: ['Refrigerante', 5],
		3: ['Cerveja', 4],
		4: ['Misto quente', 3]
	}
	listarOpcoes(opcoes)
	opcao = escolherOpcao(opcoes)
	precounit = opcoes[opcao][1]
	qtde=int(input("Escolha a quantidade: "))
	gorjeta=(precounit*qtde)*0.10
	valor_final=(precounit*qtde)+gorjeta
	print("O valor final com os 10% é igual a {}.".format(valor_final))
