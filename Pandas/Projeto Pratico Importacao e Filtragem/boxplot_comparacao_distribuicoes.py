#Boxplot - comparação de distribuições
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "homens":[4,2,7,3,1,4,2,4,8,1],
    "mulheres":[5,4,6,5,4,2,6,6,4,3]
})

boxplot = df.boxplot(column=['homens','mulheres'],
                     showmeans=True)
plt.show()