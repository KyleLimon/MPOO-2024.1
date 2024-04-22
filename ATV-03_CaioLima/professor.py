from servidor import Servidor


class Professor(Servidor):
    
    def __init__ (self,cargo, nome, endereco, formacao):
        super().__init__(self, cargo, nome, endereco)
        self.formacao = formacao
        