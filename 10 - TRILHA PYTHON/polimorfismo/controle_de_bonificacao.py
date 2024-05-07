class Funcionario:
    def __init__(self,nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def get_bonificacao(self):
        return self._salario * 0.10
        
class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd_gerenciaveis):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_gerenciaveis = qtd_gerenciaveis
        
    def get_bonificacao(self):
        return super().get_bonificacao() + 1000


class ControleDeBonificacao:
    
    def __init__(self,total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes
        
    def registra(self,funcionario):
        self._total_bonificacoes += funcionario.get_bonificacao()
    
    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes
    
if __name__ == '__main__':
    funcionario = Funcionario("João",11111111-11,2000.0)
    print("Bonificacao funcionario:{}".format(funcionario.get_bonificacao()))
    
    gerente = Gerente("João","11111111-11",2000.0,'1234',0)
    print("Bonificação gerente:{}".format(gerente.get_bonificacao()))
    
    controle = ControleDeBonificacao()
    controle.registra(funcionario)
    controle.registra(gerente)

    print("total: {}".format(controle._total_bonificacoes))