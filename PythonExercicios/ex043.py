print('CALCULADORA DE IMC')
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura*altura)
if imc < 18.5:
    print('Seu IMC é igual a {:.1f} e você está abaixo do peso.'.format(imc))
elif imc <= 25:
    print('Seu IMC é igual a {:.1f} e você está no seu peso ideal.'.format(imc))
elif imc <= 30:
    print('Seu IMC é igual a {:.1f} e você está com sobrepeso.'.format(imc))
elif imc <= 40:
    print('Seu IMC é igual a {:.1f} e você está com obesidade.'.format(imc))
else:
    print('Seu IMC é igual a {:.1f} e você está com obesidade mórbida.'.format(imc))