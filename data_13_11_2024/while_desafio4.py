while True:
    a = float(input('A: ')) #Coloque um Numero
    b = float(input('B: ')) #Coloque um Numero
    o = input('Operador (+, -, * ou /): ')
    #Vai ser colocado as somas para poder estar selecionando.

    while o != '+' and o != '-' and o != '*' and o != '/': # Aqui estara a escolha doq vc espera fazer, se por acaso for diferente vai aparecer um numero.
        print('Operador Invalido!')
        o = input('Operador (+, -, * ou /): ')
        
            
    if o == '+':
        r = a + b
    elif o == '-':
        r = a - b
    elif o == '*':
        r == a * b
    else:
        r = a / b
    print('Resultado', r)
    s = input('Digite "s" para sair ou qualquer coisa para continuar.')
    if s.lower() == 's':
        break
    