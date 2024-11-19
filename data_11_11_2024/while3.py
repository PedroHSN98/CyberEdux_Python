idade = int(input('Insira sua idade: '))
while idade < 0:
    print('Idade inválida! Tente novamente.')
    idade = int(input('Inrina sua idade: '))
print(f'A Idade é: {idade}')