from mysql.connector import ProgrammingError
from bd import nova_conexao

sql = 'SELECT * FROM contatos'

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        for contato in contatos:
            print(f'{contato[1]:2} - {contato[0]:20s} Telefone: {contato[1]}')