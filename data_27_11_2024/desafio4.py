'''
Implemente a função pegar_nomes de modo que:
1 - ela peça que o usuario digitar varios nomes.
    obs: quem decide quantos nome é o usuario
2 - ela retorna um tupla com a lista de nomes e a qtd
    de nomes inseridos

'''

def pegar_nomes():
    nomes = []
    while True:
        nome = input("Digite um nome (ou 'sair' para terminar): ")
        if nome == 'sair':
            break
        nomes.append(nome)

    qtd_nomes = len(nomes)
    return nomes, qtd_nomes

nomes, qtd_nomes = pegar_nomes()

for i in range(qtd_nomes):
    print(f"{i} | {nomes[i]}")