def teste_de_primalidade(valor):
    for candidato in range(2, valor):
        if valor % candidato == 0:
            return False
    return True

n = int(input('N: '))
for x in range(2, n+1):
    if teste_de_primalidade(x):
      print(f'{x} é primo')