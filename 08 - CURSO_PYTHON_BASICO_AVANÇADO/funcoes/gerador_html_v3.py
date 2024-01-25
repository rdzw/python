def tag_bloco(texto, classe='sucess', inline=False):
    tag = 'span' if inline else 'div'
    return f'<div class="{classe}">{texto}</div>'

#função packinge & unpacking
def tag_lista(*itens):
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul>{lista}</ul>'

if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', 'info', True))
    print(tag_bloco('inline',inline=True))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))    