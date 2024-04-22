from aluno import *
from professor import *

class Cadastrar:
    def __init__(self):
        self.alunos = []

    def adicionarAluno (self, aluno):
        self.alunos.append(aluno)

    
    def get_aluno(self):
        return self.__aluno
      
    def set_aluno(self, aluno):
        self.__aluno = aluno
