'''
Baseado no exercicio anterior, faça outro programa implementando o processo inverso> abrir o arquivo com os emails, inseri-los em uma lista e exibir a lista com print.
'''
lista = []
with open('meutexto2.txt', 'r') as arquivo:
    texto = arquivo.read()
lista.append(texto)
for i in range(len(lista)):
    print(f'{lista[i]}')