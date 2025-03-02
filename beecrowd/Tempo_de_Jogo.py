inicial, final = map(int, input().split())

if inicial < final:
    duracao = final - inicial
else:
    duracao = (24 - inicial) + final
    
print(f"O JOGO DUROU {duracao} HORA(S)")