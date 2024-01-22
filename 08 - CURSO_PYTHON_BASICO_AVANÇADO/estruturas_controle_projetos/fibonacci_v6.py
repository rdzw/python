# 0,1,1,2,3,5,8,13,21......

def fibonacci(quantidade):

    resultado = [0,1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade
    return resultado

if __name__ == '__main__':
    #listar os 20 primeiros numeros da sequencia
    for fib in fibonacci(20):
        print(fib)