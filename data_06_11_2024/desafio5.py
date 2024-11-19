peso = float(input('Digite o seu Peso em (kg): '))
altura = float(input('Digite a sua Altura em (M): '))

imc = (peso / altura**2)

print(f'Aqui esta o seu IMC {imc:.2f}')
# mf >= 5 and mf <= 7:

if (imc >= 15 and imc <= 18.55):
    print(f"Abaixo do peso, IMC={round(imc,2)}")
elif (imc > 18.55 and imc < 24.95):
    print(f"Peso normal, IMC={round(imc,2)}")
elif (imc >= 24.95 and imc < 29.95):
    print(f"Acima do peso, IMC={round(imc,2)}")
elif (imc >= 29.95 and imc < 39.95):
    print(f"Obsidade grau I, IMC={round(imc,2)}")
else:
    print('Obesidade Grau II')


