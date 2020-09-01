nome = str(input('Qual seu nome? '))
if nome == 'Rafael':
    print('Que nome bonito!!!')
elif nome == 'João' or nome == 'Pedro' or nome == 'Maria' or nome == 'Paula':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Rosane Helena':
    print('\033[31mQue belo nome feminino!!!\033[m')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia \033[34m{}\033[m!'.format(nome))