#Faça um programa de lista de nomes.
#Nesse programa, o usuario deve informar 10 nomes,
#os nomes devem ser inseridos em uma lista, e, em seguida, 
#o programa deve mostrar os 10 nomes inseridos.


nomes = []  # Cria uma lista vazia para armazenar os nomes

for i in range(10):
    lista_nomes = str(input('Coloque o 1° Nome: '))
    nomes.append(lista_nomes)
    print(nomes)

for p in range(10):
    print(nomes[p])


