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
        [sg.Button('PDF', button_color='green'), sg.Button('Cancelar', button_color='red')]
    ]

    window = sg.Window('VISUALIZAR RELATO', layout, size=(500, 400))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break
        if event == 'Salvar':
            #inserir_camera(values)
            break

    window.close()