def teste_parv(valor):
    if valor % 2 == 0: # Se valor é divisivel por 2 ele é par
        return True
    else:
        return False #Retorna False pois é impar

# código Principal

entrada = int(input('Insira um inteiro: '))

if teste_parv(entrada):
    print('O numero é par')
else:
    print('O numero é impar')