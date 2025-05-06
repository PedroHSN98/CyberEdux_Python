#Código que cria uma classe para estudante de graduação, que
#herda todos os atributos e métodos da classe Estudante.


class Estudante:
    def __init__(self):
        self.nome = None
        self.email = None
        self.semestre = 1

    def avancar_semestre(self):
        self.semestre += 1


class EstudanteDeGraduacao(Estudante):
    def __init__(self):
        super().__init__()
        self.curso = None
        self.modalidade = None

    def exibir(self):
        print('Nome:', self.nome)
        print('Curso:', self.curso)
        print('Modalidade:', self.modalidade)
