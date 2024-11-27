def formula_quadratica(a, b, c):
    delta = b**2 -4*a*c
    x1 = (-b + delta**0.5)/(2*a)
    x2 = (-b - delta**0.5)/(2*a)
    return x1, x2


coef_a = float(input('A: '))
coef_b = float(input('B: '))
coef_c = float(input('C: '))
raiz1, raiz2 = formula_quadratica(coef_a, coef_b, coef_c)
print(raiz1, raiz2)