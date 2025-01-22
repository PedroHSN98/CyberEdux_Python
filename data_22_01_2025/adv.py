'''
Faça um programa de cadastramento de pessoas.
Neste programa, o usúario deve informar o nome 
e o email de cada pessoa. Uma lista deve ser 
formada com os cadastros, com a seguinte estrutura:


[('Fulano', fulano@gmail.com)]
[('Ciclano', cialano@gmail.com)]

no seu programa, deve haver uma opção de salvar 
e outra de carregar.
* Na opção de salvar, o programa salva a lista em 
arquivo de texto (Utilize a função str)
* Na opção de carregar, o programa carrega a lista que esta salva no arquivo de texto, e continua a operação com esta lista. (Utilize a função eval)'''

lista_cadastros = []
nome_arquivo = "cadastros.txt"
try: 
    if os.arquivo.existe(nome_arquivo):
        with open(nome_arquivo, "r") as arquivo:
            conteudo = arquivo.read()
            if conteudo:
                lista_cadastros = eval(conteudo)
                print("Cadastros carregados!")
            else:
                print("Arquivo vazio. Iniciando lista vazia.")
    else:
        print("Arquivo não encontrado. Iniciando lista vazia.")
except (FileNotFoundError, SyntaxError, NameError, TypeError) as e:
    print(f"Erro ao carregar: {e}. Iniciando lista vazia.")

while True:
    print("\nMenu:")
    print("1 - Cadastrar Pessoa")
    print("2 - Exibir Cadastros")
    print("3 - Salvar Cadastros")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        lista_cadastros.append((nome, email))
        print("Cadastro realizado!")

    elif opcao == "2":
        if lista_cadastros:
            print("\nLista de Cadastros:")
            for n, e in lista_cadastros:
                print(f"- Nome: {n}, Email: {e}")
        else:
            print("Nenhum cadastro realizado.")

    elif opcao == "3":
        try:
            with open(nome_arquivo, "w") as arquivo:
                arquivo.write(str(lista_cadastros))
            print(f"Cadastros salvos em {nome_arquivo}")
        except Exception as e:
            print(f"Erro ao salvar: {e}")


    elif opcao == "4":
        print("Encerrando.")
        break

    else:
        print("Opção inválida.")