nomes = []
telefones = []

n = int(input('Quantos telefones deseja inserir? R.: '))
for i in range(n):
    nome = input(f'{i+1}° nome: ')
    telefone = input(f'{i+1}° telefone: ')
    nomes.append(nome)
    telefones.append(telefone)

while True:
    nome = input('Informe o nome da pessoa da qual você quer ver o telefone: ')
    if nome in nomes: 
        indice = nomes.index(nome)
        telefone = telefone[indice]
        print(f'O telefone de {nome} é {telefone}')
    else:
        print('Nome não encontrada na lista')