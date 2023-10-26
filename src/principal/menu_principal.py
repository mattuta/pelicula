import importlib
import PySimpleGUI as sg
import src.filme.menu_filme as filme
import src.camera.menu_camera as camera
import src.relato.menu_relato as relato
from config import janela_altura, janela_largura, vers


def tela_menu_principal():
    sg.theme('Material1')


    layout_menu = [
        [sg.Button('FILME', size=(30, 3), button_color='GRAY')],
        [sg.Button('CÂMERA', size=(30, 3), button_color='GRAY')],
        [sg.Button('RELATO', size=(30, 3), button_color='GRAY')],
        [sg.T(size=(30, 1))],
        [sg.T(size=(30, 1))],
        [sg.T(size=(30, 1))],
        [sg.Button('SOBRE', size=(30, 3), button_color='ORANGE')]
    ]

    layout_infos = [
                    [sg.Image(r'C:\DEV\pelicula\src\imagens\gilot.jpg', size=(200, 500), 
                            background_color='#FFFFFF', pad=(7, (80, 25)))],
                    [sg.Text('Aplicação desenvolvida por: Matheus de Souza Silva')],
                    [sg.Text('Versão:'), sg.Text(vers)]                
                    ]

    layout = [[sg.Column(layout_menu, element_justification='c')]] 

    window = sg.Window('SysPelícula', layout, size=(400, 400), element_justification='center')

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break
        if event == "FILME":
            window.close()
            filme.tela_menu_filme()
        if event == "RELATO":
            window.close()
            relato.tela_menu_relato()
        if event == "CÂMERA":
            window.close()
            camera.tela_menu_camera()
        if event == "SOBRE":
            modulo_sobre = importlib.import_module('src.sobre.sobre')
            modulo_sobre.sobre()
        

