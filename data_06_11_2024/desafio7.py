from random import randint 
#Numeros que o usuario estara colocando para poder estar sendo sorteado
n1 = int(input('Digite o seu primeiro numero: '))
if n1 < 0 or n1 > 9:
    print('Aposta 1 Invalida')
    exit()

n2 = int(input('Digite o seu segundo numero: '))
if n2 < 0 or n2 > 9:
    print('Aposta 2 Invalidada')
    exit()

s1 = randint(0, 9)
s2 = randint(0, 9)
s3 = randint(0, 9)
s4 = randint(0, 9)

print(s1, s2, s3, s4)

premio = 0
if n1 == s1 or n1 == s2 or n1 == s3 or n1 == s4:
    premio += 1000

if n2 == s1 or n2 == s2 or n2 == s3 or n2 == s4:
    premio += 1000
print(f'O prémio é R${premio}')

