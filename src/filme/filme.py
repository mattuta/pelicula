import sqlite3 as sql
import importlib

def consultar_combo_filme(id_filme):
    conn = sql.connect('pelicula.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''SELECT idFilme, marca, nome, formato, iso 
                       FROM filme 
                       WHERE queimado = 0''')

        rows = cursor.fetchall()

        resultados = []

        for row in rows:
            resultados_transformado = list(row)
            resultados.append(resultados_transformado)

        for row in resultados:
            print(row)
        
        conn.close()

        return resultados

    except conn.Error as e:
        print(f"Erro ao buscar filme: {e}")
        return str(e)


def consultar_filme(id_filme):
    conn = sql.connect('pelicula.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''SELECT nome, marca, formato, iso, tipo,
                                CASE 
                                    WHEN cinema = 1 THEN 'SIM'
                                    WHEN cinema = 0 THEN 'NÃO'
                                END AS cinema, 
                                CASE 
                                    WHEN rebobinado = 1 THEN 'SIM'
                                    WHEN rebobinado = 0 THEN 'NÃO'
                                END AS rebobinado,
                                CASE 
                                    WHEN queimado = 1 THEN 'SIM'
                                    WHEN queimado = 0 THEN 'NÃO'
                                END AS queimado,
                                data_aquisicao, data_validade, idFilme, notas
                        FROM filme
                        WHERE idFilme = ?''', (id_filme,))

        row = cursor.fetchone()

        if row:
            resultado = list(row)
            conn.close()
            return resultado
        else:
            return None
        
    except conn.Error as e:
        print(f"Erro ao buscar filme: {e}")
        return str(e)

def excluir_filme(id_filme):
    conn = sql.connect('pelicula.db')
    cursor = conn.cursor()

    print(f"ID FILME {id_filme}")

    try:
        cursor.execute('DELETE FROM filme WHERE idFilme = ?', (id_filme,))
        conn.commit()
        conn.close()
        return 1
        
    except conn.Error as e:
        print(f"Erro ao excluir filme: {e}")
        return str(e)
    

def atualizar_filme(filme):

    conn = sql.connect('pelicula.db')
    cursor = conn.cursor()

    print(filme['nome'])

    try:
        cursor.execute('''UPDATE filme
                       SET nome = ?, marca = ?, formato = ?, iso = ?, tipo = ?, cinema = ?,
                       rebobinado = ?, queimado = ?, data_aquisicao = ?, data_validade = ?,
                       notas = ? 
                       WHERE idFilme = ? ''',
                    (filme['nome'], filme['marca'], filme['formato'], filme['iso'], filme['tipo'],
                        filme['cinema'], filme['rebobinado'], filme['queimado'], filme['data_aquisicao'],
                        filme['data_validade'], filme['notas'], filme['idFilme']))
        
        conn.commit()
        conn.close()

        return "OK"
    
    except conn.Error as e:
        print(f"Erro ao adicionar filme: {e}")
        return str(e)