# programa que lê o sexo das pessoas mas só aceita "M" ou "F". Caso errado,
# peça para o usuário digitar novamente.
sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
while sexo != 'M' and sexo != 'F':
    print('Opção inválida! Tente novamente.')
    sexo = str(input('Digite o sexo [M/F]:')).upper().strip()[0]
print('Registro realizado com sucesso!')
