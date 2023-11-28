# P33: gráfico de barras agrupadas

# No programa a seguir, mostramos como produzir um gráfico de
# barras agrupadas que mostra o número de homens e mulheres
# inscritos em cada curso.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({"mulheres": [40, 10, 30],
                   "homens": [30, 15, 20]},
                  index=["teatro", "escultura", "pintura"])
barras = df.plot(kind="bar", legend=True, color=["yellow", "blue"])

plt.show()
