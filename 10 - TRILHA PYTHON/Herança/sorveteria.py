class Restaurante:
    """escrevo o metodo __init__ com os atributos da classe"""
    def __init__(self, restaurante_nome, cozinha_tipo):
        """parâmetros dos atributos da classe"""
        self.restaurante_nome = restaurante_nome
        self.cozinha_tipo = cozinha_tipo

    """A classe filha recebe atributos da classe pai"""
class BarracaDeSorvete(Restaurante):
    def __init__(self, sabores):
        self.sabores = sabores
        
    def mostra_sabores(self):
        print(f"Sabores: {self.sabores}")
    
"""instanciar para chamar o metodo mostrar sabores"""
sorveteria = BarracaDeSorvete("chcolate, morando")
sorveteria.mostra_sabores()