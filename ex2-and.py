peso = float(input("Qual o seu peso?KG"))
altura = float(input("Qual o sua altura?"))
IMC = peso/(altura ** 2)
print(f"seu imc é {IMC}")
print('O seu IMC é de {:.1f}'.format(IMC))
if IMC < 18.5:
 print('Diagnóstico: Abaixo do peso normal')
elif IMC >=18.5 and IMC <25:
 print('Diagnóstico: peso normal')
elif IMC >=25 and IMC <30:
 print('Diagnóstico: sobrepeso')
elif IMC >=30 and IMC <40:
 print('Diagnóstico: obeso')
elif IMC >=40:
 print('Diagnóstico: obesidade mórbida')