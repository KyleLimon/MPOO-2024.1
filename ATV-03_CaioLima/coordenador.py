from servidor import Servidor


class Coordenador(Servidor):
    
    def __init__ (self,cargo, nome, endereco):
        super().__init__(self, cargo, nome, endereco)