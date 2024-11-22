def teste_de_primalidade(valor):
    primo = True
    for candidato in range(2, valor):
        if valor % candidato == 0:
            primo = False
            break
    return primo

    
x = int(input('X: '))
    

if teste_de_primalidade(x):
    print(f'{x} é primo')
else: 
    print(f'{x} não é primo') 