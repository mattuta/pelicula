import PySimpleGUI as sg
import sqlite3
import datetime as dt
from src.principal.menu_principal import tela_menu_principal
import src.filme.menu_filme as tela_menu_filme
import importlib
     
    

def tela_editar_camera(id_camera):
    sg.theme('Reddit')

    modulo_camera = importlib.import_module('src.camera.camera')
    resultado = modulo_camera.consultar_camera(id_camera) 

    layout = [
        [sg.Text('EDITAR CÂMERA')],
        [sg.InputText(key='idCamera', default_text=resultado[10], visible=False)],
        [sg.Text('Marca', size=(15, 1)), sg.InputText(key='marca', default_text=resultado[0])],
        [sg.Text('Modelo', size=(15, 1)), sg.InputText(key='modelo', default_text=resultado[1])],
        [sg.Text('Formato', size=(15, 1)), sg.Combo(['35', '120'], key='formato', default_value=resultado[2])],
        [sg.Text('Fabricante', size=(15, 1)), sg.InputText(key='fabricante', default_text=resultado[3])],
        [sg.Text('N° Série', size=(15, 1)), sg.InputText(key='num_serie', default_text=resultado[4])],
        [sg.Text('Valor Compra', size=(15, 1)), sg.InputText(key='valor_compra', default_text=resultado[5])],
        [sg.Text('Valor Venda', size=(15, 1)), sg.InputText(key='valor_venda', default_text=resultado[6])],
        [sg.Text('Data Compra', size=(15, 1)), sg.InputText(key='data_aquisicao', default_text=resultado[7])],
        [sg.Text('Data Venda', size=(15, 1)), sg.InputText(key='data_validade', default_text=resultado[8])],
        [sg.Text('Notas', size=(15, 1)), sg.InputText(key='notas', default_text=resultado[9])],
        [sg.Button('Salvar', button_color='green'), sg.Button('Cancelar', button_color='red'), sg.Button('Voltar', button_color='blue')]
    ]

    window = sg.Window('EDITAR FILME', layout, size=(500, 400))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break
        if event == 'Salvar':
            window.close()
            modulo_editar_camera = importlib.import_module('src.camera.camera')
            resposta = modulo_editar_camera.atualizar_camera(values)
            print(f"Resposta: {resposta}")
            
            modulo_camera = importlib.import_module('src.camera.menu_camera')
            modulo_camera.tela_menu_camera()    
            #break
        if event == "Voltar":
            window.close()
            modulo_camera = importlib.import_module('src.camera.menu_camera')
            modulo_camera.tela_menu_camera()


    window.close()

#if __name__ == '__main__':
#   criar_tabela_filme()
#    tela_cadastrar_filme()