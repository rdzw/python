import matplotlib.pyplot as plt
import pandas as pd

#Pequeno programa que gera um grafico barra agrupando dados
#do aquivo zona leste.csv, onde pego a coluna do DIP e o ano,assim gerando
#um grafico de qual dip teve mais ocorrências no determinado ano.
#--------------------------------------------------------
#importar a base de dados
#--------------------------------------------------------
df = pd.read_csv(r"C:\Users\RODRIGO\Documents\python\05 - Pandas\dados\zona leste.csv")

#Exibo as informações do DataFrame.
print(df)

#Crio uma função apresentando os dados desejados.
plt.bar(df['DIP DO FATO'],df['2021'],color="red")

#Determino um titulo para o eixo X.
plt.xlabel("DIP - DIVISÃO DE INVESTIGAÇÃO POLICIAL")

#Determino um titulo para o eixo Y.
plt.ylabel("TOTAL DE OCORRÊNCIAS 2021")

#Determino um titulo geral para o grafico.
plt.title("TOTAL DE OCORRÊNCIAS POR DIP", fontsize="15")

#Imprime o Grafico
plt.show()