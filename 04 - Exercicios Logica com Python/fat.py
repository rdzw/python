# Retorna o valor númerico fornecido pelo usuário
def PegarEntrada(label):
    return int(input("Forneça o valor de {}: ".format(label)))

# Calcula o fatorial de um número
def Fatorial(n):
    fatorial = 1
    for numeroCorrente in range(n, 0, -1):
        fatorial *= numeroCorrente

    return fatorial

# Calcula o coeficiente binomial de um número
def CoeficienteBinomial(n, k):
    return Fatorial(n) / (Fatorial(k) * Fatorial(n - k))

n = PegarEntrada("n")
k = PegarEntrada("k")
print(CoeficienteBinomial(n, k))

print(sum(len('abc') + len('a')))
