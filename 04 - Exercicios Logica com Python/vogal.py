def vogal(caractere):
    if isinstance(caractere, str):
        vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        return caractere in vogais
    return False