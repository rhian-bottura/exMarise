peso = float(input("Qual o seu peso?KG"))
altura = float(input("Qual o sua altura?"))
imc = peso/(altura ** 2)
print('O seu IMC é de {:.1f}'.format(imc))
