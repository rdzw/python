# P32 Gráfico de barras vertical
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame([70, 25, 50],
                  index=["teatro", "escultura", "pintura"])
barras = df.plot(kind="bar", legend=False)

plt.show()