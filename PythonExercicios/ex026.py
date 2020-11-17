#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela
# aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite sua frase: ')).strip().lower()
print('A letra A aparece {} vezes'.format(frase.count('a')))
print('A primeira vez que a letra A apareceu foi na {}ª posição'.format(frase.index('a')+1))
print('A última vez que a letra A aparece é na {}ª posição'.format(frase.rindex('a')))

