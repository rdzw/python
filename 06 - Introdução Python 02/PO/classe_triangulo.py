class Triangulo:
    """Triângulo é um polígono de três lados e três ângulos."""

    def __init__(self, a: int, b: int, c: int):
        """Recebe como parâmetro os três lados de um triângulo a, b e c."""
        self.a = a
        self.b = b
        self.c = c

    def side_list(self) -> list:
        """Retorna os lados em formato de lista."""
        return [self.a, self.b, self.c]

    def perimetro(self):
        """Calcula o perímetro de um triangulo."""
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return 0

        return self.a + self.b + self.c