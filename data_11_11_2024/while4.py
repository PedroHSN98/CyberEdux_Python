while True:
    x = int(input('Insira um numero: '))
    if x % 2 == 0:
        print('O númeor é ár')
    else:
        print('O numero é impar')
    op = input('Dige "s" para sair ou qualquer outra coisa para continuar')
    if op == 's':
        break
print('Até mais')