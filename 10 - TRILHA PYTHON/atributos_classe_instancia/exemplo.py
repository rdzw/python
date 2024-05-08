class Estudante:
    escola = "Dio"
    
    def __init__(self, nome, matricula):
        """self é de instancia"""
        self.nome = nome
        self.matricula = matricula
        
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
aluno_1 = Estudante("Rodrigo", 1)
aluno_2 = Estudante("Keisi", 2)

print(aluno_1)
print(aluno_2)