#biblioteca
from math import pi
import sys
import errno # bliclioteca de erros

#cores para mensagens de aviso
ERRO = '\033[91m'
NORMAL = '\033[0m'


#help
def help():
    print("É necessario informar o raio do circulo")
    print("Sintaxe: {} <raio>".format(sys.argv[0][2:]))

#palavra reservada para função
#função circulo
def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        print(ERRO + "O raio deve ser um valor numerico" + NORMAL)
        sys.exit(errno.EPERM) #informando erro
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('A area do circulo', area)


