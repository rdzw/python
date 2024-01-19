#while True:
#   print('vai demorar')

from random import randint

numero_informado = -1
numero_secreto = randint(0,9)

while numero_informado != numero_secreto:
    numero_informado = int(input('informe o numero:'))
print('numero secreto {} foi encontrado'.format(numero_secreto))