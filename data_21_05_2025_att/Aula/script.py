#Atividades simulador de Carros

class Carro:
    def __init__(self, placa):
        self.velocidade_atual = 0 #km/h
        self.kilometragem = 0 #km
        self.placa = placa

    def andar(distancia): #distancia em km
        #Atualizar a kilometragem
        #Retorno o tempo de viagem
        self.kilometragem += distancia
        return distancia/self.velocidade_atual

#Agora, vamos implementar os tipos de carros
# Em cada tipo especifico de carro, o metodo andar tem um comportamento

class CarroGasolina(Carro):
    def __init__(self, placa, capacidade, autonomia):
        super().__init__(placa)
        self.autonomia = autonomia
        self.capacidade_tanque = capacidade 
        self.qtd_de_gasolina = capacidade

    # Precisamos sobreescrever o método andar para criar comoportamentos especifiocos 
    #do carro e gasolina
    def andar(self, distancia): #distancia em km
        consumo = distancia/self.velocidade_atual
        assert consumo <= self.qtd_de_gasolina, 'QTD DE gasolina insuficiente'
        self.qtd_de_gasolina -= consumo
        return super().andar(distancia)
    
class CarroEletrico(Carro):
    def __init__(self, placa, capacidade, autonomia):
        super().__init__(placa)
        self.carga_atual = capacidade #KWH
        self.capacidade = capacidade
        self.autonomia = autonomia

    def andar(self, distancia):
        #atualizar a bateria
        consumo = distancia/self.autonomia
        assert consumo <= self.carga_atual, 'Carga insuficiente de bateria'
        self.carga_atual -= consumo 
        return super().andar(distancia)

# codigo de teste

opcao = input('Digite 1 para criar um carro a gasolina ou 2 para eletrico')
placa = input('Digite a placa do carro')
if opcao == '1':
    capacidade = float(input('Capacidade em Litros'))
    autonomia = float(input('Autonomia por Litros'))
    meu_carro = CarroGasolina(placa, capacidade, autonomia)
elif opcao == '2':
    capacidade = float(input('Capacidade em kwh'))
    autonomia = float(input('Autonomia em  km/kwh'))
    meu_carro = CarroEletrico(placa, capacidade, autonomia)
else:
    print('opcao invalida')
    exit()

        

