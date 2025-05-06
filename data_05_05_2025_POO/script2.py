class Carro:  # Definir a classe Carro
    def __init__(self):
        # Atributos com valores padrão
        self.marca = None
        self.modelo = None
        self.placa = None
        self.qtd_de_combustivel = 0

    def abastecer(self, quantidade):
        if self.qtd_de_combustivel + quantidade > 30:
            print("🚫 Não é possível abastecer: limite de 30L excedido.")
            print(f"Combustível atual: {self.qtd_de_combustivel}L")
        else:
            self.qtd_de_combustivel += quantidade
            print(f"✅ Abastecido com {quantidade}L. Total: {self.qtd_de_combustivel}L")

    def exibir_dados(self):
        print("=== Dados do Carro ===")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Placa: {self.placa}")
        print(f"Combustível: {self.qtd_de_combustivel}L")

# Criando um objeto (Carro)
my_car = Carro()

# Atribuindo valores
my_car.marca = 'Chevrolet'
my_car.modelo = 'Corsa'
my_car.placa = 'MLY-5120'

# Abastecendo
my_car.abastecer(10)
my_car.abastecer(4)
my_car.abastecer(20)  # Este ultrapassa o limite e será bloqueado

# Exibindo os dados
my_car.exibir_dados()
