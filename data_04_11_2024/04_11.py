nome = input('Digite o seu nome: ')
idade = int(input('Digite sua idade: '))
assert idade >= 0, 'ERRO: Idade menor que zero'

#if idade < 0:
#   print('Idade Invalida')
#    exit()
if idade >= 60:
    print(f'{nome} é um idoso')
elif idade >= 18:
    print(f'{nome} é adulto!')
elif idade >= 12:
    print(f'{nome} é adolescente!')
else:
    print(f'{nome} é criança!')

print(f'{nome} tem {idade} anos de idade!')