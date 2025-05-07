class Carro():
    def __init__(self):
        self.marca = None
        self.modelo = None
        self.placa = None
        self.qtd_de_combustivel = 0
        self.qtd_max_combustivel = 30


    def abastecer(self, quantidade):
        assert self.qtd_de_combustivel + quantidade <= self.qtd_max_combustivel, 'Limite excedido'
        self.qtd_de_combustivel += quantidade

    
    def exibir(self):
        print('Marca:', self.marca)
        print('Modelo:', self.modelo)
        print('Placa:', self.placa)
        print('Qtd de combustível (L):', self.qtd_de_combustivel)


class PostoDeCombustivel():
    def __init__(self) -> None:
        self.carros = []
        self.valor_combustivel = 5.9


    def adicionar_carro(self, carro):
        self.carros.append(carro)

    
    def abastecer_carros(self):
        for carro in self.carros:
            qtd = carro.qtd_max_combustivel - carro.qtd_de_combustivel
            faturamento += qtd*self.valor_combustivel
            carro.abastecer(qtd)
        return faturamento


meu_posto = PostoDeCombustivel()

meu_carro_1 = Carro()
meu_carro_1.marca = 'Toyota'
meu_carro_1.modelo = 'Corolla'
meu_carro_1.placa = 'XLR-3040'
meu_carro_1.qtd_max_combustivel = 60

meu_carro_2 = Carro()
meu_carro_2.marca = 'Peugeot'
meu_carro_2.modelo = '207'
meu_carro_2.placa = 'NJJ-4354'
meu_carro_2.qtd_max_combustivel = 50

meu_carro_3 = Carro()
meu_carro_3.marca = 'Mitsubishi'
meu_carro_3.modelo = 'Lancer'
meu_carro_3.placa = 'AAA-1111'
meu_carro_3.qtd_max_combustivel = 59

meu_posto.adicionar_carro(meu_carro_1)
meu_posto.adicionar_carro(meu_carro_2)
meu_posto.adicionar_carro(meu_carro_3)

for carro in meu_posto.carros:
    carro.exibir()
    print('---')

print('Abastecendo carros...')
meu_posto.abastecer_carros()
print('---')

for carro in meu_posto.carros:
    carro.exibir()
    print('---')