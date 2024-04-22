from aluno import *
from professor import *

class Cadastrar:
    def __init__(self):
        self.alunos = []

    def adicionarAluno (self, aluno):
        self.alunos.append(aluno)