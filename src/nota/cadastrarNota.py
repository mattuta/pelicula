import PySimpleGUI as sg
import sqlite3
import datetime as dt
from src.principal.menu_principal import tela_menu_principal
import src.filme.menu_filme as tela_menu_filme
import importlib
from config import janela_altura, janela_largura

def tela_cadastrar_nota(idRelato, tipo):
    sg.theme('Reddit')

    layout = [
        [sg.Text('INSERIR NOTA')],
        [sg.Text('DESCRIÇÃO:', size=(15, 1)), sg.InputText(key='descricao')],
        [sg.Button('Salvar', button_color='green'), sg.Button('Cancelar', button_color='red'), sg.Button('Voltar', button_color='blue')]
    ]
    
    window = sg.Window('NOTA', layout, size=(janela_altura, janela_largura))

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break

        if event == 'Salvar':
            window.close()

            modulo_nota = importlib.import_module('src.nota.nota')
            modulo_nota.inserir_nota(values, idRelato, tipo)  
           
            modulo_filme = importlib.import_module('src.filme.menu_filme')
            modulo_filme.tela_menu_filme()    
            #break

        if event == "Voltar":
            window.close()
            modulo_filme = importlib.import_module('src.filme.menu_filme')
            modulo_filme.tela_menu_filme()