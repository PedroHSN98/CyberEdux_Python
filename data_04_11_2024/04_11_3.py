n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
n3 = float(input('Digite a sua terceira nota: '))

p1 = float(input('Digite o peso 1: '))
p2 = float(input('Digite o peso 2: '))
p3 = float(input('Digite o peso 3: '))

mf = (n1*p1 + n2*p2 + n3*p3)/(p1+p2+p3)

if mf <= 5:
    print('Você esta Reprovado')
elif mf >= 5 and mf <= 7:
    print('Você esta de Prova Final')
else:
    print('Você esta Aprovado')