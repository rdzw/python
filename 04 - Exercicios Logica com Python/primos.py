def EsteNumeroEPrimo(numero):
    numeroDeDivisores = 0

    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            numeroDeDivisores += 1

            if numeroDeDivisores > 2:
                return False

    return True
def maior_primo(numero):
    if numero < 2:
        return 0

    for numeroCorrente in range(numero, 2, -1):
        if EsteNumeroEPrimo(numeroCorrente):
            return numeroCorrente

# Teste números maiores ou igual a 2
def test_NumerosMaioresQueUm():
    assert maior_primo(100) == 97

# Teste números menores que 2. Por padrão retorna 0
def test_NumerosMenoresQueDois():
    assert maior_primo(1) == 0