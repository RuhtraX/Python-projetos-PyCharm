# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar
# mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo = termo + razao
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?  '))
print('Programa finalizado com {} termos mostrados.'.format(total))
