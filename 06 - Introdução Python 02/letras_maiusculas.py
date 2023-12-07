def maiusculas(palavra):
    maiusculas = []

    for i in range(len(palavra)):
        maiusculas = []

        for i in range(len(palavra)):
            caracter = palavra[i]
            decASCII = ord(caracter)

            if decASCII > 64 and decASCII < 91:
                maiusculas.append(caracter)

    return "".join(maiusculas)



