import PySimpleGUI as sg

def main_window(data):
    layout = [
        [sg.Text('Conteúdo da Janela Principal')],
        [sg.Listbox(data, size=(30, 10), key='-LIST-')],
        [sg.Button('Funcionalidade 1'), sg.Button('Funcionalidade 2'), sg.Button('Sair')]
    ]

    window = sg.Window('Minha Aplicação', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Sair':
            break
        elif event == 'Funcionalidade 1':
            # Atualiza o conteúdo da janela principal com a funcionalidade 1
            layout = [
                [sg.Text('Funcionalidade 1')],
                [sg.Button('Voltar')]
            ]
            window.close()
            window = sg.Window('Minha Aplicação', layout)
        elif event == 'Funcionalidade 2':
            # Atualiza o conteúdo da janela principal com a funcionalidade 2
            layout = [
                [sg.Text('Funcionalidade 2')],
                [sg.Button('Voltar')]
            ]
            window.close()
            window = sg.Window('Minha Aplicação', layout)

    window.close()

data = ['Item 1', 'Item 2', 'Item 3']

main_window(data)
