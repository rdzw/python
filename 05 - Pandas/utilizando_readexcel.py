#importação de planilha excel com o método read_excel()
import pandas as pd

#Leitura de um aquivo excel
#instale a biblioteca : pip install xlrd e pip install openpyxl
cidades = pd.read_excel(r"C:\Users\rodrigo\Desktop\Nova pasta\python\Pandas\dados\capitais.xlsx")
print(cidades)