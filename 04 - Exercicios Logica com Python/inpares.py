incremento = 1
numeroIniciais = []

qtdDeNumeros = int(input("Forneça um número inteiro positivo: "))

while len(numeroIniciais) < qtdDeNumeros:
    if incremento % 2 > 0:
        numeroIniciais.append(incremento)
        print(incremento)
    incremento += 1