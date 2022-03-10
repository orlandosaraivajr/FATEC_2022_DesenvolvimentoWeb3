class Primeiraclasse:
    pass

objeto = Primeiraclasse()
isinstance(objeto, object)
type(objeto)
dir(objeto)


class Pessoa:
    def __init__(self, nome, idade):
        self._nome_completo = nome
        self._idade = idade
    
    def nome_upper(self):
        return self.nome.upper()

    @property
    def nome(self):
        return self._nome_completo

    def __repr__(self):
        return self.nome + ' ' + str(self._idade) + ' anos'
    
    def __str__(self):
        return self.nome

# Retornar um dicionário com meus atributos
pessoa1 = Pessoa('Jose', 30)
pessoa1.__dict__

# Composição: Lista de Pessoas

pessoas = []
pessoas.append(Pessoa('Jose', 30))
pessoas.append(Pessoa('Maria', 20))
pessoas.append(Pessoa('João', 25))


