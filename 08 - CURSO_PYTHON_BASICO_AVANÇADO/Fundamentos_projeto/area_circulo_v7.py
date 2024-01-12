#biblioteca
from math import pi

#palavra reservada para função
#função circulo
def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    raio = input('informe o raio: ')
    area = circulo(raio)
    print('A area do circulo', area)


