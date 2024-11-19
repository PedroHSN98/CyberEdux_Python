x = int(input('Digite um Inteiro: '))
while x < 1:
    print('X tem que ser maior que 1')
    x = int(input('Digite um inteiro: '))

y = 1 
count = 0
while y <= x:
    if x % y == 0:
        print(f'{x} é divisivel por {y}')
        count += 1
    y += 1

if count == 2:
    print(f'{x} é Primo')
else:
    print(f'{x} não é Primo')
