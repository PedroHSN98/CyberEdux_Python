arquivo = open('meutexto.txt', 'r')
conteudo = arquivo.read()
arquivo.close()
print(conteudo)


 #or 


#with open('meutexto.txt', 'r') as arquivo:
#    conteudo = arquivo.read()

#print(conteudo)

# or 


#with open('../meutexto.txt', 'r') as arquivo:
#    conteudo = arquivo.read()
   # arquivo.write('Meu nome e Pedro!\n')  
   #arquivo.write('Meu nome e Pedro2')

#print(conteudo)