import importlib
import PySimpleGUI as sg
import sqlite3
import datetime as dt
from src.filme.estoqueFilme import atualizar_queima_filme, consultar_filme_disponivel, obter_id_filme
from src.camera.estoque_camera import consultar_camera_disponivel, obter_id_camera

def criar_tabela_camera():
    conn = sqlite3.connect('pelicula.db')
    cursor = conn.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS relato(
        idRelato integer primary key AUTOINCREMENT,
        id_filme integer,
        cidade text,
        estado text,
        id_camera integer,
        data_inicio text,
        data_fim text,
        notas text                           
    )''')
    conn.commit()
    conn.close()

def inserir_relato(dados_relato):
    conn = sqlite3.connect('pelicula.db')
    cursor = conn.cursor()

    try:
        cursor.execute(''' INSERT INTO relato (id_filme, cidade, estado, id_camera, data_inicio, data_fim, notas)
                       VALUES(?, ?, ?, ?, ?, ?, ?)''',
                       (dados_relato['id_filme'], dados_relato['cidade'], dados_relato['estado'],
                        dados_relato['id_camera'], dados_relato['data_inicio'], dados_relato['data_fim'],
                        dados_relato['notas'])
                       )
        
        id_relato = cursor.lastrowid

        cursor.execute('UPDATE filme SET queimado = 1 WHERE idFilme = ?', (dados_relato['id_filme'],))

        conn.commit()
        conn.close() 

        modulo_relato = importlib.import_module('src.relato.visualizar_relato')
        modulo_relato.tela_visualizar_relato(id_relato)

        return "OK"
    except sqlite3.Error as e:
        print(f"Erro ao adicionar relato: {e}")
        return str(e)

def tela_cadastrar_relato():
    sg.theme('Reddit')

    filmes = consultar_filme_disponivel()
    cameras = consultar_camera_disponivel()

    layout = [
        [sg.Text('CADASTRAR NOVO RELATO')],
        [sg.Text('Filme', size=(15, 1)), sg.Combo(filmes, key='filme')],
        [sg.Text('Câmera', size=(15, 1)), sg.Combo(cameras, key='camera')],
        [sg.Input('', key='id_filme', visible=False), sg.Input('', key='id_camera', visible=False)],
        [sg.Text('Cidade', size=(15, 1)), sg.InputText(key='cidade')],
        [sg.Text('Estado', size=(15, 1)), sg.InputText(key='estado')],
        [sg.Text('Data Início', size=(15, 1)), sg.InputText(key='data_inicio')],
        [sg.Text('Data Fim', size=(15, 1)), sg.InputText(key='data_fim')],
        [sg.Text('Notas', size=(15, 1)), sg.InputText(key='notas')],
        [sg.Button('Salvar', button_color='green'), sg.Button('Cancelar', button_color='red')]
    ]

    window = sg.Window('CADASTRAR RELATO', layout, size=(500, 400))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break
        if event == 'Salvar':
            filme_index = int(values['filme'][0])
            camera_index = values['camera'][0]

            values['id_filme'] = filme_index
            values['id_camera'] = camera_index
            
            window.close()
            
            inserir_relato(values)

            break

    window.close()