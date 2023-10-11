import PySimpleGUI as sg
import src.filme.cadastrarFilme as telaFilme
import src.filme.estoqueFilme as telaEstoque
from src.principal.menu_principal import tela_menu_principal
import importlib


def tela_menu_filme():
    sg.theme('Reddit')
    
    layout = [
        [sg.Button('Cadastrar Filme', size=(15, 1))],
        [sg.Button('Estoque de Filme', size=(15, 1), button_color='pink')],
        [sg.Button('VOLTAR', size=(15, 1), button_color='BLUE')]
    ]

    window = sg.Window('SysPelícula', layout, size=(500, 400))

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break

        if event == 'Cadastrar Filme':
            window.close()
            modulo_filme = importlib.import_module('src.filme.cadastrarFilme')
            modulo_filme.tela_cadastrar_filme()
        if event == 'Estoque de Filme':
            window.close()
            modulo_filme = importlib.import_module('src.filme.estoqueFilme')
            modulo_filme.consultar_filme()
        if event == "VOLTAR":
            window.close()
            modulo_filme = importlib.import_module('src.principal.menu_principal')
            modulo_filme.tela_menu_principal()
            
                
