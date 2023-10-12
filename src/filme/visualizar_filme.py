import PySimpleGUI as sg
import sqlite3
import datetime as dt
import src.relato.relatos as relato
import importlib

def tela_visualizar_filme(id_filme):
    sg.theme('Reddit')

    modulo_filme = importlib.import_module('src.filme.filme')
    resultado_filme = modulo_filme.consultar_filme(id_filme)

    layout = [
        [sg.Text('FICHA FILME')],
        [sg.Text('MARCA:', size=(15, 1)), sg.Text(resultado_filme[1])],
        [sg.Text('NOME:', size=(15, 1)), sg.Text(resultado_filme[0])],
        [sg.Text('FORMATO:', size=(15, 1)), sg.Text(resultado_filme[2])],
        [sg.Text('ISO:', size=(15, 1)), sg.Text(resultado_filme[3])],
        [sg.Text('TIPO:', size=(15, 1)), sg.Text(resultado_filme[4])],
        [sg.Text('CINEMA:', size=(15, 1)), sg.Text(resultado_filme[5])],
        [sg.Text('REBOBINADO:', size=(15, 1)), sg.Text(resultado_filme[6])],
        [sg.Text('QUEIMADO:', size=(15, 1)), sg.Text(resultado_filme[7])],
        [sg.Text('AQUISIÇÃO:', size=(15, 1)), sg.Text(resultado_filme[8])],
        [sg.Text('VALIDADE:', size=(15, 1)), sg.Text(resultado_filme[9])],
        [sg.Text('NOTAS:', size=(15, 1)), sg.Text(resultado_filme[11])],
        [sg.Button('EDITAR', button_color='green'), sg.Button('EXCLUIR', button_color='red')]
    ]

    window = sg.Window('VISUALIZAR FILME', layout, size=(500, 400))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break
        if event == 'EXCLUIR':
           
            resposta = sg.popup_yes_no('[Essa é uma ação irreversível.] \n Deseja realmente excluir este filme?')
            
            if resposta == 'Yes':
                window.close()
                
                modulo_filme = importlib.import_module('src.filme.filme')
                retorno_filme = modulo_filme.excluir_filme(resultado_filme[10])

                if retorno_filme == 1:
                    
                    print('Filme excluído.')
                   
                    modulo_grid = importlib.import_module('src.filme.estoqueFilme')
                    modulo_grid.consultar_filme()

            else:
                
                print('Ação cancelada ou Filme não excluído.')

            break
        if event == 'EDITAR':
            window.close()
            modulo_grid = importlib.import_module('src.filme.editarFilme')
            modulo_grid.tela_editar_filme(resultado_filme[10])


    window.close()