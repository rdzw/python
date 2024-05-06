class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia
        
    def depositar(self,valor):
        self._saldo += valor
    
    def sacar(self,valor):
        self._saldo -= valor
        
    """metodo para acessar saldo """
    def mostrar_saldo(self):
        return self._saldo
    
"""Instânciar"""
conta = Conta(100)
conta.depositar(100)
print(conta.mostrar_saldo())