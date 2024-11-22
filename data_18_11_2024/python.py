x = int(input('X: '))

primo = True
for candidato_a_divisor in range(2, x):
    if x % candidato_a_divisor == 0:
        primo = False
        break 

if primo:
    print(f'{x} é primo')
else:
    print(f'{x} não é primo')