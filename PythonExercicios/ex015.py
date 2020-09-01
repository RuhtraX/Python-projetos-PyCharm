dias=int(input('por quantos dias o veículo foi alugado? '))
km=float(input('quantos quilômetros o veículo rodou? '))
total=(dias*60)+(km*0.15)
print('o total a ser pago é de R$ {:.2f}'.format(total))