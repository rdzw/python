def nota_conceito(valor):
    nota = float(valor)

    if nota > 10:
        return 'Nota invalida'
    elif nota >= 9.1:
        return 'A'
    elif nota >= 8.1:
        return 'A'

if __name__ == 'main':
    valor_informado = input('Nota do aluno: ')
    conceito = nota_conceito(valor_informado)
    print(conceito)