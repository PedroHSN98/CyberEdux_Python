altura = float(input('Digite a suas altura em (m): '))
while altura < 0:
    print('Altura Invalida!')
    altura = float(input('Insira uma altura novamente'))

peso = float(input('Digite o seu Peso em (kg): '))
while peso < 0:
    print('Peso Invalido!')
    peso = float(input('Insira seu peso novamente: '))

imc = peso / altura**2
print(f'Imc igual a {imc:.2f}')

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso normal')
else:
    print('Acima do peso')

