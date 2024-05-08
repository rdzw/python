class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    
    @classmethod    
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)
    
p = Pessoa.criar_apartir_data_nascimento(1994,3,21,"rodrigo")
print(p.nome, p.idade)