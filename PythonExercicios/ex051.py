#programa que lê o primeiro termo e a razão de uma PA (Progreção Aritimética).
#No final mostra os 10 primeiros termos dessa progressão.
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end='-')
print('ACABOU')