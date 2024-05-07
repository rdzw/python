class Passaro:
    def voar(self):
        print("voando...")
        
class Pardal(Passaro):
    def voar(self):
        return super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz nao pode voar")

"""Poliformismo filho de passaro ele se comporta de varias formas"""
def plano_voo(obj):
    obj.voar()

p1 = Pardal()
p2 = Avestruz()

"""instanciando"""
plano_voo(p1)
plano_voo(p2)