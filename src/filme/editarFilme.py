import PySimpleGUI as sg
import sqlite3
import datetime as dt
from src.principal.menu_principal import tela_menu_principal
import src.filme.menu_filme as tela_menu_filme
import importlib


def  inserir_filme(dados_filme):
    conn = sqlite3.connect('pelicula.db')
    cursor = conn.cursor()
    
    data_criacao = dt.datetime.now().strftime("%d/%m/%Y %H:%M")

    try:
        cursor.execute('''INSERT INTO filme (nome, marca, formato, iso, tipo, cinema, rebobinado,
                        queimado, data_aquisicao, data_validade, notas)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (dados_filme['nome'], dados_filme['marca'], dados_filme['formato'], dados_filme['iso'], dados_filme['tipo'],
                        dados_filme['cinema'], dados_filme['rebobinado'], dados_filme['queimado'], dados_filme['data_aquisicao'],
                        dados_filme['data_validade'], dados_filme['notas']))
        
        conn.commit()
        conn.close()

        return "OK"
    except conn.Error as e:
        print(f"Erro ao adicionar filme: {e}")
        return str(e)        
    

def tela_editar_filme(id_filme):
    sg.theme('Reddit')

    modulo_filme = importlib.import_module('src.filme.filme')
    resultado = modulo_filme.consultar_filme(id_filme) 
    
    if resultado[7] == 'SIM':
        status_queimado = True
    else:
        status_queimado = False

    if resultado[6] == 'SIM':
        status_cinema = True
    else:
        status_cinema = False

    if resultado[5] == 'SIM':
        status_rebobinado = True
    else:
        status_rebobinado = False

    layout = [
        [sg.Text('EDITAR FILME')],
        [sg.InputText(key='idFilme', default_text=resultado[10], visible=False)],
        [sg.Text('Nome', size=(15, 1)), sg.InputText(key='nome', default_text=resultado[0])],
        [sg.Text('Marca', size=(15, 1)), sg.InputText(key='marca', default_text=resultado[1])],
        [sg.Text('Formato', size=(15, 1)), sg.Combo(['35', '120'], key='formato', default_value=resultado[2])],
        [sg.Text('ISO', size=(15, 1)), sg.InputText(key='iso', default_text=resultado[3])],
        [sg.Text('Tipo', size=(15, 1)), sg.Combo(['Colorido', 'PB'], key='tipo', default_value=resultado[4])],
        [sg.Text('Aquisição', size=(15, 1)), sg.InputText(key='data_aquisicao', default_text=resultado[8])],
        [sg.Text('Validade', size=(15, 1)), sg.InputText(key='data_validade', default_text=resultado[9])],
        [sg.Text('Notas', size=(15, 1)), sg.InputText(key='notas', default_text=resultado[11])],
        [sg.Checkbox('Queimado', key='queimado', default=status_queimado), sg.Checkbox('Cinema', key='cinema', default=status_cinema), sg.Checkbox('Rebobinado', key='rebobinado', default=status_rebobinado)],
        [sg.Button('Salvar', button_color='green'), sg.Button('Cancelar', button_color='red'), sg.Button('Voltar', button_color='blue')]
    ]

    window = sg.Window('EDITAR FILME', layout, size=(500, 300))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break
        if event == 'Salvar':
            window.close()
            modulo__editar_filme = importlib.import_module('src.filme.filme')
            resposta = modulo__editar_filme.atualizar_filme(values)
            print(f"Resposta: {resposta}")
            
            modulo_filme = importlib.import_module('src.filme.menu_filme')
            modulo_filme.tela_menu_filme()    
            #break
        if event == "Voltar":
            window.close()
            modulo_filme = importlib.import_module('src.filme.menu_filme')
            modulo_filme.tela_menu_filme()


    window.close()

#if __name__ == '__main__':
#   criar_tabela_filme()
#    tela_cadastrar_filme()