class Conta:
    def __init__(self,saldo = 0.0):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if (saldo < 0):
            print("Saldo não pode ser negativo")
        else:
            self._saldo = saldo

conta  = Conta(1000.0)
conta.saldo = -300.0

