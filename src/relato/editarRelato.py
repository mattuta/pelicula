import PySimpleGUI as sg
import sqlite3
import datetime as dt
from src.principal.menu_principal import tela_menu_principal
import src.filme.menu_filme as tela_menu_filme
import importlib
from config import janela_altura, janela_largura


def tela_editar_relato(id_relato):
    sg.theme('Reddit')

    modulo_relato = importlib.import_module('src.relato.relatos')
    resultado = modulo_relato.consultar_relato_edit(id_relato) 
 
    modulo_filme = importlib.import_module('src.filme.filme')
    res_filme = modulo_filme.consultar_combo_filme(resultado[1])

    modulo_camera = importlib.import_module('src.camera.camera')
    res_camera = modulo_camera.consultar_combo_camera(resultado[2])

    layout = [
        [sg.Text('EDITAR RELATO')],
        [sg.InputText(key='idRelato', default_text=resultado[0], visible=False)],
        [sg.Text('CIDADE', size=(15, 1)), sg.InputText(key='cidade', default_text=resultado[4])],
        [sg.Text('ESTADO', size=(15, 1)), sg.InputText(key='estado', default_text=resultado[5])],
        [sg.Text('DATA INICIO', size=(15, 1)), sg.InputText(key='data_inicio', default_text=resultado[7])],
        [sg.Text('DATA FINAL', size=(15, 1)), sg.InputText(key='data_final', default_text=resultado[8])],
        [sg.Text('FILME', size=(15, 1)), sg.Combo(res_filme, key='filme', default_value=resultado[11])],
        [sg.Text('CÂMERA', size=(15, 1)), sg.Combo(res_camera, key='camera', default_value=resultado[10])],
        [sg.InputText(key='id_filme', visible=False, default_text=resultado[1])],
        [sg.InputText(key='id_camera', visible=False, default_text=resultado[2])],
        [sg.Text('NOTAS', size=(15, 1)), sg.InputText(key='notas', default_text=resultado[9])],
        [sg.Button('Salvar', button_color='green'), sg.Button('Cancelar', button_color='red'), sg.Button('Voltar', button_color='blue')]
    ]

    window = sg.Window('EDITAR RELATO', layout, size=(janela_altura, janela_largura))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break

        if event == 'Salvar':
            window.close()
            
            modulo_editar_relato = importlib.import_module('src.relato.relatos')
            resposta = modulo_editar_relato.atualizar_relato(values)
            
            print(f"Resposta: {resposta}")
            
            modulo_relato = importlib.import_module('src.relato.visualizar_relato')
            modulo_relato.tela_visualizar_relato(values['idRelato'])


            
        if event == "Voltar":
            window.close()
            modulo_filme = importlib.import_module('src.filme.menu_filme')
            modulo_filme.tela_menu_filme()


    window.close()

#if __name__ == '__main__':
#   criar_tabela_filme()
#    tela_cadastrar_filme()