#dado um numero inteiro n ele imprimi os fatores e suas multiplicidades
n = int(input("Digite um número inteiro > 1: "))

fator = 2
multiplicidade = 0

while n > 1:
    while n % fator == 0:
        multiplicidade = multiplicidade + 1
        n = n / fator
    if multiplicidade > 0:
        print("Fator", fator, "multipliciade = ", multiplicidade)
    fator = fator + 1
    multiplicidade = 0