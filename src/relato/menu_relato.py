import PySimpleGUI as sg
import importlib
from config import janela_altura, janela_largura
from src.camera.estoque_camera import consultar_camera_disponivel
from src.filme.estoqueFilme import consultar_filme_disponivel


def tela_menu_relato():
    sg.theme('Reddit')

    filmes = consultar_filme_disponivel()
    cameras = consultar_camera_disponivel()
    
    # IMPORTAR RESULTADOS PARA EXIBIÇÃO NO GRID DE ESTOQUE
    modulo_relato = importlib.import_module('src.relato.relatos')
    grid_relato = modulo_relato.listar_relatos()

    layout_cadastrar_relato = [
                                    [sg.Text('CADASTRAR NOVO RELATO')],
                                    [sg.Text('Filme', size=(15, 1)), sg.Combo(filmes, key='filme')],
                                    [sg.Text('Câmera', size=(15, 1)), sg.Combo(cameras, key='camera')],
                                    [sg.Input('', key='id_filme', visible=False), sg.Input('', key='id_camera', visible=False)],
                                    [sg.Text('Cidade', size=(15, 1)), sg.InputText(key='cidade')],
                                    [sg.Text('Estado', size=(15, 1)), sg.InputText(key='estado')],
                                    [sg.Text('Data Início', size=(15, 1)), sg.InputText(key='data_inicio')],
                                    [sg.Text('Data Fim', size=(15, 1)), sg.InputText(key='data_fim')],
                                    [sg.Text('Notas', size=(15, 1)), sg.InputText(key='notas')],
                                    [sg.Button('Salvar', button_color='green'), sg.Button('Cancelar', button_color='red')]
                                ]

    column_headings = ['FILME','CIDADE', 'ESTADO', 'CAMERA', 'DATA', 'NOTAS']    

    layout_relatos = [
                        [sg.Table(values=grid_relato, headings=column_headings, display_row_numbers=False, auto_size_columns=False,
                            justification='right', num_rows=10, enable_events=True, key='-TABLE-')]
                    ]

    tab_novo_relato = sg.Tab('NOVO RELATO', layout_cadastrar_relato)
    tab_relatos = sg.Tab('RELATOS', layout_relatos)

    layout = [
            [sg.TabGroup([[tab_novo_relato, tab_relatos]])],
            [sg.Button('VOLTAR', size=(15, 1), button_color='BLUE')]
        ] 

    window = sg.Window('SysPelícula', layout, size=(janela_altura, janela_largura))

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break

        if event == 'Salvar':
            filme_index = int(values['filme'][0])
            camera_index = values['camera'][0]

            values['id_filme'] = filme_index
            values['id_camera'] = camera_index
            
            window.close()
            
            modulo_relato = importlib.import_module('src.relato.cadastrarRelato')
            modulo_relato.inserir_relato(values)

            break
        
        elif event == '-TABLE-':
            if values['-TABLE-']:
                window.close()
                selected_row = values['-TABLE-'][0]
                id_relato = grid_relato[selected_row][6]  # Obtém o filme da linha clicada
                modulo_relato = importlib.import_module('src.relato.visualizar_relato')
                modulo_relato.tela_visualizar_relato(id_relato)
        
        if event == "VOLTAR":
            window.close()
            modulo_filme = importlib.import_module('src.principal.menu_principal')
            modulo_filme.tela_menu_principal()