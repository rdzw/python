class Data:
    def __init__(self,dia,mes,ano):
        self.dia = dia
        self.mes  = mes
        self.ano = ano
        

    def __str__(self): # __str__ posso usar esse metodo para converte para string
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data()
d1.dia = 5
d1.mes = 12
d1.ano = 2019
print(d1)

d2 = Data()
d2.dia = 7
d2.mes = 11
d2.ano = 2020
print(d2)