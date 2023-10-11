import sqlite3

conn = sqlite3.connect('pelicula.db')

def criar_tabela_filme():
    cursor = conn.cursor()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS filme(
            idFilme integer primary key AUTOINCREMENT,
            nome text,
            marca text,
            formato text,
            iso text,
            tipo text,
            cinema text,
            rebobinado text,
            quantidade text,
            data_aquisicao text,
            data_validade text,
            notas text
        )
    ''')

    conn.commit()
    conn.close()