from pessoa import Pessoa

class Servidor(Pessoa):

    def __init__ (self, cargo, nome, logradouro, numero):
        super().__init__(self, nome, logradouro, numero)
        self.cargo = cargo
        