import csv
from urllib import request

def read(url):
    with request.urlopen(url) as entrada:
        print('baixando o CSV.....')
        dados = entrada.read().decode('latin1')
        print('Download completo !!!!')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')

# Identação é fundamental ser observado 
# para o correto funcionamento do sistema        
if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')