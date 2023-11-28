# P30 Gráfico de uma função
import pandas as pd
import matplotlib.pyplot as plt

# A primeira linha cria um DataFrame chamado df com 10 linhas
# e apenas a coluna x , com valor variando de 1 na primeira linha
# até 10 na última. Esses valores são produzidos com o uso da
# instrução list(range(1,11)) ( list() é uma função que gera uma
# lista de valores e range() a função que especifica quais serão
# os valores, neste caso o conjunto de números de 1 até o
# número anterior a 11).
df = pd.DataFrame({"x": list(range(1,11))})

df["y"] = (df.x * 2) + 3

lines = df.plot.line(x="x", y="y", legend=False)

plt.show()
