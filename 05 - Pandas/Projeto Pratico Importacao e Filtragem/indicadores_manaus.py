import matplotlib.pyplot as plt
import pandas as pd

#--------------------------------------------------------
#importar a base de dados
#--------------------------------------------------------
df = pd.read_csv(r"C:\Users\RODRIGO\Documents\python\05 - Pandas\dados\zona leste.csv")

print(df)

plt.bar(df['DIP DO FATO'],df['2021'],color="red")
plt.xlabel("DIP - DIVISÃO DE INVESTIGAÇÃO POLICIAL")
plt.ylabel("TOTAL DE OCORRÊNCIAS 2021")
plt.title("TOTAL DE OCORRÊNCIAS POR DIP", fontsize="15")

plt.show()

