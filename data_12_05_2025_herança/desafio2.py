'''
Crie as seguintes classes:

Carro:
    Atributos
        velocidade (float) - velocidade em km/h
    Métodos
        Acelerar(incremento) - aumentar velocidade em km/h
        frear(decremento) - diminuir velocidade em km/h   

CarroCombustao (subclasse de Carro):
    Atributos
        autonomia (float) - quanto de combustivel consumido a cada km rodado
    Metodos
        combustivel_consumido(horas) - retorna a quantidade de combustivel na qtd de horas especifica

'''


class Carro:
    def __init__(self):
        self.velocidade = 0.0  # velocidade em km/h
    
    def acelerar(self, incremento):
        self.velocidade += incremento
    
    def frear(self, decremento):
        self.velocidade = max(0, self.velocidade - decremento)


class CarroCombustao(Carro):
    def __init__(self, autonomia):
        super().__init__()
        self.autonomia = autonomia  # consumo em litros por km
    
    def combustivel_consumido(self, horas):
        return self.velocidade * horas * self.autonomia


carro = CarroCombustao(autonomia=0.1)  # 0.1 litros por km

carro.acelerar(60)  # Acelera para 60 km/h
print(f"Velocidade: {carro.velocidade} km/h")
print(f"Combustível consumido em 2 horas: {carro.combustivel_consumido(2):.2f} litros")

carro.frear(20)  # Reduz para 40 km/h
print(f"\nVelocidade após frear: {carro.velocidade} km/h")
print(f"Combustível consumido em 1.5 horas: {carro.combustivel_consumido(1.5):.2f} litros")