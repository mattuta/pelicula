import PySimpleGUI as sg
import importlib

def tela_menu_relato():
    sg.theme('Reddit')

    layout = [
        [sg.Button('Cadastrar Relato', size=(15, 1), button_color='orange')],
         [sg.Button('Relatos', size=(15, 1), button_color='pink')]
        ]
    

    window = sg.Window('SysPelícula', layout, size=(500, 400))

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break

        
        if event == 'Cadastrar Relato':
            window.close()
            modulo_relato = importlib.import_module('src.relato.cadastrarRelato')
            modulo_relato.tela_cadastrar_relato()
        if event == 'Relatos':
            window.close()
            modulo_relato = importlib.import_module('src.relato.relatos')
            modulo_relato.listar_relatos()
        if event == "VOLTAR":
            window.close()
            modulo_estoque = importlib.import_module('src.principal.menu_principal')
            modulo_estoque.tela_menu_principal()
