import emoji
from time import sleep
from random import choice
Papel = str
Pedra = str
Tesoura = str
lista = ['Papel','Pedra','Tesoura']
computador = choice(lista)
print(emoji.emojize('\033[36mVamos jogar\033[m \033[7mJOKENPÔ\033[m? :wink:', use_aliases=True))
sleep(1)
print(emoji.emojize('Faça sua escolha:\n[1]-:scroll:(Papel)\n[2]-:gem:(Pedra)\n[3]-:scissors:(Tesoura)', use_aliases=True))
escolha = int(input())
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
if escolha == 1 and computador == 'Papel':
    print(emoji.emojize('\033[4mNós empatamos\033[m :neutral_face:', use_aliases=True))
elif escolha == 1 and computador == 'Pedra':
    print(emoji.emojize('\033[31mVocê ganhou\033[m :angry: Papel embrulha a Pedra.', use_aliases=True))
    sleep(3)
    print(emoji.emojize('...mundiça :unamused:', use_aliases=True))
elif escolha == 1 and computador == 'Tesoura':
    print(emoji.emojize('\033[1;32mEu ganhei\033[m:smile::tada: Tesoura corta o Papel.', use_aliases=True))
elif escolha == 2 and computador == 'Papel':
    print(emoji.emojize('\033[1;32mEu ganhei\033[m:smile::tada: Papel embrulha a Pedra.', use_aliases=True))
elif escolha == 2 and computador == 'Pedra':
    print(emoji.emojize('\033[4mNós empatamos\033[m :neutral_face:', use_aliases=True))
elif escolha == 2 and computador == 'Tesoura':
    print(emoji.emojize('\033[31mVocê ganhou\033[m :angry: Pedra quebra a Tesoura.', use_aliases=True))
    sleep(3)
    print(emoji.emojize('...mundiça :unamused:', use_aliases=True))
elif escolha == 3 and computador == 'Papel':
    print(emoji.emojize('\033[31mVocê ganhou\033[m :angry: Tesoura corta o Papel.', use_aliases=True))
    sleep(3)
    print(emoji.emojize('...mundiça :unamused:', use_aliases=True))
elif escolha == 3 and computador == 'Pedra':
    print(emoji.emojize('\033[1;32mEu ganhei\033[m:smile::tada: Pedra quebra a Tesoura.', use_aliases=True))
elif escolha == 3 and computador == 'Tesoura':
    print(emoji.emojize('\033[4mNós empatamos :neutral_face:', use_aliases=True))
sleep(2)
print(emoji.emojize('Vamos de novo? :thumbsup:', use_aliases=True))
