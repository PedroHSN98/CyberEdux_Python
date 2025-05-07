class Carro():
    def __init__(self):
        self.marca = None
        self.modelo = None
        self.placa = None
        self.qtd_de_combustivel = 0


    def abastecer(self, quantidade):
        assert self.qtd_de_combustivel + quantidade <= 30, 'Limite excedido'
        self.qtd_de_combustivel += quantidade

    
    def exibir(self):
        print('Marca:', self.marca)
        print('Modelo:', self.modelo)
        print('Placa:', self.placa)
        print('Qtd de combustível (L):', self.qtd_de_combustivel)


my_car = Carro()
my_car.marca = 'Volvo'
my_car.modelo = 'XC90'
my_car.placa = 'CAR-7779'

print('--- Antes ---')
my_car.exibir()

print('Abastecendo 20L...')
my_car.abastecer(20)

print('--- Depois ---')
my_car.exibir()

print('Abastecendo 20L...')
try:
    my_car.abastecer(20)
except Exception as ex:
    print('Ocorreu um erro:', ex)

print('--- Depois ---')
my_car.exibir()