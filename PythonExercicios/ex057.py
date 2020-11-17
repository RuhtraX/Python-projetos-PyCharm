#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
while sexo != 'M' and sexo != 'F':
    print('Opção inválida! Tente novamente.')
    sexo = str(input('Digite o sexo [M/F]:')).upper().strip()[0]
print('Registro realizado com sucesso!')
