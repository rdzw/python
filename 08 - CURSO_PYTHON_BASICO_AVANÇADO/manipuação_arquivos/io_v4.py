try:
    arquivo = open('pessoas.csv')

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.split(',')))
finally:
    arquivo.close()

if arquivo.closed:
    print('Arquio foi fechado')