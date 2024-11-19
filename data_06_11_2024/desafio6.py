uni_altura = input('Unidade de altura ( m ou cm): ')
altura = float(input('Altura: '))
uni_peso = input('Unidade do peso (g ou kg): ')
peso = float(input('Peso: '))

if uni_altura == 'cm' or uni_altura == 'm':
    if uni_altura =='cm':
        altura = altura/100
else:
    print('Unidade de altura invalida!')
    exit()

if uni_peso == 'g' or uni_altura =='kg':
    if uni_peso == 'kg':
        peso = peso/1000
else:
    print('Unidade de peso invalida!')
    exit()

imc = peso / altura**2, 1

print(f' IMC:{imc:.2f}')
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


