'''
Faça um programa para criar um arquivo do Excel.
Neste arquivo, os dados da seguinte tabela devem ser 
inseridos: 
'''

import openpyxl
# import openpyxl as xl

tabela = [
    ['Fulano', 'fulano@gmail.com'],
    ['Ciclano', 'ciclano@gmail.com'],
    ['Beltrano', 'beltrano@gmail.com']
]
# ai iria ficar xl.Workbook()
wb = openpyxl.Workbook()
ws = wb.active


ws.append(['Nome', 'Email'])

for linha in tabela:
    ws.append(linha)

# Salvar o arquivo
wb.save('tabela.xlsx')

print("Arquivo Excel criado com sucesso!")


