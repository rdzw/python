numero = int(input("Informe um número inteiro: "))

if(numero % 3 == 0 and numero % 5 == 0):
    print("FizzBuzz")
else:
    print(numero)