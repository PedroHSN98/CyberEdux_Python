#Lista  
#Lista é uma coleção ordenada de mutável. Permite membros duplicados.
#     str    bool  int  float
lista = ['carro', True, 2, 3.14]
print(lista)
print(lista[1])
print(type(lista))
print('-'*30)


#Tupla 
#Tuplas são coleção ordenada e imutável(não pode adicinar ou remover os itens). Permite membros duplicados.
#     str    bool   int   float
tupla = ('carro', True, 2, 3.14)
print(tupla)
print(type(tupla))
print('-'*70)



#Dicionarios 
#O dicionario é uma coleção ordenada e mutável. Nenhum membro duplicado.
#     chave: valor     chave: valor   chave: valor       chave: valor
dicionarios = {'nome': 'carro', 'logica': True, 'numero': 2, 'outroNumero': 3.5}
print(dicionarios)
print(dicionarios['logica'])
print(type(dicionarios))
print('-'*70)



#conjuntos
#Set é uma coleção não ordenada e não indexada. Nenhum membro duplicado. 
conjunto = {'carro', True, 2, 3.14}
print(conjunto)
print(type(conjunto))


