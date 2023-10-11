import importlib
import PySimpleGUI as sg
import sqlite3
import src.relato.visualizar_relato as relato

def  listar_relatos():
    conn = sqlite3.connect('pelicula.db')
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
    conn = sqlite3.connect('pelicula.db')
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
                selected_row = values['-TABLE-'][0]
                id_relato = resultados[selected_row][6]  # Obtém o filme da linha clicada
                
                relato.tela_visualizar_relato(id_relato)
                

            

    window.close()

 