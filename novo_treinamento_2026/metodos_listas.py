filmsList = ["rock", "nemo", "futebol", "harrypotter"]


#tamanho da lista
print(len(filmsList))

#recuperar item da lista pelo indice
print(filmsList.index("harrypotter"))

#adicionar item final lista
filmsList.append("senhor")
print(filmsList)

#ordenar lista
filmsList.sort()
print(filmsList)

#remove todos itens
filmsList.clear()
print(filmsList)