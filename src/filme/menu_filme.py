import PySimpleGUI as sg
import src.filme.cadastrarFilme as telaFilme
import src.filme.estoqueFilme as telaEstoque
from src.principal.menu_principal import tela_menu_principal
import importlib
from config import janela_altura, janela_largura


def tela_menu_filme():
    sg.theme('Reddit')

    # IMPORTAR RESULTADOS PARA EXIBIÇÃO NO GRID DE ESTOQUE
    modulo_filme = importlib.import_module('src.filme.estoqueFilme')
    grid_filme = modulo_filme.consultar_filme()

    # ----------------------------------------------------------------------------------------------------------
    layout_cadastrar_filme = [[sg.Text('CADASTRAR NOVO FILME')],
                        [sg.Text('Nome', size=(15, 1)), sg.InputText(key='nome')],
                        [sg.Text('Marca', size=(15, 1)), sg.InputText(key='marca')],
                        [sg.Text('Formato', size=(15, 1)), sg.Combo(['35', '120'], key='formato')],
                        [sg.Text('ISO', size=(15, 1)), sg.InputText(key='iso')],
                        [sg.Text('Tipo', size=(15, 1)), sg.Combo(['Colorido', 'PB'], key='tipo')],
                        [sg.Text('Aquisição', size=(15, 1)), sg.InputText(key='data_aquisicao')],
                        [sg.Text('Validade', size=(15, 1)), sg.InputText(key='data_validade')],
                        [sg.Text('Notas', size=(15, 1)), sg.InputText(key='notas')],
                        [sg.Checkbox('Queimado', key='queimado'), sg.Checkbox('Cinema', key='cinema'), sg.Checkbox('Rebobinado', key='rebobinado')],
                        [sg.Button('Salvar', button_color='green'), sg.Button('Cancelar', button_color='red')]]

    column_headings = ['Nome', 'Marca', 'Formato', 'ISO', 'Tipo', 'Cinema', 'Rebobinado', 'Queimado']
    layout_estoque_filme = [
                                [sg.Table(values=grid_filme, headings=column_headings, display_row_numbers=False, auto_size_columns=False,
                                        justification='right', num_rows=10, enable_events=True, key='-TABLE-')]
                            ]
    layout_relato = [[sg.Text('Conteúdo da aba RELATO')]]

    tab_novo_filme = sg.Tab('NOVO FILME', layout_cadastrar_filme)
    tab_estoque = sg.Tab('ESTOQUE DE FILMES', layout_estoque_filme)


    layout = [
        [sg.TabGroup([[tab_novo_filme, tab_estoque]])],
        [sg.Button('VOLTAR', size=(15, 1), button_color='BLUE')]
    ]
    # ---------------------------------------------------------------------------------------------------------- 
    
    window = sg.Window('SysPelícula', layout, size=(janela_altura, janela_largura))

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break

        if event == 'Salvar':
            window.close()
            modulo_filme = importlib.import_module('src.filme.cadastrarFilme')
            modulo_filme.inserir_filme(values)
             
        if event == "VOLTAR":
            window.close()
            modulo_filme = importlib.import_module('src.principal.menu_principal')
            modulo_filme.tela_menu_principal()
        
        elif event == '-TABLE-':
            if values['-TABLE-']:
                selected_row = values['-TABLE-'][0]
                id_filme = grid_filme[selected_row][8]  # Obtém o filme da linha clicada
                print(f"ID {id_filme}")
                window.close()
                modulo_filme = importlib.import_module('src.filme.visualizar_filme')
                modulo_filme.tela_visualizar_filme(id_filme)
            
                
