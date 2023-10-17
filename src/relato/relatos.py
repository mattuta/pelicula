import importlib
import PySimpleGUI as sg
import sqlite3 as sql
import src.relato.visualizar_relato as relato



def consultar_relato_edit(id_relato):
    conn = sql.connect('pelicula.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''SELECT r.idRelato, r.id_filme, r.id_camera,
                            f.nome, r.cidade, r.estado, c.modelo, r.data_inicio, r.data_fim, r.notas,
                            c.modelo, f.nome 
                            FROM relato r
                            INNER JOIN filme f ON f.idFilme = r.id_filme
                            INNER JOIN camera c ON c.idCamera = r.id_camera
                        WHERE idRelato = ?''', (id_relato,))

        row = cursor.fetchone()

        if row:
            resultado = list(row)
            conn.close()
            return resultado
        else:
            return None
        
    except conn.Error as e:
        print(f"Erro ao buscar relato: {e}")
        return str(e)


def  listar_relatos():
    conn = sql.connect('pelicula.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''SELECT f.nome as filme, r.cidade, r.estado, c.modelo as camera, r.data_inicio, r.notas, 
                            r.idRelato 
                            FROM relato r
                            INNER JOIN filme f ON f.idFilme = r.id_filme
                            INNER JOIN camera c ON c.idCamera = r.id_camera''')

        rows = cursor.fetchall()

        resultados = []

        for row in rows:
            resultados_transformado = list(row)
            #resultados_transformado[5] = transformar(row[5])
            resultados.append(resultados_transformado)

        for row in resultados:
            print(row)
        
        conn.close()

        grid(resultados)
    except conn.Error as e:
        print(f"Erro ao buscar relato: {e}")
        return str(e)   


def consultar_relatos(id_relato):
    conn = sql.connect('pelicula.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''SELECT f.nome as filme, r.cidade as cidade, r.estado as estado, c.modelo as camera, 
                            r.data_inicio as dt_inicio, r.notas as notas,  
                            r.data_fim as dt_fim, r.idRelato as id_relato
                            FROM relato r
                            INNER JOIN filme f ON f.idFilme = r.id_filme
                            INNER JOIN camera c ON c.idCamera = r.id_camera
                        WHERE r.idRelato = ?
                       ''', (id_relato,))
        
        
        
        row = cursor.fetchone()

        if row:
            resultado_transformado = list(row)
            conn.close()
            return resultado_transformado
        else:
            return None 
        
        
    except conn.Error as e:
        print(f"Erro ao buscar relato: {e}")
        return str(e)


def grid(resultados):
    
    # Defina as colunas da grade
    column_headings = ['FILME','CIDADE', 'ESTADO', 'CAMERA', 'DATA', 'NOTAS']

    # Defina o layout da janela
    layout = [
        [sg.Table(values=resultados, headings=column_headings, display_row_numbers=False, auto_size_columns=False,
                justification='right', num_rows=10, enable_events=True, key='-TABLE-')],
        [sg.Button('Adicionar Linha'), sg.Button('Excluir Linha'), sg.Button('Voltar', button_color='blue')]
    ]

    # Crie a janela
    window = sg.Window('RELATOS', layout, resizable=True)


    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Voltar':
            window.close()
            modulo_relato = importlib.import_module('src.relato.menu_relato')
            modulo_relato.tela_menu_relato()
            break
        elif event == 'Adicionar Linha':
            resultados.append(['', '', ''])
            window['-TABLE-'].update(values=resultados)
        elif event == 'Excluir Linha':
            selected_rows = window['-TABLE-'].get_selected_rows()
            if selected_rows:
                for row_index in selected_rows:
                    resultados.pop(row_index)
                window['-TABLE-'].update(values=resultados)
        elif event == '-TABLE-':
            if values['-TABLE-']:
                window.close()
                selected_row = values['-TABLE-'][0]
                id_relato = resultados[selected_row][6]  # Obtém o filme da linha clicada
                
                relato.tela_visualizar_relato(id_relato)
                


def atualizar_relato(relato):
    
    conn = sql.connect('pelicula.db')
    cursor = conn.cursor()

  
    if isinstance(relato['filme'], list):
        print("É uma lista!")
        id_filme = relato['filme'][1]
    else:
        print("Não é uma lista.")
        id_filme = relato['id_filme']


    if isinstance(relato['camera'], list):
        print("É uma lista!")
        id_camera = relato['camera'][10]
    else:
        print("Não é uma lista.")
        id_camera = relato['id_camera']
    


    try:
        query = '''UPDATE relato
            SET id_filme = {}, cidade = '{}', estado = '{}',
            id_camera = {}, data_inicio = '{}', data_fim = '{}',
            notas = '{}'
            WHERE idRelato = {}'''.format(
                relato['id_filme'], relato['cidade'], relato['estado'],
                id_camera, relato['data_inicio'], relato['data_final'],
                relato['notas'], relato['idRelato'])
        print(query)

        cursor.execute(query)
        
        conn.commit()
        conn.close()

        return "OK"
    
    except conn.Error as e:
        print(f"Erro ao atualizar relato: {e}")
        return str(e)



def excluir_relato(id_relato):
    conn = sql.connect('pelicula.db')
    cursor = conn.cursor()

    print(f"ID RELATO {id_relato}")

    try:
        cursor.execute('DELETE FROM relato WHERE idRelato = ?', (id_relato,))
        conn.commit()
        conn.close()
        return 1
        
    except conn.Error as e:
        print(f"Erro ao excluir relato: {e}")
        return str(e)
    