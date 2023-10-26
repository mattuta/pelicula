import sqlite3 as sql
import importlib

def consultar_combo_camera(id_camera):
    conn = sql.connect('pelicula.db')
    cursor = conn.cursor()

    try:
        cursor.execute(''' SELECT marca, modelo, formato, fabricante, num_serie,
                                valor_compra, valor_venda, data_aquisicao, data_venda, notas, idCamera
                        FROM camera
                        WHERE idCamera <> ?''', (id_camera,))

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
    

def consultar_camera(id_camera):
    conn = sql.connect('pelicula.db')
    cursor = conn.cursor()

    try:
        cursor.execute(''' SELECT marca, modelo, formato, fabricante, num_serie,
                                valor_compra, valor_venda, data_aquisicao, data_venda, notas, idCamera
                        FROM camera
                        WHERE idCamera = ?''', (id_camera,))

        row = cursor.fetchone()

        if row:
            resultado = list(row)
            conn.close()
            return resultado
        else:
            return None
        
    except conn.Error as e:
        print(f"Erro ao buscar camera: {e}")
        return str(e)

def excluir_camera(id_camera):
    conn = sql.connect('pelicula.db')
    cursor = conn.cursor()

    print(f"ID CAMERA {id_camera}")

    try:
        cursor.execute('DELETE FROM camera WHERE idCamera = ?', (id_camera,))
        conn.commit()
        conn.close()
        return 1
        
    except conn.Error as e:
        print(f"Erro ao excluir câmera: {e}")
        return str(e)
    

def atualizar_camera(filme):

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