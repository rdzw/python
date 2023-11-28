# motodos unique() e value_counts()
import pandas as pd

# criando o DataFrame
dados = {"sexo": ["F", "M", "F", "F", "F", "M"],
         "bairro": ["Belverde",
                    "Belverde",
                    "Savassi",
                    "Anchieta",
                    None,
                    "Savassi"],
         "valor": [150.00,
                   35.00,
                   80.00,
                   250.00,
                   9.90,
                   25.00],
         "cartao": ["Master",
                    "Visa",
                    "Visa",
                    "Amex",
                    "Elo",
                    "Master"]}

id_clientes = [1, 2, 3, 4, 5, 6]

vendas = pd.DataFrame(dados, index=id_clientes)

# 2 - gera uma variável "grouped"
# onde a chave é "bairro" e a medida "valor"
# Essa linha é responsável por criar um objeto grouped ou objeto
# GroupBy chamado grupo_valor_bairro . Este objeto não armazena o
# resultado de nenhum cálculo, mas apenas gera estruturas internas
# que vão facilitar a produção de resultados agregados da coluna
# valor (atributo numérico) por bairro (atributo categórico, este último
# denominado de atributo chave do grupo).
grupo_valor_bairro = vendas['valor'].groupby(vendas['bairro'])

# 3-Computa agregados a partir da variável gerada
print('- Quantidade de clientes, por bairro:\n', grupo_valor_bairro.count())
print('-------------------------------------------------------------------')
print('- Valor total das vendas, por bairro:\n ', grupo_valor_bairro.sum())
print('-------------------------------------------------------------------')
print('- Valor médio das vendas, por bairro:\n', grupo_valor_bairro.mean())
