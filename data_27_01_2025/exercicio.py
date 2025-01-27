'''
Faça um programa de cadastramento de pessoas. Esse programa deve ter um menu com as seguintes opções:
1 - Cadastrar pessoas
2 - Listar cadastros
3 - Salvar cadastros
4 - Carregar Cadastros

Na opção 1m o usuario insere dados da pessoa (nome e cpf). A pessoa é, então, registrada em uma tabela formada por coleções de dados.

Na opção 2, o programa mostra, todos os cadastros no terminal.

Na opção 3, o programa salva os cadastros em um arquivo JSON.

Na opção 4, o programa abre o arquivo JSON e carrega sesus cadastros.
'''

'''
Faça um programa de cadastramento de pessoas. Esse programa deve ter um menu com as seguintes opções:
1 - Cadastrar pessoas
2 - Listar cadastros
3 - Salvar cadastros
4 - Carregar Cadastros

Na opção 1m o usuario insere dados da pessoa (nome e cpf). A pessoa é, então, registrada em uma tabela formada por coleções de dados.fazendo de lista para lista em Pyhton

Na opção 2, o programa mostra, todos os cadastros no terminal.

Na opção 3, o programa salva os cadastros em um arquivo JSON.

Na opção 4, o programa abre o arquivo JSON e carrega sesus cadastros.
'''

import json


cadastros = []

def cadastrar_pessoa():
    nome = input("Digite o nome da pessoa: ")
    cpf = input("Digite o CPF da pessoa: ")
    pessoa = {"nome": nome, "cpf": cpf}
    cadastros.append(pessoa)
    print("Pessoa cadastrada com sucesso!")

def listar_cadastros():
    if not cadastros:
        print("Nenhum cadastro encontrado.")
    else:
        for i, pessoa in enumerate(cadastros, 1):
            print(f"{i}. Nome: {pessoa['nome']}, CPF: {pessoa['cpf']}")

def salvar_cadastros():
    with open("cadastros.json", "w") as arquivo:
        json.dump(cadastros, arquivo)
    print("Cadastros salvos com sucesso!")

def carregar_cadastros():
    global cadastros
    try:
        with open("cadastros.json", "r") as arquivo:
            cadastros = json.load(arquivo)
        print("Cadastros carregados com sucesso!")
    except FileNotFoundError:
        print("Nenhum arquivo de cadastro encontrado.")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1 - Cadastrar pessoas")
        print("2 - Listar cadastros")
        print("3 - Salvar cadastros")
        print("4 - Carregar Cadastros")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_pessoa()
        elif opcao == "2":
            listar_cadastros()
        elif opcao == "3":
            salvar_cadastros()
        elif opcao == "4":
            carregar_cadastros()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()