class Restaurante:
    """escrevo o metodo __init__ com os atributos da classe"""
    def __init__(self, restaurante_nome, cozinha_tipo):
        """parâmetros dos atributos da classe"""
        self.restaurante_nome = restaurante_nome
        self.cozinha_tipo = cozinha_tipo

    """aqui crio o metodo descricao_restaurante"""
    def descricao_restaurante(self):
        msg = self.restaurante_nome + " está servindo " + self.cozinha_tipo + " ."
        print("\n" + msg)

    """crio o metodo restaurante_aberto"""
    def restaurante_aberto(self):
        print("restaurante aberto")

    """Criação de instâncias"""
restaurant = Restaurante('Alternativo', 'pizza')
print(restaurant.restaurante_nome)
print(restaurant.cozinha_tipo)

restaurant.descricao_restaurante()
restaurant.restaurante_aberto()
        




