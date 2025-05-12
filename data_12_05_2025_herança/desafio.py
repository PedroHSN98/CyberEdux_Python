'''
Implemente a classe estudante e depois a subclasse EstudanteDeMestrado
'''

'''
O eatudanteDeMestrado deve ter:
    Atributos:
        programa (str) - O programa de mestrado do qual ele participa
        orientador (str) - Orientador do estudante
        bolsa (float) - Valor mensal da bolsa

    Métodos 
        exibir - mostra tosoas os dados do estudante
'''

class Estudante:
    def __init__(self):
        self.nome = None
        self.email = None
        self.semestre = 1      
        
    def avancar_semestre(self):
        self.semestre += 1

class EstudanteDeMestrado(Estudante):
    def __init__(self, nome, email, programa, orientador, bolsa):
        super().__init__()
        self.nome = nome
        self.email = email
        self.programa = programa
        self.orientador = orientador
        self.bolsa = bolsa
    
    def exibir(self):
        print('Nome:', self.nome)
        print('Email:', self.email)
        print('Programa:', self.programa)
        print('Orientador:', self.orientador)
        print('Bolsa:', self.bolsa)
        print('Semestre:', self.semestre)


estudante_mestrado = EstudanteDeMestrado(
    nome="Lucas Portuga",
    email="lucas.portuga@gmail.com",
    programa="Ciência da Computação",
    orientador="Prof. JhonVlogues",
    bolsa=1500.00
)

estudante_mestrado.exibir()
estudante_mestrado.avancar_semestre()
print("Avanço do semestre:")
estudante_mestrado.exibir()

