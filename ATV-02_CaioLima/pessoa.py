class Pessoa:

    def __init__ (self, nome, matricula, endereco):
        self.__nome = nome
        self.__matricula = matricula
        self.__endereco = endereco

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_matricula(self):
        return self.__matricula
    
    def set_nome(self, matricula):
        self.__matricula = matricula 

    def get_endereco(self):
        return self.__endereco
    
    def set_nome(self, endereco):
        self.__endereco = endereco 

    def informacao(self):
        pass 

