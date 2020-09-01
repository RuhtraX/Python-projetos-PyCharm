# refazer o exercicio 61. mostrar a progressão aritimética dos
# 10 primeiros termos de um número e depois solicitar qtos termos mais o usuário
# quer mostrar até que digite zero
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
