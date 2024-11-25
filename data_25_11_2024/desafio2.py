# Faça um programa de lista telefonica
# neste programa:
# 1 - O usuario insere um quantidade de nomes da preferencia dela
# 2 - Para cada nome, um telefone deve ser inserido
# 3 - Apos o termino das inserções, o programa deve mostrar uma lista telefonica( com todos os nomes e listas inseridos).


nomes = []
telefones = []

n = int(input('Quantos telefones deseja inserir? R.: '))
for i in range(n):
    nome = input(f'{i+1}° nome: ')
    telefone = input(f'{i+1}° telefone: ')
    nomes.append(nome)
    telefones.append(telefone)

print('------Lista telefonica --------')
for i in range(n):
    nome = nomes[i]
    telefone = telefones[i]
    print(f'{nome} | {telefones}')