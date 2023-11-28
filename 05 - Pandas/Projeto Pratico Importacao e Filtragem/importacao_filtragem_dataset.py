#Quais os paises que tambem tem verde, amarelo, azul,
# e branco entre as cores de sua bandeira nacional?

import pandas as pd
#--------------------------------------------------------
#importar a base de dados
#--------------------------------------------------------
flags = pd.read_csv(r"C:\Users\rodrigo\Desktop\Nova pasta\python\Pandas\dados\flags.csv")

#--------------------------------------------------------------------------------------
#Alguns metodos para obter informações basicas
#-------------------------------------------------------------------------------------
#Imprimi as primeiras linhas
print('head():'); print(flags.tail())
print('-------------------------------------------------------------------------------')

#Quem tem verde,amarelo,azul e branco na bandeira
#separa as cores
verde = flags['green']
amarelo = flags['gold']
azul = flags['blue']
branco = flags['white']
soma = verde + amarelo + azul + branco

#Gera o vetor boolean com True para quem tem as 4 cores
tem_todas = (soma==4)

#Imprime os nomes dos paises com as quatro cores
print('paises com verde, amarelo, azul e branco: ')
print((flags[tem_todas.values]['name']))