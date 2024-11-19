import math

a = float(input("Me de o valor do coeficiente a: "))
b = float(input("Me de o valor do coeficiente b: "))
c = float(input("Me de o valor do coeficiente c: "))
d = float(input("Me de o valor do coeficiente d: "))
x1 = (-b + math.sqrt(b**2 - 4*a*(c-d)))/(2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*(c-d)))/(2*a)

print(f"O valor de x satisfazem {a}x**2+{b}x+{c}={d} são x={x1} e x={x2}")
