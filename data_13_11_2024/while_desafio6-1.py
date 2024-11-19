x = int(input('Digite um inteiro: '))
while x < 1:
    print('X tem que ser maior que 1')
    x = int(input('Digite um inteiro: '))

y = 2
while y < x:
    if x % y == 0:
        print(f'{x} não é Primo')
        exit()
    y += 1
print(f'{x} é primo')

