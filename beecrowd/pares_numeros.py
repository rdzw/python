contando_positivos = 0

for i in range(5):
    valor = float(input())
    if valor % 2 == 0:
        contando_positivos += 1

print(f"{contando_positivos} valores pares")
        