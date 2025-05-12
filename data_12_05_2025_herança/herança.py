class Estudante:
    def __init__(self):
        self.nome = None
        self.email = None
        self.semestre = 1      
        
    def avancar_semestre(self):
        self.semestre += 1

class EstudanteDeGraduacao:
    def __init__(self, nome, email, curso, modalidade):
        super().__init__()
        self.nome = nome
        self.email = email
        self.curso = curso
        self.modalidade = modalidade

    def exibir(self):
        print('Nome', self.nome)
        print('Curso', self.curso)
        print('Modalidade', self.modalidade)

estudante = EstudanteDeGraduacao(
    'Fulano da Silva', 
    'Fulano@gmail.com', 
    'Análise de Desenvolvimento de Sistemas', 
    'Técnologo')


#estudante.nome = 'Fulano da Silva'
#estudante.email = 'Fulano@gmail.com'
#estudante.curso = 'Análise de Desenvolvimento de Sistemas'
#estudante.modalidade = 'Técnologo'
estudante.exibir()

