#importação de arquivo json
import pandas as pd
import json

# importa o arquivo json para memoria
with open(r"C:\Users\rodrigo\Desktop\Nova pasta\python\Pandas\dados\notas.json") as f:
    j_notas = json.load(f)

#transfere as infomações para um dataframe
notas = pd.DataFrame(j_notas,
                     columns=['matricula','notas'])
print(notas)