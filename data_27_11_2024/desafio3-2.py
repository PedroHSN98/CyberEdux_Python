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
    try:
        indice = nomes.index(nome)
        telefone = telefone[indice]
        print(f'O telefone de {nome} é {telefone}')
    except ValueError as ex:
        print('Deu ruim!', str(ex))



# Try e Except, que foram inseridos aqui nesse codigo, um outro jeito de fazer o codigo do codigo anterior
