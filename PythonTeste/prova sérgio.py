print("1.X-salada = R$ 7,00")
print("2.Refrigerante = R$ 5,00")
print("3.Cerveja = R$ 4,00")
print("4.Misto quante = R$ 3,00")
if opcao=1;
    precounit=7
elif opcao=2
      precounit=5
elif opcao=3
      precounit=4
elif opcao=4
      precounit=3
opcao=input("Escolha um ítem no Menu: ")
qtde=int(input("Escolha a quantidade: "))
gorjeta=(precounit*qtde)*0.10
valor_final=(precounit*qtde)+gorjeta
print("O valor final com os 10% é igual a {}.".format(valor_final))



