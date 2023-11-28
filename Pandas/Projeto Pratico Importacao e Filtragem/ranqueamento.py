#metodos sort_values() e rank()
import pandas as pd

# 1-cria o DataFrame da prova de 50m
dados = {"nadador": ["Simonas Bilis",
                     "Benjamin Proud",
                     "Anthony Ervin",
                     "Florent Manaudou",
                     "Andriy Hovorov",
                     "Nathan Adrian",
                     "Bruno Fratus",
                     "Brad Tandy"],
         "nacionalidade": ["Lituânia",
                           "Grã-Bretanha",
                           "Estados Unidos",
                           "França",
                           "Ucrânia",
                           "Estados Unidos",
                           "Brasil",
                           "África do Sul"],
         "tempo": [22.08,
                   21.68,
                   21.40,
                   21.41,
                   21.74,
                   21.49,
                   21.79,
                   21.79]
         }
raias = list(range(1, 9))
prova50m = pd.DataFrame(dados, index=raias)
prova50m.index.name = 'raia'

# 2-ordena pelo tempo de forma crescente

# A segunda parte apresenta o método sort_values() . Este método
# serve para ordenar o DataFrame por uma ou mais colunas, que
# devem ser especificadas no parâmetro by . Neste exemplo,
# by="tempo" foi utilizado para gerar uma ordenação ascendente pela
# coluna tempo . Uma observação muito importante é que se você
# quiser mudar de fato o DataFrame (ou seja, ordená-lo de verdade
# em vez de apenas exibir as suas linhas ordenadas), precisará fazer
# uso de um comando de atribuição:

prova50m = prova50m.sort_values(by="tempo")
print("* * resultado final ordenado por tempo:")
print(prova50m)

# 3 - gera os rankings
resultado_por_raia = prova50m['tempo'].rank(method="min")
print("\n* * posição de cada nadador (por raia):")
print(resultado_por_raia)
