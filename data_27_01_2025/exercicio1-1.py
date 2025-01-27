import json

tabela = {
    'nome': [],
    'cpf': []
}

while True:
    print('1 - Cadastrar')
    print('2 - Listar')
    print('3 - Salvar')
    print('4 - Carregar')
    opcao = input('Opção: ')
    if opcao == '1':
        nome = input('Nome: ')
        cpf = input('CPF: ')
        tabela['nome'].append(nome)
        tabela['cpf'].append(cpf)
    elif opcao == '2':
        n = len(tabela['nome']) #Quantidade de cadastros
        for i in range(n):
            nome = tabela['nome'][i]
            cpf = tabela['cpf'][i]
            print(f'Nome: {nome}')
            print(f'CPF: {cpf}')
    elif opcao == '3':
        with open('cadastros.json', 'w') as f:
            f.write(json.dumps(tabela))
    elif opcao == '4':
        with open('cadastros.json', 'r') as f:
            conteudo = f.read()
            json.loads(conteudo)
    else:
        print('Opção Invalida!')