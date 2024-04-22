from endereço import Endereco

class Pessoa(Endereco):

    def __init__ (self, nome, logradouro, numero):
        super().__init__(self, logradouro, numero)
        self.__nome = nome
        
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

