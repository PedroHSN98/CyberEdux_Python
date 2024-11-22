def pegar_altura():
    #função que pede para o usuario inserir a aultura e retornar a altura valida
    altura = float(input('Digite a sua altura em M: '))
    while altura < 0:
        #força o usuario a inserir a altura novamente, caso a altura seja menor
        print('Altura invalida!')
        altura = float(input('Digite a sua altura em M: '))
    return altura

def pegar_peso():
    #função que pede para o usuario colocar o peso e retorna o peso valido.
    peso = float(input('Insira seu peso (kg): '))
    while peso <= 0: # Enquanto o peso não é valido
        #força a reinserção do peso
        print('Peso invalido')
        peso = float(input('Insira seu peso(kg): '))
    return peso


def calcula_imc(altura, pegar_peso)
    imc = peso/altura**2
    return imc

def classifica_imc(imc):
    if imc <= 18.5:
        return 1 #abaixo do peso
    elif imc < 25:
        return 2 #esta com peso normal
    else:
        return 3 #porque esta acima do peso

# codigo principal
minha_altura = pegar_altura()
meu_peso = pegar_peso()
meu_imc = calcula_imc(minha_altura, meu_peso)
classificacao = classifica_imc(meu_imc)
if classificacao == 1:
    print('Abaixo do peso')
elif classificacao == 2:
    print('Peso normal')
elif classificacao == 3:
    print('Acima do peso')
else:
    print('Classificação desconhecida')