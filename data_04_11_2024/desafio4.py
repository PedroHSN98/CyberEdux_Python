#Solicita ao usuário os dados de entrada
capital = float(input('Informe o capital investido (C): '))
taxa_juros = float(input('Informe a taxa de rendimento anual (%) (i): ')) /100
tempo = int(input('Informe o tempo de aplicação (em anos) (n) : '))

#Calcula o momento final usado a fórmula de juros composto 
montante = capital * ( 1 + taxa_juros) ** tempo

#calcula o rendimento total ( juros compostos ) 
juros = montante - capital 

#Exibe os resultados
print(f'Resultados: ')
print(f'Montante (M): R${montante:.2f}')
print(f'Juros compostos (J): R${juros:.2f}')