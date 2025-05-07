# Classe Carro
class Carro:
    def __init__(self):
        self.marca = None
        self.modelo = None
        self.placa = None
        self.qtd_de_combustivel = 0

    def abastecer(self, quantidade):
        if self.qtd_de_combustivel + quantidade > 30:
            quantidade_real = 30 - self.qtd_de_combustivel
            self.qtd_de_combustivel = 30
            return quantidade_real
        else:
            self.qtd_de_combustivel += quantidade
            return quantidade  # retorna o quanto foi de fato abastecido

    def exibir_dados(self):
        print("=== Dados do Carro ===")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Placa: {self.placa}")
        print(f"Combustível: {self.qtd_de_combustivel}L")
        print()


# Classe PostoDeCombustivel
class PostoDeCombustivel:
    def __init__(self, valor_litro_combustivel):
        self.carros = []
        self.valor_litro_combustivel = valor_litro_combustivel

    def adicionar_carro(self, carro):
        self.carros.append(carro)

    def abastecer_carros(self):
        faturamento_total = 0.0
        for carro in self.carros:
            litros_faltando = 30 - carro.qtd_de_combustivel
            if litros_faltando > 0:
                litros_abastecidos = carro.abastecer(litros_faltando)
                valor = litros_abastecidos * self.valor_litro_combustivel
                faturamento_total += valor
        return faturamento_total


# ==== EXEMPLO DE USO ====

# Criando carros
carro1 = Carro()
carro1.marca = "Fiat"
carro1.modelo = "Uno"
carro1.placa = "AAA-1111"
carro1.abastecer(10)

carro2 = Carro()
carro2.marca = "VW"
carro2.modelo = "Gol"
carro2.placa = "BBB-2222"
carro2.abastecer(25)

# Criando o posto
posto = PostoDeCombustivel(valor_litro_combustivel=5.50)

# Adicionando os carros ao posto
posto.adicionar_carro(carro1)
posto.adicionar_carro(carro2)

# Abastecendo os carros e mostrando faturamento
faturamento = posto.abastecer_carros()
print(f"Faturamento total do posto: R${faturamento:.2f}")

# Exibindo dados atualizados dos carros
carro1.exibir_dados()
carro2.exibir_dados()
