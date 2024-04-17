from pessoa import Pessoa


class Professor(Pessoa):
    
    def __init__ (self, nome, endereco, formacao):
        super().__init__(self, nome, endereco)
        self.formacao = formacao
