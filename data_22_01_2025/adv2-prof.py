lista_de_cadastros = []

while True:
    print('Opções: ')
    print('1 - Cadastros')
    print('2 - Listar Cadastros')
    print('3 - Salvar Cadastros')
    print('4 - Carregar cadastros salvos')
    opcao = input('Opção: ')
    if opcao == '1': 
        nome = input('Nome: ')
        email = input('Email: ')
        lista_de_cadastros.append((nome, email))
    elif opcao == '2':
        for nome, email in lista_de_cadastros:
            print(f'{nome} {email}')
    elif opcao == '3':
        with open('cadastros.txt', 'w') as f:
            f.write(str(lista_de_cadastros))
    elif opcao == '4':
        with open('cadastros.txt', 'r') as f:
            lista_de_cadastros = eval(f.read())
    else: 
        print('Opção Invalida!')