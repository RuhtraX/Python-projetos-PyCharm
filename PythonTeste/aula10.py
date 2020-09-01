import emoji
nome=str(input('Qual o seu nome? ')).upper().strip()
if nome == 'ANNA BEATRIZ':
    print(emoji.emojize('Que nome lindo :heart_eyes:', use_aliases=True))
else:
    print(emoji.emojize('Seu nome é tão normal :neutral_face:', use_aliases=True))
print('Bom dia {}!'.format(nome))

n1=float(input('Qual foi a sua primeira nota em matemática? '))
n2=float(input('Qual foi sua segunda nota em matemática? '))
m=(n1+n2)/2
print('Média igual a {:.1f}'.format(m))
if m>=6.0:
    print(emoji.emojize('Sua média foi boa. PARABÉNS :smile:', use_aliases=True))
else:
    print(emoji.emojize('Sua média foi ruim. ESTUDE MAIS :disappointed_relieved:', use_aliases=True))
