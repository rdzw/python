# P34: Histograma

# O programa a seguir mostra como produzir um histograma com três
# bins a partir de um conjunto de dados que armazena o número de
# horas que 30 diferentes estudantes passaram se preparando para
# uma prova.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "tempo": [4, 5, 1, 7, 7, 8, 6, 6, 5,
              2, 5, 8, 7, 1, 6, 3, 4, 8,
              5, 7, 4, 6, 3, 6, 2, 6, 8]
})
hist = df.plot(kind="hist", bins=3)

plt.show()
