'''
faça um programa em Python quqe escreve uma lista de emails inseridos pelo usúario em um arquivo, nos seguintes formatos:

fulano@gmail.com
ciclano@gmail.com
beltrano@gmail.com
'/n'
'''

esc = int(input('Escreva quantos e-mails você quiser:\n '))
lista = []
for i in range(esc):
    email = str(input(f'Digite o {i+1} email\n '))
    lista.append(email)
with open('meutexto.txt', 'w') as arquivo:
    for i in range(len(lista)):
        arquivo.write(f'{lista[i]}\n')