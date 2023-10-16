import PySimpleGUI as sg
import sqlite3
import importlib


def obter_id_camera(camera_index):
    conn = sqlite3.connect('pelicula.db')
    cursor = conn.cursor()
    
    try:
        #cursor.execute('''SELECT idCamera FROM camera WHERE modelo like "%camera_index%" ''')
        cursor.execute('SELECT idCamera FROM camera WHERE modelo like ?', ('%' + camera_index + '%',))
        
        row = cursor.fetchone()

        resultado = None

        if row:
            resultado = row[0]

        conn.close()

        return resultado
    except conn.Error as e:
        print(f"Erro ao consultar filme: {e}")
        return str(e) 
    pass

def  consultar_camera():
    conn = sqlite3.connect('pelicula.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''SELECT marca, modelo, formato, fabricante, num_serie, valor_compra,
                        valor_venda, data_aquisicao, data_venda, notas, idCamera FROM camera''')

        rows = cursor.fetchall()

        resultados = []

        for row in rows:
            resultados_transformado = list(row)
            #resultados_transformado[5] = transformar(row[5])
            resultados.append(resultados_transformado)

        for row in resultados:
            print(row)
        
        conn.close()

        grid_camera(resultados)
    except conn.Error as e:
        print(f"Erro ao adicionar filme: {e}")
        return str(e)        

def consultar_camera_disponivel():
    conn = sqlite3.connect('pelicula.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''SELECT idCamera, marca, modelo, formato FROM camera''')

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
        print(f"Erro ao consultar filme: {e}")
        return str(e)        
    

def transformar(valor):
    if valor == 1:
        return 'SIM'
    if valor == 0:
        return 'Não'
    else:
        return valor

def grid_camera(resultados):

    # Defina as colunas da grade
    column_headings = ['Marca', 'Modelo', 'Formato', 'Fabricante', 'N° Série', 'Compra R$', 'Venda R$', 'Data Aquisição', 'Data Venda', 'Notas']

    # Defina o layout da janela
    layout = [
        [sg.Table(values=resultados, headings=column_headings, display_row_numbers=False, auto_size_columns=False,
                justification='right', num_rows=10, enable_events=True, key='-TABLE-')],
        [sg.Button('Adicionar Linha'), sg.Button('Excluir Linha'), sg.Button('Voltar', button_color='blue')]
    ]

    # Crie a janela
    window = sg.Window('ESTOQUE DE CÂMERAS', layout, resizable=True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Voltar':
            window.close()
            modulo_camera = importlib.import_module('src.camera.menu_camera')
            modulo_camera.tela_menu_camera()
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
                id_camera = resultados[selected_row][10] 
                print(f"ID {id_camera}")
                window.close()
                modulo_camera = importlib.import_module('src.camera.visualizar_camera')
                modulo_camera.tela_visualizar_camera(id_camera)


    window.close()

if __name__ == '__main__':
    consultar_camera()
