'''
Faça um programa de cadastramento em Python. Neste programa, o usuário cadastrará uma determinada quantidade de pessoas. Em seguida, o programa mostrará uma tabela com todos os cadastros no terminal. A quantidade de cadastros deverá ser escolhida pelo usuário. Os dados cadastrais são os seguintes:

Nome
Sobrenome
CPF
Email
Telefone
Você deverá usar:

Listas
O método append de listas
Tuplas (opcional)
For
O código deve ser enviado como PDF.

'''

# Listas para armazenar os dados dos usuarios que ira ser inserido.
nomes = []
sobrenomes = []
cpfs = []
emails = []
telefones = []
# Solicitar a quantidade de pessoas que ira precisar ser cadastrada.
quantidade = int(input("Quantas pessoas deseja cadastrar? "))
# Loop de realização do cadastro
for i in range(quantidade):
 print(f"\nCadastro {i + 1}:")

 nome = input("Nome: ")
 sobrenome = input("Sobrenome: ")
 cpf = input("CPF: ")
 email = input("Email: ")
 telefone = input("Telefone: ")

 # Adicionar os dados dos usuarios cadastrados.
 nomes.append(nome)
 sobrenomes.append(sobrenome)
 cpfs.append(cpf)
 emails.append(email)
 telefones.append(telefone)
# Exibir os dados cadastrados em formato de tabela
print("\nDados cadastrados:")
print(f"{'Nome':<15}{'Sobrenome':<15}{'CPF':<15}{'Email':<30}{'Telefone':<15}")
print("-" * 90)
for i in range(quantidade):
 print(f"{nomes[i]:<15}{sobrenomes[i]:<15}{cpfs[i]:<15}{emails[i]:<30}{telefones[i]:<15}")