def obter_rota():
    qtd_ponto = int(input('Quantos pontos de parada deseja inserir? '))
    while qtd_ponto < 2:
        print('A rota deve ter no mínimo 2 pontos.')
        qtd_ponto = int(input('Quantos pontos de parada deseja inserir? '))
    
    rota = []
    for i in range(qtd_ponto):
        cidade = int(input(f'Insira a {i + 1}° cidade (0 - Cuiabá, 1 - Rondonópolis, 2 - Primavera do Leste): '))
        while cidade not in [0, 1, 2]:
            print('Cidade inválida. Escolha entre 0, 1 ou 2.')
            cidade = int(input(f'Insira a {i + 1}° cidade (0 - Cuiabá, 1 - Rondonópolis, 2 - Primavera do Leste): '))
        rota.append(cidade)
    return rota


def calcular_tempo_total(rota, tempos):
    tempo_total = 0
    for i in range(len(rota) - 1):
        origem = rota[i]
        destino = rota[i + 1]
        tempo_total += tempos[origem][destino]
    return tempo_total


# Tabela de tempos entre as cidades (em horas)
# tempo_de_viagem[origem][destino]
tempo_de_viagem = [
    [0, 3.25, 3.5],  # 0 - Cuiabá
    [3.25, 0, 3.1],  # 1 - Rondonópolis
    [3.5, 3.1, 0]    # 2 - Primavera do Leste
]

# Programa principal
print('Cidades disponíveis:')
print('0 - Cuiabá')
print('1 - Rondonópolis')
print('2 - Primavera do Leste')
print('Insira os números correspondentes às cidades para definir a rota.')

rota = obter_rota()
tempo_total = calcular_tempo_total(rota, tempo_de_viagem)

print(f'Rota escolhida: {rota}')
print(f'Tempo total da viagem: {tempo_total:.2f} horas')
