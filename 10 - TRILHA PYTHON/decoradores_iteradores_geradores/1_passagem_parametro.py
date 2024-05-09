def mensagem(nome):
    print('executando  nome')
    return f'oi {nome}'

def mensagem_longa(nome):
    print('executando mensagem longa')
    return f"ola tudo bem com você {nome}?"

def executar(funcao,nome):
    print("executando executar")
    return funcao(nome)

print(executar(mensagem, "rodrigo"))
print(executar(mensagem_longa, "rodrigo"))