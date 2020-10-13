listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('{:-^30}'.format('LISTAGEM DE PREÇO'))
for posicaoitem in range(0, len(listagem)):
    if posicaoitem % 2 == 0:
        print('{:.<30}'.format(listagem[posicaoitem]), end='')
    else:
        print(' R$ {:.2f}'.format(listagem[posicaoitem]))