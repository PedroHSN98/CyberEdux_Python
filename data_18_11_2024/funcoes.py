def quadrado(x):
    y = x**2
    return y 

def dizer_ola():
    print('Olá')
    
entrada = float(input('X: '))
saida = quadrado(entrada)
print(saida)
dizer_ola()