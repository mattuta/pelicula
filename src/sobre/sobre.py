import PySimpleGUI as sg
import sqlite3
import datetime as dt
import src.relato.relatos as relato
import importlib
from config import janela_altura, janela_largura, vers



def sobre():
    sg.theme('Reddit')

    sz=(15,20)
    
    col=[[sg.Text('', background_color='#ce4646', size=sz)]]
    col_infos = [[sg.Text('PELÍCULA', font=('Bauhaus 93', 50), auto_size_text=True)],
                 [sg.Text('Controle de Acervo Fotográfico', font=('Berlin Sans FB', 15, 'bold'))],
                 [sg.HorizontalSeparator()],
                 [sg.Text('DESENVOLVIDO POR:')], 
                 [sg.Text("Matheus de Souza Silva")],
                 [sg.Text('VERSÃO:', size=(15, 1))], 
                 [sg.Text(vers)]
                ]

    layout = [[sg.Column(col, element_justification='l' ), sg.Column(col_infos, element_justification='c')]]

    window = sg.Window('SOBRE', layout, size=(500, 300))

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break

        if event == "VOLTAR":
            window.close()
            modulo_filme = importlib.import_module('src.principal.menu_principal')
            modulo_filme.tela_menu_principal()

    window.close()


