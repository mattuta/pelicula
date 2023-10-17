import importlib
import PySimpleGUI as sg
import sqlite3
import datetime as dt
import src.relato.relatos as relato

def tela_visualizar_relato(idRelato):
    sg.theme('Reddit')

    resultado_relato = relato.consultar_relatos(idRelato)

    layout = [
        [sg.Text('RELATO FOTOGRÁFICO')],
        [sg.Text('Cidade:', size=(15, 1)), sg.Text(resultado_relato[1])],
        [sg.Text('Estado:', size=(15, 1)), sg.Text(resultado_relato[2])],
        [sg.Text('Data início:', size=(15, 1)), sg.Text(resultado_relato[4])],
        [sg.Text('Data final:', size=(15, 1)), sg.Text(resultado_relato[6])],
        [sg.Text('Filme:', size=(15, 1)), sg.Text(resultado_relato[0])],
        [sg.Text('Câmera:', size=(15, 1)), sg.Text(resultado_relato[3])],
        [sg.Text('Notas:', size=(15, 1)), sg.Text(resultado_relato[5])],
        [sg.Button('EDITAR', button_color='green'), sg.Button('EXCLUIR', button_color='red'), sg.Button('Voltar', button_color='blue')]
    ]

    window = sg.Window('VISUALIZAR RELATO', layout, size=(500, 400))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break

        if event == 'Voltar':
            window.close()
            modulo_relato = importlib.import_module('src.relato.relatos')
            modulo_relato.listar_relatos()
            break

        if event == 'EXCLUIR':
               
            resposta = sg.popup_yes_no('[Essa é uma ação irreversível.] \n Deseja realmente excluir este relato?')
            
            if resposta == 'Yes':
                window.close()
                
                modulo_relato = importlib.import_module('src.relato.relatos')
                retorno_relato = modulo_relato.excluir_relato(resultado_relato[7])

                if retorno_relato == 1:
                    
                    print('Relato excluído.')
                   
                    modulo_grid = importlib.import_module('src.relato.relatos')
                    modulo_grid.listar_relatos()

            else:
                
                print('Ação cancelada ou Relato não excluído.')

            break

        if event == 'EDITAR':
            window.close()
            modulo_relato = importlib.import_module('src.relato.editarRelato')
            modulo_relato.tela_editar_relato(resultado_relato[7])

    window.close()