'''
Faça um código que transforme a minha_lista em um lista
com nomes em caixa alta (ou, somente com letras maiusculas).
E em ordem alfabetica
Utilize for e o método upper de strings e sort.
'''

minha_lista = ['Fulano', 'Ciclano', 'Beltrano']
print('Antes: ', minha_lista)

# Coloque aqui seu código

print('Depois', minha_lista)
a = len(minha_lista)
minha_lista.sort()
for i in range(a):
    b = (minha_lista[i].upper())
    print(b)
