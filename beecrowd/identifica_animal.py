palavra1 = input("")
palavra2 = input("")
palavra3 = input("")

if palavra1 == "vertebrado":
    if palavra2 == "ave":
        if palavra3 == "carnivoro":
            print("aguia")
        elif palavra3 == "onivoro":
            print("pombo")
    elif palavra2 == "mamifero":
        if palavra3 == "onivoro":
            print("homen")
        elif palavra3 == "herivoro":
            print("vaca")
if palavra1 == "invertebrado":
    if palavra2 == "inseto":
        if palavra3 == "hemotofago":
            print("pulga")
        elif palavra3 == "herbivoro":
            print("lagarta")
    elif palavra2 == "anelideo":
        if palavra3 == "hematofago":
            print("sanguessuga")
        elif palavra3 == "onivoro":
            print("minhoca")
            

        
