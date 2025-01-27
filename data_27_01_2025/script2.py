import json

with open('arquivo.json', 'r') as f:
    texto = f.read()

tabela = json.loads(texto)

for linha in tabela:
    print(f'ID: {linha["id"]}')
    print(f'Nome: {linha["nome"]}')
    print(f'Email: {linha["email"]}')