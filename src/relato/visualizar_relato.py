import importlib
import PySimpleGUI as sg
import sqlite3
import datetime as dt
import src.relato.relatos as relato
from config import janela_altura, janela_largura

def tela_visualizar_relato(idRelato):
    sg.theme('Reddit')

    resultado_relato = relato.consultar_relatos(idRelato)
    
# -------------------------- MODULO SCAN ----------------------------------------    
    modulo_rev = importlib.import_module('src.relato.relatos')
    nota_revelacao = modulo_rev.consultar_rev(idRelato)

    contador = 1

    lista_formatada = []

    if not nota_revelacao:
        lista_scan = ['Nenhum registro localizado']
    else:
        for nota in nota_revelacao:
            linha = f"{contador} - {nota[0]} - {nota[1]}"
            lista_formatada.append(linha)
            contador += 1
    
    layout_revelacao = [
        #[sg.T(s=(100, 1))],
        [sg.Multiline(default_text='\n'.join(lista_formatada), size=(400, 400), disabled=True)]
    ]
#---------------------------------------------------------------------------------

# -------------------------- MODULO SCAN ----------------------------------------
    modulo_scan = importlib.import_module('src.relato.relatos')
    nota_scan = modulo_scan.consultar_scan(idRelato)
    print(f'{nota_scan}')    

    contadorScan = 1

    lista_scan = []

    if not nota_scan:
        lista_scan = ['Nenhum registro localizado']
    else:
        for scan in nota_scan:
            linhaS = f"{contadorScan} - {scan[0]} - {scan[1]}"
            lista_scan.append(linhaS)
            contadorScan += 1

    layout_scan = [
        #[sg.T(s=(100, 1))],
        [sg.Multiline(default_text='\n'.join(lista_scan), size=(400, 400), disabled=True)]
    ]
#---------------------------------------------------------------------------------

# -------------------------- MODULO OBSERVACAO ----------------------------------------
    modulo_obs = importlib.import_module('src.relato.relatos')
    nota_obs = modulo_obs.consultar_obs(idRelato)    
    
    contadorObs = 1

    lista_obs = []

    if not nota_obs:
        lista_obs = ['Nenhum registro localizado']
    else:
        for obs in nota_obs:
            linhaObs = f"{contadorScan} - {obs[0]} - {obs[1]}"
            lista_obs.append(linhaObs)
            contadorObs += 1

    layout_obs = [
        #[sg.T(s=(100, 1))],
        [sg.Multiline(default_text='\n'.join(lista_obs), size=(400, 400), disabled=True)]
    ]
#---------------------------------------------------------------------------------

    
    layout = [
        [sg.Frame('RELATO FOTOGRÁFICO', [[sg.T(s=15)], 
                                         [sg.Text('Cidade:', size=(15, 1)), sg.Text(resultado_relato[1])],
                                         [sg.Text('Estado:', size=(15, 1)), sg.Text(resultado_relato[2])],
                                         [sg.Text('Data início:', size=(15, 1)), sg.Text(resultado_relato[4])],
                                         [sg.Text('Data final:', size=(15, 1)), sg.Text(resultado_relato[6])],
                                         [sg.Text('Filme:', size=(15, 1)), sg.Text(resultado_relato[0])],
                                         [sg.Text('Câmera:', size=(15, 1)), sg.Text(resultado_relato[3])],
                                         [sg.Text('Notas:', size=(15, 1)), sg.Text(resultado_relato[5])]], size=(400, 250), )],
        [sg.Frame('REVELAÇÃO', layout_revelacao, size=(400, 100), font='Arial')],
        [sg.Frame('SCAN', layout_scan, size=(400, 100), font='Arial')],
        [sg.Frame('OBSERVAÇÕES', layout_obs, size=(400, 100), font='Arial')],
        [sg.Button('REVELAÇÃO', button_color='orange'), sg.Button('SCAN', button_color='orange'), sg.Button('OBSERVAÇÕES', button_color='orange')],
        [sg.Button('EDITAR', button_color='green'), sg.Button('EXCLUIR', button_color='red'), sg.Button('Voltar', button_color='blue')]
    ]
    

    column_layout = [
        [sg.Column(layout, scrollable=True, size=(janela_altura, janela_largura))],
    ]


    window = sg.Window('VISUALIZAR RELATO', column_layout, size=(janela_altura, janela_largura))

    while True:
        event, values = window.read()

        if event == 'REVELAÇÃO':
            modulo_nota = importlib.import_module('src.nota.cadastrarNota')
            modulo_nota.tela_cadastrar_nota(resultado_relato[7], 'R')

        if event == 'SCAN':
            modulo_nota = importlib.import_module('src.nota.cadastrarNota')
            modulo_nota.tela_cadastrar_nota(resultado_relato[7], 'S')

        if event == 'OBSERVAÇÕES': 
            modulo_nota = importlib.import_module('src.nota.cadastrarNota')
            modulo_nota.tela_cadastrar_nota(resultado_relato[7], 'O')


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