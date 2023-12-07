def menor_nome(nomes):
    # se não receber uma lista de nomes valida, retorne "Anônimo"
    if not len(nomes) or type(nomes) != list:
        return "Anônimo"

    # inicia o nome curto com o primeiro nome da lista recebida
    nomeCurto = nomes[0]
    comprimentoDoNomeCurto = len(nomes[0])

    for nome in nomes:
        # quando houver espaços em branco, remova-os
        nome = nome.strip()

        # se encontrar um nome menor que o nome definido como mais curto,
        # substitua-o
        if len(nome) < comprimentoDoNomeCurto:
            comprimentoDoNomeCurto = len(nome)
            nomeCurto = nome

    # retorne o nome mais curto capitalizado
    return nomeCurto.capitalize()
