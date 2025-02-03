'''
Faça um programa para criar um arquivo do Excel.
Neste arquivo, os dados da seguinte tabela devem ser 
inseridos: 
'''


'''
Faça um programa para criar um arquivo do Excel.
Neste arquivo, os dados da seguinte tabela devem ser 
inseridos: 
'''

import openpyxl

tabela = [
    ['Fulano', 'fulano@gmail.com'],
    ['Ciclano', 'ciclano@gmail.com'],
    ['Beltrano', 'beltrano@gmail.com']
]

wb = openpyxl.Workbook()
ws = wb.active

ws.append(['Nome', 'Email'])

for linha in tabela:
    ws.append(linha)

# Salvar o arquivo
wb.save('tabela.xlsx')

print("Arquivo Excel criado com sucesso!")