class Pessoa:

    def __init__ (self, nome, matricula, endereco):
        self.__nome = nome
        self.__endereco = endereco

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_endereco(self):
        return self.__endereco
    
    def set_endereco(self, endereco):
        self.__endereco = endereco 

    def informacao(self):
        pass 

