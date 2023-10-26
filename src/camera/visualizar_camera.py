import PySimpleGUI as sg
import importlib
from config import janela_altura, janela_largura


def tela_visualizar_camera(id_camera):
    sg.theme('Reddit')

    modulo_camera = importlib.import_module('src.camera.camera')
    resultado_camera = modulo_camera.consultar_camera(id_camera)

    layout = [
        [sg.Text('FICHA CÂMERA')],
        [sg.Text('MARCA:', size=(15, 1)), sg.Text(resultado_camera[0])],
        [sg.Text('MODELO:', size=(15, 1)), sg.Text(resultado_camera[1])],
        [sg.Text('FORMATO:', size=(15, 1)), sg.Text(resultado_camera[2])],
        [sg.Text('FABRICANTE:', size=(15, 1)), sg.Text(resultado_camera[3])],
        [sg.Text('N° SÉRIE:', size=(15, 1)), sg.Text(resultado_camera[4])],
        [sg.Text('VALOR COMPRA:', size=(15, 1)), sg.Text(resultado_camera[5])],
        [sg.Text('VALOR VENDA:', size=(15, 1)), sg.Text(resultado_camera[6])],
        [sg.Text('DATA AQUISIÇÃO:', size=(15, 1)), sg.Text(resultado_camera[7])],
        [sg.Text('DATA VENDA:', size=(15, 1)), sg.Text(resultado_camera[8])],
        [sg.Text('NOTAS:', size=(15, 1)), sg.Text(resultado_camera[9])],
        [sg.Button('EDITAR', button_color='green'), sg.Button('EXCLUIR', button_color='red'), sg.Button('Voltar', button_color='blue')]
    ]

    window = sg.Window('VISUALIZAR CAMERA', layout, size=(janela_altura, janela_largura))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break
        if event == 'EXCLUIR':
           
            resposta = sg.popup_yes_no('[Essa é uma ação irreversível.] \n Deseja realmente excluir está câmera?')
            
            if resposta == 'Yes':
                window.close()
                
                modulo_camera = importlib.import_module('src.camera.camera')
                retorno_camera = modulo_camera.excluir_camera(resultado_camera[10])

                if retorno_camera == 1:
                    
                    print('Câmera excluída.')
                   
                    modulo_grid = importlib.import_module('src.camera.estoque_camera')
                    modulo_grid.consultar_camera()

            else:
                
                print('Ação cancelada ou Câmera não excluída.')

            break
        if event == 'EDITAR':
            window.close()
            modulo_grid = importlib.import_module('src.camera.editarCamera')
            modulo_grid.tela_editar_camera(resultado_camera[10])
        
        if event == 'Voltar':
            window.close()
            modulo_camera = importlib.import_module('src.camera.estoque_camera')
            modulo_camera.consultar_camera()
            break


    window.close()