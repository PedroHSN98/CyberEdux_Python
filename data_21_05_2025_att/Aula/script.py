###Herança  e polimorfismo

class Carro():
    def __init__(self, placa):
        self.velocidade_atual = 0    #km/h
        self.kilometragem = 0        #km
        self.placa = placa

    def andar(self, distancia):
        self.kilometragem += distancia
        return distancia/self.velocidade_atual
    
    def mostrar_painel(self):
        print('PAINEL DO CARRO DE PLACA: ' ,self.placa)
        print('VELOCIDADE (km/h): ' ,self.velocidade_atual)
        print('KILOMETRAGEM (km): ' ,self.kilometragem)

#Implementar os tipos de carros, onde cada carro vai ter um comportamneto diferente com relação ao método 'andar'     
class CarroGasolina():
    def __init__(self, placa, capacidade, autonomia):
        super().__init__(placa)
        self.autonomia = autonomia
        self.capacidade = capacidade
        self.qtd_de_gasolina = capacidade

#Sobreesccrever método andar pra criar um comportamento específico do carro e gasolina
    def andar(self, distancia):
        consumo = (distancia)/(self.autonomia)
        assert consumo <= self.qtd_de_gasolina,  'Qtd de gasolina insuficiente'
        self.qtd_de_gasolina -= consumo          #Atualizar a qtd do tanque após viagem
        
    def mostrar_painel():
        super().mostrar_painel()
        print('QTD DE GASOLINA (L): ', self.qtd_de_gasolina)
        print('CAPACIDADE: ', self.capacidade)

class CarroEletrico(Carro):
    def __init__(self, placa, capacidade, autonomia):
        super().__init__(placa)
        self.autonomia = autonomia
        self.capacidade = capacidade
        self.carga_atual = capacidade

    def andar(self, distancia):
        consumo = (distancia)/(self.autonomia)
        assert consumo <= self.carga_atual
        self.carga_atual -= consumo           

    def mostrar_painel(self):
        super().mostrar_painel()     
        print('CARGA ATUAL (Kwh): ', self.carga_atual)
        print('CAPACIDADE (Kwh): ', self.capacidade)

#----Código de teste----
opcao = input('Digite 1 para criar um carro elétrico ou 2 para criar um aleatório: ')
placa = input('Digite a placa do carro: ')
if opcao == '1':
    capacidade = float(input('Capacidade em litros: '))
    autonomia = float(input('Autonomia em km/L: '))
    meu_carro = CarroGasolina(placa, capacidade, autonomia)
elif opcao == '2':
    capacidade = float(input('Capacidade em Kwh'))
    autonomia = float(input('Autonomia em km/Kwh: '))
    meu_carro = CarroEletrico(placa, capacidade, autonomia)
else: 
    print('Opação inválida')
    exit()

meu_carro.mostra_painel()      #Exibir painel atual do carro, antes da viagem
distancia  = float(input('Insira  a distância para percorrer em km: '))
print('Fazendo percurso...')
tempo_de_viagem = meu_carro.andar(distancia)
print('Tempo de viagem (h): ', tempo_de_viagem)
meu_carro.mostrar_painel()
