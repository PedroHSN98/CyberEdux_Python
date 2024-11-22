def obter_entrada(mensagem):
    entrada = float(input(mensagem))
    while entrada <= 0:
        print('Entrada invalidada! Tente novamente')
        entrada = float(input(mensagem))
    return entrada

altura = obter_entrada('Digite sua altura (m): ')
peso = obter_entrada('Digite seu peso (kg): ')

imc = peso/altura**2

if imc <= 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso normal')
else:
    print('Acima do peso')