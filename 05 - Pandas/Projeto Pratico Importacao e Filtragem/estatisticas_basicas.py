#estatisticas basicas:medidas de tendencia central
import pandas as pd

#cria o DataFrame
dados = {"jogador":["Marcelo",
                    "Pedro",
                    "Marcelo",
                    "Adriano",
                    "Mauro",
                    "Pedro",
                    "Marcelo"],
         "infração": ["FALTA VIOLENTA",
                      "RECLAMAÇÃO",
                      "FALTA COMUM",
                      "RECLAMAÇÃO",
                      "FALTA COMUM",
                      "FALTA VIOLENTA",
                      "RECLAMAÇÃO"],
         "punicao": [4,1,3,2,4,4,2]
         }

df = pd.DataFrame(dados)

#calcula as medidas de tendencia central
print("Média",df['punicao'].mean())
print("mediana:",df['punicao'].median())
print("moda:", df['punicao'].mode().values)