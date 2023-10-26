from tkinter import mainloop
import PySimpleGUI as sg
import importlib
from config import janela_altura, janela_largura


def tela_menu_camera():
    sg.theme('Reddit')

    # IMPORTAR RESULTADOS PARA EXIBIÇÃO NO GRID DE ESTOQUE
    modulo_camera = importlib.import_module('src.camera.estoque_camera')
    grid_camera = modulo_camera.consultar_camera()

    layout_cadastrar_camera = [[sg.Text('CADASTRAR NOVO CÂMERA')],
        [sg.Text('Marca', size=(15, 1)), sg.InputText(key='marca')],
        [sg.Text('Modelo', size=(15, 1)), sg.InputText(key='modelo')],
        [sg.Text('Formato', size=(15, 1)), sg.Combo(['35', '120'], key='formato')],
        [sg.Text('Fabricante', size=(15, 1)), sg.InputText(key='fabricante')],
        [sg.Text('N° Série', size=(15, 1)), sg.InputText(key='num_serie')],
        [sg.Text('Valor Compra', size=(15, 1)), sg.InputText(key='valor_compra')],
        [sg.Text('Valor Venda', size=(15, 1)), sg.InputText(key='valor_venda')],
        [sg.Text('Aquisição', size=(15, 1)), sg.InputText(key='data_aquisicao')],
        [sg.Text('Venda', size=(15, 1)), sg.InputText(key='data_venda')],
        [sg.Text('Notas', size=(15, 1)), sg.InputText(key='notas')],
        [sg.Button('Salvar', button_color='green'), sg.Button('Cancelar', button_color='red')]]


    column_headings = ['Marca', 'Modelo', 'Formato', 'Fabricante', 'N° Série', 'Compra R$', 'Venda R$', 'Data Aquisição', 'Data Venda', 'Notas']

    layout_estoque_camera = [
                            [sg.Table(values=grid_camera, headings=column_headings, display_row_numbers=False, auto_size_columns=False,
                                justification='right', num_rows=10, enable_events=True, key='-TABLE-')],
                            ]

    tab_nova_camera = sg.Tab('NOVA CÂMERA', layout_cadastrar_camera)
    tab_estoque_camera = sg.Tab('ESTOQUE DE CÂMERAS', layout_estoque_camera)


    layout = [
        [sg.TabGroup([[tab_nova_camera, tab_estoque_camera]])],
        [sg.Button('VOLTAR', size=(15, 1), button_color='BLUE')]
    ]

    window = sg.Window('SysPelícula', layout, size=(janela_altura, janela_largura))

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break

        if event == 'Salvar':
            modulo_camera = importlib.import_module('src.camera.cadastrarCamera')
            modulo_camera.inserir_camera(values)
            break
        if event == "VOLTAR":
            window.close()
            modulo_filme = importlib.import_module('src.principal.menu_principal')
            modulo_filme.tela_menu_principal()
        
        elif event == '-TABLE-':
            if values['-TABLE-']:
                selected_row = values['-TABLE-'][0]
                id_camera = grid_camera[selected_row][10] 
                print(f"ID {id_camera}")
                #window.close()
                modulo_camera = importlib.import_module('src.camera.visualizar_camera')
                modulo_camera.tela_visualizar_camera(id_camera)        
            
