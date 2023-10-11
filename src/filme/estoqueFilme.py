import PySimpleGUI as sg
import sqlite3
import importlib

def atualizar_queima_filme(filme_index):
    conn = sqlite3.connect('pelicula.db')
    cursor = conn.cursor()
        
    try:
        cursor.execute('UPDATE filme SET queimado = 1 WHERE idFilme = ?', (filme_index['id_filme'],))

        conn.close()

        return 'OK'
    except conn.Error as e:
        return str(e)
    

def obter_id_filme(filme_index):
    conn = sqlite3.connect('pelicula.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('SELECT idFilme FROM filme WHERE nome like ?', ('%' + filme_index + '%',))
        
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

def  consultar_filme():
    conn = sqlite3.connect('pelicula.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''SELECT nome, marca, formato, iso, tipo, cinema, rebobinado, queimado FROM filme''')

        rows = cursor.fetchall()

        resultados = []

        for row in rows:
            resultados_transformado = list(row)
            resultados_transformado[5] = transformar(row[5])
            resultados.append(resultados_transformado)

        for row in resultados:
            print(row)
        
        conn.close()

        grid(resultados)
    except conn.Error as e:
        print(f"Erro ao adicionar filme: {e}")
        return str(e)        

def consultar_filme_disponivel():
    conn = sqlite3.connect('pelicula.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''SELECT idFilme, marca, nome, formato, iso FROM filme WHERE queimado = 0''')

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

def grid(resultados):

    # Defina as colunas da grade
    column_headings = ['Nome', 'Marca', 'Formato', 'ISO', 'Tipo', 'Cinema', 'Rebobinado', 'Queimado']

    # Defina o layout da janela
    layout = [
        [sg.Table(values=resultados, headings=column_headings, display_row_numbers=False, auto_size_columns=False,
                justification='right', num_rows=10, enable_events=True, key='-TABLE-')],
        [sg.Button('Adicionar Linha'), sg.Button('Excluir Linha'), sg.Button('Voltar', button_color='blue')]
    ]

    # Crie a janela
    window = sg.Window('ESTOQUE DE FILME', layout, resizable=True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Voltar':
            window.close()
            modulo_filme = importlib.import_module('src.filme.menu_filme')
            modulo_filme.tela_menu_filme()
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
        

    window.close()

if __name__ == '__main__':
    consultar_filme()
