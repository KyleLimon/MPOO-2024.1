from pessoa import Pessoa

class Aluno(Pessoa):
    
    def __init__ (self, nome, endereco, matricula):
        super().__init__(self, nome, endereco)
        self.matricula = matricula 