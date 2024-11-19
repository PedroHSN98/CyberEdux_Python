x = int(input('Digite um inteiro: '))
while x < 1:
    print('X tem que ser maior que 1')
    x = int(input('Digite um inteiro: '))

for y in range(x):
    d = y + 1
    if x % d == 0:
        print(f'{x} é divisivel por {d}')