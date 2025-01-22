#modo 2 

with open('meutexto2.txt' , 'r') as f:
    linhas = f.readlines()

for i in range(len(linhas)):
    linha_atual = linhas[i]#Obtem a i-esíma string de lista
    linha_atual = linha_atual.replace('\n', '') #Processa a string
    linhas[i] = linha_atual #Devolve a string processada para a mesma posição na lista
print(linhas)

emails = [] #lista que contera apenas os emails
for linha in linhas:
    #Filtrar linhas para ignorar linhas em branco
    if linha != '':
        emails.append(linha)
    
print(emails)