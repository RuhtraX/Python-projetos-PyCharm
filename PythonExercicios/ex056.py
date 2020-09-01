# ler o nome, idade e sexo de quatro pessoas e dizer qual a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres tem menos de 20 anos.
somaidade = 0
maioridadehomem = 0
nomehomemmaisvelho = ''
totalmulheresmenos20 = 0
print('==#'*9)
for c in range(1, 5):
    nome = str(input('Nome da {}ª pessoa: '.format(c))).capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    somaidade = somaidade + idade
    if c == 1 and sexo == 'M': # comando in mais a declaração entre '' serve para as possíveis formas que o usuário possa digitar
        maioridadehomem = idade
        nomehomemmaisvelho = nome
    if c == 2 and sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomehomemmaisvelho = nome
    if c == 3 and sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomehomemmaisvelho = nome
    if c == 4 and sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomehomemmaisvelho = nome
    if sexo == 'F' and idade < 20:
        totalmulheresmenos20 = totalmulheresmenos20 + 1
    print('==#'*9)
print('A média de idade do grupo é igual a {}.'.format(somaidade/4))
print('O nome do homem mais velho é {} e ele tem {} anos.'.format(nomehomemmaisvelho, maioridadehomem))
print('O total de mulheres com menos de 20 anos é igual a {}.'.format(totalmulheresmenos20))


