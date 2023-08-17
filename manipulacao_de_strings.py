nome = "roDriGo"

print(nome.upper())
print(nome.lower())
print(nome.title())

#por espaço nas laterais da string
texto = " ola mundo! "

print(texto + ".")
print(texto.strip() + ".") 
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

#junção e centralização

menu = "python"

print("####" + menu + "###")
print(menu.center(14))
print(menu.center(14, "#"))
print("-".join(menu))