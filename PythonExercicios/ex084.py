lista = []
pessoas = []
maior = menor = 0
cont = 0
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    cont += 1
    if len(pessoas) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    pessoas.append(lista[:])
    lista.clear()
    resposta = str(input('Deseja continuar [s/n]? ')).strip().lower()[0]
    if resposta not in 'sn':
        print('Opção inválida!')
        resposta = str(input('Deseja continuar [s/n]? ')).strip().lower()[0]
    if resposta == 'n':
        break
print('Foram contabilizadas {} pessoas.'.format(cont))
print('Os mais pesados são: {}Kg'.format(maior), end='')
for peso in pessoas:
    if peso[1] == maior:
        print(' [{}] '.format(peso[0]), end='')
print('\nOs mais leves são: {}Kg'.format(menor), end='')
for peso in pessoas:
    if peso[1] == menor:
        print(' [{}] '.format(peso[0]), end='')



