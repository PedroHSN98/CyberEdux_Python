#Lista de nomes
nomes = ['Filipe', 'Raquel', 'Fabricio', 'Pedro', 'Gustavo']

print('Antes do append --')
for i in range(len(nomes)):
    nome = nomes[i]
    print(nome)

nomes.append('Lucas') #Insere 'Lucas' no fim da lista

print('Depois do append --')
for i in range(len(nomes)):
    nome = nomes[i]
    print(nome)

nomes.pop(1) #remove o elemento do índice 1

print('Depois do pop --')
for i in range(len(nomes)):
    nome = nomes[i]
    print(nome)

nomes.remove('Gustavo') #remove o Gustavo da lista

print('Depois do remove --')
for i in range(len(nomes)):
    nome = nomes[i]
    print(nome)