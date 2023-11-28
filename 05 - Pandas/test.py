#importação de CSV  para um dataframe,
# definindo ainda que a coluna SIGLA sera utilizada com indice de linha.

#importando a biblioteca pandas
import pandas as pd

#arquivo armazenado em meu computador. Com o metodo READ_CSV(),
# Parâmentro usado index_col para permitir que a coluna sigla fosse o indice linha.
paises = pd.read_csv(r"C:\Users\rodrigo\Desktop\Nova pasta\python\Pandas\dados\paises.csv" , index_col="sigla")
print(paises)