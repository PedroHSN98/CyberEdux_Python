'''
Desafio:
Faça um programa de cadastramento que:
1- Mostra, em loop, um menu com as opções:
    1.1 - Cadastrar
    1.2 - Lista cadastros
    1.3 - Buscar cadastro
2- Na opção 'Cadastrar', o usuario insere os dados da pessoa, sendo eles: nome, email, cpf e data de nascimento. Em seguida, a pessoa é cadastrada no sistema.
3 - na opção 'Lista cadastros', uma tabela com os dados de todos os cadastros é mostrada no terminal.
4- Na opção 'buscar cadastro', o usuario insere um nome e o programa mostra uma tabela com os dados de todas as pessoas com esse nome.

Utilize uma lista de tuplas para armazenar os cadastros. Cada cadastro deve ser armazenado na lista com tupla.
'''

def cadastrar():
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    cpf = input("Digite o CPF: ")
    data_nascimento = input("Digite a data de nascimento: ")
    cadastro = (nome, email, cpf, data_nascimento)
    lista_de_cadastros.append(cadastro)
    print("Cadastro realizado com sucesso!")

def listar_cadastros():
    print("\nLista de Cadastros:")
    print("-" * 70)
    print("Nome\t\tEmail\t\tCPF\t\tData de Nascimento")
    print("-" * 70)
    for cadastro in lista_de_cadastros:
        nome, email, cpf, data_nascimento = cadastro
        print(f"{nome}\t{email}\t{cpf}\t{data_nascimento}")
    print("-" * 70)

def buscar_cadastro():
    nome_buscar = input("Digite o nome a ser buscado: ")
    encontrados = [cadastro for cadastro in lista_de_cadastros if nome_buscar.lower() in cadastro[0].lower()]
    if encontrados:
        print("\nCadastros encontrados:")
        print("-" * 70)
        print("Nome\t\tEmail\t\tCPF\t\tData de Nascimento")
        print("-" * 70)
        for cadastro in encontrados:
            nome, email, cpf, data_nascimento = cadastro
            print(f"{nome}\t{email}\t{cpf}\t{data_nascimento}")
        print("-" * 70)
    else:
        print("Nenhum cadastro encontrado.")

lista_de_cadastros = []

while True:
    print("\nMenu:")
    print("1. Cadastrar")
    print("2. Listar cadastros")
    print("3. Buscar cadastro")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar()
    elif opcao == '2':
        listar_cadastros()
    elif opcao == '3':
        buscar_cadastro()
    elif opcao == '4':
        print("Saindo...")
        break
    else:
        print("Opção inválida.")