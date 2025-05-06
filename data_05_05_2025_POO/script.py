#Exemplo: Conta Bancaria
class Conta:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial
    
    def exibir_saldo(self):
        print(f'Titular: {self.titular}')
        print(f'Saldo atual: R${self.saldo:.2f}')
    
#Criando um objeto (Conta)
conta1 = Conta("Maria", 1500.00)

#Chamando o método para exibir o saldo
conta1.exibir_saldo()