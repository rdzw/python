#biblioteca
from math import pi

#palavra reservada para função
def circulo(raio):
    print('Area do circulo', pi * float(raio) ** 2)

if __name__ == '__main__':
    raio = input('informe o raio: ')
    circulo(raio)


