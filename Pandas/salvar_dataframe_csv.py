#Salvar o conteudo de um dataframe em um CSV com o metodo "to_csv()"
import pandas as pd

#cria o DataFrame
dados = {'codigo': [1001,1002,1003,1004,1005],
         'nome': ['Leite','Café','Biscoito','Chá','Torradas']}

produtos = pd.DataFrame(dados)

#salva seu conteudo para um arquivo
produtos.to_csv(r"C:\Users\rodrigo\Desktop\Nova pasta\python\Pandas\dados\produtos.csv", sep="\t", index=False)