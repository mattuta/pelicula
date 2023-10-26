import PySimpleGUI as sg
import sqlite3
import datetime as dt
from config import janela_altura, janela_largura


def criar_tabela_camera():
    conn = sqlite3.connect('pelicula.db')
    cursor = conn.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS camera(
            idCamera integer primary key AUTOINCREMENT,
            marca text,
            modelo text,
            formato text,
            fabricante text,
            num_serie text,
            valor_compra text,
            valor_venda text,
            data_aquisicao text,
            data_venda text,
            notas text
        )''')
    conn.commit()
    conn.close()

def inserir_camera(dados_camera):
    conn = sqlite3.connect('pelicula.db')
    cursor = conn.cursor()
    
    data_criacao = dt.datetime.now().strftime("%d/%m/%Y %H:%M")

    try:
        cursor.execute('''INSERT INTO camera (marca, modelo, formato, fabricante, num_serie, valor_compra,
                        valor_venda, data_aquisicao, data_venda, notas)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (dados_camera['marca'], dados_camera['modelo'], dados_camera['formato'], dados_camera['fabricante'], dados_camera['num_serie'],
                        dados_camera['valor_compra'], dados_camera['valor_venda'], dados_camera['data_aquisicao'], dados_camera['data_venda'],
                        dados_camera['notas']))
        
        conn.commit()
        conn.close()

        return "OK"
    except conn.Error as e:
        print(f"Erro ao adicionar camera: {e}")
        return str(e) 
    
def tela_cadastrar_camera():
    sg.theme('Reddit')

    layout = [
        [sg.Text('CADASTRAR NOVO CÂMERA')],
        [sg.Text('Marca', size=(15, 1)), sg.InputText(key='marca')],
        [sg.Text('Modelo', size=(15, 1)), sg.InputText(key='modelo')],
        [sg.Text('Formato', size=(15, 1)), sg.Combo(['35', '120'], key='formato')],
        [sg.Text('Fabricante', size=(15, 1)), sg.InputText(key='fabricante')],
        [sg.Text('N° Série', size=(15, 1)), sg.InputText(key='num_serie')],
        [sg.Text('Valor Compra', size=(15, 1)), sg.InputText(key='valor_compra')],
        [sg.Text('Valor Venda', size=(15, 1)), sg.InputText(key='valor_venda')],
        [sg.Text('Aquisição', size=(15, 1)), sg.InputText(key='data_aquisicao')],
        [sg.Text('Venda', size=(15, 1)), sg.InputText(key='data_venda')],
        [sg.Text('Notas', size=(15, 1)), sg.InputText(key='notas')],
        [sg.Button('Salvar', button_color='green'), sg.Button('Cancelar', button_color='red')]
    ]

    window = sg.Window('CADASTRAR CÂMERA', layout, size=(janela_altura, janela_largura))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break
        if event == 'Salvar':
            inserir_camera(values)
            break

    window.close()

if __name__ == '__main__':
    criar_tabela_camera()
    tela_cadastrar_camera()