idade = int(input('Insira sua idade: '))
while True:
    if idade >= 0:
        break
    print('Idade inválida! Tente novamente.')
    idade = int(input('Insira sua idade: '))
print(f'A idade é {idade}')