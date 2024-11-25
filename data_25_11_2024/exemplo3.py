#Lista de nomes
nomes = ['Filipe', 'Raquel', 'Fabricio', 'Pedro', 'Gustavo']

#Esvaziar Lista
for i in range(len(nomes)):
    nome_removido = nomes.pop()
    print('Nome removido: ', nome_removido)
    print('Lista atual: ', nomes)