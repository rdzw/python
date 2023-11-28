# P35: IQR + Boxplot
# Em um boxplot, Q1 e Q3 representam,
# respectivamente, a linha inferior e a linha superior da caixa
# retangular, enquanto Q2 é a reta através da caixa. Os whiskers (as
# duas linhas fora da caixa) marcam os valores mais extremos
# compreendidos entre 1,5 x IQR abaixo do primeiro quartil e acima
# do terceiro quartil. Os casos fora dessa faixa são considerados
# outliers e são plotados individualmente, fora dos whiskers. Veja que
# é isto que acontece com o valor 18 do conjunto de dados (trata-se
# da bolinha branca localizada bem no topo do gráfico).

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "tempo": [4, 5, 1, 7, 7, 8, 6, 6, 5,
              2, 5, 8, 7, 1, 6, 3, 4, 8,
              5, 7, 4, 6, 3, 6, 2, 6, 18]
})
boxplot = df.boxplot(column=['tempo'],
                     showmeans=True)

plt.show()
