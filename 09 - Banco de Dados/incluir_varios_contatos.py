from mysql.connector import ProgrammingError
from bd import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Ana', '96765-4321'),
    ('Rodrigo', '97765-4321'),
    ('Keisi', '95765-4321'),
    ('Jao', '92765-4321'),
    ('Lucio', '91765-2221'),
    ('Flamengo', '94765-2121'),
    ('vai', '90765-4321'),
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'Foram incluidos {cursor.rowcount} registros !!!')