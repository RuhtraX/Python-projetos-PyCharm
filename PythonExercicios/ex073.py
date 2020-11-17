#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.
times = ('Atlético-MG', 'Internacional', 'São Paulo', 'Palmeiras', 'Vasco da Gama', 'Flamengo', 'Sport Recife', 'Santos', 'Fortaleza', 'Fluminense', 'Ceará SC', 'Grêmio', 'Corinthians', 'Atlético-GO', 'Atlético-PR', 'Coritiba', 'Bragantino-SP', 'Botafogo', 'Bahia', 'Goiás')
print('='*30)
print('{:^30}'.format('Tabela BRASILEIRÃO'))
print('='*30)
print('Os cinco primeiros times da tabela são:')
print(times[0:5])
print('-='*15)
print('Os últimos 4 colocados da tabela são:')
print(times[16:])
print('-='*15)
print('Os times em ordem alfabética são:')
print(sorted(times))
print('-='*15)
print('O Corinthians está na posição:')
print(times.index('Corinthians'))
