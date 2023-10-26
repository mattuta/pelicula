import PySimpleGUI as sg
import sqlite3
import datetime as dt
from src.principal.menu_principal import tela_menu_principal
import src.filme.menu_filme as tela_menu_filme
import importlib
from config import janela_altura, janela_largura


def criar_tabela_filme():
    conn = sqlite3.connect('pelicula.db')
    cursor = conn.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS filme(
            idFilme integer primary key AUTOINCREMENT,
            nome text,
            marca text,
            formato text,
            iso text,
            tipo text,
            cinema text,
            rebobinado text,
            quantidade text,
            data_aquisicao text,
            data_validade text,
            notas text
        )''')
    conn.commit()
    conn.close()

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
        
        id_filme = cursor.lastrowid

        conn.commit()
        conn.close()

        modulo_filme = importlib.import_module('src.filme.visualizar_filme')
        modulo_filme.tela_visualizar_filme(id_filme)

        return "OK"
    except conn.Error as e:
        print(f"Erro ao adicionar filme: {e}")
        return str(e)        
    
def tela_cadastrar_filme():
    sg.theme('Reddit')

    layout = [
        [sg.Text('CADASTRAR NOVO FILME')],
        [sg.Text('Nome', size=(15, 1)), sg.InputText(key='nome')],
        [sg.Text('Marca', size=(15, 1)), sg.InputText(key='marca')],
        [sg.Text('Formato', size=(15, 1)), sg.Combo(['35', '120'], key='formato')],
        [sg.Text('ISO', size=(15, 1)), sg.InputText(key='iso')],
        [sg.Text('Tipo', size=(15, 1)), sg.Combo(['Colorido', 'PB'], key='tipo')],
        [sg.Text('Aquisição', size=(15, 1)), sg.InputText(key='data_aquisicao')],
        [sg.Text('Validade', size=(15, 1)), sg.InputText(key='data_validade')],
        [sg.Text('Notas', size=(15, 1)), sg.InputText(key='notas')],
        [sg.Checkbox('Queimado', key='queimado'), sg.Checkbox('Cinema', key='cinema'), sg.Checkbox('Rebobinado', key='rebobinado')],
        [sg.Button('Salvar', button_color='green'), sg.Button('Cancelar', button_color='red'), sg.Button('Voltar', button_color='blue')]
    ]

    window = sg.Window('CADASTRAR FILME', layout, size=(janela_altura, janela_largura))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break
        if event == 'Salvar':
            window.close()
            inserir_filme(values)
            #modulo_filme = importlib.import_module('src.filme.menu_filme')
            #modulo_filme.tela_menu_filme()    
            #break
        if event == "Voltar":
            window.close()
            modulo_filme = importlib.import_module('src.filme.menu_filme')
            modulo_filme.tela_menu_filme()


    window.close()

if __name__ == '__main__':
    criar_tabela_filme()
    tela_cadastrar_filme()