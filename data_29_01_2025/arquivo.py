import os
import json
from tabulate import tabulate

#mkdir serve pra criar pasta
#listdir listar arquivos na pasta
#remove apaga
while True:
    opcoes = input('Escolha a opção\n1 == Cadastrar\n2 == Buscar cadastro\n3 == listar cadastros\n4 == deletar cadastro\n')
    if opcoes == '1':
        way = "cadastros"
        try:
            os.mkdir(way)
        except FileExistsError:
            pass

        nome = input('Digite o nome do usuario\n')
        email = input('Digite o email do usuario\n')
        cpf = input('Digite o cpf do cadastro\n')
        telefone = input('Digite o telefone do cadastro\n')
        lista = [nome, email, cpf, telefone]

        with open(f'cadastros/{cpf}.json', 'w') as arquivo:
            arquivo.write(json.dumps(lista))
    if opcoes == '2':
        search = input('Digite o cpf do usuario que deseja procurar\n')
        if os.path.exists(f'cadastros/{search}.json'):
            with open(f'cadastros/{search}.json', 'r') as arquivo:
                conteudo = arquivo.read()
                jconteudo = [json.loads(conteudo)]
                #conteudo = nome, email, cpf, telefone
                cabecalho = ['nome', 'email', 'cpf', 'telefone']
            print(tabulate(jconteudo, headers=cabecalho, tablefmt="grid"))
            print(jconteudo)
        else:
            print(f'O seu usuario {search} nao existe')
    if opcoes == '3':
        arquivos = os.listdir('cadastros')
        for i in range(len(arquivos)):
            with open(f'cadastros/{arquivos[i]}', 'r') as arquivo:
                conteudo = arquivo.read()
                jconteudo = [json.loads(conteudo)]
                #conteudo = nome, email, cpf, telefone
                cabecalho = ['nome', 'email', 'cpf', 'telefone']
            print(tabulate(jconteudo, headers=cabecalho, tablefmt="grid"))
            
            
    if opcoes == '4':
        search = input('Digite o cpf do usuario que deseja apagar\n')
        if os.path.exists(f'cadastros/{search}.json'):
            os.remove(f'cadastros/{search}.json')





