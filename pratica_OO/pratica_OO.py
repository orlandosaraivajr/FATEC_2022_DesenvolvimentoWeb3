from datetime import date

class Aluno:
    def __init__(self, nome, sobrenome, curso):
            self._nome = nome
            self._sobrenome = sobrenome
            self._curso = curso

    @property
    def sobrenome(self):
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, valor):
        self._sobrenome = valor

    def __str__(self):
        pass

    def __repr__(self):
        pass


class Professor:
    def __init__(self, nome, sobrenome):
            self._nome = nome
            self._sobrenome = sobrenome
            self._disciplinas = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def disciplina(self):
        pass

    def adicionar_disciplina(self, disciplina):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass


class SalaAula:
    def __init__(self, professor):
        if isinstance(professor, Professor):
            self._professor = professor
        else:
            raise TypeError('Tipo do professor precisa instância de Professor')
        self._alunos = []

    @property
    def professor(self):
        return str(self._professor)

    @property
    def alunos(self):
        return self._alunos

    def adicionar_aluno(self, nome, sobrenome, curso):
        pass

    def busca_aluno(self, nome_procurado):
        pass
    
    def __str__(self):
        return 'Sala com prof. ' + self.professor

    def __repr__(self):
        return str(self)

