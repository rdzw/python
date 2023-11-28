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

# retorna o dominio dos atributos categoricos
# Esse método unique() retorna um array
# que armazena todas as categorias distintas do atributo escolhido.
# Por exemplo, no DataFrame vendas , temos seis linhas, mas apenas
# duas categorias distintas para o atributo sexo : {"F", "M"}.

print('Dominio dos atributos categoricos:')
print('----------------------------------')
print('sexo:', vendas['sexo'].unique())
print('bairro:', vendas['bairro'].unique())
print('cartao:', vendas['cartao'].unique())

# retorna as frequencias dos valores de cada coluna
# value_counts() que faz a mesma coisa que o unique() , acrescido de
# um bônus e tanto: além de apresentar as categorias distintas do
# atributo, o método computa o número de ocorrências de cada uma.
# Ou seja, ele é capaz de gerar uma tabela de frequências. Por
# exemplo, considerando novamente o atributo sexo , temos que a
# categoria "F" possui frequência 4, enquanto "M" tem frequência 2.

print("\n")
print('Tabelas de frequencia:')
print('--------------------------')
print("\n1-sexo:")
print(vendas['sexo'].value_counts())
print("\n2-bairro:")
print(vendas['bairro'].value_counts())
print("\n3-cartão:")
print(vendas['cartao'].value_counts())
