class Bicicleta:
    def __init__(self, cor, modelo, ano, valor) :
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("plim plim...")

    def parar(self):
        print("parar")
        print("bicicleta parada")
    
    def trocar_marcha(nro_marcha):
        print("marcha trocada...")


b2 = Bicicleta("verde", "monark" ,2000, 30)
print(b2)
