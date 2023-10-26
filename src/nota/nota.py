import PySimpleGUI as sg
import sqlite3
import datetime as dt
from src.principal.menu_principal import tela_menu_principal
import src.filme.menu_filme as tela_menu_filme
import importlib


def inserir_nota(values, idRelato, tipo):
    conn = sqlite3.connect('pelicula.db')
    cursor = conn.cursor()
    
    data_criacao = dt.datetime.now().strftime("%d/%m/%Y %H:%M")

    try:
        cursor.execute('''INSERT INTO nota_relato (desc_nota, tp_nota, id_relato, dt_nota)
                    VALUES (?, ?, ?, ?)''',
                    (values['descricao'], tipo, idRelato, data_criacao))
        
        conn.commit()
        conn.close()

        return "OK"
    except conn.Error as e:
        print(f"Erro ao adicionar nota: {e}")
        return str(e)