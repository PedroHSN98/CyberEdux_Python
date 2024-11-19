a = float(input('Me de o valor do coeficiente a: '))
b = float(input('Me de o valor do coeficiente b: '))
c = float(input('Me de o valor do coeficiente c: '))

d = b**2 - 4*a*c

if d == 0:
    print('A eq tem uma soluções reais')
elif d > 0:
    print('duas solução real')
else:
    print('A equação n tem solução real')

