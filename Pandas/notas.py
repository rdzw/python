#impotação de csv sem cabeçalho e com ";" como separador
# "sep" caractere ou expressao regular utilizado para separar campos em cada linha
#
import pandas as pd

notas = pd.read_csv(r"C:\Users\rodrigo\Desktop\Nova pasta\python\Pandas\dados\notas.csv" , sep=";",
                    names=['matricula','nota1','nota2'])
print(notas)