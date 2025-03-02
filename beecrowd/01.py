"""
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:

Perimetro = XX.X

Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem

Area = XX.X
Entrada

A entrada contém três valores reais.
Saída

O resultado deve ser apresentado com uma casa decimal.
Exemplo de Entrada 	Exemplo de Saída

6.0 4.0 2.0
Area = 10.0
6.0 4.0 2.1
Perimetro = 12.1
"""
A = input(float(""))
B = input(float(""))
C = input(float(""))


# verificar se os lados formam um triangulo
if (A+B+C) and (A+B>C) and (B+C>A):
    perimetro = A+B+C
    print(f"Perimetro = {perimetro:.1f}")
else:
    area = ((A+B) * C) / 2
    print(f"Area = {area:.1f}")
