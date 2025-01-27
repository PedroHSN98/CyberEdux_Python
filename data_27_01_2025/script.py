import json 

tabela = [
    {'id': 1, 'nome': 'Fulano', 'email': ('fulano@mail.com', 'fu@mail.com'), 'active': True},
    {'id': 2, 'nome': 'Ciclano', 'email': None, 'active': False},
    {'id': 3, 'nome': 'Beltrano', 'email': 'beltrano@mail.com', 'active': True}
]

with open('arquivo.json', 'w') as f:
    f.write(json.dumps(tabela))

