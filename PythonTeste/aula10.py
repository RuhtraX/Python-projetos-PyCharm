def lerNota(ordinal: int):
    nota = input(f'Qual foi a sua {ordinal}ª nota em matemática? ')
    while not nota.isnumeric() or float(nota) < 0 or float(nota) > 10:
        print(f'{nota} não é uma nota válida. Tente novamente.')
        nota = input(f'Qual foi a sua {ordinal}ª nota em matemática? ')
    return float(nota)
nome=input('Qual o seu nome? ').upper().strip()
if nome == 'ANNA BEATRIZ':
    print('Que nome lindo 😍')
else:
    print('Seu nome é tão normal 😐')
print('Bom dia {}!'.format(nome))

n1=lerNota(1)
n2=lerNota(2)
m=(n1+n2)/2
print('Média igual a {:.1f}'.format(m))
if m>=6.0:
    print('Sua média foi boa. PARABÉNS 😊')
else:
    print('Sua média foi ruim. ESTUDE MAIS 😔')
