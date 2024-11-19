import math
# - - Obtendo as notas
n1 = float(input("Digite a N1: "))
n2 = float(input("Digite a N2: "))
# - - Obtendo dos pesos 
p1 = float(input("Digite o peso da N1: "))
p2 = float(input("Digite o peso da N2: ")) 
p3 = float(input("Digite o peso da N3: "))
# Obtem da Mf
mf = float(input("Digite a nota final minima para aprovação: "))
# Calcule N3
n3 = (mf*(p1 + p2 + p3) - n1*p1 - n2*p2)/p3
print(f"Você precisa de {math.ceil(n3)} na N3 para ser aprovado.")








