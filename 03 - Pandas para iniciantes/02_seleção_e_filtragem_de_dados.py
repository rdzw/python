# -*- coding: utf-8 -*-
"""02 - seleção e filtragem de dados

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OTPOKUAnLEQPjxMRZV8aKzS6suijhT2p
"""

# importando a biblioteca 05 - Pandas
import pandas as pd

# Lendo arquivos HTML
df = pd.read_html('https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6')[0]

df

# selecionando uma coluna do DataFrame
coluna = df['Name']

# selecionando várias colunas do DataFrame
colunas = df[['Name', 'Type 1', 'Attack']]

# selecionando linhas do DataFrame com base em condições, ex >, <, <=, >=, ==.
linhas = df[df['Attack'] > 100]

colunas

#Inspecionando informações
df.info()

#Inspecionando a base
df.tail()

#Inspecionando o shape
df.shape

df[(df["Attack"] >= 80) & (df["Defense"] >= 150)]

#Operação entre colunas
df["Indice de força"] = df['Attack'] + df['Defense'] + df['Speed']

#Pegando o maior valor do indíce de força.
df.sort_values(by = "Indice de força", ascending = False)

#Utilizando o método iloc para selecionar uma linha específica:

# criando um DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# selecionando a segunda linha (índice 1) usando o método iloc
linha = df.iloc[1]

df

print(linha)

# selecionando as linhas 0 e 2 usando o método iloc
linhas = df.iloc[[0, 2]]

print(linhas)

# selecionando a célula da coluna 'A' e linha 1 usando o método iloc (linha, coluna)
valor = df.iloc[1, 0]

print(valor)

#Utilizando o método loc para selecionar uma linha específica:

# criando um DataFrame com índices
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}, index=['a', 'b', 'c'])

# selecionando a linha de índice 'b' usando o método loc
linha = df.loc['b']

print(linha)

df

# selecionando as linhas de índice 'a' e 'c' usando o método loc
linhas = df.loc[['a', 'c']]

print(linhas)

# selecionando as linhas onde o valor da coluna 'A' é maior que 1 usando o método loc
linhas = df.loc[df['A'] > 1]

print(linhas)