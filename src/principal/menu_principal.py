import PySimpleGUI as sg
import src.filme.menu_filme as filme
import src.camera.menu_camera as camera
import src.relato.menu_relato as relato


def tela_menu_principal():
    sg.theme('Reddit')



    layout = [
        [sg.Button('FILME', size=(15, 1), button_color='PINK')],
        [sg.Button('CÂMERA', size=(15, 1), button_color='GREEN')],
        [sg.Button('RELATO', size=(15, 1), button_color='ORANGE')]
    ]

    window = sg.Window('SysPelícula', layout, size=(500, 400))

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