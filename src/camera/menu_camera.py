from tkinter import mainloop
import PySimpleGUI as sg
import importlib


def tela_menu_camera():
    sg.theme('Reddit')

    layout = [
        [sg.Button('Cadastrar Câmera', size=(15, 1))],
        [sg.Button('Estoque de Câmera', size=(15, 1))],
        [sg.Button('VOLTAR', size=(15, 1), button_color='BLUE')]
    ]

    window = sg.Window('SysPelícula', layout, size=(500, 400))

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break

        
        if event == 'Cadastrar Câmera':
            window.close()
            modulo_camera = importlib.import_module('src.camera.cadastrarCamera')
            modulo_camera.tela_cadastrar_camera()
        if event == 'Estoque de Câmera':
            window.close()
            modulo_estoque = importlib.import_module('src.camera.estoque_camera')
            modulo_estoque.consultar_camera()
        if event == "VOLTAR":
            window.close()
            modulo_estoque = importlib.import_module('src.principal.menu_principal')
            modulo_estoque.tela_menu_principal()
                
            
