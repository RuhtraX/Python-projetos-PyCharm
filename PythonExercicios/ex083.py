#verificar se uma expressão é valida ou não de acordo com a quantidade de parenteses abertos e fechados
expr = str(input('Digite sua expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida.')
else:
    print('Expressão INVÁLIDA!')
