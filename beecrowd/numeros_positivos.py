positivos = 0 #isso seria um contador

for i in range(6):
    valor = float(input())
    if valor > 0:
        positivos += 1 #acada positivo ele conta e acrescenta
    
print(f"{positivos} valores positivos")