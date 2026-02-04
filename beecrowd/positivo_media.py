positivos = 0 #isso seria um contador
soma = 0

for i in range(6):
    valor = float(input())
    if valor > 0:
        positivos += 1 #acada positivo ele conta e acrescenta
        soma += valor
        media = soma / positivos
            
print(f"{positivos} valores positivos")
print(f"{media:.1f}")
